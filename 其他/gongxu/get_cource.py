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
    url = 'https://gp.chinahrt.com/gp6/lms/stu/trainplanCourseHandle/selected_course?platformId=151&trainplanId='+trainplanId+'&curPage=1&pageSize=50&classType&learnFinish&selectCourseClassId'
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
    trainplanId = 'b98b59a9f5734ab08c09e98f53fa845e'
    ck = 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTgzZDU3N2IxZWZjNGY0M2E4YzlAMjc2IiwibW9iaWxlIjoiMTg3MzcyNDE3NDgiLCJ1c2VyTmFtZSI6IjQxMCoqKio0MDI1MjAwNDYyIiwidXNlcklkIjoiOWM5NGRlNjJkN2U4NDkxMzgyNmMyYzViZTE1MjVhNzQiLCJpYXQiOjE3MjQ1NDUxNDEsImp0aSI6IjBhYjA5ZjFiOTA1NDQ1MDVhNzQzZTc0ZDdmMDMzMzg0In0.tXsxIiV5FaYOVvATdp3T9foSKj07G_G01s3fOARKxFM'
    print(get_all_cource(ck,trainplanId))