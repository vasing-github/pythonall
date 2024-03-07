# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json
import datetime
import re

# 平昌要闻
news_type_pcyw = 1
# 基层动态
news_type_xzdt = 2
# 视频新闻
news_type_spxw =3
# 公示公告
news_type_gsgg = 4
# 5政策文件、
news_type_zcwj = 5
# 6热点关注、
news_type_rdgz = 6
# 7便民信息、
news_type_bmxx = 7
# 8常用电话、
news_type_cydh = 8
# 9办事服务
news_type_bsfw = 9

menu_dic = {
    news_type_pcyw: 'http://www.scpc.gov.cn/ywdt/pcyw/index.html',
    news_type_xzdt: 'http://www.scpc.gov.cn/ywdt/xzdt/index.html',
    news_type_spxw: 'http://www.scpc.gov.cn/ywdt/spxw/index.html',
    news_type_gsgg: 'http://www.scpc.gov.cn/ywdt/gsgg/index.html',
    news_type_rdgz: 'http://www.scpc.gov.cn/ywdt/rdgz/index.html',
    news_type_bmxx: 'http://www.scpc.gov.cn/ywdt/bmxx/index.html'
}

# 政策文件有三个 行政规范性文件  县政府文件  县政府办公室文件
zcwj_list = ['http://www.scpc.gov.cn/public/column/6601841?type=4&action=list&nav=2&sub=0&catId=6717224',
             'http://www.scpc.gov.cn/public/column/6601841?type=4&action=list&nav=2&sub=1&catId=6717171',
             'http://www.scpc.gov.cn/public/column/6601841?type=4&action=list&nav=2&sub=2&catId=6717181']

# 常用电话爬取
cydhurl = 'http://www.scpc.gov.cn/content/article/10277961'
def switchKey(key):
    switcher = {
        1: '平昌要闻',
        2: '基层动态',
        3: '视频新闻',
        4: '公示公告',
        5: '政策文件',
        6: '热点关注',
        7: '便民信息',
        8: '常用电话',
        9: '办事服务'
    }
    return switcher.get(key, "Invalid key")


def getzcwjhreflist():
    url = 'http://www.scpc.gov.cn/public/column/6601841?type=4&action=list&nav=2&sub=0&catId=6717224'

    data = {}
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    # 以 Beautiful Soup 解析 HTML 程序码
    soup = BeautifulSoup(response.text, 'html.parser')
    # 提取 id 为 fdzd_gknr 的 div 标签下的所有 a 标签
    a_elements = soup.find('div', {'class': 'listnews'}).find_all('a')
    # 输出所有 li标签的文本内容和链接地址
    menuList = []
    print(len(a_elements))
    for a in a_elements:
        if a is not None:
            menuList.append(a["href"])
    print(menuList)
    return menuList

def getnewslist(url):
    # if not bumen.startswith('http'):
    #     bumen = 'http://www.scpc.gov.cn' + bumen
    # 平昌要闻
    # news_type_pcyw = 1
    # url = 'http://www.scpc.gov.cn/ywdt/pcyw/index.html'

    # 基层动态
    # news_type_xzdt = 2
    # url = 'http://www.scpc.gov.cn/ywdt/xzdt/index.html'

    # 视频新闻
    # news_type_spxw = 3
    # url = 'http://www.scpc.gov.cn/ywdt/spxw/index.html'

    # 公示公告
    # news_type_gsgg = 4
    # url = 'http://www.scpc.gov.cn/ywdt/gsgg/index.html'

    # 6热点关注、
    # news_type_rdgz = 6
    # url = 'http://www.scpc.gov.cn/ywdt/rdgz/index.html'

    # 7便民信息、
    # news_type_bmxx = 7
    # url = 'http://www.scpc.gov.cn/ywdt/bmxx/index.html'


    data = {}
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    # 以 Beautiful Soup 解析 HTML 程序码
    soup = BeautifulSoup(response.text, 'html.parser')
    # 提取 id 为 fdzd_gknr 的 div 标签下的所有 a 标签
    a_elements = soup.find('div', {'class': 'listnews'}).find_all('a')
    # 输出所有 li标签的文本内容和链接地址
    menuList=[]
    print(len(a_elements))
    for a in a_elements:
        if a is not None:
            menuList.append(a["href"])
    print(menuList)
    return menuList
def getnewsinfo(url,type):
    new_dic = {}
    data = {}
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    # 以 Beautiful Soup 解析 HTML 程序码
    soup = BeautifulSoup(response.text, 'html.parser')


    div = soup.find('div', class_='newsinfo')
    if div is None:
        return None
    info = {span.text.split('：')[0]: span.text.split('：')[1] for span in div.find_all('span')[:3] if '：' in span.text}
    if '发布时间' in info:
        new_dic['publish_time']=info['发布时间']
    if '来源' in info:
        new_dic['source'] = info['来源']
    if '作者' in info:
        new_dic['author'] = info['作者']


    if type != news_type_spxw:
        div = soup.find('div', class_='xxgk-wzcon')
    else:
        div = soup.find('div',class_ = 'video_main_content')

    dealdiv(div)
    new_dic['content'] = div
    new_dic['tittle'] = soup.find('h1', class_='newstitle')
    pattern = r'(\d+)(\.html)?$'
    numbers = re.findall(pattern, url)
    new_dic['id'] = int(numbers[0][0])
    new_dic['type'] = type

    return new_dic

