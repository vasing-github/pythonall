import time

import requests

from 其他.xiaoxue.test4 import courseid


def upload_time(courseid):


    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Aspxauth': 'BearereyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTExMzc3LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3NTA0MTc3LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.oNlK2W_VvsB8ZYW22HKfdWpXbmb0Gk77D0TFrjxd3mM',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'token=BearereyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTExMzc3LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3NTA0MTc3LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.oNlK2W_VvsB8ZYW22HKfdWpXbmb0Gk77D0TFrjxd3mM; refreshToken=eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTkwNTc3LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3NTA0MTc3LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.atseULfA7j8r3GOWP8c3oSV5IsNdW-QzyDX2pHuEyTM; JSESSIONID=235E3B83CBA3352DC502534A005C461A',
        'Origin': 'https://www.hngbzx.gov.cn',
        'Referer': 'https://www.hngbzx.gov.cn/wechat/',
        'Refreshtoken': 'eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTkwNTc3LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3NTA0MTc3LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.atseULfA7j8r3GOWP8c3oSV5IsNdW-QzyDX2pHuEyTM',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36 Edg/128.0.0.0',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }



    json_data = {
        'courseId': str(courseid),
        'timeNode': '005959',
    }

    response = requests.post('https://www.hngbzx.gov.cn/api/mobile/uploadTimeNode', cookies=cookies, headers=headers, json=json_data)
    print(response.text)

def get_course(chanal):


    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Aspxauth': 'BearereyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTAxMTQxLCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3NDkzOTQxLCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.5liAZEbaJRE89MfsaGiQsdIuq0drLu-0U3RjItbT-8k',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'token=BearereyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTAxMTQxLCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3NDkzOTQxLCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.5liAZEbaJRE89MfsaGiQsdIuq0drLu-0U3RjItbT-8k; refreshToken=eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTgwMzQxLCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3NDkzOTQxLCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.8U3_H4nqfEVwEA3y2oavJCINbheeXNe57j9l4lxNZdo; JSESSIONID=49C6AF6B17BB4C5AAA8F70440829E632',
        'Origin': 'https://www.hngbzx.gov.cn',
        'Referer': 'https://www.hngbzx.gov.cn/wechat',
        'Refreshtoken': 'eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTgwMzQxLCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3NDkzOTQxLCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.8U3_H4nqfEVwEA3y2oavJCINbheeXNe57j9l4lxNZdo',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36 Edg/128.0.0.0',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    json_data = {
        'sort': 'id',
        'order': 'desc',
        'page': 1,
        'rows': 30,
        'channelId': chanal,
        'topicType': '',
    }

    response = requests.post(
        'https://www.hngbzx.gov.cn/api/mobile/getCourseInfoList',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(response.json()['data']['list'])
    return response.json()['data']['list']

def get_course_detail(c):


    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Aspxauth': 'BearereyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTExMzc3LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3NTA0MTc3LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.oNlK2W_VvsB8ZYW22HKfdWpXbmb0Gk77D0TFrjxd3mM',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'token=BearereyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTExMzc3LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3NTA0MTc3LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.oNlK2W_VvsB8ZYW22HKfdWpXbmb0Gk77D0TFrjxd3mM; refreshToken=eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTkwNTc3LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3NTA0MTc3LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.atseULfA7j8r3GOWP8c3oSV5IsNdW-QzyDX2pHuEyTM; JSESSIONID=7D5416367274170C4ADD66D0502C6D81',
        'Origin': 'https://www.hngbzx.gov.cn',
        'Referer': 'https://www.hngbzx.gov.cn/wechat/',
        'Refreshtoken': 'eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTkwNTc3LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3NTA0MTc3LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.atseULfA7j8r3GOWP8c3oSV5IsNdW-QzyDX2pHuEyTM',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36 Edg/128.0.0.0',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    json_data = {
        'id': str(c),
    }

    response = requests.post('https://www.hngbzx.gov.cn/api/mobile/getCourseDetail', cookies=cookies, headers=headers,
                             json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    # data = '{"id":"14099"}'
    # response = requests.post('https://www.hngbzx.gov.cn/api/mobile/getCourseDetail', cookies=cookies, headers=headers, data=data)

def get_second(c):


    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Aspxauth': 'BearereyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTExMzc3LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3NTA0MTc3LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.oNlK2W_VvsB8ZYW22HKfdWpXbmb0Gk77D0TFrjxd3mM',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'token=BearereyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTExMzc3LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3NTA0MTc3LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.oNlK2W_VvsB8ZYW22HKfdWpXbmb0Gk77D0TFrjxd3mM; refreshToken=eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTkwNTc3LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3NTA0MTc3LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.atseULfA7j8r3GOWP8c3oSV5IsNdW-QzyDX2pHuEyTM; JSESSIONID=EEB85424E75643EAFCEAA5E272BBED88',
        'Origin': 'https://www.hngbzx.gov.cn',
        'Referer': 'https://www.hngbzx.gov.cn/wechat/',
        'Refreshtoken': 'eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTkwNTc3LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3NTA0MTc3LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.atseULfA7j8r3GOWP8c3oSV5IsNdW-QzyDX2pHuEyTM',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36 Edg/128.0.0.0',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    json_data = {
        'courseId': c,
        'keyword': '',
        'page': 1,
        'rows': 10,
    }

    response = requests.post(
        'https://www.hngbzx.gov.cn/api/mobile/getCourseCommentList',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    # data = '{"courseId":14099,"keyword":"","page":1,"rows":10}'
    # response = requests.post('https://www.hngbzx.gov.cn/api/mobile/getCourseCommentList', cookies=cookies, headers=headers, data=data)

cookies = {
    'token': 'BearereyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi6I6r6JOdIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NTk1Njg1LCJ1c2VyaWQiOjIyNjE1NiwiaWF0IjoxNzI3NTg4NDg1LCJ1c2VybmFtZSI6Im1sMTUyMDMwNzQ1MjYifQ.JlSgIz2wn21KDZh7jY2ce7GX2We85dpwA6etJW-yN2Q',
    'refreshToken': 'eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi6I6r6JOdIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3Njc0ODg1LCJ1c2VyaWQiOjIyNjE1NiwiaWF0IjoxNzI3NTg4NDg1LCJ1c2VybmFtZSI6Im1sMTUyMDMwNzQ1MjYifQ.1eAkSTZY7ReNBvRWuS6atBVPSig3S_nS9b8a1RoETPc',
    'JSESSIONID': '216A9B94E866B07EE3EFE9F0102E401E',
}

if __name__ == '__main__':
    chanal_zhiding = 644
    chanal_bixiu = 560
    # chanal_xuanxiuzhuanti = 643
    # chanal_xuanxiukecheng = 51
    chanal_list = [chanal_zhiding]

    for chanal in chanal_list:
        courses = get_course(chanal)
        for course in courses:
            print(course['courseId'])
            get_course_detail(course['courseId'])
            get_second(course['courseId'])
            upload_time(course['courseId'])
            time.sleep(2)
            upload_time(course['courseId'])
            time.sleep(6)

    # upload_time(13964)



    # upload_time()