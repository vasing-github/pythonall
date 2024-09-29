
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
    print(mac_result)
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

def get_method_position(s, u):

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': make_autho(),
        'Connection': 'keep-alive',
        'Origin': 'https://basic.smartedu.cn',
        'Referer': 'https://basic.smartedu.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        'sdp-app-id': 'e5649925-441d-4a53-b525-51a2f1c4e0a8',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(
        'https://x-study-record-api.ykt.eduyun.cn/v1/resource_learning_positions/'+s[0]+'/'+u,
        headers=headers,
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

def test_study_details():
    import requests

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
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        'sdp-app-id': 'e5649925-441d-4a53-b525-51a2f1c4e0a8',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'user_id': 452651017041,
        'resource_id': '0de67197-af6f-43ab-8d89-59a75aab289e',
        'resource_name': '大力弘扬教育家精神',
        'resource_type': 't_course',
        'catalog_type': 'teacherTraining',
        'topic_type': '0de67197-af6f-43ab-8d89-59a75aab289e',
        'progress': 53,
        'status': 1,
        'ext_info': '{\"cv\":1,\"platform\":\"web\",\"tags\":\"2024年“暑期教师研修”专题\",\"origin\":\"2024年“暑期教师研修”专题\",\"cover\":\"https://s-file-1.ykt.cbern.com.cn/zxx/X-COURSE/416/1_1720504053551.jpg\",\"last_learning_activity\":{\"activity_id\":\"434f5cd1-86eb-4e4e-aa46-2d23ac7acb0d\",\"title\":\"俞国平：坚守初心教育是我一生的事业\"},\"activity_last_learning_resource\":{\"8fbce011-a3d7-4be3-94f8-1f5aabe4e747\":\"bdd57b36-b05f-4cb0-8c74-89d3fd2ffd25\",\"10bf14c1-705d-49d1-8dd5-a6af524f0af5\":\"4e811eb5-9a6f-4b92-a3c5-b12ce74fb941\",\"caf38b23-8be9-4d51-a38a-0a7b2cba64f8\":\"0aa5d024-d829-4c52-8b6d-0df4c27d9729\",\"8cca7166-61d4-4ef7-a6d6-c707221bf85b\":\"e5b40524-b780-4b54-92bd-2e876c78226e\",\"2b9bdff8-b780-4f8a-97ae-491fef6a8a56\":\"0d489fcf-650d-4f54-8b72-3d25321c0268\",\"e523d96b-b281-482b-aeb7-f13e3e8484dd\":\"e14ed5d5-0808-40a4-96ca-d3b3db7231a7\",\"b915de7d-20a3-4767-9d6b-2518edd109c9\":\"8679da36-82cf-4aeb-b7ab-66297459ae6d\",\"974f1396-4992-44a4-aef3-a9c6f4d46acd\":\"4be91d27-2906-44bc-9d46-507c5e6394de\",\"32009c3f-855e-4c9c-bee5-a14230cbdc35\":\"eae262a1-6351-493f-b0d7-426068310bcc\",\"c5f5a77d-1e9e-4693-95ce-dd584d1c3052\":\"43e93f1e-3791-448d-a627-aec90d38a971\",\"c1cfe7b4-f52a-4303-9401-f7c88eda09cb\":\"13b8e79d-fb92-4d03-a662-c6886a57c64d\",\"81c724bc-2549-41a9-b8e0-8898e6dbe6ce\":\"81006645-a9c2-44aa-b68e-33677b1abe37\",\"ad571636-9e99-440e-87c4-b90b293858ac\":\"f0a8c777-f25d-4c4f-bed2-3735fb18db26\",\"bcaca201-e5b4-4f3b-95bc-40b11fbc0971\":\"9ebf0d87-5db0-4afd-a575-f1788f6c1261\",\"f76bee19-9224-44e2-8424-645e945fc213\":\"ba44c1ed-125e-43ec-ad73-c188d10c00e3\",\"c0296e3e-dc32-4f9b-a38d-2e65fa135e75\":\"b76f9ad0-4842-4c17-8283-2fb17fe54e9b\",\"633868a6-b44d-4dfb-926e-1d470ab0ab76\":\"88303b1a-cc57-4581-915a-38921f138ea3\",\"e602b8d7-1850-4c07-a361-eebeb14a6507\":\"6a486a59-402c-4d45-ac26-d9affad5f195\",\"bdd2303c-87b4-4de3-9cf8-2165a191901d\":\"304ccc80-6bed-46ea-9fa4-06beb6cf4c63\",\"9b70fd00-834c-48a1-8160-6a96549521ce\":\"bd095643-5603-4252-bb24-4e7e266dc5bb\",\"96df16fa-eded-4c6d-802a-ae3a5e5b9ae7\":\"b4fc334e-312e-4974-b694-d29fc02baa3f\",\"b9b45b30-dcc6-49f6-bc4e-660b20a5b8f5\":\"62ceba4e-15db-43c7-9a4d-1559d455e0f1\",\"d62da55b-4bc7-4e9e-978f-9854312bd945\":\"80ab0d68-972b-4fe0-b6d1-b446da7bb482\",\"28d99634-a485-4a77-9ca6-64038082e116\":\"ba0330e0-c9ae-4051-9ad9-477dfeae5a40\",\"50033a2e-d5dc-41f5-9351-446f51c2257e\":\"5a59063c-3554-4943-8e34-a4155ae38ab7\",\"4d925522-2af0-43fa-9a1e-afcb11643087\":\"e268c288-0b75-4bde-a42e-1edd646f6474\",\"6b4d49a7-3607-4e2e-b2d8-61166df3fff4\":\"05e13430-7490-44c5-9a02-8a34433187e5\",\"a3594606-43cd-43ef-89c8-6493ed291a4f\":\"5a13a076-7b70-4282-bcfe-2057c92c9bbd\",\"aa156150-44c9-4473-8a16-dadf91410695\":\"81bb7231-3406-46fd-9215-82bfb1fd72c3\",\"8e9166af-e7c2-44ac-b7c4-b1438fbf7c36\":\"d70bc182-9edb-409a-8e5e-05c58f9ef05e\",\"434f5cd1-86eb-4e4e-aa46-2d23ac7acb0d\":\"bcd718cd-2f7e-4def-89c1-cecc5551c060\",\"ffbaba41-8b32-428d-b3d9-e69aeda13dd6\":\"3236f301-65e9-44ae-8dfd-ec2b3aea79a0\"},\"activity_progress\":{\"8fbce011-a3d7-4be3-94f8-1f5aabe4e747\":2,\"10bf14c1-705d-49d1-8dd5-a6af524f0af5\":2,\"caf38b23-8be9-4d51-a38a-0a7b2cba64f8\":2,\"8cca7166-61d4-4ef7-a6d6-c707221bf85b\":2,\"e523d96b-b281-482b-aeb7-f13e3e8484dd\":2,\"2b9bdff8-b780-4f8a-97ae-491fef6a8a56\":2,\"b915de7d-20a3-4767-9d6b-2518edd109c9\":2,\"974f1396-4992-44a4-aef3-a9c6f4d46acd\":2,\"32009c3f-855e-4c9c-bee5-a14230cbdc35\":2,\"c5f5a77d-1e9e-4693-95ce-dd584d1c3052\":2,\"c1cfe7b4-f52a-4303-9401-f7c88eda09cb\":2,\"81c724bc-2549-41a9-b8e0-8898e6dbe6ce\":2,\"ad571636-9e99-440e-87c4-b90b293858ac\":2,\"bcaca201-e5b4-4f3b-95bc-40b11fbc0971\":2,\"f76bee19-9224-44e2-8424-645e945fc213\":2,\"c0296e3e-dc32-4f9b-a38d-2e65fa135e75\":2,\"633868a6-b44d-4dfb-926e-1d470ab0ab76\":2,\"e602b8d7-1850-4c07-a361-eebeb14a6507\":2,\"96df16fa-eded-4c6d-802a-ae3a5e5b9ae7\":2,\"d62da55b-4bc7-4e9e-978f-9854312bd945\":2,\"b9b45b30-dcc6-49f6-bc4e-660b20a5b8f5\":2,\"28d99634-a485-4a77-9ca6-64038082e116\":2,\"50033a2e-d5dc-41f5-9351-446f51c2257e\":2,\"4d925522-2af0-43fa-9a1e-afcb11643087\":2,\"6b4d49a7-3607-4e2e-b2d8-61166df3fff4\":2,\"a3594606-43cd-43ef-89c8-6493ed291a4f\":2,\"aa156150-44c9-4473-8a16-dadf91410695\":2},\"resource_progress\":{\"bdd57b36-b05f-4cb0-8c74-89d3fd2ffd25\":2,\"4e811eb5-9a6f-4b92-a3c5-b12ce74fb941\":2,\"0aa5d024-d829-4c52-8b6d-0df4c27d9729\":2,\"e5b40524-b780-4b54-92bd-2e876c78226e\":2,\"e14ed5d5-0808-40a4-96ca-d3b3db7231a7\":2,\"0d489fcf-650d-4f54-8b72-3d25321c0268\":2,\"8679da36-82cf-4aeb-b7ab-66297459ae6d\":2,\"4be91d27-2906-44bc-9d46-507c5e6394de\":2,\"eae262a1-6351-493f-b0d7-426068310bcc\":2,\"43e93f1e-3791-448d-a627-aec90d38a971\":2,\"13b8e79d-fb92-4d03-a662-c6886a57c64d\":2,\"81006645-a9c2-44aa-b68e-33677b1abe37\":2,\"f0a8c777-f25d-4c4f-bed2-3735fb18db26\":2,\"9ebf0d87-5db0-4afd-a575-f1788f6c1261\":2,\"ba44c1ed-125e-43ec-ad73-c188d10c00e3\":2,\"b76f9ad0-4842-4c17-8283-2fb17fe54e9b\":2,\"88303b1a-cc57-4581-915a-38921f138ea3\":2,\"6a486a59-402c-4d45-ac26-d9affad5f195\":2,\"b4fc334e-312e-4974-b694-d29fc02baa3f\":2,\"80ab0d68-972b-4fe0-b6d1-b446da7bb482\":2,\"62ceba4e-15db-43c7-9a4d-1559d455e0f1\":2,\"ba0330e0-c9ae-4051-9ad9-477dfeae5a40\":2,\"5a59063c-3554-4943-8e34-a4155ae38ab7\":2,\"e268c288-0b75-4bde-a42e-1edd646f6474\":2,\"05e13430-7490-44c5-9a02-8a34433187e5\":2,\"5a13a076-7b70-4282-bcfe-2057c92c9bbd\":2,\"81bb7231-3406-46fd-9215-82bfb1fd72c3\":2},\"miniwork_progress\":{},\"resource_max_pos\":{\"bdd57b36-b05f-4cb0-8c74-89d3fd2ffd25\":{\"pos\":324,\"type\":\"video\"},\"4e811eb5-9a6f-4b92-a3c5-b12ce74fb941\":{\"pos\":1177,\"type\":\"video\"},\"0aa5d024-d829-4c52-8b6d-0df4c27d9729\":{\"pos\":771,\"type\":\"video\"},\"e5b40524-b780-4b54-92bd-2e876c78226e\":{\"pos\":1460,\"type\":\"video\"},\"0d489fcf-650d-4f54-8b72-3d25321c0268\":{\"pos\":746,\"type\":\"video\"},\"e14ed5d5-0808-40a4-96ca-d3b3db7231a7\":{\"pos\":682,\"type\":\"video\"},\"8679da36-82cf-4aeb-b7ab-66297459ae6d\":{\"pos\":567,\"type\":\"video\"},\"4be91d27-2906-44bc-9d46-507c5e6394de\":{\"pos\":578,\"type\":\"video\"},\"eae262a1-6351-493f-b0d7-426068310bcc\":{\"pos\":711,\"type\":\"video\"},\"43e93f1e-3791-448d-a627-aec90d38a971\":{\"pos\":606,\"type\":\"video\"},\"13b8e79d-fb92-4d03-a662-c6886a57c64d\":{\"pos\":669,\"type\":\"video\"},\"81006645-a9c2-44aa-b68e-33677b1abe37\":{\"pos\":583,\"type\":\"video\"},\"f0a8c777-f25d-4c4f-bed2-3735fb18db26\":{\"pos\":718,\"type\":\"video\"},\"9ebf0d87-5db0-4afd-a575-f1788f6c1261\":{\"pos\":721,\"type\":\"video\"},\"ba44c1ed-125e-43ec-ad73-c188d10c00e3\":{\"pos\":515,\"type\":\"video\"},\"b76f9ad0-4842-4c17-8283-2fb17fe54e9b\":{\"pos\":611,\"type\":\"video\"},\"88303b1a-cc57-4581-915a-38921f138ea3\":{\"pos\":900,\"type\":\"video\"},\"6a486a59-402c-4d45-ac26-d9affad5f195\":{\"pos\":563,\"type\":\"video\"},\"304ccc80-6bed-46ea-9fa4-06beb6cf4c63\":{\"pos\":0,\"type\":\"video\"},\"bd095643-5603-4252-bb24-4e7e266dc5bb\":{\"pos\":0,\"type\":\"video\"},\"b4fc334e-312e-4974-b694-d29fc02baa3f\":{\"pos\":131,\"type\":\"video\"},\"62ceba4e-15db-43c7-9a4d-1559d455e0f1\":{\"pos\":193,\"type\":\"video\"},\"80ab0d68-972b-4fe0-b6d1-b446da7bb482\":{\"pos\":296,\"type\":\"video\"},\"ba0330e0-c9ae-4051-9ad9-477dfeae5a40\":{\"pos\":180,\"type\":\"video\"},\"5a59063c-3554-4943-8e34-a4155ae38ab7\":{\"pos\":190,\"type\":\"video\"},\"e268c288-0b75-4bde-a42e-1edd646f6474\":{\"pos\":166,\"type\":\"video\"},\"05e13430-7490-44c5-9a02-8a34433187e5\":{\"pos\":205,\"type\":\"video\"},\"5a13a076-7b70-4282-bcfe-2057c92c9bbd\":{\"pos\":197,\"type\":\"video\"},\"81bb7231-3406-46fd-9215-82bfb1fd72c3\":{\"pos\":170,\"type\":\"video\"},\"d70bc182-9edb-409a-8e5e-05c58f9ef05e\":{\"pos\":0,\"type\":\"video\"}},\"activity_exam_progress\":{},\"activity_event\":{},\"resource_study_time_ignore\":[]}',
    }

    response = requests.post('https://x-study-record-api.ykt.eduyun.cn/v1/study_details', headers=headers,
                             json=json_data)
    print(response.text)


