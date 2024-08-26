
import requests
import hmac
import hashlib
import base64
from urllib.parse import urlparse
import time
import random

def get_first_cource():
    headers = {
        'authority': 's-file-1.ykt.cbern.com.cn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': 'https://basic.smartedu.cn',
        'referer': 'https://basic.smartedu.cn/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }

    response = requests.get('https://s-file-1.ykt.cbern.com.cn/teach/api_static/trains/2024sqpx.json', headers=headers)
    print(response.json()['train_course_ids'])
    return response.json()['train_course_ids']

def make_autho():
    # 测试参数
    e = "https://elearning-train-gateway.ykt.eduyun.cn/v1/spi/trains/5d7cf98c-3a42-4b13-8e5f-56f40ce08b1d/courses/4eb65b2f-0b53-4d3f-8027-81d69dca7f18/progress/actions/async"
    # t = "1723628466564:GQ2ZRMRF"
    n = "post"
    r = "L2RqbFNWDM"
    # 获取当前时间戳（以毫秒为单位）
    timestamp = str(int(time.time() * 1000))

    # 生成8位随机字符串
    random_string = generate_random_string(8)

    # 组装t
    t = f"{timestamp}:{random_string}"

    # print(t)


    # 生成MAC
    mac_result = generate_mac(e, t, n, r)
    # print(mac_result)
    return mac_result

def generate_mac(e, t, n, r):
    # 解析URL
    parsed_url = urlparse(e)
    relative = parsed_url.path
    if parsed_url.query:
        relative += '?' + parsed_url.query
    authority = parsed_url.netloc

    # 构造待签名字符串
    i = f"{t}\n{n.upper()}\n{relative}\n{authority}\n"

    # 生成HMAC-SHA256哈希值
    mac = hmac.new(r.encode(), i.encode(), hashlib.sha256).digest()

    # 将哈希值编码为Base64格式
    mac_base64 = base64.b64encode(mac).decode()

    return mac_base64
def generate_random_string(length):
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for _ in range(length):
        result += characters[random.randint(0, 35)]
    return result


def postion(b,s,u):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': make_autho(),
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://basic.smartedu.cn',
        'Referer': 'https://basic.smartedu.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        # 'sdp-app-id': 'e5649925-441d-4a53-b525-51a2f1c4e0a8',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'position': (int(s[1]) + 1) if b else 0,
    }

    response = requests.put(
        'https://x-study-record-api.ykt.eduyun.cn/v1/resource_learning_positions/'+s[0]+'/'+u,
        headers=headers,
        json=json_data,
    )

    print(response.text)



