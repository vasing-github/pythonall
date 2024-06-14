import requests
import conf
def get_all_cource(ck, trainplanId):

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Hrttoken': ck,
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
    url = 'https://gp.chinahrt.com/gp6/lms/stu/trainplanCourseHandle/selected_course?platformId=151&trainplanId='+trainplanId+'&curPage=1&pageSize=20&classType&learnFinish&selectCourseClassId'
    # print(url)
    response = requests.get(url,headers=headers,verify = False)
    # print(response.text)
    list_cource = response.json()['data']['courseStudyList']
    ret_list = []
    for cource in list_cource:
        if cource['learnPercent'] == '100':
            continue
        ret_list.append(cource['courseId'])
    return ret_list


if __name__ == '__main__':
    trainplanId = '578c78426b91414096f0f94d26f335e6'
    ck = 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk3NjEwMjQwMTA2QDE1MSIsIm1vYmlsZSI6IjEzNTY4NDg5ODM4IiwidXNlck5hbWUiOiI1MTM3MjMxOTc2MTAyNDAxMDYiLCJ1c2VySWQiOiJwMXMwXzIyY2YwZDg0LTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcxNzczMzgwNCwianRpIjoiNmJkYTcxYWUyZGM5NGUyM2JmYTMyYWUxZTgyODNhNzMifQ.ZuWvzBtNItvTBMkbeqLkCP2OSNP9pKZyKY7F_mhq2Us'
    print(get_all_cource(ck,trainplanId))