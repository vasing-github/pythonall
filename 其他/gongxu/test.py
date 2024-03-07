import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Hrttoken': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk4MDAzMjgzMzM2QDE1MSIsIm1vYmlsZSI6IjEzNTY4NDcxMjY2IiwidXNlck5hbWUiOiI1MTM3MjMxOTgwMDMyODMzMzYiLCJ1c2VySWQiOiJwMXMwXzI1MzIyZTEyLTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcwOTc5NTAzMSwianRpIjoiMmMzMjNkNjkyOTQ2NGRlY2E0NzMxNmY2YWY1MThkNmQifQ.WF2xw43lxx9w_bJlf0S0DWNx4oqxS7OEXMNKNKFOQZw',
    'Origin': 'https://edu.chinahrt.com',
    'Referer': 'https://edu.chinahrt.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'appid': 'gp6-1',
    'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'courseId': '2c9ff022029b4d0fa3a64948fc00a73c',
    'trainplanId': 'b34287b27e1142fb9f00d0046e6a9ee9',
    'platformId': '151',
}

response = requests.get('https://gp.chinahrt.com/gp6/lms/stu/course/courseDetail', params=params, headers=headers, verify=False)
print(response.text)