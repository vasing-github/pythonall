import base64
import json
import random
import time

import requests
from Crypto.Cipher import AES
from bs4 import BeautifulSoup


def millisecond_to_time(ms):
    seconds = ms // 1000
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def format_str(c, a):
    l = ""
    k = len(str(c))
    if k > 0:
        if k + 2 > a:
            return str(c)
        else:
            g = a - k - 2
            h = 10 ** g
            b = random.randint(0, h - 1)
            f = len(str(b))
            if f < g:
                b = b * (10 ** (g - f))
            l += f"{k:02}" + str(c) + str(b)
    else:
        return str(c)
    return l


def encrypt(e):
    b = "bGVhcm5zcGFjZWFlczEyMw=="
    c = base64.b64decode(b).decode('utf-8')
    f = AES.new(c.encode('utf-8'), AES.MODE_ECB)
    padded_e = e + (16 - len(e) % 16) * chr(16 - len(e) % 16)
    d = f.encrypt(padded_e.encode('utf-8'))
    return base64.b64encode(d).decode('utf-8')


def gets(c, s, a, p):
    A = {
        "courseId": c,
        "endTime": s + a,
        "interval": True,
        "itemId": p,
        "playComplete": False,
        "position": s + a,
        "recordType": "interval",
        "startTime": s,
        "videoTotalTime": "00:39:32"
    }

    u = abs(A["endTime"] - A["startTime"])
    A["studyTimeLong"] = 0 if (u <= 1 and u > 0) else u
    A["startTimeStr"] = millisecond_to_time(A["startTime"] * 1000)
    A["endTimeStr"] = millisecond_to_time(A["endTime"] * 1000)

    x = {
        "courseId": A["courseId"],
        "itemId": A["itemId"],
        "time1": format_str(int(time.time() * 1000), 20),
        "time2": format_str(int(A["startTime"]), 20),
        "time3": format_str(36 * 60 + 6, 20),  # Convert "00:36:06" to seconds
        "time4": format_str(int(A["endTime"]), 20),
        "videoIndex": 0,
        "time5": format_str(A["studyTimeLong"], 20),
        "terminalType": 0,
        "recordType": A["recordType"]
    }

    s = encrypt(json.dumps(x))

    return s


