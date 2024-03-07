# -*- coding: utf-8 -*-

import datetime
import used_data
import conf
from quanmsms import sdk  # pip install quanmsms
from sendNotify import *
import random

used_name = used_data.used_name
day = used_data.day

def check_day():
    global day
    today = datetime.date.today()
    if day != str(today):
        day = str(today)
        used_name.clear()

def add_data(data):
    global used_name
    used_name.append(data)

def remove_data(data):
    global used_name
    if data in used_name:
        used_name.remove(data)

def save_data():
    with open('used_data.py', 'w') as f:
        f.write('used_name = ' + str(used_name) + '\n')
        f.write('day = \'' + day + '\'\n')

# choice = random.choice(list)
check_day()
for name, dic in conf.switch.items():
    if name in used_name:
        continue
    print(dic['openid'], dic['apikey'])
    sms = sdk.SDK(dic['openid'], dic['apikey'])

    # sendOK, info, apiStatus = sms.send('17311067255', 3, {'user': random.choice(conf.name), 'from_name': random.choice(conf.from_name)})
    sendOK, info, apiStatus = sms.send('17311067255', 0, {'code': '12332'})
    # sendOK, info, apiStatus = sms.send('17311067255', 3, {'user': '张总', 'from_name': '黑客联盟'})
    print(sendOK)  # 是否成功(布尔值)
    print(apiStatus)  # api状态码
    print(info)  # 描述信息
    if apiStatus == '207':
        add_data(name)
        continue
    if apiStatus != '207' and apiStatus != '200':
        title = f"??消息提醒：泉鸣轰炸失败"
        msg = f"{name}\n{info}"
        send(title, msg)
    break
save_data()


