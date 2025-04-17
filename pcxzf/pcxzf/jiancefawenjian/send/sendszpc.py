import sys
import os

# 获取当前文件的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目的根目录
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
# 将项目根目录添加到 sys.path
sys.path.append(project_root)
import pymysql
from jiancefawenjian import conf
import requests
import json
from .conf2 import access_token  # ensure you have this module conf2 with access_token
from datetime import datetime
token = access_token
def get_access_token():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + conf.qy_id + '&corpsecret=' + conf.secret_szpc
    response = requests.get(url)
    if response.status_code == 200:
        token_info = response.json()
        if 'access_token' in token_info:
            save_token(token_info['access_token'])
            return token_info['access_token']
        else:
            print(f"Failed to obtain token: {token_info.get('errmsg', 'Unknown error')}")
            return None
    else:
        print(f"HTTP Error {response.status_code}: Failed to contact token service.")
        return None


def save_token(token):
    with open('.conf2.py', 'w') as f:
        f.write('access_token = \'' + token + '\'\n')


def send_card_message(token, message_payload):
    """Sends a card message to WeChat Work."""
    url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}'

    response = requests.post(url,  data=json.dumps(message_payload))

    return response.json()


def get_all_companies_with_rankings():
    """
    获取所有单位的年度积分和排名情况
    
    Returns:
        tuple: (所有单位列表, 单位积分字典, 单位排名字典, 总排名数)
    """
    # 获取当前年份
    current_year = datetime.now().year
    start_date = f"{current_year}-1-1"
    
    # 连接数据库
    connection = pymysql.connect(**conf.database)
    cursor = connection.cursor()
    
    # 执行SQL查询获取所有单位的年度积分 (分数大的排前面)
    sql = f"""
    SELECT d.dict_label, COALESCE(SUM(a.score), 0) AS total_score
    FROM sys_dict_data d
    LEFT JOIN assessment_record a ON d.dict_label = a.company_name AND a.date >= '{start_date}'
    WHERE d.dict_type = 'bm_list'
    GROUP BY d.dict_label
    ORDER BY total_score DESC;
    """
    print(f"执行SQL: {sql}")
    cursor.execute(sql)
    result = cursor.fetchall()
    
    print("\n原始查询结果 (按分数从大到小):")
    for i, (company, score) in enumerate(result[:10]):  # 只打印前10个进行检验
        print(f"{i+1}. {company}: {score}")
    
    # 处理并列排名 - 修正后的逻辑
    all_companies = []
    annual_scores = {}
    rankings = {}
    
    current_rank = 1
    previous_score = None
    unique_ranks = set()
    
    print("\n排名计算过程 (修正后):")
    for i, (company_name, score) in enumerate(result):
        all_companies.append(company_name)
        annual_scores[company_name] = score
        
        # 如果分数变化，排名加1
        if previous_score is not None and score != previous_score:
            current_rank += 1
            print(f"分数变化: {previous_score} -> {score}, 排名变为: {current_rank}")
        elif i > 0:
            print(f"分数相同: {score}, 保持排名: {current_rank}")
        else:
            print(f"初始分数: {score}, 初始排名: {current_rank}")
        
        rankings[company_name] = current_rank
        unique_ranks.add(current_rank)
        previous_score = score
    
    print("\n最终排名结果 (前10个):")
    for i, company in enumerate(all_companies[:10]):
        print(f"{company}: 分数={annual_scores[company]}, 排名={rankings[company]}")
    
    cursor.close()
    connection.close()
    
    return all_companies, annual_scores, rankings, len(unique_ranks)


def create_card_payload(comp, weekly_score, annual_score, ranking, total_ranks, curdate):
    """Create payload for the card message."""
    weekly_score = str(int(weekly_score)) if weekly_score is not None else "0"
    
    # 格式化排名信息
    if ranking is not None:
        ranking_text = f"{ranking}/{total_ranks}(存在并列排名)"
    else:
        ranking_text = "暂未公开"
    
    # 格式化年度积分信息
    if annual_score is not None:
        annual_score_text = str(annual_score)
    else:
        annual_score_text = "未到公布时间"
    
    return {
        # "touser": "WuXiaoLong",
        "toparty": '|'.join(str(i) for i in conf.bumen_departid[comp]),
        "msgtype": "template_card",
        "agentid": conf.agent_id_szpc,  # You must set your agent_id here
        "template_card": {
            "card_type": "text_notice",
            "source": {
                "icon_url": "https://wework.qpic.cn/wwpic/252813_jOfDHtcISzuodLa_1629280209/0",
                "desc": "\'平政哨兵\'考核通知",
                "desc_color": 1
            },
            "main_title": {
                "title": comp,
                "desc": f"扣分时间：{curdate}",
            },
            "emphasis_content": {
                "title": weekly_score,
                "desc": "本周扣分"
            },
            "quote_area": {
                "type": 0,
                "quote_text": f"考核排名：{ranking_text}\n考核时间：每周一\n年度扣分：{annual_score_text}"
            },
            "sub_title_text": "政府网站内容保障考核实行扣分制，扣分详情进入政务工作群或登录数字平昌综合治理后台获取！",
            "jump_list": [

                {
                    "type": 1,
                    "url": "http://222.215.24.208:81",
                    "title": "跳转'数字平昌'综合治理后台"
                }
            ],
            "card_action": {
                "type": 1,
                "url": "http://222.215.24.208:81"
            }
        }
        }


