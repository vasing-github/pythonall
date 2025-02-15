
bumenList = {'平昌县人民政府办公室': '/public/column/6601841?type=4&action=list', '平昌县发展和改革局': '/public/column/6601861?type=2', '平昌县经济和信息化局': '/public/column/6601881?type=2', '平昌县教育科技和体育局': '/public/column/6601901?type=2', '平昌县公安局': '/public/column/6601921?type=2', '平昌县民政局': '/public/column/6601941?type=2', '平昌县司法局': '/public/column/6601961?type=2', '平昌县财政局': '/public/column/6601981?type=2', '平昌县人力资源和社会保障局': '/public/column/6602001?type=2', '平昌县自然资源和规划局': '/public/column/6602021?type=2', '平昌县住房和城乡建设局': '/public/column/6602041?type=2', '平昌县交通运输局': '/public/column/6602061?type=2', '平昌县水利局': '/public/column/6602081?type=2', '平昌县农业农村局': '/public/column/6602101?type=2', '平昌县商务局': '/public/column/6602121?type=2', '平昌县文化广播电视和旅游局': '/public/column/6602141?type=2', '平昌县卫生健康局': '/public/column/6602161?type=2', '平昌县退役军人事务局': '/public/column/6602181?type=2', '平昌县应急管理局': '/public/column/6602201?type=2', '平昌县审计局': '/public/column/6602221?type=2', '平昌县市场监督管理局': '/public/column/6602241?type=2', '巴中市平昌生态环境局': '/public/column/6602261?type=2', '平昌县统计局': '/public/column/6602281?type=2', '平昌县乡村振兴局': '/public/column/6602301?type=2', '平昌县信访局': '/public/column/6602321?type=2', '平昌县林业局': '/public/column/6602341?type=2', '平昌县医疗保障局': '/public/column/6602361?type=2', '平昌县行政审批局': '/public/column/6602381?type=2', '平昌县综合行政执法局': '/public/column/6602401?type=2', '四川平昌经济开发区管理委员会': '/public/column/6604364?type=2', '平昌县金宝新区管理委员会': '/public/column/6602841?type=2', '平昌县佛头山管理委员会': '/public/column/6602881?type=2', '平昌县同州街道办事处': '/public/column/6603021?type=2', '平昌县江口街道办事处': '/public/column/6603041?type=2', '平昌县金宝街道办事处': '/public/column/6604081?type=2', '平昌县白衣镇人民政府': '/public/column/6603081?type=2', '平昌县涵水镇人民政府': '/public/column/6603541?type=2', '平昌县岳家镇人民政府': '/public/column/6603561?type=2', '平昌县西兴镇人民政府': '/public/column/6603521?type=2', '平昌县龙岗镇人民政府': '/public/column/6603241?type=2', '平昌县土垭镇人民政府': '/public/column/6603461?type=2', '平昌县佛楼镇人民政府': '/public/column/6603581?type=2', '平昌县响滩镇人民政府': '/public/column/6603101?type=2', '平昌县大寨镇人民政府': '/public/column/6603501?type=2', '平昌县驷马镇人民政府': '/public/column/6603061?type=2', '平昌县青云镇人民政府': '/public/column/6603621?type=2', '平昌县兰草镇人民政府': '/public/column/6603221?type=2', '平昌县澌岸镇人民政府': '/public/column/6603361?type=2', '平昌县粉壁镇人民政府': '/public/column/6603321?type=2', '平昌县得胜镇人民政府': '/public/column/6603261?type=2', '平昌县元山镇人民政府': '/public/column/6603161?type=2', '平昌县灵山镇人民政府': '/public/column/6603741?type=2', '平昌县土兴镇人民政府': '/public/column/6603481?type=2', '平昌县云台镇人民政府': '/public/column/6603181?type=2', '平昌县三十二梁镇人民政府': '/public/column/6604061?type=2', '平昌县板庙镇人民政府': '/public/column/6603201?type=2', '平昌县邱家镇人民政府': '/public/column/6603301?type=2', '平昌县笔山镇人民政府': '/public/column/6603121?type=2', '平昌县泥龙镇人民政府': '/public/column/6603661?type=2', '平昌县岩口镇人民政府': '/public/column/6603701?type=2', '平昌县镇龙镇人民政府': '/public/column/6603141?type=2', '平昌县望京镇人民政府': '/public/column/6603281?type=2', '平昌县江家口镇人民政府': '/public/column/6604071?type=2'}
xlsx_name = '网站监测反馈v2.2.xlsx'
correct_name = '机器人改错记录'
send_gongdan_xlsx = '缓存中的附件需提交工单.xlsx'
# 标题样式
from openpyxl.styles import Font
tittle_font = Font(size=20, bold=True)
header_font = Font(size=13, bold=True)
import requests
from bs4 import BeautifulSoup
import time
import datetime