def get_vedio_time(section_id, point_id):
    # cookies = {
    #     'dumaScrollAreaId_17CookieName': '0',
    #     'JSESSIONID': 'B0AC083F9AE16D6771FB46C3EC4F8E38.learnspace-tomcat-0010_learnspace_learning_aliyun',
    #     'learnspace_learning_https': 'c96f70eaa34a28797e1e54e16104eeb0',
    #     'language': 'zh_CN',
    #     'UNTYXLCOOKIE': '"Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="',
    #     'learning-course': 'd5e19c05fe784c8ca1808e217aa80daf_f54137387c454fc69ee92637f0c8c1d0___',
    #     '_uid': '5f6c7a82-9179-437f-8cc8-c9baeb73fb3a',
    # }
    #
    # headers = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    #     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #     'Connection': 'keep-alive',
    #     # 'Cookie': 'dumaScrollAreaId_17CookieName=0; JSESSIONID=B0AC083F9AE16D6771FB46C3EC4F8E38.learnspace-tomcat-0010_learnspace_learning_aliyun; learnspace_learning_https=c96f70eaa34a28797e1e54e16104eeb0; language=zh_CN; UNTYXLCOOKIE="Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="; learning-course=d5e19c05fe784c8ca1808e217aa80daf_f54137387c454fc69ee92637f0c8c1d0___; _uid=5f6c7a82-9179-437f-8cc8-c9baeb73fb3a',
    #     'Referer': 'https://yxdzcbs-kfkc.webtrn.cn/learnspace/learn/learn/templatethree/courseware_index.action?params.courseId=f54137387c454fc69ee92637f0c8c1d0___',
    #     'Sec-Fetch-Dest': 'iframe',
    #     'Sec-Fetch-Mode': 'navigate',
    #     'Sec-Fetch-Site': 'same-origin',
    #     'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    #     'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': '"Windows"',
    # }

    params = {
        'params.courseId': courseid,
        'params.itemId': point_id,
        'params.templateStyleType': '',
        'params.parentId': section_id,
        'params.videoTime': '8',
        'params.connItem': point_id,
        '_t': '1724310738016',
    }

    response = requests.get(
        'https://yxdzcbs-kfkc.webtrn.cn/learnspace/learn/learn/templatethree/content_video.action',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到id为videoTime的input标签
    video_time_input = soup.find('input', id='videoTime')

    if video_time_input:
        # 获取value属性的值
        time_str = video_time_input['value']

        # 将时间字符串转换为秒数
        h, m, s = map(int, time_str.split(':'))
        total_seconds = h * 3600 + m * 60 + s

        print(f"视频时长为 {total_seconds} 秒")
        return total_seconds
    else:
        print("未找到id为videoTime的input标签")


def get_all_course_itemid():
    params = {
        'params.courseId': courseid,
    }

    response = requests.get(
        'https://yxdzcbs-kfkc.webtrn.cn/learnspace/learn/learn/templatethree/courseware_index.action',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    return response


def bs4_get_dic(response):
    soup = BeautifulSoup(response.text, 'html.parser')

    learn_menu = soup.find('div', id='learnMenu')
    resources_dict = {}

    if learn_menu:
        chapters = learn_menu.find_all('div', class_='s_chapter')
        for chapter in chapters:
            chapter_id = chapter.get('id').split('_')[-1]
            resources_dict[chapter_id] = {}

            sections = chapter.find_next_sibling('div', class_='s_sectionlist').find_all('div', class_='s_section')
            for section in sections:
                section_id = section.get('id').split('_')[-1]
                resources_dict[chapter_id][section_id] = []

                points = section.find_next_sibling('div', class_='s_sectionwrap').find_all('div', class_='s_point')
                for point in points:
                    point_id = point.get('id').split('_')[-1]
                    resources_dict[chapter_id][section_id].append(point_id)

    return resources_dict


def get_last_position(pointid):
    data = {
        'itemId': pointid,
    }

    response = requests.post(
        'https://yxdzcbs-kfkc.webtrn.cn/learnspace/course/study/learningTime_getLastPlayPosition.action',
        cookies=cookies,
        headers=headers,
        data=data,
    )

    print(response.json())
    return response.json()['data']['lastPlayPosition']


def get_time(resources_dict):
    for chapter_id, sections in resources_dict.items():

        for section_id, points in sections.items():

            for point_id in points:
                get_vedio_time(section_id, point_id)
                return


def get_now_point():
    data = {
        'params.courseId': courseid,
    }

    response = requests.post(
        'https://yxdzcbs-kfkc.webtrn.cn/learnspace/learn/learnCourseware/queryLearningItem.json',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    if response.json()['data'] == "":
        return 1,1,1
    return response.json()['data']['secId'], response.json()['data']['parentId'], response.json()['data']['itemId']


def send_300(courseid):
    # cookies = {
    #     'JSESSIONID': '63B3D79A5AB5701A462BEE27CF110446.learnspace-tomcat-0007_learnspace_learning_aliyun',
    #     'learnspace_learning_https': 'f875be7496c6aa6add8508ee1d907940',
    #     'language': 'zh_CN',
    #     'UNTYXLCOOKIE': '"Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="',
    #     'learning-course': 'd5e19c05fe784c8ca1808e217aa80daf_' + courseid,
    #     '_uid': 'f8055a87-6374-4c00-a442-761ec1d8c146',
    # }
    #
    # headers = {
    #     'Accept': 'application/json, text/javascript, */*; q=0.01',
    #     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #     'Connection': 'keep-alive',
    #     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #     # 'Cookie': 'JSESSIONID=63B3D79A5AB5701A462BEE27CF110446.learnspace-tomcat-0007_learnspace_learning_aliyun; learnspace_learning_https=f875be7496c6aa6add8508ee1d907940; language=zh_CN; UNTYXLCOOKIE="Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="; learning-course=d5e19c05fe784c8ca1808e217aa80daf_f54137387c454fc69ee92637f0c8c1d0___; _uid=f8055a87-6374-4c00-a442-761ec1d8c146',
    #     'Origin': 'https://yxdzcbs-kfkc.webtrn.cn',
    #     'Referer': 'https://yxdzcbs-kfkc.webtrn.cn/learnspace/learn/learn/templatethree/index.action?params.courseId=17b6399160c2494a83707fa6974bf80c___&params.templateType=3&params.templateStyleType=3&params.template=templatethree&params.previewItemId=&params.tplRoot=learn',
    #     'Sec-Fetch-Dest': 'empty',
    #     'Sec-Fetch-Mode': 'cors',
    #     'Sec-Fetch-Site': 'same-origin',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    #     'X-Requested-With': 'XMLHttpRequest',
    #     'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': '"Windows"',
    # }

    data = {
        'courseId': courseid,
        'studyTime': '300',
        'limitId': limitid,
    }

    response = requests.post(
        'https://yxdzcbs-kfkc.webtrn.cn/learnspace/course/study/learningTime_saveLearningTime.action',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.text)


def save_detail():
    # cookies = {
    #     'JSESSIONID': '63B3D79A5AB5701A462BEE27CF110446.learnspace-tomcat-0007_learnspace_learning_aliyun',
    #     'learnspace_learning_https': 'f875be7496c6aa6add8508ee1d907940',
    #     'language': 'zh_CN',
    #     'UNTYXLCOOKIE': '"Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="',
    #     'learning-course': 'd5e19c05fe784c8ca1808e217aa80daf_' + courseid,
    #     '_uid': 'f8055a87-6374-4c00-a442-761ec1d8c146',
    # }
    #
    # headers = {
    #     'Accept': 'application/json, text/javascript, */*; q=0.01',
    #     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #     'Connection': 'keep-alive',
    #     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #     # 'Cookie': 'JSESSIONID=63B3D79A5AB5701A462BEE27CF110446.learnspace-tomcat-0007_learnspace_learning_aliyun; learnspace_learning_https=f875be7496c6aa6add8508ee1d907940; language=zh_CN; UNTYXLCOOKIE="Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="; learning-course=d5e19c05fe784c8ca1808e217aa80daf_f54137387c454fc69ee92637f0c8c1d0___; _uid=f8055a87-6374-4c00-a442-761ec1d8c146',
    #     'Origin': 'https://yxdzcbs-kfkc.webtrn.cn',
    #     'Referer': 'https://yxdzcbs-kfkc.webtrn.cn/learnspace/learn/learn/templatethree/index.action?params.courseId=' + courseid + '&params.templateType=3&params.templateStyleType=3&params.template=templatethree&params.previewItemId=&params.tplRoot=learn',
    #     'Sec-Fetch-Dest': 'empty',
    #     'Sec-Fetch-Mode': 'cors',
    #     'Sec-Fetch-Site': 'same-origin',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    #     'X-Requested-With': 'XMLHttpRequest',
    #     'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': '"Windows"',
    # }

    data = {
        'courseId': courseid,
    }

    response = requests.post(
        'https://yxdzcbs-kfkc.webtrn.cn/learnspace/course/study/learningTime_queryLearningTime.action',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.text)


def save_record(c, s, a, p):
    # cookies = {
    #     'JSESSIONID': '63B3D79A5AB5701A462BEE27CF110446.learnspace-tomcat-0007_learnspace_learning_aliyun',
    #     'learnspace_learning_https': 'f875be7496c6aa6add8508ee1d907940',
    #     'language': 'zh_CN',
    #     'UNTYXLCOOKIE': '"Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="',
    #     '_uid': 'f8055a87-6374-4c00-a442-761ec1d8c146',
    #     'learnspace_https': '4a5d268647c45c34767aac10728da656',
    #     'JSESSIONID': '2DACD0F3F8F7A50563040E7E03F4FF40.learnspace-tomcat-0011_learnspace_aliyun',
    #     'learning-course': 'd5e19c05fe784c8ca1808e217aa80daf_' + c,
    # }
    #
    # headers = {
    #     'Accept': 'application/json, text/javascript, */*; q=0.01',
    #     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #     'Connection': 'keep-alive',
    #     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #     # 'Cookie': 'JSESSIONID=63B3D79A5AB5701A462BEE27CF110446.learnspace-tomcat-0007_learnspace_learning_aliyun; learnspace_learning_https=f875be7496c6aa6add8508ee1d907940; language=zh_CN; UNTYXLCOOKIE="Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="; _uid=f8055a87-6374-4c00-a442-761ec1d8c146; learnspace_https=4a5d268647c45c34767aac10728da656; JSESSIONID=2DACD0F3F8F7A50563040E7E03F4FF40.learnspace-tomcat-0011_learnspace_aliyun; learning-course=d5e19c05fe784c8ca1808e217aa80daf_17b6399160c2494a83707fa6974bf80c___',
    #     'Origin': 'https://yxdzcbs-kfkc.webtrn.cn',
    #     'Referer': 'https://yxdzcbs-kfkc.webtrn.cn/learnspace/learn/learn/templatethree/content_video.action?params.courseId=17b6399160c2494a83707fa6974bf80c___&params.itemId=8a8380968e9f210e018eb797f38737da&params.templateStyleType=3&params.parentId=8a8380968e9f210e018eb797f38737d9&_t=1724126681806',
    #     'Sec-Fetch-Dest': 'empty',
    #     'Sec-Fetch-Mode': 'cors',
    #     'Sec-Fetch-Site': 'same-origin',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    #     'X-Requested-With': 'XMLHttpRequest',
    #     'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': '"Windows"',
    # }

    data = {
        'studyRecord': gets(c, s, a, p),
        'limitId': limitid,
    }

    response = requests.post(
        'https://yxdzcbs-kfkc.webtrn.cn/learnspace/course/study/learningTime_saveVideoLearnDetailRecord.action',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.text)
    if response.json()['success'] == 'false':
        return response.json()['success'],0
    return response.json()['success'], response.json()['data']['timeRecordResult']['itemCompleteStatus']


def goto_learn(postion, point_id, total_seconds):
    start = int(postion)
    add = 300
    for i in range(1, 100):
        if start == 0:
            add = 4
        send_300(courseid)
        if start + add > total_seconds:
            print("刷课进行中：:", get_now_point())
            add = total_seconds - start
            ret, item_change = save_record(courseid, start, add, point_id)
        else:
            ret, item_change = save_record(courseid, start, add, point_id)
        if ret == 'false':
            time.sleep(5)
            ret, item_change = save_record(courseid, start, add, point_id)
        if item_change == 'true':
            print("课程状态改变后：:", get_now_point())
            time.sleep(5)
            return
        if ret == 'true':
            start = start + add
        add = 300
        print(start, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        time.sleep(150)



def start(resources_dict, last_chapter_id, last_section_id, last_point_id):
    if last_chapter_id == 1:
        for chapter_id, sections in resources_dict.items():

                for section_id, points in sections.items():
                        flag = False
                        for point_id in points:
                            if not flag:
                                if last_point_id == point_id:
                                    total_seconds = get_vedio_time(section_id, point_id)
                                    postion = get_last_position(point_id)
                                    print("上次学习时长：", postion)
                                    if postion == 0:
                                        goto_learn(0, point_id, total_seconds)
                                    elif int(total_seconds) - int(postion) > 300:
                                        goto_learn(postion, point_id, total_seconds)
                                    else:
                                        print("还剩5分钟，怎么没跳下一节课？？？")
                                        flag = True
                            else:
                                total_seconds = get_vedio_time(section_id, point_id)
                                postion = get_last_position(point_id)
                                print("上次学习时长：", postion)
                                if postion == 0:
                                    goto_learn(0, point_id, total_seconds)
                                elif int(total_seconds) - int(postion) > 300:
                                    goto_learn(postion, point_id, total_seconds)
                                else:
                                    print("还剩5分钟，怎么没跳下一节课？？？")
                                    flag = True

                                print(get_now_point())

    else:
        for chapter_id, sections in resources_dict.items():
            if last_chapter_id == chapter_id:
                for section_id, points in sections.items():

                    if last_section_id == section_id:
                        flag = False
                        for point_id in points:
                            if not flag:
                                if last_point_id == point_id:
                                    total_seconds = get_vedio_time(section_id, point_id)
                                    postion = get_last_position(point_id)
                                    print("上次学习时长：", postion)
                                    if postion == 0:
                                        goto_learn(0, point_id, total_seconds)
                                    elif int(total_seconds) - int(postion) > 300:
                                        goto_learn(postion, point_id, total_seconds)
                                    else:
                                        print("还剩5分钟，怎么没跳下一节课？？？")
                                        flag = True
                            else:
                                flag = False
                                total_seconds = get_vedio_time(section_id, point_id)
                                postion = get_last_position(point_id)
                                print("上次学习时长：", postion)
                                if postion == 0:
                                    goto_learn(0, point_id, total_seconds)
                                elif int(total_seconds) - int(postion) > 300:
                                    goto_learn(postion, point_id, total_seconds)
                                else:
                                    print("还剩5分钟，怎么没跳下一节课？？？")
                                    flag = True

                                print(get_now_point())


courseid = '29e27a94f9ed4a58bd457eda29751881___'
limitid = '70e50963fdb542308148e480259687f5'

cookies = {
    'dumaScrollAreaId_17CookieName': '0',
    'JSESSIONID': 'B0AC083F9AE16D6771FB46C3EC4F8E38.learnspace-tomcat-0010_learnspace_learning_aliyun',
    'learnspace_learning_https': 'c96f70eaa34a28797e1e54e16104eeb0',
    'language': 'zh_CN',
    'UNTYXLCOOKIE': '"Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="',
    'learning-course': 'd5e19c05fe784c8ca1808e217aa80daf_'+courseid,
    '_uid': '5f6c7a82-9179-437f-8cc8-c9baeb73fb3a',
    'learnspace_https': 'a1e2c63969e260ca9d2497fce3d2921a',
    'JSESSIONID': 'C2BCA1554B064D3E226D2343CE9BABF6.learnspace-tomcat-0010_learnspace_aliyun',
}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    # 'Cookie': 'dumaScrollAreaId_17CookieName=0; JSESSIONID=B0AC083F9AE16D6771FB46C3EC4F8E38.learnspace-tomcat-0010_learnspace_learning_aliyun; learnspace_learning_https=c96f70eaa34a28797e1e54e16104eeb0; language=zh_CN; UNTYXLCOOKIE="Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="; learning-course=d5e19c05fe784c8ca1808e217aa80daf_f54137387c454fc69ee92637f0c8c1d0___; _uid=5f6c7a82-9179-437f-8cc8-c9baeb73fb3a',
    'Referer': 'https://yxdzcbs-kfkc.webtrn.cn/learnspace/learn/learn/templatethree/index.action?params.courseId='+courseid+'&params.templateType=3&params.templateStyleType=3&params.template=templatethree&params.previewItemId=&params.tplRoot=learn',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


if __name__ == '__main__':
    last_chapter_id, last_section_id, last_point_id = get_now_point()

    response = get_all_course_itemid()
    resources_dict = bs4_get_dic(response)
    print(resources_dict)
    start(resources_dict, last_chapter_id, last_section_id, last_point_id)
    # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))