def test2_study_details():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Authorization': 'MAC id="7F938B205F876FC3A30551F3A4931383A0EEAAB1A22B98532C4F17D64B13A755A153E1FD1F3C38A943A31A4D11C6F6C6FF7DF7DCBB08EBE3",nonce="1727366470112:1LRCSSDP",mac="9zFd8Hcc5bg1VFZs+qJL4vwWQTm+IsVQf32vMuCWBl4="',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://basic.smartedu.cn',
        'Referer': 'https://basic.smartedu.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        'sdp-app-id': 'e5649925-441d-4a53-b525-51a2f1c4e0a8',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'user_id': 452651017041,
        'resource_id': '0de67197-af6f-43ab-8d89-59a75aab289e',
        'resource_name': '大力弘扬教育家精神',
        'resource_type': 't_course',
        'catalog_type': 'teacherTraining',
        'topic_type': '0de67197-af6f-43ab-8d89-59a75aab289e',
        'progress': 53,
        'status': 1,
        'ext_info': '{\"cv\":1,\"platform\":\"web\",\"tags\":\"2024年“暑期教师研修”专题\",\"origin\":\"2024年“暑期教师研修”专题\",\"cover\":\"https://s-file-1.ykt.cbern.com.cn/zxx/X-COURSE/416/1_1720504053551.jpg\",\"last_learning_activity\":{\"activity_id\":\"434f5cd1-86eb-4e4e-aa46-2d23ac7acb0d\",\"title\":\"俞国平：坚守初心教育是我一生的事业\"},\"activity_last_learning_resource\":{\"8fbce011-a3d7-4be3-94f8-1f5aabe4e747\":\"bdd57b36-b05f-4cb0-8c74-89d3fd2ffd25\",\"10bf14c1-705d-49d1-8dd5-a6af524f0af5\":\"4e811eb5-9a6f-4b92-a3c5-b12ce74fb941\",\"caf38b23-8be9-4d51-a38a-0a7b2cba64f8\":\"0aa5d024-d829-4c52-8b6d-0df4c27d9729\",\"8cca7166-61d4-4ef7-a6d6-c707221bf85b\":\"e5b40524-b780-4b54-92bd-2e876c78226e\",\"2b9bdff8-b780-4f8a-97ae-491fef6a8a56\":\"0d489fcf-650d-4f54-8b72-3d25321c0268\",\"e523d96b-b281-482b-aeb7-f13e3e8484dd\":\"e14ed5d5-0808-40a4-96ca-d3b3db7231a7\",\"b915de7d-20a3-4767-9d6b-2518edd109c9\":\"8679da36-82cf-4aeb-b7ab-66297459ae6d\",\"974f1396-4992-44a4-aef3-a9c6f4d46acd\":\"4be91d27-2906-44bc-9d46-507c5e6394de\",\"32009c3f-855e-4c9c-bee5-a14230cbdc35\":\"eae262a1-6351-493f-b0d7-426068310bcc\",\"c5f5a77d-1e9e-4693-95ce-dd584d1c3052\":\"43e93f1e-3791-448d-a627-aec90d38a971\",\"c1cfe7b4-f52a-4303-9401-f7c88eda09cb\":\"13b8e79d-fb92-4d03-a662-c6886a57c64d\",\"81c724bc-2549-41a9-b8e0-8898e6dbe6ce\":\"81006645-a9c2-44aa-b68e-33677b1abe37\",\"ad571636-9e99-440e-87c4-b90b293858ac\":\"f0a8c777-f25d-4c4f-bed2-3735fb18db26\",\"bcaca201-e5b4-4f3b-95bc-40b11fbc0971\":\"9ebf0d87-5db0-4afd-a575-f1788f6c1261\",\"f76bee19-9224-44e2-8424-645e945fc213\":\"ba44c1ed-125e-43ec-ad73-c188d10c00e3\",\"c0296e3e-dc32-4f9b-a38d-2e65fa135e75\":\"b76f9ad0-4842-4c17-8283-2fb17fe54e9b\",\"633868a6-b44d-4dfb-926e-1d470ab0ab76\":\"88303b1a-cc57-4581-915a-38921f138ea3\",\"e602b8d7-1850-4c07-a361-eebeb14a6507\":\"6a486a59-402c-4d45-ac26-d9affad5f195\",\"bdd2303c-87b4-4de3-9cf8-2165a191901d\":\"304ccc80-6bed-46ea-9fa4-06beb6cf4c63\",\"9b70fd00-834c-48a1-8160-6a96549521ce\":\"bd095643-5603-4252-bb24-4e7e266dc5bb\",\"96df16fa-eded-4c6d-802a-ae3a5e5b9ae7\":\"b4fc334e-312e-4974-b694-d29fc02baa3f\",\"b9b45b30-dcc6-49f6-bc4e-660b20a5b8f5\":\"62ceba4e-15db-43c7-9a4d-1559d455e0f1\",\"d62da55b-4bc7-4e9e-978f-9854312bd945\":\"80ab0d68-972b-4fe0-b6d1-b446da7bb482\",\"28d99634-a485-4a77-9ca6-64038082e116\":\"ba0330e0-c9ae-4051-9ad9-477dfeae5a40\",\"50033a2e-d5dc-41f5-9351-446f51c2257e\":\"5a59063c-3554-4943-8e34-a4155ae38ab7\",\"4d925522-2af0-43fa-9a1e-afcb11643087\":\"e268c288-0b75-4bde-a42e-1edd646f6474\",\"6b4d49a7-3607-4e2e-b2d8-61166df3fff4\":\"05e13430-7490-44c5-9a02-8a34433187e5\",\"a3594606-43cd-43ef-89c8-6493ed291a4f\":\"5a13a076-7b70-4282-bcfe-2057c92c9bbd\",\"aa156150-44c9-4473-8a16-dadf91410695\":\"81bb7231-3406-46fd-9215-82bfb1fd72c3\",\"8e9166af-e7c2-44ac-b7c4-b1438fbf7c36\":\"d70bc182-9edb-409a-8e5e-05c58f9ef05e\",\"434f5cd1-86eb-4e4e-aa46-2d23ac7acb0d\":\"bcd718cd-2f7e-4def-89c1-cecc5551c060\",\"ffbaba41-8b32-428d-b3d9-e69aeda13dd6\":\"3236f301-65e9-44ae-8dfd-ec2b3aea79a0\"},\"activity_progress\":{\"8fbce011-a3d7-4be3-94f8-1f5aabe4e747\":2,\"10bf14c1-705d-49d1-8dd5-a6af524f0af5\":2,\"caf38b23-8be9-4d51-a38a-0a7b2cba64f8\":2,\"8cca7166-61d4-4ef7-a6d6-c707221bf85b\":2,\"e523d96b-b281-482b-aeb7-f13e3e8484dd\":2,\"2b9bdff8-b780-4f8a-97ae-491fef6a8a56\":2,\"b915de7d-20a3-4767-9d6b-2518edd109c9\":2,\"974f1396-4992-44a4-aef3-a9c6f4d46acd\":2,\"32009c3f-855e-4c9c-bee5-a14230cbdc35\":2,\"c5f5a77d-1e9e-4693-95ce-dd584d1c3052\":2,\"c1cfe7b4-f52a-4303-9401-f7c88eda09cb\":2,\"81c724bc-2549-41a9-b8e0-8898e6dbe6ce\":2,\"ad571636-9e99-440e-87c4-b90b293858ac\":2,\"bcaca201-e5b4-4f3b-95bc-40b11fbc0971\":2,\"f76bee19-9224-44e2-8424-645e945fc213\":2,\"c0296e3e-dc32-4f9b-a38d-2e65fa135e75\":2,\"633868a6-b44d-4dfb-926e-1d470ab0ab76\":2,\"e602b8d7-1850-4c07-a361-eebeb14a6507\":2,\"96df16fa-eded-4c6d-802a-ae3a5e5b9ae7\":2,\"d62da55b-4bc7-4e9e-978f-9854312bd945\":2,\"b9b45b30-dcc6-49f6-bc4e-660b20a5b8f5\":2,\"28d99634-a485-4a77-9ca6-64038082e116\":2,\"50033a2e-d5dc-41f5-9351-446f51c2257e\":2,\"4d925522-2af0-43fa-9a1e-afcb11643087\":2,\"6b4d49a7-3607-4e2e-b2d8-61166df3fff4\":2,\"a3594606-43cd-43ef-89c8-6493ed291a4f\":2,\"aa156150-44c9-4473-8a16-dadf91410695\":2},\"resource_progress\":{\"bdd57b36-b05f-4cb0-8c74-89d3fd2ffd25\":2,\"4e811eb5-9a6f-4b92-a3c5-b12ce74fb941\":2,\"0aa5d024-d829-4c52-8b6d-0df4c27d9729\":2,\"e5b40524-b780-4b54-92bd-2e876c78226e\":2,\"e14ed5d5-0808-40a4-96ca-d3b3db7231a7\":2,\"0d489fcf-650d-4f54-8b72-3d25321c0268\":2,\"8679da36-82cf-4aeb-b7ab-66297459ae6d\":2,\"4be91d27-2906-44bc-9d46-507c5e6394de\":2,\"eae262a1-6351-493f-b0d7-426068310bcc\":2,\"43e93f1e-3791-448d-a627-aec90d38a971\":2,\"13b8e79d-fb92-4d03-a662-c6886a57c64d\":2,\"81006645-a9c2-44aa-b68e-33677b1abe37\":2,\"f0a8c777-f25d-4c4f-bed2-3735fb18db26\":2,\"9ebf0d87-5db0-4afd-a575-f1788f6c1261\":2,\"ba44c1ed-125e-43ec-ad73-c188d10c00e3\":2,\"b76f9ad0-4842-4c17-8283-2fb17fe54e9b\":2,\"88303b1a-cc57-4581-915a-38921f138ea3\":2,\"6a486a59-402c-4d45-ac26-d9affad5f195\":2,\"b4fc334e-312e-4974-b694-d29fc02baa3f\":2,\"80ab0d68-972b-4fe0-b6d1-b446da7bb482\":2,\"62ceba4e-15db-43c7-9a4d-1559d455e0f1\":2,\"ba0330e0-c9ae-4051-9ad9-477dfeae5a40\":2,\"5a59063c-3554-4943-8e34-a4155ae38ab7\":2,\"e268c288-0b75-4bde-a42e-1edd646f6474\":2,\"05e13430-7490-44c5-9a02-8a34433187e5\":2,\"5a13a076-7b70-4282-bcfe-2057c92c9bbd\":2,\"81bb7231-3406-46fd-9215-82bfb1fd72c3\":2},\"miniwork_progress\":{},\"resource_max_pos\":{\"bdd57b36-b05f-4cb0-8c74-89d3fd2ffd25\":{\"pos\":324,\"type\":\"video\"},\"4e811eb5-9a6f-4b92-a3c5-b12ce74fb941\":{\"pos\":1177,\"type\":\"video\"},\"0aa5d024-d829-4c52-8b6d-0df4c27d9729\":{\"pos\":771,\"type\":\"video\"},\"e5b40524-b780-4b54-92bd-2e876c78226e\":{\"pos\":1460,\"type\":\"video\"},\"0d489fcf-650d-4f54-8b72-3d25321c0268\":{\"pos\":746,\"type\":\"video\"},\"e14ed5d5-0808-40a4-96ca-d3b3db7231a7\":{\"pos\":682,\"type\":\"video\"},\"8679da36-82cf-4aeb-b7ab-66297459ae6d\":{\"pos\":567,\"type\":\"video\"},\"4be91d27-2906-44bc-9d46-507c5e6394de\":{\"pos\":578,\"type\":\"video\"},\"eae262a1-6351-493f-b0d7-426068310bcc\":{\"pos\":711,\"type\":\"video\"},\"43e93f1e-3791-448d-a627-aec90d38a971\":{\"pos\":606,\"type\":\"video\"},\"13b8e79d-fb92-4d03-a662-c6886a57c64d\":{\"pos\":669,\"type\":\"video\"},\"81006645-a9c2-44aa-b68e-33677b1abe37\":{\"pos\":583,\"type\":\"video\"},\"f0a8c777-f25d-4c4f-bed2-3735fb18db26\":{\"pos\":718,\"type\":\"video\"},\"9ebf0d87-5db0-4afd-a575-f1788f6c1261\":{\"pos\":721,\"type\":\"video\"},\"ba44c1ed-125e-43ec-ad73-c188d10c00e3\":{\"pos\":515,\"type\":\"video\"},\"b76f9ad0-4842-4c17-8283-2fb17fe54e9b\":{\"pos\":611,\"type\":\"video\"},\"88303b1a-cc57-4581-915a-38921f138ea3\":{\"pos\":900,\"type\":\"video\"},\"6a486a59-402c-4d45-ac26-d9affad5f195\":{\"pos\":563,\"type\":\"video\"},\"304ccc80-6bed-46ea-9fa4-06beb6cf4c63\":{\"pos\":0,\"type\":\"video\"},\"bd095643-5603-4252-bb24-4e7e266dc5bb\":{\"pos\":0,\"type\":\"video\"},\"b4fc334e-312e-4974-b694-d29fc02baa3f\":{\"pos\":131,\"type\":\"video\"},\"62ceba4e-15db-43c7-9a4d-1559d455e0f1\":{\"pos\":193,\"type\":\"video\"},\"80ab0d68-972b-4fe0-b6d1-b446da7bb482\":{\"pos\":296,\"type\":\"video\"},\"ba0330e0-c9ae-4051-9ad9-477dfeae5a40\":{\"pos\":180,\"type\":\"video\"},\"5a59063c-3554-4943-8e34-a4155ae38ab7\":{\"pos\":190,\"type\":\"video\"},\"e268c288-0b75-4bde-a42e-1edd646f6474\":{\"pos\":166,\"type\":\"video\"},\"05e13430-7490-44c5-9a02-8a34433187e5\":{\"pos\":205,\"type\":\"video\"},\"5a13a076-7b70-4282-bcfe-2057c92c9bbd\":{\"pos\":197,\"type\":\"video\"},\"81bb7231-3406-46fd-9215-82bfb1fd72c3\":{\"pos\":170,\"type\":\"video\"},\"d70bc182-9edb-409a-8e5e-05c58f9ef05e\":{\"pos\":0,\"type\":\"video\"}},\"activity_exam_progress\":{},\"activity_event\":{},\"resource_study_time_ignore\":[]}',    }

    response = requests.post('https://x-study-record-api.ykt.eduyun.cn/v1/study_details', headers=headers,
                             json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    # data = '{"user_id":452651017041,"resource_id":"0de67197-af6f-43ab-8d89-59a75aab289e","resource_name":"大力弘扬教育家精神","resource_type":"t_course","catalog_type":"teacherTraining","topic_type":"0de67197-af6f-43ab-8d89-59a75aab289e","progress":53,"status":1,"ext_info":"{\\"cv\\":1,\\"platform\\":\\"web\\",\\"tags\\":\\"2024年“暑期教师研修”专题\\",\\"origin\\":\\"2024年“暑期教师研修”专题\\",\\"cover\\":\\"https://s-file-1.ykt.cbern.com.cn/zxx/X-COURSE/416/1_1720504053551.jpg\\",\\"last_learning_activity\\":{\\"activity_id\\":\\"434f5cd1-86eb-4e4e-aa46-2d23ac7acb0d\\",\\"title\\":\\"俞国平：坚守初心教育是我一生的事业\\"},\\"activity_last_learning_resource\\":{\\"8fbce011-a3d7-4be3-94f8-1f5aabe4e747\\":\\"bdd57b36-b05f-4cb0-8c74-89d3fd2ffd25\\",\\"10bf14c1-705d-49d1-8dd5-a6af524f0af5\\":\\"4e811eb5-9a6f-4b92-a3c5-b12ce74fb941\\",\\"caf38b23-8be9-4d51-a38a-0a7b2cba64f8\\":\\"0aa5d024-d829-4c52-8b6d-0df4c27d9729\\",\\"8cca7166-61d4-4ef7-a6d6-c707221bf85b\\":\\"e5b40524-b780-4b54-92bd-2e876c78226e\\",\\"2b9bdff8-b780-4f8a-97ae-491fef6a8a56\\":\\"0d489fcf-650d-4f54-8b72-3d25321c0268\\",\\"e523d96b-b281-482b-aeb7-f13e3e8484dd\\":\\"e14ed5d5-0808-40a4-96ca-d3b3db7231a7\\",\\"b915de7d-20a3-4767-9d6b-2518edd109c9\\":\\"8679da36-82cf-4aeb-b7ab-66297459ae6d\\",\\"974f1396-4992-44a4-aef3-a9c6f4d46acd\\":\\"4be91d27-2906-44bc-9d46-507c5e6394de\\",\\"32009c3f-855e-4c9c-bee5-a14230cbdc35\\":\\"eae262a1-6351-493f-b0d7-426068310bcc\\",\\"c5f5a77d-1e9e-4693-95ce-dd584d1c3052\\":\\"43e93f1e-3791-448d-a627-aec90d38a971\\",\\"c1cfe7b4-f52a-4303-9401-f7c88eda09cb\\":\\"13b8e79d-fb92-4d03-a662-c6886a57c64d\\",\\"81c724bc-2549-41a9-b8e0-8898e6dbe6ce\\":\\"81006645-a9c2-44aa-b68e-33677b1abe37\\",\\"ad571636-9e99-440e-87c4-b90b293858ac\\":\\"f0a8c777-f25d-4c4f-bed2-3735fb18db26\\",\\"bcaca201-e5b4-4f3b-95bc-40b11fbc0971\\":\\"9ebf0d87-5db0-4afd-a575-f1788f6c1261\\",\\"f76bee19-9224-44e2-8424-645e945fc213\\":\\"ba44c1ed-125e-43ec-ad73-c188d10c00e3\\",\\"c0296e3e-dc32-4f9b-a38d-2e65fa135e75\\":\\"b76f9ad0-4842-4c17-8283-2fb17fe54e9b\\",\\"633868a6-b44d-4dfb-926e-1d470ab0ab76\\":\\"88303b1a-cc57-4581-915a-38921f138ea3\\",\\"e602b8d7-1850-4c07-a361-eebeb14a6507\\":\\"6a486a59-402c-4d45-ac26-d9affad5f195\\",\\"bdd2303c-87b4-4de3-9cf8-2165a191901d\\":\\"304ccc80-6bed-46ea-9fa4-06beb6cf4c63\\",\\"9b70fd00-834c-48a1-8160-6a96549521ce\\":\\"bd095643-5603-4252-bb24-4e7e266dc5bb\\",\\"96df16fa-eded-4c6d-802a-ae3a5e5b9ae7\\":\\"b4fc334e-312e-4974-b694-d29fc02baa3f\\",\\"b9b45b30-dcc6-49f6-bc4e-660b20a5b8f5\\":\\"62ceba4e-15db-43c7-9a4d-1559d455e0f1\\",\\"d62da55b-4bc7-4e9e-978f-9854312bd945\\":\\"80ab0d68-972b-4fe0-b6d1-b446da7bb482\\",\\"28d99634-a485-4a77-9ca6-64038082e116\\":\\"ba0330e0-c9ae-4051-9ad9-477dfeae5a40\\",\\"50033a2e-d5dc-41f5-9351-446f51c2257e\\":\\"5a59063c-3554-4943-8e34-a4155ae38ab7\\",\\"4d925522-2af0-43fa-9a1e-afcb11643087\\":\\"e268c288-0b75-4bde-a42e-1edd646f6474\\",\\"6b4d49a7-3607-4e2e-b2d8-61166df3fff4\\":\\"05e13430-7490-44c5-9a02-8a34433187e5\\",\\"a3594606-43cd-43ef-89c8-6493ed291a4f\\":\\"5a13a076-7b70-4282-bcfe-2057c92c9bbd\\",\\"aa156150-44c9-4473-8a16-dadf91410695\\":\\"81bb7231-3406-46fd-9215-82bfb1fd72c3\\",\\"8e9166af-e7c2-44ac-b7c4-b1438fbf7c36\\":\\"d70bc182-9edb-409a-8e5e-05c58f9ef05e\\",\\"434f5cd1-86eb-4e4e-aa46-2d23ac7acb0d\\":\\"bcd718cd-2f7e-4def-89c1-cecc5551c060\\"},\\"activity_progress\\":{\\"8fbce011-a3d7-4be3-94f8-1f5aabe4e747\\":2,\\"10bf14c1-705d-49d1-8dd5-a6af524f0af5\\":2,\\"caf38b23-8be9-4d51-a38a-0a7b2cba64f8\\":2,\\"8cca7166-61d4-4ef7-a6d6-c707221bf85b\\":2,\\"e523d96b-b281-482b-aeb7-f13e3e8484dd\\":2,\\"2b9bdff8-b780-4f8a-97ae-491fef6a8a56\\":2,\\"b915de7d-20a3-4767-9d6b-2518edd109c9\\":2,\\"974f1396-4992-44a4-aef3-a9c6f4d46acd\\":2,\\"32009c3f-855e-4c9c-bee5-a14230cbdc35\\":2,\\"c5f5a77d-1e9e-4693-95ce-dd584d1c3052\\":2,\\"c1cfe7b4-f52a-4303-9401-f7c88eda09cb\\":2,\\"81c724bc-2549-41a9-b8e0-8898e6dbe6ce\\":2,\\"ad571636-9e99-440e-87c4-b90b293858ac\\":2,\\"bcaca201-e5b4-4f3b-95bc-40b11fbc0971\\":2,\\"f76bee19-9224-44e2-8424-645e945fc213\\":2,\\"c0296e3e-dc32-4f9b-a38d-2e65fa135e75\\":2,\\"633868a6-b44d-4dfb-926e-1d470ab0ab76\\":2,\\"e602b8d7-1850-4c07-a361-eebeb14a6507\\":2,\\"96df16fa-eded-4c6d-802a-ae3a5e5b9ae7\\":2,\\"d62da55b-4bc7-4e9e-978f-9854312bd945\\":2,\\"b9b45b30-dcc6-49f6-bc4e-660b20a5b8f5\\":2,\\"28d99634-a485-4a77-9ca6-64038082e116\\":2,\\"50033a2e-d5dc-41f5-9351-446f51c2257e\\":2,\\"4d925522-2af0-43fa-9a1e-afcb11643087\\":2,\\"6b4d49a7-3607-4e2e-b2d8-61166df3fff4\\":2,\\"a3594606-43cd-43ef-89c8-6493ed291a4f\\":2,\\"aa156150-44c9-4473-8a16-dadf91410695\\":2,\\"434f5cd1-86eb-4e4e-aa46-2d23ac7acb0d\\":2},\\"resource_progress\\":{\\"bdd57b36-b05f-4cb0-8c74-89d3fd2ffd25\\":2,\\"4e811eb5-9a6f-4b92-a3c5-b12ce74fb941\\":2,\\"0aa5d024-d829-4c52-8b6d-0df4c27d9729\\":2,\\"e5b40524-b780-4b54-92bd-2e876c78226e\\":2,\\"e14ed5d5-0808-40a4-96ca-d3b3db7231a7\\":2,\\"0d489fcf-650d-4f54-8b72-3d25321c0268\\":2,\\"8679da36-82cf-4aeb-b7ab-66297459ae6d\\":2,\\"4be91d27-2906-44bc-9d46-507c5e6394de\\":2,\\"eae262a1-6351-493f-b0d7-426068310bcc\\":2,\\"43e93f1e-3791-448d-a627-aec90d38a971\\":2,\\"13b8e79d-fb92-4d03-a662-c6886a57c64d\\":2,\\"81006645-a9c2-44aa-b68e-33677b1abe37\\":2,\\"f0a8c777-f25d-4c4f-bed2-3735fb18db26\\":2,\\"9ebf0d87-5db0-4afd-a575-f1788f6c1261\\":2,\\"ba44c1ed-125e-43ec-ad73-c188d10c00e3\\":2,\\"b76f9ad0-4842-4c17-8283-2fb17fe54e9b\\":2,\\"88303b1a-cc57-4581-915a-38921f138ea3\\":2,\\"6a486a59-402c-4d45-ac26-d9affad5f195\\":2,\\"b4fc334e-312e-4974-b694-d29fc02baa3f\\":2,\\"80ab0d68-972b-4fe0-b6d1-b446da7bb482\\":2,\\"62ceba4e-15db-43c7-9a4d-1559d455e0f1\\":2,\\"ba0330e0-c9ae-4051-9ad9-477dfeae5a40\\":2,\\"5a59063c-3554-4943-8e34-a4155ae38ab7\\":2,\\"e268c288-0b75-4bde-a42e-1edd646f6474\\":2,\\"05e13430-7490-44c5-9a02-8a34433187e5\\":2,\\"5a13a076-7b70-4282-bcfe-2057c92c9bbd\\":2,\\"81bb7231-3406-46fd-9215-82bfb1fd72c3\\":2,\\"bcd718cd-2f7e-4def-89c1-cecc5551c060\\":2},\\"miniwork_progress\\":{},\\"resource_max_pos\\":{\\"bdd57b36-b05f-4cb0-8c74-89d3fd2ffd25\\":{\\"pos\\":324,\\"type\\":\\"video\\"},\\"4e811eb5-9a6f-4b92-a3c5-b12ce74fb941\\":{\\"pos\\":1177,\\"type\\":\\"video\\"},\\"0aa5d024-d829-4c52-8b6d-0df4c27d9729\\":{\\"pos\\":771,\\"type\\":\\"video\\"},\\"e5b40524-b780-4b54-92bd-2e876c78226e\\":{\\"pos\\":1460,\\"type\\":\\"video\\"},\\"0d489fcf-650d-4f54-8b72-3d25321c0268\\":{\\"pos\\":746,\\"type\\":\\"video\\"},\\"e14ed5d5-0808-40a4-96ca-d3b3db7231a7\\":{\\"pos\\":682,\\"type\\":\\"video\\"},\\"8679da36-82cf-4aeb-b7ab-66297459ae6d\\":{\\"pos\\":567,\\"type\\":\\"video\\"},\\"4be91d27-2906-44bc-9d46-507c5e6394de\\":{\\"pos\\":578,\\"type\\":\\"video\\"},\\"eae262a1-6351-493f-b0d7-426068310bcc\\":{\\"pos\\":711,\\"type\\":\\"video\\"},\\"43e93f1e-3791-448d-a627-aec90d38a971\\":{\\"pos\\":606,\\"type\\":\\"video\\"},\\"13b8e79d-fb92-4d03-a662-c6886a57c64d\\":{\\"pos\\":669,\\"type\\":\\"video\\"},\\"81006645-a9c2-44aa-b68e-33677b1abe37\\":{\\"pos\\":583,\\"type\\":\\"video\\"},\\"f0a8c777-f25d-4c4f-bed2-3735fb18db26\\":{\\"pos\\":718,\\"type\\":\\"video\\"},\\"9ebf0d87-5db0-4afd-a575-f1788f6c1261\\":{\\"pos\\":721,\\"type\\":\\"video\\"},\\"ba44c1ed-125e-43ec-ad73-c188d10c00e3\\":{\\"pos\\":515,\\"type\\":\\"video\\"},\\"b76f9ad0-4842-4c17-8283-2fb17fe54e9b\\":{\\"pos\\":611,\\"type\\":\\"video\\"},\\"88303b1a-cc57-4581-915a-38921f138ea3\\":{\\"pos\\":900,\\"type\\":\\"video\\"},\\"6a486a59-402c-4d45-ac26-d9affad5f195\\":{\\"pos\\":563,\\"type\\":\\"video\\"},\\"304ccc80-6bed-46ea-9fa4-06beb6cf4c63\\":{\\"pos\\":0,\\"type\\":\\"video\\"},\\"bd095643-5603-4252-bb24-4e7e266dc5bb\\":{\\"pos\\":0,\\"type\\":\\"video\\"},\\"b4fc334e-312e-4974-b694-d29fc02baa3f\\":{\\"pos\\":131,\\"type\\":\\"video\\"},\\"62ceba4e-15db-43c7-9a4d-1559d455e0f1\\":{\\"pos\\":193,\\"type\\":\\"video\\"},\\"80ab0d68-972b-4fe0-b6d1-b446da7bb482\\":{\\"pos\\":296,\\"type\\":\\"video\\"},\\"ba0330e0-c9ae-4051-9ad9-477dfeae5a40\\":{\\"pos\\":180,\\"type\\":\\"video\\"},\\"5a59063c-3554-4943-8e34-a4155ae38ab7\\":{\\"pos\\":190,\\"type\\":\\"video\\"},\\"e268c288-0b75-4bde-a42e-1edd646f6474\\":{\\"pos\\":166,\\"type\\":\\"video\\"},\\"05e13430-7490-44c5-9a02-8a34433187e5\\":{\\"pos\\":205,\\"type\\":\\"video\\"},\\"5a13a076-7b70-4282-bcfe-2057c92c9bbd\\":{\\"pos\\":197,\\"type\\":\\"video\\"},\\"81bb7231-3406-46fd-9215-82bfb1fd72c3\\":{\\"pos\\":170,\\"type\\":\\"video\\"},\\"d70bc182-9edb-409a-8e5e-05c58f9ef05e\\":{\\"pos\\":0,\\"type\\":\\"video\\"},\\"bcd718cd-2f7e-4def-89c1-cecc5551c060\\":{\\"pos\\":174,\\"type\\":\\"video\\"}},\\"activity_exam_progress\\":{},\\"activity_event\\":{},\\"resource_study_time_ignore\\":[]}"}'.encode()
    # response = requests.post('https://x-study-record-api.ykt.eduyun.cn/v1/study_details', headers=headers, data=data)
    print(response.text)


if __name__ == '__main__':

    user_id = '452591324786'

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
                # get_method_position(source, user_id)

                postion(True, source, user_id)
                # get_method_position(source, user_id)
                a = a+1

    #             # time.sleep(2)



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
