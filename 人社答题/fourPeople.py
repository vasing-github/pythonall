# -*- coding: gbk -*-

import time
import random

import requests


def match(str,prox):
    url = 'https://battle.wetruetech.com/weixin/param/MATCH_TIME?sessionToken='+cofig.sessionToken
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
    response = requests.get(url, headers=headers,timeout=30, proxies=prox,verify=False)
    print('第一步开始找人匹配：',response.text)
    print('第一步是否成功：',response.json()['code'])
    return response.json()['code']

def get_questions(prox):
    url = 'https://battle.wetruetech.com/weixin/battle/match?roundType=4&sessionToken='+cofig.sessionToken
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
    print('第二步拿到所有题目',response.json()['data']['teams'][0]['players'][0]['records'])
    if response.json()['data']['teams'][0]['players'][0]['id'] in cofig.playersid:
        return response.json()['data']['teams'][0]['players'][0]['records'],response.json()['data']['id']
    elif response.json()['data']['teams'][1]['players'][0]['id'] in cofig.playersid:
        return response.json()['data']['teams'][1]['players'][0]['records'],response.json()['data']['id']
    elif response.json()['data']['teams'][2]['players'][0]['id'] in cofig.playersid:
        return response.json()['data']['teams'][2]['players'][0]['records'],response.json()['data']['id']
    elif response.json()['data']['teams'][3]['players'][0]['id'] in cofig.playersid:
        return response.json()['data']['teams'][3]['players'][0]['records'],response.json()['data']['id']
    return 0

def battle(id):
    duration = random.randint(6000, 7000)
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

import cofig
if __name__ == '__main__':
    sessionToken = cofig.sessionToken
    prox = None
    # prox = cofig.getproxies()
    # battle(151585210)

    for i in range(3):
        if match('kk',prox) == "10000":
            records = get_questions(prox)
            if records != 0:
                for term in records[0]:
                    time.sleep(6)
                    battle(term['id'])
                getscore(records[1],prox)


