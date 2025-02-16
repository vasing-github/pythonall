
bumenList = {'平昌县人民政府办公室': '/public/column/6601841?type=4&action=list', '平昌县发展和改革局': '/public/column/6601861?type=2', '平昌县经济和信息化局': '/public/column/6601881?type=2', '平昌县教育科技和体育局': '/public/column/6601901?type=2', '平昌县公安局': '/public/column/6601921?type=2', '平昌县民政局': '/public/column/6601941?type=2', '平昌县司法局': '/public/column/6601961?type=2', '平昌县财政局': '/public/column/6601981?type=2', '平昌县人力资源和社会保障局': '/public/column/6602001?type=2', '平昌县自然资源和规划局': '/public/column/6602021?type=2', '平昌县住房和城乡建设局': '/public/column/6602041?type=2', '平昌县交通运输局': '/public/column/6602061?type=2', '平昌县水利局': '/public/column/6602081?type=2', '平昌县农业农村局': '/public/column/6602101?type=2', '平昌县商务局': '/public/column/6602121?type=2', '平昌县文化广播电视和旅游局': '/public/column/6602141?type=2', '平昌县卫生健康局': '/public/column/6602161?type=2', '平昌县退役军人事务局': '/public/column/6602181?type=2', '平昌县应急管理局': '/public/column/6602201?type=2', '平昌县审计局': '/public/column/6602221?type=2', '平昌县市场监督管理局': '/public/column/6602241?type=2', '巴中市平昌生态环境局': '/public/column/6602261?type=2', '平昌县统计局': '/public/column/6602281?type=2', '平昌县乡村振兴局': '/public/column/6602301?type=2', '平昌县信访局': '/public/column/6602321?type=2', '平昌县林业局': '/public/column/6602341?type=2', '平昌县医疗保障局': '/public/column/6602361?type=2', '平昌县行政审批局': '/public/column/6602381?type=2', '平昌县综合行政执法局': '/public/column/6602401?type=2', '四川平昌经济开发区管理委员会': '/public/column/6604364?type=2', '平昌县金宝新区管理委员会': '/public/column/6602841?type=2', '平昌县佛头山管理委员会': '/public/column/6602881?type=2', '平昌县同州街道办事处': '/public/column/6603021?type=2', '平昌县江口街道办事处': '/public/column/6603041?type=2', '平昌县金宝街道办事处': '/public/column/6604081?type=2', '平昌县白衣镇人民政府': '/public/column/6603081?type=2', '平昌县涵水镇人民政府': '/public/column/6603541?type=2', '平昌县岳家镇人民政府': '/public/column/6603561?type=2', '平昌县西兴镇人民政府': '/public/column/6603521?type=2', '平昌县龙岗镇人民政府': '/public/column/6603241?type=2', '平昌县土垭镇人民政府': '/public/column/6603461?type=2', '平昌县佛楼镇人民政府': '/public/column/6603581?type=2', '平昌县响滩镇人民政府': '/public/column/6603101?type=2', '平昌县大寨镇人民政府': '/public/column/6603501?type=2', '平昌县驷马镇人民政府': '/public/column/6603061?type=2', '平昌县青云镇人民政府': '/public/column/6603621?type=2', '平昌县兰草镇人民政府': '/public/column/6603221?type=2', '平昌县澌岸镇人民政府': '/public/column/6603361?type=2', '平昌县粉壁镇人民政府': '/public/column/6603321?type=2', '平昌县得胜镇人民政府': '/public/column/6603261?type=2', '平昌县元山镇人民政府': '/public/column/6603161?type=2', '平昌县灵山镇人民政府': '/public/column/6603741?type=2', '平昌县土兴镇人民政府': '/public/column/6603481?type=2', '平昌县云台镇人民政府': '/public/column/6603181?type=2', '平昌县三十二梁镇人民政府': '/public/column/6604061?type=2', '平昌县板庙镇人民政府': '/public/column/6603201?type=2', '平昌县邱家镇人民政府': '/public/column/6603301?type=2', '平昌县笔山镇人民政府': '/public/column/6603121?type=2', '平昌县泥龙镇人民政府': '/public/column/6603661?type=2', '平昌县岩口镇人民政府': '/public/column/6603701?type=2', '平昌县镇龙镇人民政府': '/public/column/6603141?type=2', '平昌县望京镇人民政府': '/public/column/6603281?type=2', '平昌县江家口镇人民政府': '/public/column/6604071?type=2'}
xlsx_name = '网站监测反馈v2.2.xlsx'
correct_name = '机器人改错记录'

# 标题样式
from openpyxl.styles import Font
tittle_font = Font(size=20, bold=True)
header_font = Font(size=13, bold=True)
import requests
from bs4 import BeautifulSoup
import time
import datetime



cookie = '7ca8fc0d-df02-4dae-ab66-d48255e18897'

kaipu_area = '5119020013'
kaipu_cust_password = 'c4Sl468WEn1sYVRLzvv6Wm72ZuHo3olY6zqPpmYbOmWuimvx9UI85oeINEW35MRRS7BXZA2kmNsRqqctkYZRJ/8saQfOBTqSYBcRF3WuwFOvfwNeZbNcBwy9xWAa2FUG7rTWFBpL4ExWtBsaSM/tQk8RXPDcqSFiYNWXgyIGJSA='

jiyuehua_user = '刘海波'
jiyuehua_password= '3527fb9de00f56fc72d96e72d78cfc0d75975a61f140225ac73bcf5257ed55c10aaa1e837d5e667030336f8fc4509b336a93e86850d785c99f8fcfdfee77fdb29a36f8a2a5e67409aa61dcff2304f393957f53be953f2b0916a13dac540b6d396566d4bd1511ccd7e66190f267cf89f3ac0dca7265dc3f32084f5a811497e678'
jiyuehua_port = '82' # 这个东西也没用，但是不同账号请求的端口不一样，应该是服务器的分布式问题。巴州区是82端口，平昌是83端口
jiyuehua_bzgov_shriojid = 'bz_govb_SHIROJSESSIONID' #这个东西没用，只是要注意巴州区登录是b，平昌登录是c,并且后面获取文章内容等请求都要修改参数，
jiyuehua_httpstart = 'http://www.bzqzf.gov.cn'
jiyuehua_pathstart = 'www.bzqzf.gov.cn'
jiyuehua_siteid = '6787291'
send_gongdan_xlsx = '缓存中的附件需提交工单.xlsx'
send_modified = '网站改错记录.xlsx'
send_person = ('RenShengRuoZhiRuChuJian','BanSui')
## 巴州区和南江更新文章时classIds，updateDate不要填，否则服务器验证不通过，在saveOrUpdate方法里面

# 测试小群的key
key_cs = 'ed7d0b07-57e3-4c1c-a8ca-e8d0c7850401'

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
