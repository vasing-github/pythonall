import time

import requests
def test(data,vedio):


    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': '_abfpc=068558c0127bdfb7a931fe9b532a095106e5f962_2.0; cna=6adcc4cd14438a4187f79130a69c05ea; UM_distinctid=1917cc355c10-0f630a6fac0afb-4c657b58-240000-1917cc355c2c0; Hm_lvt_6f8e7b522fd6a613e06b99f5354900b3=1724376375; CNZZDATA1281062390=985325964-1724375062-%7C1724376845; Hm_lvt_f0b6b943aec9775d7c6c7020bf856c6b=1724375278,1724659636,1724743718,1724915220; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221914ec1a1e0846-07a2a8fb27669c8-4c657b58-2359296-1914ec1a1e112cf%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxNGVjMWExZTA4NDYtMDdhMmE4ZmIyNzY2OWM4LTRjNjU3YjU4LTIzNTkyOTYtMTkxNGVjMWExZTExMmNmIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221914ec1a1e0846-07a2a8fb27669c8-4c657b58-2359296-1914ec1a1e112cf%22%7D; UC_SSO_TGC-e5649925-441d-4a53-b525-51a2f1c4e0a8-product=230a9609-e356-473d-a5af-45a50fb20950; passport=https://core.teacher.vocational.smartedu.cn/p/passport; u-lastLoginTime=1725850393661; u-activeState=1; u-mobileState=0; u-mobile=15111305878; requestSource=teacher.higher.smartedu.cn; u-preLoginTime=0; u-token=eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJhN2YxYjA3ZC03ZjE2LTRiZjEtOGE0Zi0yNTA2ZTFkOWRjMjQiLCJpYXQiOjE3MjU4NTAzOTMsInN1YiI6Ijc0NTUyNjU0MDE2NDYxNjE5MiIsImlzcyI6Imd1b3JlbnQiLCJhdHRlc3RTdGF0ZSI6MCwic3JjIjoid2ViIiwiYWN0aXZlU3RhdGUiOjEsIm1vYmlsZSI6IjE1MTExMzA1ODc4IiwicGxhdGZvcm1JZCI6IjEzMTQ1ODU0OTgzMzExIiwiYWNjb3VudCI6IjE1MTExMzA1ODc4IiwiZXhwIjoxNzI1ODg2MzkzfQ.vOFx3TKKRAlicpIbl3sVrJ4NK-b8dGZf_rpzkokV06M; u-token-legacy=eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJhN2YxYjA3ZC03ZjE2LTRiZjEtOGE0Zi0yNTA2ZTFkOWRjMjQiLCJpYXQiOjE3MjU4NTAzOTMsInN1YiI6Ijc0NTUyNjU0MDE2NDYxNjE5MiIsImlzcyI6Imd1b3JlbnQiLCJhdHRlc3RTdGF0ZSI6MCwic3JjIjoid2ViIiwiYWN0aXZlU3RhdGUiOjEsIm1vYmlsZSI6IjE1MTExMzA1ODc4IiwicGxhdGZvcm1JZCI6IjEzMTQ1ODU0OTgzMzExIiwiYWNjb3VudCI6IjE1MTExMzA1ODc4IiwiZXhwIjoxNzI1ODg2MzkzfQ.vOFx3TKKRAlicpIbl3sVrJ4NK-b8dGZf_rpzkokV06M; u-id=745526540164616192; u-account=15111305878; ufo-nk=6ZmI5ZCR; u-name=web_user_eca76diG; ufo-urn=MTUxMTEzMDU4Nzg=; ufo-un=6ZmI5ZCR; ufo-id=745526540164616192; CNZZDATA1281120612=687623788-1724683340-https%253A%252F%252Fteacher.higher.smartedu.cn%252F%7C1725851305',
        'Origin': 'https://core.teacher.vocational.smartedu.cn',
        'Referer': 'https://core.teacher.vocational.smartedu.cn/p/course/vocational/v_876618626595598336?itemId=876287671176585216&type=1&segId=876287598567849984&projectId=876287350832422912&orgId=608196190709395456&originP=1&service=https%3A%2F%2Fteacher.higher.smartedu.cn%2Fh%2Fsubject%2Fsummer2024%2F&lessonId=876684363924234240',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'u-platformId': '13145854983311',
    }

    params = {
        'orgId': '608196190709395456',
    }

    data = {
        'courseId': data['courseId'],
        'itemId': data['itemId'],
        'videoId': vedio,
        'playProgress': '1459',
        'segId': data['segId'],
        'type': '1',
        'tjzj': '1',
        'clockInDot': '1459',
        'sourceId': '876287350832422912',
        'timeLimit': '-1',
        'originP': '2',
    }

    response = requests.post(
        'https://core.teacher.vocational.smartedu.cn/p/course/services/member/study/progress',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )

    print(response.text)
    return response.json()

