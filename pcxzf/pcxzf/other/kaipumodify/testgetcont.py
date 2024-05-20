import requests

cookies = {
    'authenticatecenterjsessionid': 'NDYzMDcxZWItOTlkOC00ZDA4LTg3Y2UtZDQyOGM2NmM2NDdi',
    'bz_govc_SHIROJSESSIONID': '4a6e79d7-6d24-4c7c-bb88-2945791d638b',
    'historyCookie': '%E5%B9%B3%E6%98%8C%E5%99%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%87%AA%E7%84%B6%E8%B5%84%E6%BA%90%E5%92%8C%E8%A7%84%E5%88%92%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%86%9C%E4%B8%9A%E5%86%9C%E6%9D%91%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%B4%A2%E6%94%BF%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%9E%8D%E5%AA%92%E4%BD%93%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E7%A4%BA%E8%8C%83%E5%B9%BC%E5%84%BF%E5%9B%AD%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B1%9F%E5%8F%A3%E6%B0%B4%E4%B9%A1%E6%B0%B4%E5%88%A9%E9%A3%8E%E6%99%AF%E5%8C%BA%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%B1%80%2C%E5%8E%BF%E5%86%9C%E4%B8%9A%E5%86%9C%E6%9D%91%E5%B1%80',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    # 'Cookie': 'authenticatecenterjsessionid=NDYzMDcxZWItOTlkOC00ZDA4LTg3Y2UtZDQyOGM2NmM2NDdi; bz_govc_SHIROJSESSIONID=1aee0a6d-3f13-44bd-9a17-dfd99b0ed07a; historyCookie=%E5%B9%B3%E6%98%8C%E5%8E%BF%E9%95%87%E9%BE%99%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%87%AA%E7%84%B6%E8%B5%84%E6%BA%90%E5%92%8C%E8%A7%84%E5%88%92%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%86%9C%E4%B8%9A%E5%86%9C%E6%9D%91%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%B4%A2%E6%94%BF%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%9E%8D%E5%AA%92%E4%BD%93%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E7%A4%BA%E8%8C%83%E5%B9%BC%E5%84%BF%E5%9B%AD%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B1%9F%E5%8F%A3%E6%B0%B4%E4%B9%A1%E6%B0%B4%E5%88%A9%E9%A3%8E%E6%99%AF%E5%8C%BA%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%B1%80%2C%E5%8E%BF%E5%86%9C%E4%B8%9A%E5%86%9C%E6%9D%91%E5%B1%80',
    'Referer': 'http://10.15.3.133:83/todolist/showDetail?typeCode=public_content&columnId=6603181&id=13940017&isOpen=true&_=1715850502563',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
}

params = {
    'contentId': '13853572',
    'organId': '6603181',
    'attribute': '',
    'IsAjax': '1',
    'dataType': 'JSON',
    '_': '1715850503020',
}

response = requests.get(
    'http://10.15.3.133:83/public/content/getPublicContent',
    params=params,
    cookies=cookies,
    headers=headers,
    verify=False,
)
print(response.text)