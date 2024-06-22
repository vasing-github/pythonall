import requests
def search():

    cookies = {
        'historyCookie': '%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%AC%E5%AE%89%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%B8%8D%E5%8A%A8%E4%BA%A7%E7%99%BB%E8%AE%B0%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E5%B1%80%2C%E4%B8%AD%E5%9B%BD%E6%94%BF%E5%BA%9C%E7%BD%91%2C%E5%8E%BF%E5%8D%AB%E7%94%9F%E5%81%A5%E5%BA%B7%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E6%B3%93%E6%BA%90%E5%B8%B8%E9%9D%92%E5%85%AC%E7%94%A8%E4%BA%8B%E4%B8%9A%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%9E%8D%E5%AA%92%E4%BD%93%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%B0%E8%8D%89%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E6%96%B0%E5%8D%8E%E7%A4%BE',
        'bz_govc_SHIROJSESSIONID': 'c1fe79d0-4665-4908-b249-a8a13f86a598',
    }
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'authenticatecenterjsessionid=NDYzMDcxZWItOTlkOC00ZDA4LTg3Y2UtZDQyOGM2NmM2NDdi; bz_govc_SHIROJSESSIONID=1aee0a6d-3f13-44bd-9a17-dfd99b0ed07a; historyCookie=%E5%B9%B3%E6%98%8C%E5%8E%BF%E9%95%87%E9%BE%99%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%87%AA%E7%84%B6%E8%B5%84%E6%BA%90%E5%92%8C%E8%A7%84%E5%88%92%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%86%9C%E4%B8%9A%E5%86%9C%E6%9D%91%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%B4%A2%E6%94%BF%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%9E%8D%E5%AA%92%E4%BD%93%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E7%A4%BA%E8%8C%83%E5%B9%BC%E5%84%BF%E5%9B%AD%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B1%9F%E5%8F%A3%E6%B0%B4%E4%B9%A1%E6%B0%B4%E5%88%A9%E9%A3%8E%E6%99%AF%E5%8C%BA%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%B1%80%2C%E5%8E%BF%E5%86%9C%E4%B8%9A%E5%86%9C%E6%9D%91%E5%B1%80',
        'Origin': 'http://10.15.3.133:83',
        # 'Referer': 'http://10.15.3.133:83/index;JSESSIONID=3e600d6e-405a-4581-909d-f696446239f3?s=1715842811771&siteId=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'isAjax': '1',
        'dataType': 'json',
    }

    data = {
        'title': '平昌县市场监督管理局:关于2批次食品不合格情况的通告（2024年第1期）',
        'typeCodes': 'articleNews,pictureNews,videoNews,messageBoard,workGuide,interviewInfo,public_content,grassroots_public',
        'sortField': 'createDate',
        'sortOrder': 'desc',
        'pageIndex': '0',
        'pageSize': '20',
    }

    response = requests.post(
        'http://10.15.3.133:83/content/getQueryPageByEngine',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )

    print(response.text)
    return response.json()


if __name__ == '__main__':
    content = search()
    print(content['data']['article']['id'])
