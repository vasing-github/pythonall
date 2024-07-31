# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

import requests
import text
import conf
token = text.token

endDate = datetime.now()
startDate = endDate - timedelta(days=30)

endDate_str = endDate.strftime('%Y-%m-%d')
startDate_str = startDate.strftime('%Y-%m-%d')

cuomin_start_date = endDate - timedelta(days=7)
cuomin_start_date_str = cuomin_start_date.strftime('%Y-%m-%d')

current_time = endDate.strftime('%Y-%m-%d %H:%M:%S')


def oauth():
    cookies = {
        'Path': '/',
        'Path': '/',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Authorization': 'Basic dWNhcC1jbG91ZC1uZXdtZWRpYS13ZWItYXBwOnVjYXA=',
        'Connection': 'keep-alive',
        # 'Cookie': 'Path=/; Path=/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'isToken': 'false',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'grant_type': 'custcode',
        'scope': 'server',
        'custCode': '511900',
        'custPassWord': 'Br1HpHrNS2U/wnper1/OOrWq1ZFktsJBKuuMmeVIbE43RnlGFirEuoMz3Mm9U6DRGGxecBBqc+YrqAPz+SCzLYmJuakNQVROXOH6ZtPQ1bqLsgQFbvhcsa80twh/GDsDKzQ2ZxTPAGXSyEtceI4rdQfXxPDMYv8SFjO2OTSCZ+Y=',
    }

    response = requests.get('https://datais.ucap.com.cn/auth/oauth/token', params=params, cookies=cookies,
                            headers=headers)
    return response.json()["access_token"]


