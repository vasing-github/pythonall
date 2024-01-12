import requests

cookies = {
    'HWWAFSESID': '40854762319bc867f7',
    'HWWAFSESTIME': '1703639525975',
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
    'check': 1,
    'dataState': True,
    'dateType': 1,
    'codeType': 1,
    'custCode': '5119230005',
    'startDate': '2023-12-11',
    'endDate': '2024-01-10',
    'rectifyStatus': 0,
    'searchBox': '',
    'questionLevel': '',
    'labelIds': [],
    'resultType': '',
    'pageType': '',
    'recommendUpdateList': [],
    'checkType': 0,
    'exportType': 0,
    'protectCode': '5119230005',
    'custLevel': '1',
    'unitLevel': 3,
    'isHandoff': 1,
}

response = requests.post(
    'https://datais.ucap.com.cn/cloud-website-web/websiteSensitiveDetail/exportDataExcel',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
print(response.text)