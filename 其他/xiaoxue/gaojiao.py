import time

import requests
def test(vedioid,):
    cookies = {
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219106477814552-064f5d0f19a297-26001e51-2359296-1910647781510df%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkxMDY0Nzc4MTQ1NTItMDY0ZjVkMGYxOWEyOTctMjYwMDFlNTEtMjM1OTI5Ni0xOTEwNjQ3NzgxNTEwZGYifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219106477814552-064f5d0f19a297-26001e51-2359296-1910647781510df%22%7D',
        'Hm_lvt_f0b6b943aec9775d7c6c7020bf856c6b': '1725528549',
        '_abfpc': 'c37fea70a00b141d0be78b447f7c913ab28bad6e_2.0',
        'cna': '31aa5347a9c68a1bbb90c9923bbc1185',
        'UC_SSO_TGC-e5649925-441d-4a53-b525-51a2f1c4e0a8-product': '5a7110b1-6cb7-42e1-9515-eeb9c19aec39',
        'UM_distinctid': '1921d2a45a779-0a7de8fc2291e1-26001151-240000-1921d2a45a890',
        'passport': 'https://core.teacher.vocational.smartedu.cn/p/passport',
        'u-lastLoginTime': '1727066181033',
        'u-activeState': '1',
        'u-mobileState': '0',
        'u-mobile': '15009252112',
        'requestSource': 'teacher.higher.smartedu.cn',
        'u-preLoginTime': '1727058535542',
        'u-token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxMDMzN2Y2Zi0xNTRkLTRmMzctOGUzZi05ZDdiMTI1YjdjN2QiLCJpYXQiOjE3MjcwNjYxODEsInN1YiI6IjkwMTI0NDg1ODA1NjE3OTcxMiIsImlzcyI6Imd1b3JlbnQiLCJhdHRlc3RTdGF0ZSI6MCwic3JjIjoid2ViIiwiYWN0aXZlU3RhdGUiOjEsIm1vYmlsZSI6IjE1MDA5MjUyMTEyIiwicGxhdGZvcm1JZCI6IjEzMTQ1ODU0OTgzMzExIiwiYWNjb3VudCI6IjE1MDA5MjUyMTEyIiwiZXhwIjoxNzI3MTAyMTgxfQ.hWuoLLzLacCl6-m68X4OmpOMvJGYzjJMrz1YH_1WvX0',
        'u-token-legacy': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxMDMzN2Y2Zi0xNTRkLTRmMzctOGUzZi05ZDdiMTI1YjdjN2QiLCJpYXQiOjE3MjcwNjYxODEsInN1YiI6IjkwMTI0NDg1ODA1NjE3OTcxMiIsImlzcyI6Imd1b3JlbnQiLCJhdHRlc3RTdGF0ZSI6MCwic3JjIjoid2ViIiwiYWN0aXZlU3RhdGUiOjEsIm1vYmlsZSI6IjE1MDA5MjUyMTEyIiwicGxhdGZvcm1JZCI6IjEzMTQ1ODU0OTgzMzExIiwiYWNjb3VudCI6IjE1MDA5MjUyMTEyIiwiZXhwIjoxNzI3MTAyMTgxfQ.hWuoLLzLacCl6-m68X4OmpOMvJGYzjJMrz1YH_1WvX0',
        'u-id': '901244858056179712',
        'u-account': '15009252112',
        'ufo-nk': '5ZSQ5a2Q6ZKm',
        'u-name': 'web_user_l4O6y8eB',
        'ufo-urn': 'MTUwMDkyNTIxMTI=',
        'ufo-un': '5ZSQ5a2Q6ZKm',
        'ufo-id': '901244858056179712',
        'CNZZDATA1281120612': '1495717380-1727066323-https%253A%252F%252Fteacher.higher.smartedu.cn%252F%7C1727067451',
    }

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
        'courseId': '876618626654318592',
        'itemId': '876288659548336128',
        'videoId': vedioid,
        'playProgress': '1459',
        'segId': '876288598578003968',
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


if __name__ == '__main__':
    i = 44
    s = '8766909100835389'

    # 循环20次
    for _ in range(20):
        # 拼接字符串
        result = s + str(i)
        print(result)
        # i增加3
        i += 3

        for _ in range(1,100):
            res = test(result)
            if res['data']['progress'] == "1.0":
                break
            time.sleep(20)