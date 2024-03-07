import requests

cookies = {
    'Area': '271000',
    'AreaKey': 'gz',
    'MEIQIA_TRACK_ID': '2bfGOsqNY72YV76kTtfIya5A4Wk',
    'MEIQIA_VISIT_ID': '2bfGOsBtE7Z7NmPEMVEUwAjgLRN',
}

headers = {
    'authority': 'www.91goodschool.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'Area=271000; AreaKey=gz; MEIQIA_TRACK_ID=2bfGOsqNY72YV76kTtfIya5A4Wk; MEIQIA_VISIT_ID=2bfGOsBtE7Z7NmPEMVEUwAjgLRN',
    'origin': 'https://www.91goodschool.com',
    'referer': 'https://www.91goodschool.com/regist',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'mobile': '18728773736',
    'ticket': 't039oLWFKV092jnYra8BXX8XbeQsJzKvXzV0KSvJ2PsHqFSk5zZdkuAV096CeYBRYz28a0EoPiVNCzicYHBseAullBimv696t4IIpM4Rd6lCWa_UO6uMg-xzbzhAs-oTOgC',
    'randstr': '@nyD',
}

response = requests.post('https://www.91goodschool.com/ajax/sendregistcode', cookies=cookies, headers=headers, data=data)
print(response.text)