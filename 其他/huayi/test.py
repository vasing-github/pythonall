
def test():
    import requests

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://scjg.100anquan.com',
        'Referer': 'https://scjg.100anquan.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = '{"ua":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36","platform":"h5-pc","uuid":"28968088","rid":1726629788275,"ver":"v1.0.7","appver":"3.5.7","business":"1001","userid":"","appid":"FE6D9582A9BE3D0A","event":"heartbeat","vid":"C55BA22BAB36486B63835A29B2A11961","retry":0,"code":200,"cdn":"cd15-ccd1-2.play.bokecc.com","heartinter":60,"num":1,"playerstatus":1,"blocktimes":0,"blockduration":0}'

    response = requests.post('https://logger.csslcloud.net/event/vod/v1/client', headers=headers, data=data)
    print(response.text)

def timestap(timestamp):
    import datetime

    # 假设你的时间戳是 1633072800

    timestamp = 1726629325300
    # 将时间戳转换为 datetime 对象
    dt_object = datetime.datetime.fromtimestamp(timestamp)

    # 将 datetime 对象格式化为字符串
    time_string = dt_object.strftime('%Y-%m-%d %H:%M:%S')

    print(time_string)


if __name__ == '__main__':

    # test()
    # timestap(1726629788275)
    print("test")
    print("test")
