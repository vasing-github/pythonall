import requests
from datetime import datetime, timedelta
import conf
import json


def checkpa():
    url = 'http://222.215.24.208:8888/checkpa'
    response = requests.get(url)
    print(response.json())
    return response.json()['time'], response.json()['prox_num'], response.json()['all_num']


def sendmsg(time_str, prox_num, all_num, mini_num):
    # 给定的时间字符串
    # time_str = '2024-04-07 14:01:38.217497'
    # 将字符串转换为datetime对象
    given_time = datetime.strptime(time_str.split('.')[0], '%Y-%m-%d %H:%M:%S')
    time_only = given_time.strftime('%H:%M:%S')
    # 获取当前时间
    current_time = datetime.now()

    # 计算两个时间的差值
    time_difference = current_time - given_time

    # 判断差值是否在半小时内
    tittle = ''
    desc_color = 0
    if time_difference <= timedelta(minutes=40):
        print("给定的时间在当前时间的半小时内。")
        tittle = '大屏更新成功'
        desc_color = 3
    else:
        print("给定的时间不在当前时间的半小时内。")
        tittle = '大屏更新失败'
        desc_color = 2
    # 定义要发送的消息内容
    #
    data = {
            "msgtype": "template_card",
            "template_card": {
                "card_type": "text_notice",
                "source": {
                    "icon_url": "https://wework.qpic.cn/wwpic/252813_jOfDHtcISzuodLa_1629280209/0",
                    "desc": "政务公开大屏监测",
                    "desc_color": desc_color
                },
                "main_title": {
                    "title": tittle,
                    # "desc": "网址更新情况"
                },
                "emphasis_content": {
                    "title": all_num,
                    "desc": "网站公开总数"
                },
                "quote_area": {
                    "type": 2,
                    "appid":'wx818b6787d83f80cc',
                    "pagepath": "PAGEPATH",
                    # "title": "本次更新细节",
                    "quote_text": f"最后更新时间：{time_only}\n三务公开总数：{mini_num}\n消耗代理数量：{prox_num}"
                },
                "sub_title_text": "点击卡片进入数字平昌小程序，参与积分活动换取精美礼品！",

                "jump_list": [

                    {
                        "type": 2,
                        "appid": "wx818b6787d83f80cc",
                        "pagepath": "PAGEPATH",
                        "title": "跳转小程序"
                    }
                ],
                "card_action": {
                "type": "2",
                "appid": "wx818b6787d83f80cc",
                "pagepath": "PAGEPATH"
                }
            }
        }


    # 定义企业微信机器人的webhook地址
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key="+conf.key_choose+'&debug=1'

    # 发送HTTP POST请求
    response = requests.post(url, data=json.dumps(data))

    # 输出响应结果
    print(response.text)


def check_minicode():
    url = 'http://222.215.24.208:8888/checkminipa'
    response = requests.get(url)
    print(response.json())
    return response.json()['time'], response.json()['total_num']


if __name__ == '__main__':
    time, pro_num, gknum = checkpa()
    redis_uptime, mini_num = check_minicode()
    sendmsg(time, pro_num, gknum, mini_num)