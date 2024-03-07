import requests

cookies = {
    'connect.sid': 's%3ASEaAKss5ESClFVATjQcveixY.LDdgOAKQ52MClqiUE3VOTjuPULuwptCO6r9NEPV6uqU',
}

headers = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'connect.sid=s%3ASEaAKss5ESClFVATjQcveixY.LDdgOAKQ52MClqiUE3VOTjuPULuwptCO6r9NEPV6uqU',
    'Referer': 'https://zfwzgl.www.gov.cn/boxpro/custom/index',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    '_t': '1706170667228',
}

response = requests.get('https://zfwzgl.www.gov.cn/boxpro/check_code', params=params, cookies=cookies, headers=headers)
print(response.text)