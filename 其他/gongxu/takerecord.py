import requests
import conf
def taskrecord(recordid,studycode,src,sectionid,studytime, userid,planid):
    cookies = {
        'JSESSIONID': conf.jessionid,
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'JSESSIONID=2CB53C6C9987FBB99B324B1EB2B5C971',
        'Origin': 'https://videoadmin.chinahrt.com',
        'Referer': src,
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
        'studyCode': studycode,
        'updateRedisMap': '1',
        'recordId': recordid,
        'sectionId': sectionid,
        'signId': '151#'+planid+'#'+userid,
        # 'signId': '151#97624af4fdea4442890d4c257dbe83f2#db94e12f4a9d45a19936bc304cbe26c4',

        'time': studytime,
        'businessId': 'gp5',
    }
    # print(data)

    response = requests.post('https://videoadmin.chinahrt.com/videoPlay/takeRecord', cookies=cookies, headers=headers, data=data)
    print(response.text)
    return response.json()['status']

