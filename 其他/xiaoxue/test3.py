import requests
from bs4 import BeautifulSoup
import test

def get_vedio_time(section_id,point_id):
    cookies = {
        'dumaScrollAreaId_17CookieName': '0',
        'JSESSIONID': 'B0AC083F9AE16D6771FB46C3EC4F8E38.learnspace-tomcat-0010_learnspace_learning_aliyun',
        'learnspace_learning_https': 'c96f70eaa34a28797e1e54e16104eeb0',
        'language': 'zh_CN',
        'UNTYXLCOOKIE': '"Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="',
        'learning-course': 'd5e19c05fe784c8ca1808e217aa80daf_f54137387c454fc69ee92637f0c8c1d0___',
        '_uid': '5f6c7a82-9179-437f-8cc8-c9baeb73fb3a',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        # 'Cookie': 'dumaScrollAreaId_17CookieName=0; JSESSIONID=B0AC083F9AE16D6771FB46C3EC4F8E38.learnspace-tomcat-0010_learnspace_learning_aliyun; learnspace_learning_https=c96f70eaa34a28797e1e54e16104eeb0; language=zh_CN; UNTYXLCOOKIE="Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="; learning-course=d5e19c05fe784c8ca1808e217aa80daf_f54137387c454fc69ee92637f0c8c1d0___; _uid=5f6c7a82-9179-437f-8cc8-c9baeb73fb3a',
        'Referer': 'https://yxdzcbs-kfkc.webtrn.cn/learnspace/learn/learn/templatethree/courseware_index.action?params.courseId=f54137387c454fc69ee92637f0c8c1d0___',
        'Sec-Fetch-Dest': 'iframe',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'params.courseId': 'f54137387c454fc69ee92637f0c8c1d0___',
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

    cookies = {
        'dumaScrollAreaId_17CookieName': '0',
        'JSESSIONID': 'B0AC083F9AE16D6771FB46C3EC4F8E38.learnspace-tomcat-0010_learnspace_learning_aliyun',
        'learnspace_learning_https': 'c96f70eaa34a28797e1e54e16104eeb0',
        'language': 'zh_CN',
        'UNTYXLCOOKIE': '"Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="',
        'learning-course': 'd5e19c05fe784c8ca1808e217aa80daf_f54137387c454fc69ee92637f0c8c1d0___',
        '_uid': '5f6c7a82-9179-437f-8cc8-c9baeb73fb3a',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        # 'Cookie': 'dumaScrollAreaId_17CookieName=0; JSESSIONID=B0AC083F9AE16D6771FB46C3EC4F8E38.learnspace-tomcat-0010_learnspace_learning_aliyun; learnspace_learning_https=c96f70eaa34a28797e1e54e16104eeb0; language=zh_CN; UNTYXLCOOKIE="Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="; learning-course=d5e19c05fe784c8ca1808e217aa80daf_f54137387c454fc69ee92637f0c8c1d0___; _uid=5f6c7a82-9179-437f-8cc8-c9baeb73fb3a',
        'Referer': 'https://yxdzcbs-kfkc.webtrn.cn/learnspace/learn/learn/templatethree/index.action?params.courseId=f54137387c454fc69ee92637f0c8c1d0___&params.templateType=3&params.templateStyleType=3&params.template=templatethree&params.previewItemId=&params.tplRoot=learn',
        'Sec-Fetch-Dest': 'iframe',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'params.courseId': 'f54137387c454fc69ee92637f0c8c1d0___',
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

    cookies = {
        'JSESSIONID': 'B0AC083F9AE16D6771FB46C3EC4F8E38.learnspace-tomcat-0010_learnspace_learning_aliyun',
        'learnspace_learning_https': 'c96f70eaa34a28797e1e54e16104eeb0',
        'language': 'zh_CN',
        'UNTYXLCOOKIE': '"Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="',
        'learning-course': 'd5e19c05fe784c8ca1808e217aa80daf_f54137387c454fc69ee92637f0c8c1d0___',
        '_uid': '5f6c7a82-9179-437f-8cc8-c9baeb73fb3a',
        'learnspace_https': 'a1e2c63969e260ca9d2497fce3d2921a',
        'JSESSIONID': 'C2BCA1554B064D3E226D2343CE9BABF6.learnspace-tomcat-0010_learnspace_aliyun',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'JSESSIONID=B0AC083F9AE16D6771FB46C3EC4F8E38.learnspace-tomcat-0010_learnspace_learning_aliyun; learnspace_learning_https=c96f70eaa34a28797e1e54e16104eeb0; language=zh_CN; UNTYXLCOOKIE="Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="; learning-course=d5e19c05fe784c8ca1808e217aa80daf_f54137387c454fc69ee92637f0c8c1d0___; _uid=5f6c7a82-9179-437f-8cc8-c9baeb73fb3a; learnspace_https=a1e2c63969e260ca9d2497fce3d2921a; JSESSIONID=C2BCA1554B064D3E226D2343CE9BABF6.learnspace-tomcat-0010_learnspace_aliyun',
        'Origin': 'https://yxdzcbs-kfkc.webtrn.cn',
        'Referer': 'https://yxdzcbs-kfkc.webtrn.cn/learnspace/learn/learn/templatethree/content_video.action?params.courseId=f54137387c454fc69ee92637f0c8c1d0___&params.itemId='+pointid+'&params.templateStyleType=3&params.parentId=8a8380938e9f1f8a018eb78f747b3bd0&params.videoTime=900&params.connItem='+pointid+'&_t=1724318732979',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

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

                get_vedio_time(section_id,point_id)
                return

def get_now_point():
    import requests

    cookies = {
        'JSESSIONID': 'B0AC083F9AE16D6771FB46C3EC4F8E38.learnspace-tomcat-0010_learnspace_learning_aliyun',
        'learnspace_learning_https': 'c96f70eaa34a28797e1e54e16104eeb0',
        'language': 'zh_CN',
        'UNTYXLCOOKIE': '"Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="',
        'learning-course': 'd5e19c05fe784c8ca1808e217aa80daf_f54137387c454fc69ee92637f0c8c1d0___',
        '_uid': '5f6c7a82-9179-437f-8cc8-c9baeb73fb3a',
        'learnspace_https': 'a1e2c63969e260ca9d2497fce3d2921a',
        'JSESSIONID': 'C2BCA1554B064D3E226D2343CE9BABF6.learnspace-tomcat-0010_learnspace_aliyun',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'JSESSIONID=B0AC083F9AE16D6771FB46C3EC4F8E38.learnspace-tomcat-0010_learnspace_learning_aliyun; learnspace_learning_https=c96f70eaa34a28797e1e54e16104eeb0; language=zh_CN; UNTYXLCOOKIE="Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="; learning-course=d5e19c05fe784c8ca1808e217aa80daf_f54137387c454fc69ee92637f0c8c1d0___; _uid=5f6c7a82-9179-437f-8cc8-c9baeb73fb3a; learnspace_https=a1e2c63969e260ca9d2497fce3d2921a; JSESSIONID=C2BCA1554B064D3E226D2343CE9BABF6.learnspace-tomcat-0010_learnspace_aliyun',
        'Origin': 'https://yxdzcbs-kfkc.webtrn.cn',
        'Referer': 'https://yxdzcbs-kfkc.webtrn.cn/learnspace/learn/learn/templatethree/courseware_index.action?params.courseId=f54137387c454fc69ee92637f0c8c1d0___',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'params.courseId': 'f54137387c454fc69ee92637f0c8c1d0___',
    }

    response = requests.post(
        'https://yxdzcbs-kfkc.webtrn.cn/learnspace/learn/learnCourseware/queryLearningItem.json',
        cookies=cookies,
        headers=headers,
        data=data,
    )

def goto_learn(postion,section_id,point_id):
    test.learn(postion,point_id)

if __name__ == '__main__':
    response = get_all_course_itemid()
    resources_dict = bs4_get_dic(response)
    # get_time(resources_dict)

    # 直接从上次进度开始  明天继续写
    get_now_point()
    for chapter_id, sections in resources_dict.items():

        for section_id, points in sections.items():

            for point_id in points:
                total_seconds = get_vedio_time(section_id, point_id)
                postion = get_last_position(point_id)
                print("上次学习时长：",postion)
                if postion == 0:
                    goto_learn(0,section_id,point_id)
                elif int(total_seconds) - int(postion) > 300:
                    goto_learn(postion,section_id,point_id)
                else:
                    continue
