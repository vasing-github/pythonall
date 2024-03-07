# -*- coding: utf-8 -*-
import requests
from datetime import datetime, timedelta
import conf
import json
import text

token = text.token
wait_fix = text.wait_fix
text_yinsi_num = text.text_yinsi_num
text_out_num = text.text_out_num
text_link_use_num = text.text_link_use_num

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


def save_data():
    with open('text.py', 'w') as f:
        f.write('token = \'' + token + '\'\n')
        f.write('wait_fix = ' + str(wait_fix) + '\n')
        f.write('text_yinsi_num = ' + str(text_yinsi_num) + '\n')
        f.write('text_out_num = ' + str(text_out_num) + '\n')
        f.write('text_link_use_num = ' + str(text_link_use_num) + '\n')


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
    print("out_link_num:",response.json()['data']['detail']['0'])
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
    print("yinsi_num:",response.json()['data']['allCount'])
    return response.json()['data']['allCount']
def start_search(token):

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
    if response.status_code !=200:
        new_token = get_new_token()
        wait_num = start_search(new_token)[2]
        return 1,new_token,wait_num
    waitrefix = response.json()['data']['notRectifiedNum']
    print('waitrefix:',waitrefix)
    print(response.text)
    return 0,'',waitrefix
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


def send_msg(cuomin, yinsi_num, outnum, kai_link_use_num, uptime= None):
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
        'Authorization': 'Bearer '+token,
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


if __name__ == '__main__':
    is_up_token, new_token, kaipu_waitrefix = start_search(token)
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

