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

def record():
    import requests

    cookies = {
        'dd_sid': 'k0_20662136fb1ad8663e48_2136206666d81afb10eec608070b9299a8c48ad5d4d1',
        'account': 'oauth_k1%3AnLyw1YhjkUnYtY7w1bsDXbvzfHYXmBSbr%2FnhoncvEd4%2B3bbdT%2FKYxETOclpx0NBIURZlA8xeUt%2FsYJZEJCESdAMHwWP9tD3C6Yx8KjDhpAA%3D',
        'deviceid': 'NTdlNDE2NzJmMzFhNWE2NmY1_unified',
        'pub_uid': 'Y8%2BEa6rnfMIGpbCUnj7izw%3D%3D',
        'dt_s': 'u-23eaf33d-91bc29bb48-213fb66c-657c8d-79e59a61-3499a16f-519c-440c-934f-8227b67e1730',
        'XSRF-TOKEN': '23d59819-69b1-439a-9d2b-10a7c16701eb',
        'up_ab': 'y',
        'preview_ab': 'y',
        'cna': 'EglfH6gI7ikCAd7XGNB6ziTb',
        'xlly_s': '1',
        'doc_atoken': 'NjAyNjAwMjUzBOYQAMoytaGsIEYqiMnHmKfpjlxsdROe',
        'tfstk': 'fxyZvyDYrOBwe96XhckqYTV0JKDtvAbWo-gjmoqmfV0i51Hqo2zlXEi1XWo45ya6h1UfuWz0JfgGk5N2uuUqhAMihqzUyzJfX5abTszTqfMb3opqmo4AXqsOOlEtHxb5PrWSBlEd6mk1Vjmhm0immdiF-uZtHxbBAKf5UlUysGoUIxjEKmnroxvmiMlnVmDDIjvMte0K-qDmsCYHKcnioIvMsMrnJmDmoNNznRJE7fjyEYHTAwf4j4qiSlqaKhhX6k3eEL2UTb3od2JDnJoTvH4YXL5jr73sNljPdEn3KUeYHtdqsDnEPMSUtX2jo2edq-RvMXjKY4sP4Idx_1nEPM4DMIhs4Du5Ak1..',
        'isg': 'BFRURlyuzt9LUFqThTfiKAwGJZLGrXiXwWpWxO4wI18J2fMjF71QJvyT3dPBIbDv',
    }

    headers = {
        'authority': 'saas.daxue.dingtalk.com',
        'saassign': '9a765502fc62e06cf07eeb9b85033c28',
        'x-xsrf-token': '23d59819-69b1-439a-9d2b-10a7c16701eb',
        'sec-ch-ua-mobile': '?0',
        'ulcookie': '438c3853d884118a90bf4bd036e12497',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 dingtalk-win/1.0.0 nw(0.14.7) DingTalk(7.0.20-RC.5169101) Mojo/1.0.0 Native AppType(rc) Channel/201200',
        'isajax': 'true',
        'saastime': '1725438907213',
        'accept': 'application/json, text/plain, */*',
        'bx-v': '2.5.14',
        'content-type': 'application/json;charset=UTF-8',
        'sign': '9547830b28b54bd12fbe19622736424e',
        'sec-ch-ua': '"Chromium";v="91"',
        # 'cookie': 'dd_sid=k0_20662136fb1ad8663e48_2136206666d81afb10eec608070b9299a8c48ad5d4d1; account=oauth_k1%3AnLyw1YhjkUnYtY7w1bsDXbvzfHYXmBSbr%2FnhoncvEd4%2B3bbdT%2FKYxETOclpx0NBIURZlA8xeUt%2FsYJZEJCESdAMHwWP9tD3C6Yx8KjDhpAA%3D; deviceid=NTdlNDE2NzJmMzFhNWE2NmY1_unified; pub_uid=Y8%2BEa6rnfMIGpbCUnj7izw%3D%3D; dt_s=u-23eaf33d-91bc29bb48-213fb66c-657c8d-79e59a61-3499a16f-519c-440c-934f-8227b67e1730; XSRF-TOKEN=23d59819-69b1-439a-9d2b-10a7c16701eb; up_ab=y; preview_ab=y; cna=EglfH6gI7ikCAd7XGNB6ziTb; xlly_s=1; doc_atoken=NjAyNjAwMjUzBOYQAMoytaGsIEYqiMnHmKfpjlxsdROe; tfstk=f99qvr69-xH4MGM_CiWN4vAMyRXArt0QSd_1jhxGcZbcljBNSa8nDPsjDQSwlUTbCjLs7Q8Mys_mWIOa7HLNCt6cCN8yJeysDIT6af8vxs66QheNjhYtDNixNnKABO0IRFkCHnK-MGWjAR4uE3IUm-srrHtABO07VRcILnLUixkknOmPEGIFSO2Gs0WlcMXgn120ZzbRrNXGiS4uEiIcS520i0-lyGXGSNdyIKyPusmUK9BvV2mCwwxconx2EuC8M3byq3Jl037XmIegILSVMdgGAXGOGCxd9K_P46aOqL4pBdHT_sjR4wir4QfkCNbJeDva65Co2g7IYDPT6slA4wikS5FOGMSPR0t5.; isg=BEJCAf6wkMUzPIyZp9nsQo6Ak0ikE0Ytg6xgToxYKbUL3-ZZdaD9PfPRi9mjj77F',
        'origin': 'https://saas.daxue.dingtalk.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://saas.daxue.dingtalk.com/dingtalk/pc/detail.jhtml?appId=5488&corpId=dinge855d17bd97359a8f2c783f7214b6d69',
        'accept-language': 'zh-CN,zh;q=0.9',
    }

    json_data = {
        'source': 4,
        'studyType': 2,
        'resourceId': '115478547',
        'packageId': '109869621',
        'courseId': '110628977',
        'courseTime': 240,
        'learnTime': 60,
        'type': 2,
    }

    response = requests.post(
        'https://saas.daxue.dingtalk.com/dingtalk/course/record.jhtml',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    print(response.text)


if __name__ == '__main__':


    record()




