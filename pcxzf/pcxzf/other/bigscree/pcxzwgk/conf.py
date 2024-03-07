# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# 爬虫执行时间

first_hour = 10
firt_minutes = 55

second_hour = 10
sencond_minutes = 56

third_hour = 19
third_minutes = 0

# # 平昌要闻
# news_type_pcyw = 1
# # 基层动态
# news_type_xzdt = 2
# # 视频新闻
# news_type_spxw =3
# # 公示公告
# news_type_gsgg = 4
# # 5政策文件、
# news_type_zcwj = 5
# # 6热点关注、
# news_type_rdgz = 6
# # 7便民信息、
# news_type_bmxx = 7
# # 8常用电话、
# news_type_cydh = 8
# # 9办事服务
# news_type_bsfw = 9
ywdt_dic = {
    'gsgg': 'http://www.scpc.gov.cn/ywdt/gsgg/index.html',  # 公示公告
    'xzdt': 'http://www.scpc.gov.cn/ywdt/xzdt/index.html',  # 基层动态
    'bmgz': 'http://www.scpc.gov.cn/ywdt/bmdt/index.html',  # 部门工作
    'rdgz': 'http://www.scpc.gov.cn/ywdt/rdgz/index.html',  # 热点关注
    'bmxx': 'http://www.scpc.gov.cn/ywdt/bmxx/index.html',  # 便民信息
    'pcyw': 'http://www.scpc.gov.cn/ywdt/pcyw/index.html',  # 平昌要闻
}
jichu_dic = {
     #  基础信息公开
    'zcjd': 'http://www.scpc.gov.cn/zwgk/zcjd/index.html',  # 政策解读
    'cfqz': 'http://www.scpc.gov.cn/zwgk/jbxxgk/cfqz/index.html',  # 处罚强制
    'czyjs': 'http://www.scpc.gov.cn/ztzl/pcxczyjsgk/czyjs/index.html',  # 财政预决算
    'bmys': 'http://www.scpc.gov.cn/ztzl/pcxczyjsgk/bmys/index.html',  # 部门预算
    'bmjs': 'http://www.scpc.gov.cn/ztzl/pcxczyjsgk/bmjs/index.html',  # 部门决算
    'dwys': 'http://www.scpc.gov.cn/ztzl/pcxczyjsgk/dwys/index.html',  # 单位预算
    'dwjs': 'http://www.scpc.gov.cn/ztzl/pcxczyjsgk/dwjs/index.html',  # 单位决算
    'xzsyxsf': 'http://www.scpc.gov.cn/zwgk/jbxxgk/xzsyxsf/index.html',  # 行政事业性收费
    'xwcwh': 'http://www.scpc.gov.cn/zwgk/xwcwh/index.html',  # 县委常委会
    'xzfcwh': 'http://www.scpc.gov.cn/zwgk/xzfcwh/index.html',  # 县政府常务会
    'qthy': 'http://www.scpc.gov.cn/zwgk/jbxxgk/qthy/index.html',  # 全体会议
    'rsxx': 'http://www.scpc.gov.cn/zwgk/rsxx/index.html',  # 人事信息
    'tjxx': 'http://www.scpc.gov.cn/zwgk/jbxxgk/tjxx/index.html',  # 统计信息
    'yjzj': 'http://www.scpc.gov.cn/zwgk/jbxxgk/jcygk/yjzj/index.html',  # 决策预公开-意见征集
    'jgfk': 'http://www.scpc.gov.cn/zwgk/jbxxgk/jcygk/jgfk/index.html',  # 决策预公开-结果反馈
    'jcjg': 'http://www.scpc.gov.cn/zwgk/jbxxgk/jcygk/jcjg/index.html',  # 决策预公开-决策结果
}
# 重点领域，不跳转到部门乡镇自己页面的部分
height_area_with_total_dic = {
    #  重点领域
    'zqsk': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/zqsk/index.html',  # 祝企纾困
    'jsjf': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/jsjf/index.html',  # 减税降费
    'ggzyjy': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/zyjy/index.html',  # 公共资源交易
    'szjc': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/hjbh/index.html',  # 水质监测
    'zdxx': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/zdxx/index.html',  # 征地信息
    'jgxx': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/jghsf/index.html',  # 价格信息
    'bdcdj': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/bdcdj/index.html',  # 不动产登记
    'czzjzdjc': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/czzjzdjc/index.html',  # 财政资金直达基层
}
# 专题专栏-
zhuanti_total_list = [
    'http://www.scpc.gov.cn/ztzl/xxxjpzsjlcsczyzsjs/index.html',
    'http://www.scpc.gov.cn/ztzl/lhzt/index.html',
    'http://www.scpc.gov.cn/ztzl/tpbk/index.html',
    'http://www.scpc.gov.cn/ztzl/yfzx/index.html',
    'http://www.scpc.gov.cn/ztzl/zfxxzdgkjbml/xzbsc/index.html',
    'http://www.scpc.gov.cn/ztzl/zfxxzdgkjbml/xjbm/index.html',
    'http://www.scpc.gov.cn/ztzl/xyxxsgs/xzxk/index.html',
    'http://www.scpc.gov.cn/ztzl/xyxxsgs/xzcf/index.html',
    'http://www.scpc.gov.cn/ztzl/xyxxsgs/xkml/index.html',
    'http://www.scpc.gov.cn/ztzl/pcxsdlyjczwgkbzml/pcxbmsdlyjczwgkbzml/index.html',  # 部门试点目录
    'http://www.scpc.gov.cn/ztzl/pcxsdlyjczwgkbzml/pcxgzjdbscsdlyjczwgkbzml/index.html',  # 乡镇试点目录
]



def make_request_get(url, params=None, proxies=None):
    if not url.startswith('http'):
        url = 'http://www.scpc.gov.cn' + url
    try:
        response = requests.get(url, params=params, proxies=proxies)
    except Exception as e:
        print('网络波动', url)
        try:
            print(url)
            response = requests.get(url, params=params, proxies=getproxies())
        except Exception as e:
            print('代理过期', url)
            response = requests.get(url, params=params, proxies=getproxies(up=True))

    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    return response, soup


def getproxies(up=False):
    global proxies  # 在函数内部修改全局变量，需要声明 global
    if up or proxies is None:
        # 提取代理API接口，获取1个代理IP
        api_url = "https://dps.kdlapi.com/api/getdps/?secret_id=o6zqx71jh7hiii663qrt&num=1&signature=ae5jtj55np18yfpsjrra5gagd1ljuymx&pt=1&sep=1&transferip=1"

        # 获取API接口返回的代理IP
        proxy_ip = requests.get(api_url, verify=False).text

        # 用户名密码认证(私密代理/独享代理)
        username = "d4348123377"
        password = "vas962464"
        proxies = {
            "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
            "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
        }
    print('代理：', proxies)
    return proxies
