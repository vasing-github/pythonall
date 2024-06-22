# -*- coding: utf-8 -*-

import json
import os
import re
import sys
from datetime import datetime, timedelta
from io import BytesIO

import hudongcontent
import requests

import conf

current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目的根目录
project_root = os.path.abspath(os.path.join(current_dir, os.pardir))
# 将项目根目录添加到 sys.path
sys.path.append(project_root)

import kaipumodify.cfg.text as text
from kaipumodify.loginwz import getjsseion
from openpyxl import Workbook
from openpyxl import load_workbook
import getcontent2, getcontent

token = text.token
wait_fix = text.wait_fix
text_yinsi_num = text.text_yinsi_num
text_out_num = text.text_out_num
text_link_use_num = text.text_link_use_num
bz_gov_id = text.bz_gov_id
jid = text.jid

endDate = datetime.now()
startDate = endDate - timedelta(days=30)
endDate_str = endDate.strftime('%Y-%m-%d')
startDate_str = startDate.strftime('%Y-%m-%d')


def modify_wait_fix(num, yinsinum, outnum, linkusenum):
    global wait_fix, text_yinsi_num, text_out_num, text_link_use_num
    wait_fix = num
    text_yinsi_num = yinsinum
    text_out_num = outnum
    text_link_use_num = linkusenum


def modify_token(newtoken):
    global token
    token = newtoken


def modify_cookie(new_bz_gov_id, new_jid):
    global bz_gov_id, jid
    bz_gov_id = new_bz_gov_id
    jid = new_jid


def save_data():
    with open('text.py', 'w') as f:
        f.write('token = \'' + token + '\'\n')
        f.write('wait_fix = ' + str(wait_fix) + '\n')
        f.write('text_yinsi_num = ' + str(text_yinsi_num) + '\n')
        f.write('text_out_num = ' + str(text_out_num) + '\n')
        f.write('text_link_use_num = ' + str(text_link_use_num) + '\n')
        f.write('bz_gov_id = \'' + bz_gov_id + '\'\n')
        f.write('jid = \'' + jid + '\'\n')


