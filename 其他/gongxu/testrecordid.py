import requests

cookies = {
    'JSESSIONID': '2FBFE1F6184436312EB4751C84A2FE13',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=2FBFE1F6184436312EB4751C84A2FE13',
    'Referer': 'https://edu.chinahrt.com/',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'param': '1rjLpEqd3yKSioZ366q12ScthzgyEgBNIPqYFIvtVmXr7wg7MKbWQrMoolnIY/J4xnEb49Hvz8/4uEY5pZjhGkgASeT0Gen7Qnj7JRxQn9Ugy/WGiWMkzHjEAHjuNYgtWwhg63OigtMY3h4N2Hq2yOA1XHl1OS5nfKtTJdlVXu4USml6BR+DFHVbN23Iv3vyDFQDUqmcZhjmyLNgY4nxQmE+DyceUrHD1b9Oz583QJeR1V2SfMVSfrLFpF2kGRLBduY1w6w+ACpeg5iUdxaOcsO/NJs/YQ8uUFycTSxRmoKScZJsTIyUTpYuWPjrHqG3Ys27MVGAN63FDAIdBD986Ql2pbyt5PErOn67CG/MVmSvOUHQmi62AbHXTvhvVNJl2HBXADebbezEtewFQQHjEyc8r0b4IA8UTGoZj35hpC2HIWJzdCC1tEdEJf2cuqwOrlg8mwNUbOj2CawvzIkWQshgqnRlWjdyj7BRlTVURXOJX3nTTivHBPaJD5FvZoosnqxAglOQLrPkUlqKXZHH4WKKdmjoeJYdWzjO2O2OK0Snovzu3xjWL/hNYKxDXnC81rclZZmjl1S0OnjmL5X9o1i/BC822wd5O0vmkKJS1yc1bKmJqvzP+cPg3ULBBzd2ypLyczI7vDAnZbtZdbfIOw==',
}

response = requests.get('https://videoadmin.chinahrt.com/videoPlay/playEncrypt', params=params, cookies=cookies, headers=headers)
print(response.text)