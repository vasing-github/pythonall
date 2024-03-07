# -*- coding: utf-8 -*-
import time

import requests
from sendNotify import *
from datetime import datetime
import conf
sendmsg = {}
for name,dic in conf.switch.items():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://dev.quanmwl.com',
        'Connection': 'keep-alive',
        'Referer': 'https://dev.quanmwl.com/console',
        'Cookie': dic['cookie'],
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    data = {
        'uid': dic['uid'],
    }

    response = requests.post('https://dev.quanmwl.com/service/user_daily_check',  headers=headers, data=data)
    print(response.text)
    print(response.status_code)
    sendmsg[name] = response.text
    time.sleep(10)
# sendmsg= {'686': '{"state": "202", "mess": "今日您已签到，请勿重复操作"}', '688': '{"state": "202", "mess": "今日您已签到，请勿重复操作"}', '691': '{"state": "202", "mess": "今日您已签到，请勿重复操作"}'}
print(sendmsg)
title = f"??消息提醒：泉鸣签到"
msg = f"?{str(datetime.now())[:19]}\n" + ''

for key, value in sendmsg.items():
    msg += f"{key}: {value}\n"
send(title, msg)