def sendmsg(comp, weekly_score, annual_score, ranking, total_ranks, curdate):
    global token
    payload = create_card_payload(comp, weekly_score, annual_score, ranking, total_ranks, curdate)
    result = send_card_message(token, payload)

    if 'errcode' in result and (result['errcode'] == 40014 or result['errcode'] == 42001):
        print("Token expired, acquiring new token...")
        token = get_access_token()  # Assuming this function is working as intended
        result = send_card_message(token, payload)

    print(result)


def testsendszpc():
    print("test success!")


def get_all_companies():
    """
    获取系统中所有的单位名称
    
    Returns:
        list: 所有单位名称列表
    """
    # 连接数据库
    connection = pymysql.connect(**conf.database)
    cursor = connection.cursor()
    
    # 执行SQL查询获取所有单位
    sql = """
    SELECT dict_label
    FROM sys_dict_data
    WHERE dict_type = 'bm_list'
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    
    # 提取单位名称
    companies = [row[0] for row in result]
    
    cursor.close()
    connection.close()
    
    return companies

def sendszpc(res):
    current_date = datetime.now()
    # 格式化日期
    formatted_date = current_date.strftime('%Y-%m-%d')
    
    # 一次性获取所有单位的年度积分和排名
    all_companies, annual_scores, rankings, total_ranks = get_all_companies_with_rankings()
    
    # 将res转换为字典，方便查找
    weekly_scores = {row[0]: row[1] for row in res}
    
    # 为每个单位发送消息
    for company in all_companies:
        # 如果单位在res中有扣分记录，使用记录的分数，否则使用0
        weekly_score = weekly_scores.get(company, 0)
        annual_score = annual_scores.get(company, 0)
        ranking = rankings.get(company)
        
        sendmsg(company, weekly_score, annual_score, ranking, total_ranks, formatted_date)

def main():
    connection = pymysql.connect(**conf.database)
    cursor = connection.cursor()
    sql = """
            SELECT company_name, SUM(score) AS total_score
            FROM assessment_record
            WHERE date = '2025-4-14'
            GROUP BY company_name
            ORDER BY total_score DESC;
            """
    cursor.execute(sql)
    # 获取查询结果
    result = cursor.fetchall()

    sendszpc(result)
    cursor.close()
    connection.close()

def test_ranking():
    """
    测试排名功能的函数
    """
    # 获取所有单位的年度积分和排名
    all_companies, annual_scores, rankings, total_ranks = get_all_companies_with_rankings()
    
    # 打印前5个单位的信息 (按排名从前到后)
    print("排名情况预览 (分数越大，排名越靠前):")
    for i, company in enumerate(all_companies[:5]):
        print(f"公司: {company}")
        print(f"年度扣分: {annual_scores[company]}")
        print(f"排名: {rankings[company]}/{total_ranks} (存在并列排名)")
        print("-" * 30)
    
    # 创建测试数据
    test_res = [(all_companies[0], -5), (all_companies[1], -10)]
    
    # 测试发送
    current_date = datetime.now().strftime('%Y-%m-%d')
    print(f"\n测试使用以下数据发送: {test_res}")
    print("(负数表示扣分，-5比-10大，所以-5排名靠前)")
    
    # 将res转换为字典
    weekly_scores = {row[0]: row[1] for row in test_res}
    
    # 为前3个单位生成卡片消息
    for company in all_companies[:3]:
        weekly_score = weekly_scores.get(company, 0)
        annual_score = annual_scores.get(company, 0)
        ranking = rankings.get(company)
        
        print(f"\n公司: {company}")
        print(f"本周扣分: {weekly_score}")
        print(f"年度扣分: {annual_score}")
        print(f"排名: {ranking}/{total_ranks}")
        
        # 打印卡片消息内容
        payload = create_card_payload(company, weekly_score, annual_score, ranking, total_ranks, current_date)
        print("卡片消息:", payload["template_card"]["quote_area"]["quote_text"])

def test_debug_ranking():
    """仅用于调试排名计算问题的测试函数"""
    all_companies, annual_scores, rankings, total_ranks = get_all_companies_with_rankings()
    print("\n排名总数:", total_ranks)
    
    # 检查特定分数段的排名
    print("\n检查不同分数的排名情况:")
    for score in [0, -1, -2, -5, -10, -20]:
        companies_with_score = [c for c in all_companies if annual_scores[c] == score]
        if companies_with_score:
            company = companies_with_score[0]
            print(f"分数 {score}: {company} 排名 {rankings[company]}")
        else:
            print(f"找不到分数为 {score} 的单位")
    
    return

if __name__ == '__main__':
    # 运行调试测试
    # test_debug_ranking()
    
    # 正常功能
    main()



