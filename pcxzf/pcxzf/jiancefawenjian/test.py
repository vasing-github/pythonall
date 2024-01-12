import requests
from datetime import datetime, timedelta

# 计算开始和结束日期
endDate = datetime.now()
startDate = endDate - timedelta(days=30)

# 格式化日期
endDate_str = endDate.strftime('%Y-%m-%d')
startDate_str = startDate.strftime('%Y-%m-%d')
print(endDate_str)
cookies = {
    'HWWAFSESID': 'f75a576f6300770d41',
    'HWWAFSESTIME': '1704358245439',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'Bearer 94cb2b62-10f2-4a97-8f09-debd68462919',
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
print(response.json()['data']['notRectifiedNum'])