def get_cuomin_list():
    cookies = {
        'HWWAFSESID': '49d6373a41e52c2bd8',
        'HWWAFSESTIME': '1716168884097',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': 'Bearer ' + token,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'HWWAFSESID=49d6373a41e52c2bd8; HWWAFSESTIME=1716168884097',
        'Origin': 'https://datais.ucap.com.cn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'page': {
            'size': 100,
            'current': 1,
        },
        'check': 1,
        'dataState': True,
        'dateType': 1,
        'codeType': 1,
        'custCode': '5119230005',
        'startDate': startDate_str,
        'endDate': endDate_str,
        'rectifyStatus': 0,
        'searchBox': '',
        'questionLevel': '',
        'labelIds': [],
        'resultType': '',
        'pageType': '',
        'recommendUpdateList': [],
        'protectCode': '5119230005',
        'custLevel': '1',
        'unitLevel': 3,
        'isHandoff': 1,
    }

    response = requests.post(
        'https://datais.ucap.com.cn/cloud-website-web/websiteSensitiveDetail/listPageByDto',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(response.text)
    return response.json()['data']['records']


def get_link_use_num(token):
    cookies = {
        'HWWAFSESID': 'b092d732d20af40cfc',
        'HWWAFSESTIME': '1709105903507',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': 'Bearer ' + token,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'HWWAFSESID=b092d732d20af40cfc; HWWAFSESTIME=1709105903507',
        'Origin': 'https://datais.ucap.com.cn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'startDate': startDate_str,
        'endDate': endDate_str,
        'status': 1,
        'dateType': 0,
        'isSure': 0,
        'urlType': '',
        'checkType': '',
        'siteInfo': '',
        'siteCustCode': '5119230005',
        'protectCode': '5119230005',
        'custLevel': '1',
        'unitLevel': 3,
        'isHandoff': 1,
    }

    response = requests.post(
        'https://datais.ucap.com.cn/cloud-website-web/websiteDeadLink/getStatisticsByQueryDto',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    a = response.json()['data']['channelNotRectified']
    b = response.json()['data']['homeNotRectified']
    print("link_use_num:", a + b)
    return a + b


def get_out_link(token):
    cookies = {
        'HWWAFSESID': 'b092d732d20af40cfc',
        'HWWAFSESTIME': '1709105903507',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': 'Bearer ' + token,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'HWWAFSESID=b092d732d20af40cfc; HWWAFSESTIME=1709105903507',
        'Origin': 'https://datais.ucap.com.cn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'page': {
            'size': 100,
            'current': 1,
        },
        'check': 1,
        'dataState': True,
        'dateType': 4,
        'inspectionType': 1,
        'startDate': startDate_str,
        'endDate': endDate_str,
        'codeType': 1,
        'codeTypeVal': [
            '5119230005',
        ],
        'pageType': '',
        'reviewType': '',
        'protectCode': '5119230005',
        'custLevel': '1',
        'unitLevel': 3,
        'isHandoff': 1,
    }

    response = requests.post(
        'https://datais.ucap.com.cn/cloud-website-web/websiteOutLink/reviewDetailStatistics',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print("out_link_num:", response.json()['data']['detail']['0'])
    return response.json()['data']['detail']['0']


def get_yinsi_num(token):
    cookies = {
        'HWWAFSESID': 'b092d732d20af40cfc',
        'HWWAFSESTIME': '1709105903507',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': 'Bearer ' + token,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'HWWAFSESID=b092d732d20af40cfc; HWWAFSESTIME=1709105903507',
        'Origin': 'https://datais.ucap.com.cn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'check': 1,
        'codeType': 1,
        'codeTypeVal': [
            '5119230005',
        ],
        'resultTypeList': [
            1,
            2,
        ],
        'dateType': 1,
        'startDate': startDate_str,
        'endDate': endDate_str,
        'page': {
            'size': 100,
            'current': 1,
        },
        'pageType': '',
        'reviewType': 0,
        'protectCode': '5119230005',
        'custLevel': '1',
        'unitLevel': 3,
        'isHandoff': 1,
    }

    response = requests.post(
        'https://datais.ucap.com.cn/cloud-website-web/websiteInfoLeakageMaster/reviewStatistics',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print("yinsi_num:", response.json()['data']['allCount'])
    return response.json()['data']['allCount']


def start_search():
    print(endDate_str)
    cookies = {
        'HWWAFSESID': '40854762319bc867f7',
        'HWWAFSESTIME': '1703639525975',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': 'Bearer ' + token,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'HWWAFSESID=40854762319bc867f7; HWWAFSESTIME=1703639525975',
        'Origin': 'https://datais.ucap.com.cn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'page': {
            'size': 10,
            'current': 1,
        },
        'check': 1,
        'codeType': 1,
        'dataState': True,
        'custCode': '5119230005',
        'dateType': 1,
        'startDate': startDate_str,
        'endDate': endDate_str,
        'rectifyStatus': '',
        'searchBox': '',
        'protectCode': '5119230005',
        'custLevel': '1',
        'unitLevel': 3,
        'isHandoff': 1,
    }

    response = requests.post(
        'https://datais.ucap.com.cn/cloud-website-web/websiteSensitiveDetail/getRectifiedNum',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(response.json())
    if response.status_code != 200:
        dealtoken()
        return start_search()
    waitrefix = response.json()['data']['notRectifiedNum']
    print('waitrefix:', waitrefix)

    return waitrefix


def dealtoken():
    print("get new token ..........")
    new_token = get_new_token()
    modify_token(new_token)
    save_data()


def get_new_token():
    cookies = {
        'HWWAFSESID': '40854762319bc867f7',
        'HWWAFSESTIME': '1703639525975',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': 'Basic dWNhcC1jbG91ZC1uZXdtZWRpYS13ZWItYXBwOnVjYXA=',
        'Connection': 'keep-alive',
        # 'Cookie': 'HWWAFSESID=40854762319bc867f7; HWWAFSESTIME=1703639525975',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'isToken': 'false',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'grant_type': 'custcode',
        'scope': 'server',
        'custCode': '5119230005',
        'custPassWord': 'gPMVQsFEv2EeGOCuhua3ZKEJYtPSYIod94HM341mnctbt6gl72Yl2QvzwUngHgOH4AaWXE1K3MIA1cu02+VpsW7U+2ncYyG8fArt6u9xSm+Zgh+34UfWu3EhMT24MhOVokS2A17Mdnvs6AG6ich2DndAAXd7b0LQvXUUAfV4kGo=',
    }

    response = requests.get('https://datais.ucap.com.cn/auth/oauth/token', params=params, cookies=cookies,
                            headers=headers)

    return response.json()["access_token"]


def send_msg(cuomin, yinsi_num, outnum, kai_link_use_num, uptime=None):
    # 定义要发送的消息内容
    # 获取当前时间，精确到分钟
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": f" 检测到开普云有新错敏<font color=\"warning\">{cuomin}</font>条\n\n隐私泄露<font color=\"warning\">{yinsi_num}</font>条\n\n外链暗链<font color=\"warning\">{outnum}</font>条\n\n链接不可用<font color=\"warning\">{kai_link_use_num}</font>条\n\n\n开普检测时间：{uptime}\n\n机器人检测时间：{current_time}\n<@WuXiaoLong>\n"
        }
    }

    key = conf.key_cs
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=" + key
    # 发送HTTP POST请求
    response = requests.post(url, data=json.dumps(data))

    # 输出响应结果
    print(response.text)


def get_kaipu_uptime(token):
    cookies = {
        'HWWAFSESID': '40854762319bc867f7',
        'HWWAFSESTIME': '1703639525975',
    }
    endDate = datetime.now()
    startDate = endDate - timedelta(days=30)

    # 格式化日期
    endDate_str = endDate.strftime('%Y-%m-%d')
    startDate_str = startDate.strftime('%Y-%m-%d')
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': 'Bearer ' + token,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'HWWAFSESID=40854762319bc867f7; HWWAFSESTIME=1703639525975',
        'Origin': 'https://datais.ucap.com.cn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'page': {
            'size': 10,
            'current': 1,
        },
        'check': 1,
        'dataState': True,
        'dateType': 1,
        'codeType': 1,
        'custCode': '5119230005',
        'startDate': startDate_str,
        'endDate': endDate_str,
        'rectifyStatus': 0,
        'searchBox': '',
        'questionLevel': '',
        'labelIds': [],
        'resultType': '',
        'pageType': '',
        'recommendUpdateList': [],
        'protectCode': '5119230005',
        'custLevel': '1',
        'unitLevel': 3,
        'isHandoff': 1,
    }

    response = requests.post(
        'https://datais.ucap.com.cn/cloud-website-web/websiteSensitiveDetail/listPageByDto',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(token)
    print(response.json()['data']['records'][0]['updateTime'])
    return response.json()['data']['records'][0]['updateTime']


def kaipucorrect(ids):
    cookies = {
        'HWWAFSESID': '49d6373a41e52c2bd8',
        'HWWAFSESTIME': '1716168884097',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': 'Bearer ' + token,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'HWWAFSESID=49d6373a41e52c2bd8; HWWAFSESTIME=1716168884097',
        'Origin': 'https://datais.ucap.com.cn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'ids': ids,
        'rectifyStatus': 1,
    }

    response = requests.post(
        'https://datais.ucap.com.cn/cloud-website-web/websiteSensitiveDetail/updateCheckTypeByIds',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(response.text)


def get_all_tips():
    is_up_token, new_token, kaipu_waitrefix = start_search()
    yinsi_num = get_yinsi_num(new_token if is_up_token else token)
    kai_out_num = get_out_link(new_token if is_up_token else token)
    kai_link_use_num = get_link_use_num(new_token if is_up_token else token)

    if kaipu_waitrefix != 0 or yinsi_num != 0 or kai_out_num != 0 or kai_link_use_num != 0:
        if wait_fix < kaipu_waitrefix or text_yinsi_num < yinsi_num or text_out_num < kai_out_num or text_link_use_num < kai_link_use_num:
            # 执行更新语句，更新数据
            modify_wait_fix(kaipu_waitrefix, yinsi_num, kai_out_num, kai_link_use_num)
            uptime = ''
            if kaipu_waitrefix != 0:
                uptime = get_kaipu_uptime(new_token if is_up_token else token)
            send_msg(kaipu_waitrefix, yinsi_num, kai_out_num, kai_link_use_num, uptime)
        if wait_fix != kaipu_waitrefix or yinsi_num != text_yinsi_num or text_out_num != kai_out_num or text_link_use_num != kai_link_use_num:
            modify_wait_fix(kaipu_waitrefix, yinsi_num, kai_out_num, kai_link_use_num)
    else:
        if wait_fix != kaipu_waitrefix or yinsi_num != text_yinsi_num or text_out_num != kai_out_num or text_link_use_num != kai_link_use_num:
            modify_wait_fix(kaipu_waitrefix, yinsi_num, kai_out_num, kai_link_use_num)

    if is_up_token:
        modify_token(new_token)

    save_data()


def get_new_bzid_jid():
    print("bz_gov_id token press...........")
    new_bz_gov_id, new_jid = getjsseion.get_new_cookie()
    modify_cookie(new_bz_gov_id, new_jid)
    save_data()


def isgetnewsseion(res):
    pass


def add_to_correct(correctlist, correctids, cuomin):
    correctids.append(cuomin['id'])
    correctlist.append((cuomin['sensitiveWords'], cuomin['recommendUpdate'], cuomin['snapshotNew'], cuomin['url'],
                        cuomin['parentUrl'], cuomin['pageTypeMeaning'], cuomin['parentTitle']))


def cuo_1_argument(numbers, cuomin, correctlist, correctids):
    res = getcontent2.getcontent(numbers[0], bz_gov_id, jid)
    if res['status'] == -9:
        get_new_bzid_jid()
        res = getcontent2.getcontent(numbers[0], bz_gov_id, jid)
    getcontent2.savearticnews(res, cuomin['sensitiveWords'], cuomin['recommendUpdate'], bz_gov_id,
                              jid)
    add_to_correct(correctlist, correctids, cuomin)


def cuo_2_aruments(numbers, cuomin, correctlist, correctids):
    res = getcontent.getcontent(numbers[0], numbers[1], bz_gov_id, jid)
    if res['status'] == -9:
        get_new_bzid_jid()
        res = getcontent.getcontent(numbers[0], numbers[1], bz_gov_id, jid)
    getcontent.saveorupdate(res, cuomin['sensitiveWords'], cuomin['recommendUpdate'], bz_gov_id,
                            jid)
    add_to_correct(correctlist, correctids, cuomin)


def cuo_hudong(cuomin, correctlist, correctids):
    hudongcontent.start_kaipu(cuomin, bz_gov_id, jid)
    add_to_correct(correctlist, correctids, cuomin)


def dealcuo():
    kaipu_waitrefix = start_search()
    if kaipu_waitrefix != 0:

        list_cuomin = get_cuomin_list()
        correctlist = []
        correctids = []
        for cuomin in list_cuomin:
            if cuomin['pageType'] == "3":  # 表示是文章类型
                if cuomin['column'] != '互动交流':
                    numbers = re.findall(r'\d+', cuomin['url'])
                    # 将提取出的数字转换为整数
                    numbers = [int(num) for num in numbers]
                    # 判断 URL 类型并返回结果
                    if len(numbers) == 1:
                        cuo_1_argument(numbers, cuomin, correctlist, correctids)
                    elif len(numbers) == 2:
                        cuo_2_aruments(numbers, cuomin, correctlist, correctids)
                    else:
                        print("未知情况")
                        send_nosee()


                elif cuomin['column'] == '互动交流':
                    cuo_hudong(cuomin, correctlist, correctids)

        send_correct_msg(correctlist)
        kaipucorrect(correctids)


def send_nosee():
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": f" 检测到开普云有新类型错敏，机器人无法修改，请人工核实。\n<@WuXiaoLong>\n"
        }
    }

    key = conf.key_cs
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=" + key
    # 发送HTTP POST请求
    response = requests.post(url, data=json.dumps(data))

    # 输出响应结果
    print(response.text)