cookie = '7ca8fc0d-df02-4dae-ab66-d48255e18897'

kaipu_area = '5119220006'
kaipu_cust_password = 'bV5SS5l9XkWtVpBq9TwOSKLeeE2k/oidpgzVypzRAXOwKznO3THnC7t5TeBtlUEYiDnH71x+h2kd8DqNtAgny3k5tJWtVLpQ3p7Go8Cl9+W10GrjZz99Im/capE86DqAz2PG0aAjjYNhPXiCCOv3QA/+zhGY4tGYPG8VWilWP88='

jiyuehua_user = '南江县政府办'
jiyuehua_password= '05c028e63d348deaf3e6666b52fee6f2e5b6b8147dee108ef28c1912f248128f862c4d2250f282c67f60ca92677236a05127bb70242bd44ed0cf496cbd8fe9ef5918fb2ab3ff73638514500a9d5d089df35e1fdce5ee6927fb8f533ccca627df21fad6ebfeb2fd1c02fd87115af22aec0aa75431bb74b1682808d2d24ccad07a'
jiyuehua_port = '83' # 这个东西也没用，但是不同账号请求的端口不一样，应该是服务器的分布式问题。巴州区是82端口，平昌是83端口
jiyuehua_bzgov_shriojid = 'bz_govc_SHIROJSESSIONID' #这个东西没用，只是要注意巴州区登录是b，平昌登录是c,并且后面获取文章内容等请求都要修改参数，南江是c
jiyuehua_httpstart = 'http://www.scnj.gov.cn'
jiyuehua_pathstart = 'www.scnj.gov.cn'
jiyuehua_siteid = '6787171'
jiyuehua_upfile_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
# 测试小群的key
key_cs = '80aecfd9-ee46-4f37-8148-00329b65d284'

proxies = None
def getproxies(up = False):
    global proxies  # 在函数内部修改全局变量，需要声明 global
    if up or proxies is None:
        # 提取代理API接口，获取1个代理IP
        api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=o6zqx71jh7hiii663qrt&num=1&signature=ae5jtj55np18yfpsjrra5gagd1ljuymx&pt=1&sep=1&transferip=1"

        # 获取API接口返回的代理IP
        proxy_ip = requests.get(api_url,verify=False).text

        # 用户名密码认证(私密代理/独享代理)
        username = "d4348123377"
        password = "vas962464"
        proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
        }
    print('代理：',proxies)
    return proxies
def make_request_get(url,params = None,proxies=None):
    if not url.startswith('http'):
        url = 'http://www.scpc.gov.cn' + url
    try:

        response = requests.get(url, params=params,proxies = proxies)

    except Exception as e:
        print('网络波动',url)
        try:
            print(url)
            response = requests.get(url, params=params,proxies = getproxies())
        except Exception as e:
            print('代理过期',url)
            response = requests.get(url, params=params,proxies = getproxies(up= True))

    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    return response,soup

if __name__ == '__main__':
    url_test = 'http://www.ccgp-sichuan.gov.cn/freecms/site/sichuan/ggxx/info/2023/8a69c8b18c0bd8aa018c1dd48e712503.html?noticeType=00102'
    response = make_request_get(url_test)