def vocation(data):



    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        # 'Cookie': '_abfpc=3e71e827d622b217bb745dbec3adb807f565c21a_2.0; cna=99e133751bb47b2866767a1470a8ec28; UM_distinctid=19198b16d942b1-0d92e3c190a1f4-4c657b58-1fa400-19198b16d952b7; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219184bb6d9dfbb-0a08a380bcc96e-4c657b58-2073600-19184bb6d9e1353%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxODRiYjZkOWRmYmItMGEwOGEzODBiY2M5NmUtNGM2NTdiNTgtMjA3MzYwMC0xOTE4NGJiNmQ5ZTEzNTMifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219184bb6d9dfbb-0a08a380bcc96e-4c657b58-2073600-19184bb6d9e1353%22%7D; Hm_lvt_f0b6b943aec9775d7c6c7020bf856c6b=1724493578,1724508607,1724843558,1725034501; UC_SSO_TGC-e5649925-441d-4a53-b525-51a2f1c4e0a8-product=815f068b-81f9-41de-a79c-59d62a762435; passport=https://core.teacher.vocational.smartedu.cn/p/passport; u-lastLoginTime=1727270049690; u-activeState=1; u-mobileState=0; u-mobile=18767151550; u-preLoginTime=1727266255916; u-token=eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5YWY2YTdkNS03ZWUzLTQ4MTItYjZjYy0zNTM5ODQ4Y2NiYjYiLCJpYXQiOjE3MjcyNzAwNDksInN1YiI6IjYyNzA4NDQ5MDY3MTcyMjQ5NiIsImlzcyI6Imd1b3JlbnQiLCJhdHRlc3RTdGF0ZSI6MCwic3JjIjoid2ViIiwiYWN0aXZlU3RhdGUiOjEsIm1vYmlsZSI6IjE4NzY3MTUxNTUwIiwicGxhdGZvcm1JZCI6IjEzMTQ1ODU0OTgzMzExIiwiYWNjb3VudCI6IjE4NzY3MTUxNTUwIiwiZXhwIjoxNzI3MzA2MDQ5fQ.7MvQH5XIkdrUWuh8X3yOBudcx3z9i7kV_f2uc1kf19k; u-token-legacy=eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5YWY2YTdkNS03ZWUzLTQ4MTItYjZjYy0zNTM5ODQ4Y2NiYjYiLCJpYXQiOjE3MjcyNzAwNDksInN1YiI6IjYyNzA4NDQ5MDY3MTcyMjQ5NiIsImlzcyI6Imd1b3JlbnQiLCJhdHRlc3RTdGF0ZSI6MCwic3JjIjoid2ViIiwiYWN0aXZlU3RhdGUiOjEsIm1vYmlsZSI6IjE4NzY3MTUxNTUwIiwicGxhdGZvcm1JZCI6IjEzMTQ1ODU0OTgzMzExIiwiYWNjb3VudCI6IjE4NzY3MTUxNTUwIiwiZXhwIjoxNzI3MzA2MDQ5fQ.7MvQH5XIkdrUWuh8X3yOBudcx3z9i7kV_f2uc1kf19k; u-id=627084490671722496; u-account=18767151550; requestSource=teacher.vocational.smartedu.cn; ufo-nk=5b6Q6JW+; u-name=web_user_8aM9f8x1; ufo-urn=MTg3NjcxNTE1NTA=; ufo-un=5b6Q6JW+; ufo-id=627084490671722496; connect.sid=s%3A_iSRtm4MUvXzxYiE7NKyAaLHz38wo6ja.cV9CzSMDWiHoXMGgRFmD0Trl%2FIIpF28yuhjZAV%2FEtNI; CNZZDATA1281062390=175988450-1727270058-https%253A%252F%252Fteacher.vocational.smartedu.cn%252F%7C1727273978',
        'Referer': 'https://core.teacher.vocational.smartedu.cn/p/course/vocational/v_876300755386859520?itemId=876285334442536960&type=1&segId=876285076672602112&projectId=876283839269629952&orgId=571896669159477248&originP=2&service=https%3A%2F%2Fteacher.vocational.smartedu.cn%2Fh%2Fsubject%2Fsummer2024%2F',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'projectId': '876283839269629952',
        'courseId': data['courseId'],
        'itemId':  data['itemId'],
        '_': '1727273977693',
        'orgId': '571896669159477248',
    }

    response = requests.get(
        'https://core.teacher.vocational.smartedu.cn/p/course/services/org/member/study/project/course/vocational',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(response.text)

import conf
cookies = {
        '_abfpc': '3e71e827d622b217bb745dbec3adb807f565c21a_2.0',
        'cna': '99e133751bb47b2866767a1470a8ec28',
        'UM_distinctid': '19198b16d942b1-0d92e3c190a1f4-4c657b58-1fa400-19198b16d952b7',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219184bb6d9dfbb-0a08a380bcc96e-4c657b58-2073600-19184bb6d9e1353%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxODRiYjZkOWRmYmItMGEwOGEzODBiY2M5NmUtNGM2NTdiNTgtMjA3MzYwMC0xOTE4NGJiNmQ5ZTEzNTMifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219184bb6d9dfbb-0a08a380bcc96e-4c657b58-2073600-19184bb6d9e1353%22%7D',
        'Hm_lvt_f0b6b943aec9775d7c6c7020bf856c6b': '1724493578,1724508607,1724843558,1725034501',
        'UC_SSO_TGC-e5649925-441d-4a53-b525-51a2f1c4e0a8-product': '815f068b-81f9-41de-a79c-59d62a762435',
        'passport': 'https://core.teacher.vocational.smartedu.cn/p/passport',
        'u-lastLoginTime': '1727270049690',
        'u-activeState': '1',
        'u-mobileState': '0',
        'u-mobile': '18767151550',
        'u-preLoginTime': '1727266255916',
        'u-token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5YWY2YTdkNS03ZWUzLTQ4MTItYjZjYy0zNTM5ODQ4Y2NiYjYiLCJpYXQiOjE3MjcyNzAwNDksInN1YiI6IjYyNzA4NDQ5MDY3MTcyMjQ5NiIsImlzcyI6Imd1b3JlbnQiLCJhdHRlc3RTdGF0ZSI6MCwic3JjIjoid2ViIiwiYWN0aXZlU3RhdGUiOjEsIm1vYmlsZSI6IjE4NzY3MTUxNTUwIiwicGxhdGZvcm1JZCI6IjEzMTQ1ODU0OTgzMzExIiwiYWNjb3VudCI6IjE4NzY3MTUxNTUwIiwiZXhwIjoxNzI3MzA2MDQ5fQ.7MvQH5XIkdrUWuh8X3yOBudcx3z9i7kV_f2uc1kf19k',
        'u-token-legacy': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5YWY2YTdkNS03ZWUzLTQ4MTItYjZjYy0zNTM5ODQ4Y2NiYjYiLCJpYXQiOjE3MjcyNzAwNDksInN1YiI6IjYyNzA4NDQ5MDY3MTcyMjQ5NiIsImlzcyI6Imd1b3JlbnQiLCJhdHRlc3RTdGF0ZSI6MCwic3JjIjoid2ViIiwiYWN0aXZlU3RhdGUiOjEsIm1vYmlsZSI6IjE4NzY3MTUxNTUwIiwicGxhdGZvcm1JZCI6IjEzMTQ1ODU0OTgzMzExIiwiYWNjb3VudCI6IjE4NzY3MTUxNTUwIiwiZXhwIjoxNzI3MzA2MDQ5fQ.7MvQH5XIkdrUWuh8X3yOBudcx3z9i7kV_f2uc1kf19k',
        'u-id': '627084490671722496',
        'u-account': '18767151550',
        'requestSource': 'teacher.vocational.smartedu.cn',
        'ufo-nk': '5b6Q6JW+',
        'u-name': 'web_user_8aM9f8x1',
        'ufo-urn': 'MTg3NjcxNTE1NTA=',
        'ufo-un': '5b6Q6JW+',
        'ufo-id': '627084490671722496',
        'connect.sid': 's%3A_iSRtm4MUvXzxYiE7NKyAaLHz38wo6ja.cV9CzSMDWiHoXMGgRFmD0Trl%2FIIpF28yuhjZAV%2FEtNI',
        'CNZZDATA1281062390': '175988450-1727270058-https%253A%252F%252Fteacher.vocational.smartedu.cn%252F%7C1727273978',
    }
if __name__ == '__main__':
    # i = 44
    # s = '8766909100835389'
    #
    # # 循环20次
    # for _ in range(20):
    #     # 拼接字符串
    #     result = s + str(i)
    #     print(result)
    #     # i增加3
    #     i += 3
    #
    #     for _ in range(1,100):
    #         res = test(result)
    #         if res['data']['progress'] == "1.0":
    #             break
    #         time.sleep(20)

    last_vedioid = '877417676198686720'
    dont_change = True
    for big in conf.confdata:
        vocation(big['data'])
        for vedioid in big['vedioid']:
            print("vedioid是多少哦：", vedioid)
            if dont_change:
                if vedioid == last_vedioid:

                    for _ in range(1, 100):
                        res = test(big['data'],vedioid)
                        if res['data']['progress'] == "1.0":
                            dont_change = False
                            break
                        time.sleep(20)
            else:
                last_vedioid = vedioid
                for _ in range(1, 100):
                    res = test(big['data'], vedioid)
                    if res['data']['progress'] == "1.0":
                        dont_change = False
                        break
                    time.sleep(20)