def get_cuomin_list():
    cookies = {
        'Path': '/',
        'Path': '/',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Authorization': 'Bearer ' + token,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'Path=/; Path=/',
        'Origin': 'https://datais.ucap.com.cn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'page': {
            'size': 2000,
            'current': 1,
        },
        'check': 1,
        'dataState': True,
        'dateType': 1,
        'codeType': 0,
        'custCode': '511900',
        'startDate': cuomin_start_date_str,
        'endDate': endDate_str,
        'rectifyStatus': 0,
        'searchBox': '',
        'questionLevel': '',
        'labelIds': [],
        'resultType': '',
        'pageType': '',
        'recommendUpdateList': [],
        'protectCode': '511900',
        'custLevel': '0',
        'unitLevel': 2,
        'isHandoff': 1,
    }

    response = requests.post(
        'https://datais.ucap.com.cn/cloud-website-web/websiteSensitiveDetail/listPageByDto',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    if response.status_code != 200:
        dealtoken()
        return get_cuomin_list()
    return response.json()


def modify_token(newtoken):
    global token
    token = newtoken


def save_data():
    with open('text.py', 'w') as f:
        f.write('token = \'' + token + '\'\n')


def dealtoken():
    print("token  press get new..............")
    new_token = oauth()
    modify_token(new_token)
    save_data()


def send_msg(data):
    # 发送请求
    response = requests.post(
        'https://www.pushplus.plus/api/send',
        headers={
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'Cookie': 'Hm_lvt_1c61e24eff639e825f5a3d7f957635c6=1720596043; HMACCOUNT=0803B689966FD539; pushToken=7d2e9476f37d4f5c97a3843e2127a0b7; Hm_lpvt_1c61e24eff639e825f5a3d7f957635c6=1720596060',
            'Origin': 'https://www.pushplus.plus',
            'Referer': 'https://www.pushplus.plus/push2.html',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'pushToken': '7d2e9476f37d4f5c97a3843e2127a0b7',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        },
        json=data
    )

    print(response.text)


def getoutlink():
    cookies = {
        'Path': '/',
        'HWWAFSESID': '36ac173061f98f7d6f',
        'HWWAFSESTIME': '1721186085080',
        'Path': '/',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Authorization': 'Bearer ' + token,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'Path=/; HWWAFSESID=36ac173061f98f7d6f; HWWAFSESTIME=1721186085080; Path=/',
        'Origin': 'https://datais.ucap.com.cn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'page': {
            'size': 5000,
            'current': 1,
        },
        'check': 1,
        'dataState': True,
        'dateType': 4,
        'inspectionType': 1,
        'startDate': startDate_str,
        'endDate': endDate_str,
        'codeType': 0,
        'codeTypeVal': [
            '511900',
        ],
        'pageType': '',
        'reviewType': 0,
        'protectCode': '511900',
        'custLevel': '0',
        'unitLevel': 2,
        'isHandoff': 1,
    }

    response = requests.post(
        'https://datais.ucap.com.cn/cloud-website-web/websiteOutLink/listDetailByDto',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    return response.json()


def get_link_use():
    cookies = {
        'Path': '/',
        'HWWAFSESID': '36ac173061f98f7d6f',
        'HWWAFSESTIME': '1721186085080',
        'Path': '/',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Authorization': 'Bearer ' + token,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'Path=/; HWWAFSESID=36ac173061f98f7d6f; HWWAFSESTIME=1721186085080; Path=/',
        'Origin': 'https://datais.ucap.com.cn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'page': {
            'size': 300,
            'current': 1,
        },
        'dateType': 0,
        'isSure': 0,
        'startDate': startDate_str,
        'endDate': endDate_str,
        'urlType': '',
        'checkType': 0,
        'siteInfo': '',
        'status': 1,
        'parentCustCode': '511900',
        'sortField': 'scan_time',
        'sortFlag': False,
        'linkUrl': '',
        'protectCode': '511900',
        'custLevel': '0',
        'unitLevel': 2,
        'isHandoff': 1,
    }

    response = requests.post(
        'https://datais.ucap.com.cn/cloud-website-web/websiteDeadLink/listPageByQueryDto',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    return response.json()


def get_update():
    cookies = {
        'Path': '/',
        'HWWAFSESID': '36ac173061f98f7d6f',
        'HWWAFSESTIME': '1721186085080',
        'Path': '/',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Authorization': 'Bearer ' + token,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'Path=/; HWWAFSESID=36ac173061f98f7d6f; HWWAFSESTIME=1721186085080; Path=/',
        'Origin': 'https://datais.ucap.com.cn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'page': {
            'size': 5000,
            'current': 1,
        },
        'statisticsDate': endDate_str,
        'parentCode': '511900',
        'upStatus2List': [
            3,
        ],
        'sortField': 'up_status',
        'sortFlag': False,
        'custLevel': '0',
        'unitLevel': 2,
        'channelName': '',
        'status': '',
        'updateTimeLimit': '',
        'siteInfo': '',
        'protectCode': '511900',
        'isHandoff': 1,
    }

    response = requests.post(
        'https://datais.ucap.com.cn/cloud-website-web/websiteChannelUpdateMonitor/listPageByQueryDto',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    return response.json()


def get_yinsi():
    cookies = {
        'Path': '/',
        'HWWAFSESID': '7ff857355c8b68535f',
        'HWWAFSESTIME': '1721353697724',
        'Path': '/',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Authorization': 'Bearer '+token,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'Path=/; HWWAFSESID=7ff857355c8b68535f; HWWAFSESTIME=1721353697724; Path=/',
        'Origin': 'https://datais.ucap.com.cn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'page': {
            'size': 5000,
            'current': 1,
        },
        'check': 1,
        'resultTypeList': [
            1,
            2,
        ],
        'dateType': 1,
        'codeType': 0,
        'codeTypeVal': [
            '511900',
        ],
        'startDate': startDate_str,
        'endDate': endDate_str,
        'pageType': '',
        'reviewType': 0,
        'protectCode': '511900',
        'custLevel': '0',
        'unitLevel': 2,
        'isHandoff': 1,
    }

    response = requests.post(
        'https://datais.ucap.com.cn/cloud-website-web/websiteInfoLeakageMaster/listByDto',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    return response.json()


def makedata(site_counts, title):
    units_table = "| 单位名称 | 数量 |\n| :----- | :--: |\n"
    for site_name, count in site_counts.items():
        units_table += f"| {site_name} | {count} |\n"
    data = {
        "topic": conf.topic,
        "token": conf.token,
        "title": title,
        "content": f"{units_table}\n```markdown\n{current_time}\n免登录接收开普云消息提醒，关闭公众号消息免打扰，每天定时接收错敏数据、栏目更新、死链外链等网站监测数据。",
        "template": "markdown",
        "channel": "wechat"
    }
    return data


def deal_res(response, title):
    list_cuomin = response['data']['records']
    site_counts = {}

    for cuomin in list_cuomin:
        site_name = cuomin['siteName']
        if site_name in site_counts:
            site_counts[site_name] += 1
        else:
            site_counts[site_name] = 1
    data = makedata(site_counts, title)
    send_msg(data)


def cuominfunc():
    response = get_cuomin_list()
    deal_res(response, '错敏提醒')


def outlinkfun():
    response = getoutlink()
    deal_res(response, '外链提醒')


def linusefunc():
    response = get_link_use()
    deal_res(response, '死链提醒')


def updatefunc():
    response = get_update()
    deal_res(response, '栏目更新提醒')


def yinsifunc():
    response = get_yinsi()
    deal_res(response, '隐私泄露提醒')


if __name__ == '__main__':
    cuominfunc()
    outlinkfun()
    linusefunc()
    updatefunc()
    yinsifunc()
