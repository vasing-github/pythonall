import json
import os
import sys
import pymysql
import conf
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目的根目录
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
# 将项目根目录添加到 sys.path
sys.path.append(project_root)
from kaipumodify.cfg import dealtext
import kaipumodify.cfg.text as text

bz_gov_id = text.bz_gov_id
jid = text.jid

from datetime import datetime

# 获取当前日期
current_date = datetime.now().strftime('%Y-%m-%d')

# 生成字符串
title = f"政务公开工作红黑榜（{current_date}期）"

print(title)


def save_red_black(c):
    cookies = {
        'bz_govc_SHIROJSESSIONID': bz_gov_id,
        'historyCookie': '%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E9%98%B2%E6%B1%9B%E6%8A%97%E6%97%B1%E6%8C%87%E6%8C%A5%E9%83%A8%2C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%B4%E5%88%A9%E5%B1%80%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%86%9C%E4%B8%9A%E5%86%9C%E6%9D%91%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%8F%B8%E6%B3%95%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%91%E6%94%BF%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%9E%8D%E5%AA%92%E4%BD%93%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%BA%94%E6%80%A5%E7%AE%A1%E7%90%86%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'bz_govc_SHIROJSESSIONID=5142795e-eeaf-4062-8aeb-08d67db2cde6; historyCookie=%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E9%98%B2%E6%B1%9B%E6%8A%97%E6%97%B1%E6%8C%87%E6%8C%A5%E9%83%A8%2C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%B4%E5%88%A9%E5%B1%80%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%86%9C%E4%B8%9A%E5%86%9C%E6%9D%91%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%8F%B8%E6%B3%95%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%91%E6%94%BF%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%9E%8D%E5%AA%92%E4%BD%93%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%BA%94%E6%80%A5%E7%AE%A1%E7%90%86%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4',
        'Origin': 'http://10.15.3.133:83',
        'Referer': 'http://10.15.3.133:83/index;JSESSIONID=5b900487-5bad-40aa-aa28-1872ea50b10c?s=1718587404541&siteId=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'IsAjax': '1',
        'dataType': 'JSON',
        '_': '0.1927895790766574',
    }

    data = {
        'remoteContent': '',
        'fromIndex': '',
        'id': '',
        'columnId': '6800509',
        'siteId': '6787191',
        'title': f"政务公开工作红黑榜（{current_date}期）",
        'subTitle': '',
        'shortTitle': '',
        'author': '',
        'responsibilityEditor': '吴晓龙',
        'resources': '平昌县人民政府办公室',
        'redirectLink': '',
        'imageLink': '',
        'isNew': '0',
        'isTop': '0',
        'topValidDate': '',
        'isBold': '0',
        'isUnderline': '0',
        'isTilt': '0',
        'titleColor': '',
        'remarks': '一.本周政务公开工作红榜单位：',
        'content': c,
        'isPublish': '1',
        'publishDate': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'typeCode': 'articleNews',
        'isAllowComments': '0',
        'quoteStatus': '0',
        'recordStatus': 'Normal',
        'workFlowStatus': '',
        'videoStatus': '100',
        'allImgSrc': '',
        'flag': 'true',
        'imgNum': '0',
        'subIsBold': '0',
        'subIsTilt': '0',
        'subIsUnderline': '0',
        'subTitleColor': '',
        'topTitle': '',
        'topIsBold': '0',
        'topIsTilt': '0',
        'topIsUnderline': '0',
        'topTitleColor': '',
        'smallTitle': '',
        'smallIsBold': '0',
        'smallIsTilt': '0',
        'smallIsUnderline': '0',
        'smallTitleColor': '',
        'qsYear': '',
        'qsMonth': '',
        'qsNum': '',
        'isLight': '0',
        'smallLinkUrl': '',
        'smallLinkTitle': '',
        'picUrl': '',
        'normalUrl': '',
        'recommend': '0',
        'keyWords': '',
        'reportType': '',
        'interviewContentId': '',
        'newsThemeType': '',
        'isLink': '0',
        'articleText': '',
        'hit': '0',
    }

    res = requests.post(
        'http://10.15.3.133:83/articleNews/saveArticleNews',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )
    return res.json()


def get_new_bzid_jid():
    global bz_gov_id, jid
    bz_gov_id, jid = dealtext.jiyue_token()


