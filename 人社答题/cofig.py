
import requests
def getproxies():

    # 提取代理API接口，获取1个代理IP
    api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=oi4bk8pawzh238afp0a0&num=1&signature=o5chwtr32oxfqykl7bd6k9ujpuiuq9ou&pt=1&sep=1&transferip=1"

    # 获取API接口返回的代理IP
    proxy_ip = requests.get(api_url,verify=False).text

    # 用户名密码认证(私密代理/独享代理)
    username = "d4090728410"
    password = "cq1sexrt"
    proxies = {
        "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
        "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
    }
    return proxies


def getproxiesJuliang():
    # 提取代理API接口，获取1个代理IP
    api_url = "http://v2.api.juliangip.com/dynamic/getips?filter=1&num=1&pt=1&result_type=text&split=1&trade_no=1714847436698741&sign=65352fcd6478ed0cd2689b540ad627f6"

    # 获取API接口返回的代理IP
    proxy_ip = requests.get(api_url).text

    # 用户名密码认证(动态代理/独享代理)
    username = "17311067255"
    password = "vas9624.."
    proxies = {
        "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
        "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
    }
    return proxies


sessionToken = '591d54ee23532b32004c41d44a9d14d8'
playersid = [760374,691579]


if __name__ == '__main__':
    pass