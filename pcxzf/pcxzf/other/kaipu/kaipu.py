import requests
from datetime import datetime, timedelta
import sql
import conf
import json
def start_search(token):
    # 计算开始和结束日期
    endDate = datetime.now()
    startDate = endDate - timedelta(days=30)

    # 格式化日期
    endDate_str = endDate.strftime('%Y-%m-%d')
    startDate_str = startDate.strftime('%Y-%m-%d')
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
    print(waitrefix)
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
def send_msg(msg,uptime):
    # 定义要发送的消息内容
    # 获取当前时间，精确到分钟
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": f" 检测到开普云有新错敏<font color=\"warning\">{msg}</font>条\n\n\n开普检测时间：{uptime}\n\n机器人检测时间：{current_time}\n<@WuXiaoLong>\n"
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

    connection, cursor = sql.create_connection()
    sql_result = sql.execute_query(connection, cursor, "SELECT * FROM recordsth WHERE recordname = 'kaipuyun'")
    print(sql_result)
    print(sql_result[0][2])
    print('-----------------------------')

    is_up_token,new_token,kaipu_waitrefix = start_search(sql_result[0][2])
    # 将查询到的数据与您现有的数据进行比较

    if kaipu_waitrefix != 0:
        if sql_result[0][1] < kaipu_waitrefix:
            # 执行更新语句，更新数据
            sql.update_data(connection, cursor,
                            "UPDATE recordsth SET num_int = {} WHERE recordname = 'kaipuyun'".format(kaipu_waitrefix))
            uptime = get_kaipu_uptime(new_token if is_up_token else sql_result[0][2])
            send_msg(kaipu_waitrefix,uptime)
    else:
        if sql_result[0][1] != kaipu_waitrefix:
            sql.update_data(connection, cursor,
                            "UPDATE recordsth SET num_int = {} WHERE recordname = 'kaipuyun'".format(kaipu_waitrefix))

    if is_up_token:
        sql.update_data(connection, cursor,
                        "UPDATE recordsth SET num_str = '{}' WHERE recordname = 'kaipuyun'".format(new_token))

    sql_result = sql.execute_query(connection, cursor, "SELECT * FROM recordsth WHERE recordname = 'kaipuyun'")
    print(sql_result)
    print(sql_result[0][2])


    sql.close_connection(connection, cursor )

