import time

import requests
import conf



def taskrecord(recordid,studycode,src,sectionid,studytime, userid,planid):
    cookies = {
        'JSESSIONID': conf.jessionid,
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'JSESSIONID=2CB53C6C9987FBB99B324B1EB2B5C971',
        'Origin': 'https://videoadmin.chinahrt.com',
        'Referer': src,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'studyCode': studycode,
        'updateRedisMap': '1',
        'recordId': recordid,
        'sectionId': sectionid,
        'signId': '151#'+planid+'#'+userid,
        # 'signId': '151#97624af4fdea4442890d4c257dbe83f2#db94e12f4a9d45a19936bc304cbe26c4',

        'time': studytime,
        'businessId': 'gp5',
    }
    # print(data)

    response = requests.post('https://videoadmin.chinahrt.com/videoPlay/takeRecord', cookies=cookies, headers=headers, data=data)
    print(response.text)
    return response.json()['status']

def takeRecode2(token,time):
    cookies = {
        'p_h5_u': '16F1CFCC-428E-40F0-9C1A-7712E951CBFA',
        'Hm_lvt_69ccfa3777e8e6193e66dde22ab2c896': '1728396152',
        'JSESSIONID': '89557CA9C9BD211EDA7CE9DAD91831DA',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'text/html',
        # 'Cookie': 'p_h5_u=16F1CFCC-428E-40F0-9C1A-7712E951CBFA; Hm_lvt_69ccfa3777e8e6193e66dde22ab2c896=1728396152; JSESSIONID=89557CA9C9BD211EDA7CE9DAD91831DA',
        'Origin': 'https://videoadmin.chinahrt.com',
        'Referer': 'https://videoadmin.chinahrt.com/videoPlay/playEncrypt?param=M6FUERTovrwJKhmQd7T7TyNBK%2BVNxhzqSH0PXmorPcZ3rSPEh3uIvka%2FyE3InQ%2F4DeUOXdLAPuFPbuWqM7gto7EJzxuiNJ27XTKne2kfX8TwXayEpRR%2BBx2qNm6PaNCE53UxECkhSGHXaE2JZNesZcBB1Bq7RHzNHSfUBuJKLjfmarzBgbbLGN2syT6eiq6vwEyaN4d0RseygKNXisXChNY0p7ylVdk4v1dbWewWqZuuBDyOjSMk2O24DL5TXVXZXye1%2BqOdFYvD9kO%2Fu%2Bz8Oj81JeICop8ZbzZhMwdpeTR4t90WxoLqIDLXvThch3r497Bog%2F0WEWxJo0Q45XO%2FgnMbH346bgkNOkaJESugyk5g3qKyTh1hrBPKvdUStLHZWf6ATqOukafkePOfTVsE72Wdin2EOP8g71nTG47tn%2FkqZjdlnc5ql%2Bt4TCJov1Mx6c6Nrgir4YLbbwZGklmZ1Dnwwn%2BVRzbLkiALS6FFyYu4brhU3gr%2FLUowarzrA84anZDSZ3MkRcMJ9DVC%2Bd9mFi%2BCJ7Qm5n2W0x8syZAQqbLu%2FBHPS2jN%2F%2BYnFrYVYWaBknTBMgqn%2Fa%2FVKppiSD00vLZDlOnEzQ%2BHt9hibjBB4EIMGcY3OCoKUElK8o%2Fomlz1QidAZXmJy3x6bXBEhbIoMEGHnEgpMK2nE9VKvcCHOAAB%2BNKw5cuPokYJdSJ8LPA%2B',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = '{"token":"'+token+'","time":'+time+'}'

    response = requests.post(
        'https://videoadmin.chinahrt.com/videoPlay/takeRecordByToken',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.text)
    return response.json()


def one_course_ing(token,study_time,total_time):
    add = 17
    for i in range(1000):
        print(i)
        res = takeRecode2(token, str(study_time + add * i))
        time.sleep(1)
        if res['code'] != "0":
            res = takeRecode2(token, str(study_time + add * i))
            return
        else:
            if res['data'] != token:
                token = res['data']
        if study_time + add * i >= total_time:
            return


if __name__ == '__main__':
    token = 'fd33fc71403281f7252a4fedbddb0cbc'
    sutytime = 2560

    add = 15
    for i in range(100):
        print(i)
        res = takeRecode2(token, str(sutytime + add * i))
        time.sleep(1)
        if res['code'] != "0":
            res = takeRecode2(token, str(sutytime + add * i))
        else:
            if res['data'] != token:
                token = res['data']

    # takeRecode2(token,str(sutytime))
    # time.sleep(1)
    # takeRecode2(token, str(sutytime + 30))
    # time.sleep(1)
    # takeRecode2(token, str(sutytime + 60))
    # time.sleep(1)
    # takeRecode2(token, str(sutytime + 90))
    # time.sleep(1)
    # takeRecode2(token, str(sutytime + 100))