def dealdiv(div):

    img_tags = div.find_all('img')
    if img_tags is not None:
        for img in img_tags:
            src = img.get('src')
            if not src.startswith('http'):
                new_src = 'http://www.scpc.gov.cn' + src
                img['src'] = new_src

    span_tags = div.find_all('span')
    if span_tags is not None:
        for span in span_tags:
            # 获取span标签的data-url属性
            data_url = span.get('data-url')

            # 如果data-url属性是相对路径（即它不以'http'开头）
            if data_url and not data_url.startswith('http'):
                # 在data-url属性前面添加URL的前半段
                new_data_url = 'http://www.scpc.gov.cn' + data_url
                # 更新span标签的data-url属性
                span['data-url'] = new_data_url

def dorequest(dic,senddic):
    url = 'https://szpc.pcxzf.cn:8080/system/list'
    # url = '10.167.39.125:8080/system/list'
    headers = {'Content-Type': 'application/json'}

    data = {
        'newsId': dic.get('id'),
        "newsType": dic.get('type'),
        "newsAuthor": dic.get('source'),
        "newsContent": str(dic.get('content')) if dic.get('content') else None,  # 使用prettify方法将Tag对象转换为字符串
        "newsTitle": str(dic.get('tittle')) if dic.get('tittle') else None,  # 这里你需要提供文章的标题
        "publishTime": dic.get('publish_time')
    }

    # 移除字典中值为None的项
    data = {k: v for k, v in data.items() if v is not None}
    response = requests.post(url,headers = headers, data=json.dumps(data))

    if response.status_code == 200:
        if '操作成功' in response.text:
            senddic[dic['type']] = senddic.get(dic['type'], 0) + 1

    else:
        print("发送失败，错误代码：", response.text)

def getzzwjlist(url):
    data = {}
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    a_elements = soup.find('div', {'class': 'xxgk_nav_con'}).find_all('a')
    menuList = []
    print(len(a_elements))
    for a in a_elements:
        if a is not None:
            menuList.append(a["href"])
    print(menuList)
    return menuList
def getzzwjinfo(url):
    new_dic = {}
    data = {}
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    # 以 Beautiful Soup 解析 HTML 程序码
    soup = BeautifulSoup(response.text, 'html.parser')
    new_dic['tittle'] = soup.find('h1', class_='gk_title')
    div = soup.find('div', class_='gk_newsinfo clearfix')

    if div is None:
        return None

    # 提取日期
    date = soup.find('span', class_='sp').text
    new_dic['publish_time'] = date

    # 提取来源
    source = soup.find('div', id='resources').text.strip().split('：')[1]
    new_dic['source'] = source

    div = soup.find('div', class_='xxgk-wzcon')
    dealdiv(div)
    new_dic['content'] = div

    pattern = r'(\d+)\.html$'
    numbers = re.findall(pattern, url)
    new_dic['id'] = int(re.findall(pattern, url)[0])
    new_dic['type'] = news_type_zcwj
    # print(new_dic)
    return new_dic

def sendMsg(msg):
    # 定义要发送的消息内容

    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": f" # <font color=\"warning\">数字平昌小程序新闻推送监测</font>\n\n今日新增：\n\n\n"
        }
    }
    for key, value in msg.items():
        data["markdown"]["content"] += f" ## {switchKey(key)}:"
        data["markdown"]["content"] += f" {value}条\n"

    # 定义企业微信机器人的webhook地址
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=425a53f6-696e-46c1-9d4a-fae8940b136f"

    # 发送HTTP POST请求
    response = requests.post(url, data=json.dumps(data))
    print(data)
    # 输出响应结果
    print(response.text)
def sendlistnews(list_news):
    for data in reversed(list_news):
        if data is not None:
            # print(data)
            dorequest(data, send_dic)
    list_news.clear()

if __name__ == '__main__':
    list_news = []
    send_dic = {}

    for type,href in menu_dic.items():
        href_lsit = getnewslist(href)
        for new in href_lsit:
            list_news.append(getnewsinfo(new,type))

        sendlistnews(list_news)

    # 爬取政策文件
    for href in zcwj_list:
        href_list = getzzwjlist(href)
        for new in href_list:
            list_news.append(getzzwjinfo(new))
        sendlistnews(list_news)

    # 爬取常用电话
    list_news.append(getnewsinfo(cydhurl,news_type_cydh))
    sendlistnews(list_news)

    # 发送数据到数据库
    for data in list_news:
        if data is not None:
            dorequest(data,send_dic)

    print(send_dic)
    # send_dic = {1: 12, 3: 1, 7: 1}
    # 机器人通知
    sendMsg(send_dic)