def dealresult(result):
    # 初始化两个列表来存储单位名称
    deducted_units = []
    non_deducted_units = []

    # 遍历查询结果
    for row in result:
        unit_name = row[0]
        total_score = row[1]
        if total_score < 0:
            deducted_units.append(unit_name)
        else:
            non_deducted_units.append(unit_name)
    if not deducted_units:
        return
    # 将列表转换为字符串，并用 '、' 分隔，最后一个单位用句号结尾
    deducted_units_str = '、'.join(deducted_units) + '。' if deducted_units else ''
    non_deducted_units_str = '、'.join(non_deducted_units) + '。' if non_deducted_units else ''

    print("被扣分单位:", deducted_units_str)
    print("未扣分单位:", non_deducted_units_str)
    content =  '<p style="margin: 0px; padding: 0px; list-style: none; color: rgb(51, 51, 51); font-family: &quot;Microsoft YaHei&quot;, 宋体, tahoma, Verdana, arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: justify; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; text-indent: 2em;"><span style="font-weight: bold;">一、本周政务公开工作红榜单位：</span></p><p style="margin: 0px; padding: 0px; list-style: none; color: rgb(51, 51, 51); font-family: &quot;Microsoft YaHei&quot;, 宋体, tahoma, Verdana, arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: justify; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; text-indent: 2em;">'+non_deducted_units_str+'</p><p style="margin: 0px; padding: 0px; list-style: none; color: rgb(51, 51, 51); font-family: &quot;Microsoft YaHei&quot;, 宋体, tahoma, Verdana, arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: justify; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; text-indent: 2em;"><span style="font-weight: bold;">二、本周政务公开工作黑榜单位：</span></p><p style="margin: 0px; padding: 0px; list-style: none; color: rgb(51, 51, 51); font-family: &quot;Microsoft YaHei&quot;, 宋体, tahoma, Verdana, arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: justify; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; text-indent: 2em;">'+deducted_units_str+'<br></p><p style="margin: 0px; padding: 0px; list-style: none; color: rgb(51, 51, 51); font-family: &quot;Microsoft YaHei&quot;, 宋体, tahoma, Verdana, arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: justify; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; text-indent: 2em;"><br></p><p style="margin: 0px; padding: 0px; list-style: none; color: rgb(51, 51, 51); font-family: &quot;Microsoft YaHei&quot;, 宋体, tahoma, Verdana, arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: justify; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; text-indent: 2em;">注：政务公开工作红黑榜由“平政哨兵”机器人自动记录并发布到本专栏，以周环比监测数据为依据，保障到位的单位列入红榜，未保障到位的列入黑榜。若本周无单位进入黑榜则不公布本期榜单。</p>'
    res = save_red_black(content)
    if 'status' in res and res['status'] == -9:
        get_new_bzid_jid()
        res = save_red_black(content)
    print(res)
    if 'status' in res and res['status'] == 1:
        sendmsg(True,res['data'])
    else:
        sendmsg(False,1)


def sendmsg(s,id):
    _url = 'http://www.scpc.gov.cn/content/article/' + str(id)
    if s:
        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": f"自动保障栏目-政务公开红黑榜，请人工核实。\n\n\n[{title}]({_url})\n\n\n{_url}\n\n\n<@WuXiaoLong>\n<@MingFengWangBaoNing>"
            }
        }
    else:
        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": f"自动保障栏目-政务公开红黑榜失败，请人工核实。\n\n<@WuXiaoLong>\n<@MingFengWangBaoNing>"
            }
        }
    key = conf.key_cs
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=" + key
    # 发送HTTP POST请求
    response = requests.post(url, data=json.dumps(data))

    # 输出响应结果
    print(response.text)


def startMain():
    connection = pymysql.connect(**conf.database)
    cursor = connection.cursor()
    sql = f"""
                    SELECT d.dict_label, COALESCE(SUM(a.score), 0) AS total_score
        FROM sys_dict_data d
        LEFT JOIN assessment_record a ON d.dict_label = a.company_name AND a.date >= '{current_date}'
        WHERE d.dict_type = 'bm_list'
        GROUP BY d.dict_label
        ORDER BY total_score;
                    """

    cursor.execute(sql)
    # 获取查询结果
    result = cursor.fetchall()

    dealresult(result)
    cursor.close()
    connection.close()


if __name__ == '__main__':
    startMain()
    # sendMsg(13951138,'县委十四届常委会第103次会议召开')