def get_active_id(cid):

    headers = {
        'authority': 's-file-1.ykt.cbern.com.cn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        # 'if-modified-since': 'Tue, 13 Aug 2024 10:43:43 GMT',
        # 'if-none-match': 'W/"e81a638658c518fbe1662c9fe8227279"',
        'origin': 'https://basic.smartedu.cn',
        'referer': 'https://basic.smartedu.cn/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }

    response = requests.get(
        'https://s-file-1.ykt.cbern.com.cn/teach/s_course/v2/business_courses/'+cid+'/course_relative_infos/zh-CN.json',
        headers=headers,
    )

    return (response.json()['course_detail']['activity_set_id'])


def get_fulls(aid):
    headers = {
        'authority': 's-file-2.ykt.cbern.com.cn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        # 'if-modified-since': 'Tue, 13 Aug 2024 10:43:32 GMT',
        # 'if-none-match': 'W/"44a776b160ea5f8eba6632d17fd865e1"',
        'origin': 'https://basic.smartedu.cn',
        'referer': 'https://basic.smartedu.cn/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }

    response = requests.get(
        'https://s-file-2.ykt.cbern.com.cn/teach/s_course/v2/activity_sets/'+aid+'/fulls.json',
        headers=headers,
    )

    return response.json()['nodes']


def async_begin(u,r):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': make_autho(),
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://basic.smartedu.cn',
        'Referer': 'https://basic.smartedu.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
        'device_id': '0be5c698499f47838e38a140b2dd818a',
        # 'sdp-app-id': 'e5649925-441d-4a53-b525-51a2f1c4e0a8',
        # 'sdp-xpath-id': '66235ce5-81f9-4293-81ec-192db59bca21',
        'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'user_id': u,
        'resource_id': r,
        # 'resource_name': '综合育人能力提升',
        'resource_type': 't_course',
        'catalog_type': 'teacherTraining',
        'topic_type': 'f78d68fb-0386-4a26-aeb9-d0835b35bde2',
        'progress': 2,
        'status': 1,
        # 'ext_info': '{"cv":1,"platform":"web","tags":"2024年“暑期教师研修”专题","origin":"2024年“暑期教师研修”专题","cover":"https://s-file-1.ykt.cbern.com.cn/zxx/X-COURSE/416/6_1720503927229.jpg","last_learning_activity":{"activity_id":"3ddecd3b-0329-4925-b2e1-247e1446d844","title":"04贯彻落实《意见》精神，推动劳动教育高质量发展"},"activity_last_learning_resource":{"d026521f-f177-40f9-aa96-3bbcfb457d22":"0bdf45b8-c0ea-439f-9d58-4d16d123c8b2","12b4ab15-7af8-4491-8fb0-6437a1919cc3":"7d4818c6-7a3e-448a-8497-8e19dc7fe80b","4c170915-bd51-4309-b546-c20064106daa":"0e2fd7d3-714d-4c5e-8fee-6e543c297371","3ddecd3b-0329-4925-b2e1-247e1446d844":"241f16f9-6875-47a4-91c6-ec866ed046eb"},"activity_progress":{"d026521f-f177-40f9-aa96-3bbcfb457d22":2,"12b4ab15-7af8-4491-8fb0-6437a1919cc3":2},"resource_progress":{"0bdf45b8-c0ea-439f-9d58-4d16d123c8b2":2,"7d4818c6-7a3e-448a-8497-8e19dc7fe80b":2,"241f16f9-6875-47a4-91c6-ec866ed046eb":1},"miniwork_progress":{},"resource_max_pos":{"0bdf45b8-c0ea-439f-9d58-4d16d123c8b2":{"pos":996,"type":"video"},"7d4818c6-7a3e-448a-8497-8e19dc7fe80b":{"pos":401,"type":"video"},"0e2fd7d3-714d-4c5e-8fee-6e543c297371":{"pos":0,"type":"video"},"241f16f9-6875-47a4-91c6-ec866ed046eb":{"pos":1,"type":"video"}},"activity_exam_progress":{},"activity_event":{},"resource_study_time_ignore":[]}',
    }

    response = requests.post(
        'https://elearning-train-gateway-safe.ykt.eduyun.cn/v1/spi/trains/5d7cf98c-3a42-4b13-8e5f-56f40ce08b1d/courses/f78d68fb-0386-4a26-aeb9-d0835b35bde2/progress/actions/async_begin',
        headers=headers,
        json=json_data,
    )



def extract_resources(node,sources):
    if len(node['child_nodes']) != 0:
        for child in node.get('child_nodes', []):
            extract_resources(child,sources)
    else:
        a_source = node['relations']['activity']['activity_resources']
        if len(a_source) != 1:
            print('发现一个视频多个资源:', node['name'])
        else:
            sources.append((a_source[0]['resource_id'], a_source[0]['study_time']))

def positon_record(sid,uid):

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Access-Control-Request-Headers': 'authorization,sdp-app-id',
        'Access-Control-Request-Method': 'GET',
        'Connection': 'keep-alive',
        'Origin': 'https://basic.smartedu.cn',
        'Referer': 'https://basic.smartedu.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

    response = requests.options(
        'https://x-study-record-api.ykt.eduyun.cn/v1/resource_learning_positions/'+sid+'/'+uid,
        headers=headers,
    )

    response = requests.get(
        'https://x-study-record-api.ykt.eduyun.cn/v1/resource_learning_positions/' + sid + '/' + uid,
        headers=headers,
    )
    print(response.text)


if __name__ == '__main__':

    user_id = '452588780689'

    first_cource = get_first_cource()
    for cource in first_cource:
        print('大课程：',cource)
        activity_set_id = get_active_id(cource)
        print(activity_set_id)
        nodes = get_fulls(activity_set_id)
        a = 1

        for node in nodes:

            sources = []
            extract_resources(node, sources)
            print(sources)
            for source in sources:
                if a >= 20:
                    break
                # async_begin(user_id, source)
                postion(False, source, user_id)
                postion(True, source, user_id)
                a = a+1
                # time.sleep(2)



    # activity_set_id = get_active_id('6ed00ea1-3f76-484e-9a23-9a4349b40721')
    #
    # nodes = get_fulls(activity_set_id)
    #
    # for node in nodes:
    #     sources = []
    #     extract_resources(node, sources)
    #     print(sources)
    #     for source in sources:
    #         # async_begin(user_id,source)
    #         # postion(False,source, user_id)
    #         postion(True,source,user_id)
    #         positon_record(source[0],user_id)



    # source = ('e0042a21-a0ea-4dfb-9332-49e4e4736370',901)
    # postion(True,source,user_id)


    # positon_record('9316d0de-c2af-45f1-87ef-5802279cb0d0',user_id)
