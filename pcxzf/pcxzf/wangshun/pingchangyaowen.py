import requests
import conf
import datetime
import openpyxl
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
    print(pcyw_news_list)
    return pcyw_news_list


def get_bmgz(pcyw_list):
    page_index = 1
    bmgz_news_list = []
    while True:
        # 构造请求的URL
        url = f'http://www.scpc.gov.cn/content/column/6789801?pageIndex={page_index}'
        # 尝试发送请求并获取响应
        try:
            response = conf.make_request_get(url)
        # 如果发生错误，打印错误信息并退出循环
        except Exception as e:
            print(f'Error: {e}')
            break

        if not deal_res(response, bmgz_news_list,pcyw_list):
            break

        page_index += 1
    print(bmgz_news_list)
    return bmgz_news_list
def get_jcdt(pcyw_list):
    page_index = 1
    jcdt_news_list = []
    while True:
        # 构造请求的URL
        url = f'http://www.scpc.gov.cn/content/column/6789811?pageIndex={page_index}'
        # 尝试发送请求并获取响应
        try:
            response = conf.make_request_get(url)
        # 如果发生错误，打印错误信息并退出循环
        except Exception as e:
            print(f'Error: {e}')
            break

        if not deal_res(response, jcdt_news_list, pcyw_list):
            break

        page_index += 1
    print(jcdt_news_list)
    return jcdt_news_list


def startMain():

    pingchangyaowen_list = get_pcyw()

    bumengongzuo_list = get_bmgz(pingchangyaowen_list)

    jcdt_list = get_jcdt(pingchangyaowen_list)

    make_excel(pingchangyaowen_list, conf.pcyw_excel_name)
    make_excel(bumengongzuo_list, conf.bmgz_excel_name)
    make_excel(jcdt_list, conf.jcdt_excel_name)


def make_excel(news_list,excelname):
    # 创建一个Workbook对象
    wb = openpyxl.Workbook()

    # 获取当前的Worksheet对象
    ws = wb.active

    # 遍历列表中的每一个元组
    for tup in news_list:
        # 将元组添加到表格的一行中
        ws.append(tup)
        print(tup)
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
    date_target = datetime.datetime.strptime(conf.target_date, "%Y-%m-%d")
    return date_obj < date_target
def deal_news_href(href):
    if not href.startswith('http://www.scpc.gov.cn'):
        return 1,""
    res_dup = conf.make_request_get(href)

    div = res_dup[1].find('div', class_='newsinfo')
    if div is None:
        return None
    info = {span.text.split('：')[0]: span.text.split('：')[1] for span in div.find_all('span')[:3] if '：' in span.text}

    if '来源' in info:
        # 判断info['来源']是否包含out_comp列表中的任意一个字段
        if not any(field in info['来源'] for field in conf.out_comp):
            # 如果不包含，判定为JIA
            return 0,info['来源'],info['作者']  if '作者' in info else ""
    return 1,""

def deal_tittle(str,pcyw_list):
    tittle = str.split('【')[-1].split('】')[-1]
    if pcyw_list is not None:
        for tup in pcyw_list:
            # 判断字符串是否在元组的第一个元素中
            if tittle in tup[0]:
                return 1,''
    return  0,tittle
def jugedate_after(date):
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
    after_date = datetime.datetime.strptime(conf.after_date, "%Y-%m-%d")
    return date_obj >= after_date
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
                if jugedate_after(date):
                    continue
                title_deal = deal_tittle(li.find('a', class_='left')['title'],pcyw_list)
                if title_deal[0]:
                    continue
                href = li.find('a', class_='left')['href']
                newsinfo = deal_news_href(href)
                if newsinfo[0]:
                    continue
                news_list.append((title_deal[1],date,newsinfo[1],newsinfo[2]))

    # 第一页测试结束这里改为真

    return True
if __name__ == '__main__':

    startMain()


