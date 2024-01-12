# -*- coding: gbk -*-

import time
import random

import requests


def getquestion(str,prox,seesionToken):
    url = 'https://battle.wetruetech.com/weixin/battle/match?roundType=1&sessionToken='+seesionToken
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',

        'Host': 'battle.wetruetech.com',
       'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site': 'cross-site',

        'Referer': 'https://servicewechat.com/wx0d86afd2217d329d/7/page-frame.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8391'
    }
    response = requests.get(url, headers=headers,timeout=10,proxies=prox,verify=False)
    print(response.text)
    print(response.json()['data']['teams'][0]['players'][0]['records'][0]['id'])
    return response.json()['data']['teams'][0]['players'][0]['records'][0]['id']
def battle(recorid,prox,seesionToken):
    duration = random.randint(6000, 7000)
    url = 'https://battle.wetruetech.com/weixin/battle/record?recordId='+str(recorid)+'&correct=true&duration='+str(duration)+'&sessionToken='+seesionToken
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
    response = requests.get(url, headers=headers, timeout=10,proxies=prox,verify=False)
    print(response.text)



import cofig
if __name__ == '__main__':
    sessionToken = cofig.sessionToken

    prox = None
    for i in range(51):
        # prox = cofig.getproxiesJuliang()
        print('第几题了：',i)
        recordid = getquestion('kk',prox,sessionToken)
        time.sleep(6)
        # prox = cofig.getproxiesJuliang()
        battle(recordid,prox,sessionToken)
        time.sleep(2)
