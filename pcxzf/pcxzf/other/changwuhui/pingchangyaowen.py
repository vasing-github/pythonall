import requests
import conf
import datetime
import openpyxl
import re
import json
import collections
def get_pcyw():
    page_index = 1
    pcyw_news_list = []
    while True:
        # 构造请求的URL
        url = f'http://www.scpc.gov.cn/content/column/6789791?pageIndex={page_index}'
        # 尝试发送请求并获取响应
        try:
            response = conf.make_request_get(url)
        # 如果发生错误，打印错误信息并退出循环
        except Exception as e:
            print(f'Error: {e}')
            break

        if not deal_res(response, pcyw_news_list,None):
            break

        page_index += 1
    return pcyw_news_list
def deal_li_elment(s):
    num = re.findall(r'\d+', s)  # 提取阿拉伯数字
    chn_num = re.findall(r'(十[一二三四五六七八九]?|二十[一二三四五六七八九十]?)', s)  # 提取中文数字
    if len(num) != 1 or len(chn_num)!= 1:
        return '',''
    return int(num[0]),chn_num[0]
def get_new_cw_or_cw_buisines(url):

    response = conf.make_request_get(url)

    div_elment = response[1].find('div', {'class': 'listnews'})
    if div_elment is not None:
        li_elment = div_elment.find_all('li')
        for li in li_elment:
            tittle = li.find('a', class_='left')['title']

            return deal_li_elment(tittle)
def puls_ch_num(str_num):
    # 将汉字数字转换为阿拉伯数字并加一
    num = conf.cn_num[str_num] + 1

    # 将阿拉伯数字转换回汉字数字
    new_str_num = conf.num_cn[num]

    return new_str_num
def re_result(data,cw_dup):
    for item in data:
        title = item[0]
        chn_num = re.findall(r'(十[一二三四五六七八九]?|二十[一二三四五六七八九十]?)', title)  # 提取中文数字
        num = re.findall(r'\d+', title)

        if chn_num and num:
            chn_num = chn_num[0]
            num = int(num[0])

            if chn_num == cw_dup[1] and cw_dup[0] < num <= cw_dup[0] + 5:
                return title
            elif chn_num == puls_ch_num(cw_dup[1]) and 1 <= num <= 5:
                return title

def sendMsg(msg):
    # 定义要发送的消息内容

    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": f" 检测到融媒体中心发布了新的常委会/常务会，快去复制到政务公开-基础信息公开\n\n\n{msg}\n\n\n<@WuXiaoLong>\n<@MingFengWangBaoNing>"
        }
    }


    key = conf.key_cs
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=" + key
    # 发送HTTP POST请求
    response = requests.post(url, data=json.dumps(data))

    # 输出响应结果
    print(response.text)

def deal_cw_jugement(pcyw_list,url):
    cw_dup = get_new_cw_or_cw_buisines(url)
    print(cw_dup)
    result = re_result(pcyw_list, cw_dup)

    if result is not None:
        print(result)
        sendMsg(result)
def startMain():
    # pcyw_list = [('十四届县委常委会召开会议专题传达学习省委十二届四次全会精神', '2023-12-07', '平昌县融媒体中心', ''), ('杜小兵主持召开县政府十九届第44次常务会议', '2023-12-04', '县融媒体中心', ''), ('张勋主持召开十四届县委常委会第80次会议', '2023-12-01', '县融媒体中心', ''), ('县政府十九届第43次常务会议召开', '2023-11-28', '县融媒体中心', '')]
    pcyw_list = get_pcyw()
    print(pcyw_list)
    # pcyw_list = [('县政府十九届第44次常务会议召开', '2023-12-20', '县融媒体中心', ''), ('十四届县委常委会召开会议专题传达学习省委十二届四次全会精神', '2023-12-07', '平昌县融媒体中心', ''), ('杜小兵主持召开县政府十九届第42次常务会议', '2023-12-04', '县融媒体中心', ''), ('张勋主持召开十四届县委常委会第80次会议', '2023-12-01', '县融媒体中心', ''), ('县政府十九届第43次常务会议召开', '2023-11-28', '县融媒体中心', '')]

    deal_cw_jugement(pcyw_list,conf.zf_cw_url)
    deal_cw_jugement(pcyw_list,conf.xw_cw_url)




def make_excel(news_list,excelname):
    # 创建一个Workbook对象
    wb = openpyxl.Workbook()

    # 获取当前的Worksheet对象
    ws = wb.active

    # 遍历列表中的每一个元组
    for tup in news_list:
        # 将元组添加到表格的一行中
        ws.append(tup)
    counter = collections.Counter(tup[2] for tup in news_list)

    # 打印计数结果
    print(counter)
    ws.append(['单位', '数量'])

    # 遍历字典中的每一个键值对
    for key, value in counter.items():
        # 将键值对添加到表格的一行中
        ws.append([key, value])

    # 保存表格到文件中
    wb.save(excelname)
def jugedate(date):
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
    date_target = datetime.datetime.now() - datetime.timedelta(days=conf.before_date)
    return date_obj < date_target
def deal_news_href(href):
    if not href.startswith('http://www.scpc.gov.cn'):
        return 1,""
    res_dup = conf.make_request_get(href)
    print(href)
    div = res_dup[1].find('div', class_='newsinfo')
    if div is None:
        return None
    info = {span.text.split('：')[0]: span.text.split('：')[1] for span in div.find_all('span')[:3] if '：' in span.text}

    if '来源' in info:
        # 判断info['来源']是否包含out_comp列表中的任意一个字段
        if any(field in info['来源'] for field in conf.out_comp):
            # 如果包含，返回0,info['来源'],info['作者']  if '作者' in info else ""
            return 0,info['来源'],info['作者']  if '作者' in info else ""
    return 1,""


def deal_tittle(str,pcyw_list):
    tittle = str.split('【')[-1].split('】')[-1]

    if '常务会' in tittle or '常委会' in tittle:
        return  0,tittle
    return 1,''


def deal_res(response, news_list,pcyw_list):
# 这里返回假则不再翻页
    div_elment = response[1].find('div', {'class': 'listnews'})
    if div_elment is not None:
        li_elment = div_elment.find_all('li')
        for li in li_elment:
            if li.find('span', class_='right date') is not None:
                date = li.find('span', class_='right date').text
                if  jugedate(date):
                    return False


                # 这里判断标题是否包含常务会常委会
                title_deal = deal_tittle(li.find('a', class_='left')['title'], pcyw_list)
                if title_deal[0]:
                    continue

                    # 这里判断如果不是融媒体发的就跳过
                href = li.find('a', class_='left')['href']
                newsinfo = deal_news_href(href)
                if newsinfo[0]:
                    continue
                news_list.append((title_deal[1],date,newsinfo[1],newsinfo[2]))

    # 第一页测试结束这里改为真

    return True
if __name__ == '__main__':

    startMain()


