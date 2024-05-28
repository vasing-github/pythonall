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


def create_card_payload(comp, score,curdate):
    """Create payload for the card message."""
    score = int(score)  # 将 Decimal 转换为 float
    score = str(score)
    return {
        # "touser": "WuXiaoLong",
        "toparty": '|'.join(str(i) for i in conf.bumen_departid[comp]),
        "msgtype": "template_card",
        "agentid": conf.agent_id_szpc,  # You must set your agent_id here
        "template_card": {
            "card_type": "text_notice",
            "source": {
                "icon_url": "https://wework.qpic.cn/wwpic/252813_jOfDHtcISzuodLa_1629280209/0",
                "desc": "政府网站内容保障考核通知",
                "desc_color": 1
            },
            "main_title": {
                "title": comp,
                "desc": f"扣分时间：{curdate}",
            },
            "emphasis_content": {
                "title": score,
                "desc": "本周扣分"
            },
            "quote_area": {
                "type": 0,
                "quote_text": f"考核排名：暂未公开\n考核时间：每周一\n年度积分：未到公布时间"
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


def sendmsg(comp,score, curdate):
    global token
    payload = create_card_payload(comp, score,curdate)
    result = send_card_message(token, payload)

    if 'errcode' in result and (result['errcode'] == 40014 or result['errcode'] == 42001):
        print("Token expired, acquiring new token...")
        token = get_access_token()  # Assuming this function is working as intended
        result = send_card_message(token, payload)

    print(result)


def testsendszpc():
    print("test success!")


def sendszpc(res):
    current_date = datetime.now()
    # 格式化日期
    formatted_date = current_date.strftime('%Y-%m-%d')
    # formatted_date = '2024-4-22'
    for row in res:
        # print(row[0],row[1])
        sendmsg(row[0], row[1], formatted_date)

def main():
    connection = pymysql.connect(**conf.database)
    cursor = connection.cursor()
    sql = """
            SELECT company_name, SUM(score) AS total_score
            FROM assessment_record
            WHERE date = '2024-5-20'
            GROUP BY company_name;
            """
    cursor.execute(sql)
    # 获取查询结果
    result =cursor.fetchall()

    sendszpc(result)
    cursor.close()
    connection.close()

if __name__ == '__main__':

    pass