def send_correct_msg(correctlist):
    key = conf.key_cs

    wb = Workbook()

    ws = wb.active

    row = ws.max_row if ws.max_row == 1 else ws.max_row + 2

    # 合并单元格设置标题和表头
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=4)
    ws.cell(row=row, column=1).value = '机器人改错记录  ' + endDate_str
    # 设置合并后单元格的字体样式
    ws.cell(row=row, column=1).font = conf.tittle_font

    ws.append(['错敏词', '修改词', '快照', '地址', '父地址', '错敏类型', '父标题'])
    # 设置新添加的行的字体为加粗
    for row in [ws[row + 1]]:
        for cell in row:
            cell.font = conf.header_font

    # 遍历字典

    for tup in correctlist:
        ws.append(tup)
    ws.column_dimensions['A'].width = 20
    # 设置列A的宽度为50
    ws.column_dimensions['B'].width = 20
    ws.column_dimensions['C'].width = 20
    ws.column_dimensions['D'].width = 20
    ws.column_dimensions['E'].width = 20
    # 保存文件

    formatted_date = endDate.strftime('%Y-%m-%d %H_%M_%S')  # 使用下划线代替冒号
    filename = conf.correct_name + formatted_date + '.xlsx'
    wb.save(filename)
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=" + key

    # 加载现有的Excel文件
    wb = load_workbook(filename)
    # 获取活动工作表

    # 将工作簿保存到一个字节流中
    output = BytesIO()
    wb.save(output)

    # 准备发送文件
    files = {"file": (filename, output.getvalue())}
    response = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=' + key + '&type=file',
        files=files)

    print(response.text)

    # 检查是否有'media_id'在响应中
    if 'media_id' in response.json():
        # 发送消息
        headers = {"Content-Type": "application/json"}
        message = {
            "msgtype": "file",
            "file": {
                "media_id": response.json()["media_id"]
            }
        }
        response = requests.post(url, headers=headers, json=message)

        # 输出响应结果
        print(response.text)
    else:
        print("No media_id in response")


if __name__ == '__main__':
    dealcuo()
    # formatted_date = endDate.strftime('%Y-%m-%d %H_%M_%S')  # 使用下划线代替冒号
    # filename = conf.correct_name + formatted_date + '.xlsx'
    # print(filename)
    # getjsseion.hello()
