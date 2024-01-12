# -*- coding: gbk -*-

import time
import random
import cofig
import requests
def getscore(id,prox):
    url = 'https://battle.wetruetech.com/weixin/battle/detail?roundId='+str(id)+'&sessionToken=' + cofig.sessionToken
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',

        'Host': 'battle.wetruetech.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Referer': 'https://servicewechat.com/wx0d86afd2217d329d/7/page-frame.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8391'
    }
    response = requests.get(url, headers=headers, timeout=10, proxies=prox,verify=False)
    print('第四步结果', response.text)


def battle(id):
    duration = random.randint(3000, 4000)
    url = 'https://battle.wetruetech.com/weixin/battle/record?recordId=' + str(
        id) + '&correct=true&duration=' + str(duration) + '&sessionToken=' + cofig.sessionToken
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',

        'Host': 'battle.wetruetech.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Referer': 'https://servicewechat.com/wx0d86afd2217d329d/7/page-frame.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8391'
    }
    response = requests.get(url, headers=headers, timeout=10, proxies=prox,verify=False)
    print('第三步开始答题：',response.text)

prox = None
# records = []
# for term in records:
#     time.sleep(3)
#     battle(term)
getscore(42836933, prox)