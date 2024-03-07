import requests

cookies = {
    'HWWAFSESID': 'b092d732d20af40cfc',
    'HWWAFSESTIME': '1709105903507',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Authorization': 'Bearer 388ee97f-ae8b-4c4e-acad-f9a6087bdff9',
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
    'startDate': '2024-01-30',
    'endDate': '2024-02-29',
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
print(response.text)
print("yinsi_num:", response.json()['data']['allCount'])