import requests

cookies = {
    'JSESSIONID': 'FD21F1BB1DF3BCAC757A82BA643A6CB4',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'JSESSIONID=FD21F1BB1DF3BCAC757A82BA643A6CB4',
    'Origin': 'https://videoadmin.chinahrt.com',
    # 'Referer': 'https://videoadmin.chinahrt.com/videoPlay/playEncrypt?param=1rjLpEqd3yKSioZ366q12ScthzgyEgBNIPqYFIvtVmXr7wg7MKbWQrMoolnIY%2FJ4xnEb49Hvz8%2F4uEY5pZjhGkgASeT0Gen7Qnj7JRxQn9Ugy%2FWGiWMkzHjEAHjuNYgtWwhg63OigtMY3h4N2Hq2yOA1XHl1OS5nfKtTJdlVXu4USml6BR%2BDFHVbN23Iv3vyDFQDUqmcZhjmyLNgY4nxQmE%2BDyceUrHD1b9Oz583QJeR1V2SfMVSfrLFpF2kGRLBduY1w6w%2BACpeg5iUdxaOcsO%2FNJs%2FYQ8uUFycTSxRmoKScZJsTIyUTpYuWPjrHqG3Ys27MVGAN63FDAIdBD986Ql2pbyt5PErOn67CG%2FMVmSvOUHQmi62AbHXTvhvVNJl2HBXADebbezEtewFQQHjEyc8r0b4IA8UTGoZj35hpC2HIWJzdCC1tEdEJf2cuqwOLD0PnKkoPax4jIeMBvdgpJk0Y3SN%2F2cIH%2F2h3i0Xd%2BbwAsHCeznk%2Fu5Xy1homPBDYClJH10LcO%2Bsa4DE30j7KP0fD9mjNkYOYkkKANIsmDcoKxoNHQ%2BBlqd6jeGVOpjrmLNflb%2BL%2B88lfZ6ThbZ1%2BG7GFQ1SWeFF0g%2F8eWcJRNMIvc0mNy6pP3ZRptZEbP94ieXOsaZ%2Fe%2FSeNvZb0orX0gHH7tlU8aUCLgiSXr%2FiVJ0%3D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'studyCode': 'jhkSd0Td0vvJMu3DtFJ7O',
    'updateRedisMap': '1',
    'recordId': 'Kr8TAHWsRx5OTUurFmDZB',
    'sectionId': 'e0QdGP6T7NPtjbW3Ec8ud1-2',
    'signId': '151#b34287b27e1142fb9f00d0046e6a9ee9#p1s0_25322e12-92be-11e3-b77c-d4ae526c695b',
    'time': '2000.42365',
    'businessId': 'gp5',
}

response = requests.post('https://videoadmin.chinahrt.com/videoPlay/takeRecord', cookies=cookies, headers=headers, data=data)
print(response.text)