# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import aiohttp
# 爬虫执行时间

first_hour = 3
firt_minutes = 0

second_hour = 11
sencond_minutes = 1

third_hour = 16
third_minutes = 30

ywdt_dic = {
    '公示公告': 'http://www.scpc.gov.cn/ywdt/gsgg/index.html',  # 公示公告
    '基层动态': 'http://www.scpc.gov.cn/ywdt/xzdt/index.html',  # 基层动态
    '部门工作': 'http://www.scpc.gov.cn/ywdt/bmdt/index.html',  # 部门工作
    '热点关注': 'http://www.scpc.gov.cn/ywdt/rdgz/index.html',  # 热点关注
    '便民信息': 'http://www.scpc.gov.cn/ywdt/bmxx/index.html',  # 便民信息
    '平昌要闻': 'http://www.scpc.gov.cn/ywdt/pcyw/index.html',  # 平昌要闻
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
    '助企纾困': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/zqsk/index.html',  # 祝企纾困
    '减税降费': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/jsjf/index.html',  # 减税降费
    '公共资源交易': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/zyjy/index.html',  # 公共资源交易
    '水质监测': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/hjbh/index.html',  # 水质监测
    '征地信息': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/zdxx/index.html',  # 征地信息
    '价格信息': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/jghsf/index.html',  # 价格信息
    '不动产登记': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/bdcdj/index.html',  # 不动产登记
    '财政资金直达基层': 'http://www.scpc.gov.cn/zwgk/zdlyxxgk/czzjzdjc/index.html',  # 财政资金直达基层
}
# 重点领域跳转到乡镇页面的部分
height_area_redirct_dic = {
    '卫生健康': 'http://www.scpc.gov.cn/public/column/6602161?type=4&action=list&nav=2&sub=6&catId=6715931',  # 卫生健康
    '食品药品监管': 'http://www.scpc.gov.cn/public/column/6602241?type=4&action=list&nav=2&sub=6&catId=6715931',  # 食品药品监管
    '就业创业': 'http://www.scpc.gov.cn/public/column/6602001?type=4&action=list&nav=2&sub=5&catId=6715921',  # 就业创业
    '养老服务': 'http://www.scpc.gov.cn/public/column/6601941?type=4&catId=6715921&action=list',  # 养老服务
    '教育科技': 'http://www.scpc.gov.cn/public/column/6601901?type=4&action=list&nav=2&sub=5&catId=6715921',  # 教育科技
    '涉农补贴': 'http://www.scpc.gov.cn/public/column/6602101?type=4&action=list&nav=2&sub=4&catId=6715911',  # 涉农补贴
    '公共文化服务': 'http://www.scpc.gov.cn/public/column/6602141?type=4&action=list&nav=2&sub=4&catId=6715921',  # 公共文化服务
    '社会救助': 'http://www.scpc.gov.cn/public/column/6601941?type=4&action=list&nav=2&sub=6&catId=6715931',  # 社会救助
    '住房保障': 'http://www.scpc.gov.cn/public/column/6602041?type=4&action=list&nav=2&sub=6&catId=6715931',  # 住房保障
    '放管服改革': 'http://www.scpc.gov.cn/public/column/6602381?type=4&action=list&nav=2&sub=5&catId=6715931',  # 放管服改革
    '应急管理': 'http://www.scpc.gov.cn/public/column/6602201?type=4&action=list&nav=2&sub=5&catId=6715921',  # 应急管理
    '环评公示': 'http://www.scpc.gov.cn/public/column/6602261?type=4&action=list&nav=2&sub=4&catId=6715911',  # 环评公示
    '监测预警': 'http://www.scpc.gov.cn/public/column/6602201?type=4&action=list&nav=2&sub=5&catId=6715931',  # 监测预警
    '医疗保障': 'http://www.scpc.gov.cn/public/column/6602361?type=4&action=list&nav=2&sub=5&catId=6715931',  # 医疗保障
    '环境质量公报': 'http://www.scpc.gov.cn/public/column/6602261?type=4&action=list&nav=2&sub=6&catId=6715931',  # 环境质量公报



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
# 专给专题专栏占比使用
zhuanti_of_dic = {
    '主题教育': ['http://www.scpc.gov.cn/ztzl/xxxjpzsjlcsczyzsjs/index.html'],
    '预决算': ['http://www.scpc.gov.cn/ztzl/pcxczyjsgk/czyjs/index.html','http://www.scpc.gov.cn/ztzl/pcxczyjsgk/bmys/index.html','http://www.scpc.gov.cn/ztzl/pcxczyjsgk/bmjs/index.html','http://www.scpc.gov.cn/ztzl/pcxczyjsgk/dwys/index.html','http://www.scpc.gov.cn/ztzl/pcxczyjsgk/dwjs/index.html'],
    '两会专题': ['http://www.scpc.gov.cn/ztzl/lhzt/index.html'],
    '乡村振兴': ['http://www.scpc.gov.cn/ztzl/tpbk/index.html'],
    '依法治县':['http://www.scpc.gov.cn/ztzl/xxxjpzsjlcsczyzsjs/index.html'],
    '政府信息公开':['http://www.scpc.gov.cn/ztzl/zfxxzdgkjbml/xzbsc/index.html','http://www.scpc.gov.cn/ztzl/zfxxzdgkjbml/xjbm/index.html'],
    '信用双公示':['http://www.scpc.gov.cn/ztzl/xyxxsgs/xzxk/index.html', 'http://www.scpc.gov.cn/ztzl/xyxxsgs/xzcf/index.html', 'http://www.scpc.gov.cn/ztzl/xyxxsgs/xkml/index.html'],
    '试点领域':['http://www.scpc.gov.cn/ztzl/pcxsdlyjczwgkbzml/pcxbmsdlyjczwgkbzml/index.html','http://www.scpc.gov.cn/ztzl/pcxsdlyjczwgkbzml/pcxgzjdbscsdlyjczwgkbzml/index.html'],

}


# 基层政务公开领域和负责单位映射
jczwgk_area_comp_dic = {'公共文化服务': '文广旅局', '就业领域': '人社局', '涉农补贴': '农业局', '食品药品': '市监局', '社会救助': '民政局', '卫生健康': '卫健局', '养老服务': '民政局', '义务教育': '教科体局', '公共法律': '司法局', '税收管理': '税务局', '广播电视和网络视听': '文广旅局', '旅游领域': '文广旅局', '社会保险': '人社局', '自然资源': '自规局', '城市综合执法': '执法局', '户籍管理': '公安局', '财政预决算': '财政局', '市政服务': '住建局', '农村危房改造': '住建局', '国有土地上房屋征收与补偿': '住建局', '保障性住房': '住建局', '新闻出版版权': '县委宣传部', '生态环境': '生态环境局', '统计领域': '统计局', '公共资源交易': '交易中心', '交通运输': '交运局', '扶贫领域': '乡村振兴局', '重大建设项目': '发改局', '安全生产': '应急局', '救灾领域': '应急局'}

proxies = None
prox_num = 0

async def make_request_get(url, params=None, proxies=None):
    if not url.startswith('http'):
        url = 'http://www.scpc.gov.cn' + url

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, params=params, proxy=proxies) as response:
                text = await response.text()
                soup = BeautifulSoup(text, 'html.parser')
                return response, soup
        except Exception as e:
            print('网络波动', url)
            try:
                print(url)
                async with session.get(url, params=params, proxy=getproxies()['http']) as response:
                    text = await response.text()
                    soup = BeautifulSoup(text, 'html.parser')
                    return response, soup
            except Exception as e:
                print('代理过期', url)
                async with session.get(url, params=params, proxy=getproxies(up=True)['http']) as response:
                    text = await response.text()
                    soup = BeautifulSoup(text, 'html.parser')
                    return response, soup

async def make_request_post(url, data=None, proxies=None):
    if not url.startswith('http'):
        url = 'http://www.scpc.gov.cn' + url

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(url, data=data, proxy=proxies) as response:
                text = await response.text()
                soup = BeautifulSoup(text, 'html.parser')
                return response, soup
        except Exception as e:
            print('网络波动', url)
            try:
                print(url)
                async with session.post(url, params=data, proxy=getproxies()['http']) as response:
                    text = await response.text()
                    soup = BeautifulSoup(text, 'html.parser')
                    return response, soup
            except Exception as e:
                print('代理过期', url)
                async with session.post(url, params=data, proxy=getproxies(up=True)['http']) as response:
                    text = await response.text()
                    soup = BeautifulSoup(text, 'html.parser')
                    return response, soup

def getproxies(up=False):
    global proxies, prox_num  # 在函数内部修改全局变量，需要声明 global

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
        prox_num += 1
    print('代理：', proxies)
    return proxies
