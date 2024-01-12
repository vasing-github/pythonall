import requests

cookies = {
    'PHPSESSID': 'hdoh3lra9jeuf12rnj504bio8d',
}

headers = {
    'authority': 'gvote.jasaas.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=hdoh3lra9jeuf12rnj504bio8d',
    'origin': 'https://gvote.jasaas.com',
    'referer': 'https://gvote.jasaas.com/subject/bz2023sdms.html',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'event': 'vote',
    'mobile': '19150471195',
    'subject': '1',
}

response = requests.post('https://gvote.jasaas.com/api/sms/send.html', cookies=cookies, headers=headers, data=data)
print(response.text)