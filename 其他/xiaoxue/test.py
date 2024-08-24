import time

import requests

from 其他.xiaoxue import test2


def send_300(courseid):
    cookies = {
        'JSESSIONID': '63B3D79A5AB5701A462BEE27CF110446.learnspace-tomcat-0007_learnspace_learning_aliyun',
        'learnspace_learning_https': 'f875be7496c6aa6add8508ee1d907940',
        'language': 'zh_CN',
        'UNTYXLCOOKIE': '"Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="',
        'learning-course': 'd5e19c05fe784c8ca1808e217aa80daf_'+courseid,
        '_uid': 'f8055a87-6374-4c00-a442-761ec1d8c146',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'JSESSIONID=63B3D79A5AB5701A462BEE27CF110446.learnspace-tomcat-0007_learnspace_learning_aliyun; learnspace_learning_https=f875be7496c6aa6add8508ee1d907940; language=zh_CN; UNTYXLCOOKIE="Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="; learning-course=d5e19c05fe784c8ca1808e217aa80daf_f54137387c454fc69ee92637f0c8c1d0___; _uid=f8055a87-6374-4c00-a442-761ec1d8c146',
        'Origin': 'https://yxdzcbs-kfkc.webtrn.cn',
        'Referer': 'https://yxdzcbs-kfkc.webtrn.cn/learnspace/learn/learn/templatethree/index.action?params.courseId=17b6399160c2494a83707fa6974bf80c___&params.templateType=3&params.templateStyleType=3&params.template=templatethree&params.previewItemId=&params.tplRoot=learn',
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
    cookies = {
        'JSESSIONID': '63B3D79A5AB5701A462BEE27CF110446.learnspace-tomcat-0007_learnspace_learning_aliyun',
        'learnspace_learning_https': 'f875be7496c6aa6add8508ee1d907940',
        'language': 'zh_CN',
        'UNTYXLCOOKIE': '"Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="',
        'learning-course': 'd5e19c05fe784c8ca1808e217aa80daf_'+courseid,
        '_uid': 'f8055a87-6374-4c00-a442-761ec1d8c146',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'JSESSIONID=63B3D79A5AB5701A462BEE27CF110446.learnspace-tomcat-0007_learnspace_learning_aliyun; learnspace_learning_https=f875be7496c6aa6add8508ee1d907940; language=zh_CN; UNTYXLCOOKIE="Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="; learning-course=d5e19c05fe784c8ca1808e217aa80daf_f54137387c454fc69ee92637f0c8c1d0___; _uid=f8055a87-6374-4c00-a442-761ec1d8c146',
        'Origin': 'https://yxdzcbs-kfkc.webtrn.cn',
        'Referer': 'https://yxdzcbs-kfkc.webtrn.cn/learnspace/learn/learn/templatethree/index.action?params.courseId='+courseid+'&params.templateType=3&params.templateStyleType=3&params.template=templatethree&params.previewItemId=&params.tplRoot=learn',
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
        'courseId': '17b6399160c2494a83707fa6974bf80c___',
    }

    response = requests.post(
        'https://yxdzcbs-kfkc.webtrn.cn/learnspace/course/study/learningTime_queryLearningTime.action',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.text)

def save_record(c,s,a,p):


    cookies = {
        'JSESSIONID': '63B3D79A5AB5701A462BEE27CF110446.learnspace-tomcat-0007_learnspace_learning_aliyun',
        'learnspace_learning_https': 'f875be7496c6aa6add8508ee1d907940',
        'language': 'zh_CN',
        'UNTYXLCOOKIE': '"Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="',
        '_uid': 'f8055a87-6374-4c00-a442-761ec1d8c146',
        'learnspace_https': '4a5d268647c45c34767aac10728da656',
        'JSESSIONID': '2DACD0F3F8F7A50563040E7E03F4FF40.learnspace-tomcat-0011_learnspace_aliyun',
        'learning-course': 'd5e19c05fe784c8ca1808e217aa80daf_'+c,
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'JSESSIONID=63B3D79A5AB5701A462BEE27CF110446.learnspace-tomcat-0007_learnspace_learning_aliyun; learnspace_learning_https=f875be7496c6aa6add8508ee1d907940; language=zh_CN; UNTYXLCOOKIE="Y21lb25saW5lLmNtYS1jbWMuY29tLmNufHxhNTVhYmVkYjA1NDNhNWViM2NlNmQ5ZTgxZGRiNzI1ZXx8MTc3MjY2MzY1OTl8fHl4ZHpjYnM="; _uid=f8055a87-6374-4c00-a442-761ec1d8c146; learnspace_https=4a5d268647c45c34767aac10728da656; JSESSIONID=2DACD0F3F8F7A50563040E7E03F4FF40.learnspace-tomcat-0011_learnspace_aliyun; learning-course=d5e19c05fe784c8ca1808e217aa80daf_17b6399160c2494a83707fa6974bf80c___',
        'Origin': 'https://yxdzcbs-kfkc.webtrn.cn',
        'Referer': 'https://yxdzcbs-kfkc.webtrn.cn/learnspace/learn/learn/templatethree/content_video.action?params.courseId=17b6399160c2494a83707fa6974bf80c___&params.itemId=8a8380968e9f210e018eb797f38737da&params.templateStyleType=3&params.parentId=8a8380968e9f210e018eb797f38737d9&_t=1724126681806',
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
        'studyRecord': test2.gets(c,s,a,p),
        'limitId': limitid,
    }

    response = requests.post(
        'https://yxdzcbs-kfkc.webtrn.cn/learnspace/course/study/learningTime_saveVideoLearnDetailRecord.action',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.text)


courseid = 'f54137387c454fc69ee92637f0c8c1d0___'
limitid = '70e50963fdb542308148e480259687f5'


def learn(s,pointid):
    start = s
    add = 300
    for i in range(1, 10):
        send_300(courseid)
        # save_detail()

        time.sleep(151)
        save_record(courseid, start, add,pointid)
        start = start + add
        print(start)

if __name__ == '__main__':


    # start = 600
    # add = 600
    # for i in range(1,10):
    #     send_300(courseid)
    #     # save_detail()
    #
    #     time.sleep(151)
    #     save_record(courseid,start,add)
    #     start = start + add
    #     print(start)



    send_300(courseid)
    # save_detail()

    start = 1800
    add = 600
    save_record(courseid, start, add)
