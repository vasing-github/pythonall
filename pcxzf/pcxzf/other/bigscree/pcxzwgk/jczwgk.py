import asyncio
import json
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import conf
import re
import time

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'search_history=%E5%8E%95%E6%89%80%E9%9D%A9%E5%91%BD; SHIROJSESSIONID=8b77c272-388b-411e-8dc2-f5115ea2bd40',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}




async def get_all_type_menu():
    url = 'http://www.scpc.gov.cn/ztzl/jczwgk/gkly/ggwhfw/index.html'

    res, soup = await conf.make_request_get(url)
    div_elment = soup.find('div', {'class': 'classify_name ly_box'})
    # print(div_elment)
    a_element = div_elment.find_all('a')
    area_type_dic = {}
    if a_element is not None:
        for _a in a_element:
            title = _a.get('title')
            href = _a.get('href')
            area_type_dic[title] = href
    return area_type_dic


async def get_first_munu(url):
    res, soup = await conf.make_request_get(url)
    div_elment = soup.find('div', {'class': 'classify_name sx_box'})
    a_element = div_elment.find_all('a')
    first_menu_dic = {}
    if a_element is not None:
        for _a in a_element:
            title = _a.get('title')
            href = _a.get('href')
            first_menu_dic[title] = href
    return first_menu_dic


async def get_second_menu(url):
    res, soup = await conf.make_request_get(url)
    # 提取curFirstLevelChildId的值
    cur_first_level_child_id = soup.find(id='curFirstLevelChildId')
    # 如果能拿到这个值说明一级事项给的链接没有跳转，如果拿不到说明没有二级事项，一级事项就跳转了
    if cur_first_level_child_id is not None:
        cur_first_level_child_id = soup.find(id='curFirstLevelChildId')['value']
        url = "http://www.scpc.gov.cn/site/label/8888"
        params = {
            "isJson": "true",
            "id": cur_first_level_child_id,
            "isChild": "true",
            "labelName": "columnTree"
        }
        # response = requests.get(url, params=params)
        res, soup = await conf.make_request_get(url, params)
        second_menu_dic = {}
        text = await res.text()
        if text != 'null':

            json_response = json.loads(text)
            # json_response = await res.json()
            for item in  json_response:
                name = item.get('name')
                html_path = item.get('htmlPath')
                if not name or not html_path:
                    continue  # 如果name或html_path为空，则跳过当前循环
                second_menu_dic[name] = html_path
        else:
            # 返回1表示没有二级事项且不跳转
            return 1, cur_first_level_child_id
    else:
        # 返回2表示没有二级事项，但是跳转了
        return 2, 0
    return 3, second_menu_dic


async def get_page(url):
    # 正则表达式
    pattern = r'www\.scpc\.gov\.cn(.*)'
    # 搜索匹配的路径
    match = re.search(pattern, url)
    if match:
        url = match.group(1)
    res, soup = await conf.make_request_get(url)
    # 二级事项跳转目录不尽相同，如果div有listnews，直接在这个页面找，并且有些会翻页,第一步找含有listnews的能否翻页，第二部找是否有listnews，第三步找没有listnews的
    # 找到包含pageCount的<script>标签
    script_tag = soup.find('script', string=re.compile('pageCount'))
    # 使用正则表达式从<script>标签的内容中提取pageCount的值
    if script_tag is not None:
        page_count_match = re.search(r'pageCount\s*:\s*(\d+)', script_tag.string)
        page_count = page_count_match.group(1)
        script_tag = soup.find('script', string=re.compile(r"http://www.scpc.gov.cn/content/column/\d+\?pageIndex="))

        # 使用正则表达式从<script>标签的内容中提取URL的值
        if script_tag is not None:
            url_match = re.search(r"(http://www.scpc.gov.cn/content/column/\d+\?pageIndex=)", script_tag.string)
            if url_match:
                url = url_match.group(1)
                print(f"提取的URL是: {url}")
                return await deal_page(page_count, url)
    else:
        # 如果没有pagecount，可能是只有一页，所以传值1，但也可能是不跳转，所以没有pagecount，这个时候在基层政务公开这个页面找右侧列表
        div_elment = soup.find('div', {'class': 'navjz clearfix'})
        if div_elment is not None:
            a_element = div_elment.find_all('a')
            page_news_dic = {}
            if a_element is not None:
                for _a in a_element:
                    title = _a.get('title')
                    href = _a.get('href')
                    page_news_dic[title] = href
                return await deal_area_page_news(page_news_dic)
        else:
            return await deal_page(1, url)


async def deal_area_page_news(page_news_dic):
    list_all_page = 0
    for title, url in page_news_dic.items():
        res, soup = await conf.make_request_get(url)
        div_elment = soup.find('div', {'class': 'newsinfo clearfix'})
        if div_elment is None:
            continue
        date_span = div_elment.find('span', class_='sp')
        # 提取日期字符串
        date_str = date_span.text.split('：')[1].strip()
        # 只获取日期部分，不包括时间
        date_only = date_str.split(' ')[0]
        date_obj = datetime.strptime(date_only, '%Y-%m-%d')  # 你需要根据你的日期字符串的实际格式来调整这个值

        # 获取当前的日期
        now = datetime.now()

        # 判断日期是否在当前月份
        if date_obj.month != now.month or date_obj.year != now.year:
            break

        list_all_page += 1

    return list_all_page, len(page_news_dic)


async def deal_page(page_count, url):
    list_all_page = 0

    all_gk_num = 0
    for i in range(1, int(page_count) + 1):
        # if flag:
        #     break
        new_url = url + '?pageIndex=' + str(i)
        # print(new_url)
        res, soup = await conf.make_request_get(new_url)
        # 如果这里的网页请求不到，说明就是在基层政务公开这个专栏发的，没有跳转到其他地方链接，这个时候要用网页里面获取页面内容的js方法请求
        # 有些页面加了pageindex仍然能访问，但实际却并不会跳转，这一部分再上面处理
        if res.status != 404:

            div_elment = soup.find('div', {'class': 'listnews'})
            if div_elment is not None:
                li_elment = div_elment.find_all('li')
                all_gk_num += len(li_elment)
                for li in li_elment:

                    if li.find('span', class_='right date') is not None:
                        date = li.find('span', class_='right date').text
                        # 使用 strptime 方法将字符串转换为 datetime 对象
                        date_obj = datetime.strptime(date, '%Y-%m-%d')  # 你需要根据你的日期字符串的实际格式来调整这个值

                        # 获取当前的日期
                        now = datetime.now()
                        # print(date_obj.month)
                        # print(now.month)
                        # 判断日期是否在当前月份
                        if date_obj.month != now.month or date_obj.year != now.year:
                            break
                        list_all_page += 1
        else:
            await deal_has_sencond_not_redict(url, list_all_page)

    return list_all_page, all_gk_num


async def deal_has_sencond_not_redict(url, list_all_page):
    res, soup = await conf.make_request_get(url)
    div_elment = soup.find('div', {'class': 'navjz clearfix'})
    if div_elment is not None:
        a_element = div_elment.find_all('a')
        page_news_dic = {}
        if a_element is not None:
            for _a in a_element:
                title = _a.get('title')
                href = _a.get('href')
                page_news_dic[title] = href
        return await deal_area_page_news(page_news_dic)


async def deal_first_menu_not_direct(url, cur_id):
    url = "http://www.scpc.gov.cn/site/label/8888"
    # 请求的数据
    data = {
        "id": cur_id,
        "isChild": "true",
        "siteId": 6787191,
        "pageSize": 100,
        "pageIndex": 1,
        "length": 54,
        "isDate": "false",
        "isHit": "false",
        "isLine": "true",
        "lineCount": 5,
        "dateFormat": "yyyy-MM-dd",
        "file": "/c3/jh/articleNewsPageList_new_jczw",
        "labelName": "articleNewsPageList"
    }

    # 发送请求
    response, soup = await conf.make_request_post(url, data=data)

    a_element = soup.find_all('a')
    page_news_dic = {}
    if a_element is not None:
        for _a in a_element:
            title = _a.get('title')
            href = _a.get('href')
            # 如果标题已经在字典中，就添加到对应的列表
            if title in page_news_dic:
                timestamp = int(time.time() * 1e6)  # 获取当前时间戳，精度为微秒
                title = f"{title}_{timestamp}"
            page_news_dic[title] = href
    return await deal_area_page_news(page_news_dic)


async def deal_first_menu_direct(url):
    res, soup = await conf.make_request_get(url)
    script_tag = soup.find('script', string=re.compile('pageCount'))
    # 使用正则表达式从<script>标签的内容中提取pageCount的值
    if script_tag is not None:
        page_count_match = re.search(r'pageCount\s*:\s*(\d+)', script_tag.string)
        page_count = page_count_match.group(1)
        script_tag = soup.find('script', string=re.compile(r"http://www.scpc.gov.cn/content/column/\d+\?pageIndex="))

        # 使用正则表达式从<script>标签的内容中提取URL的值
        if script_tag is not None:
            url_match = re.search(r"(http://www.scpc.gov.cn/content/column/\d+\?pageIndex=)", script_tag.string)
            if url_match:
                url = url_match.group(1)
                print(f"提取的URL是: {url}")
                return await deal_page(page_count, url)
    else:
        # 如果没有pagecount，可能是只有一页，所以传值1，但也可能是不跳转，所以没有pagecount，这个时候在基层政务公开这个页面找右侧列表
        div_elment = soup.find('div', {'class': 'navjz clearfix'})
        if div_elment is not None:
            a_element = div_elment.find_all('a')
            page_news_dic = {}
            if a_element is not None:
                for _a in a_element:
                    title = _a.get('title')
                    href = _a.get('href')
                    page_news_dic[title] = href
                return await deal_area_page_news(page_news_dic)
        else:
            return await deal_page(1, url)


def judgement_news(articles):
    is_less_than_four = len(articles) < 4

    # 判断最新更新时间是否大于90天
    latest_update_date = datetime.strptime(articles[0][0], '%Y-%m-%d') if articles else None
    is_latest_update_more_than_ninety = latest_update_date and (
                datetime.now() - latest_update_date > timedelta(days=90))

    # 判断相邻两个文章的更新时间是否大于90天
    list_each_more_ninety = [
        f"文章 '{articles[i][1]}' 和 '{articles[i + 1][1]}' 之间的更新时间大于90天"
        for i in range(len(articles) - 1)
        if
        datetime.strptime(articles[i][0], '%Y-%m-%d') - datetime.strptime(articles[i + 1][0], '%Y-%m-%d') > timedelta(
            days=90)
    ]

    return is_less_than_four, is_latest_update_more_than_ninety, list_each_more_ninety


def deal_information(menu_dup, error_news_dup, len_less_four_list, uptime_more_ninteen, each_more_ninteen):
    if error_news_dup[0]:
        len_less_four_list.append(menu_dup)
    if error_news_dup[1]:
        uptime_more_ninteen.append(menu_dup)
    if len(error_news_dup[2]) > 0:
        each_more_ninteen.append((menu_dup, error_news_dup[2]))


async def startMain():
    area_num_dic = {}
    area_type_dic = await get_all_type_menu()
    allgk = 0
    for area, href in area_type_dic.items():
        _a = 0
        print('领域：', area)
        if area == '税收管理':
            continue
        first_menu_dic = await get_first_munu(href)
        for first_key, first_href in first_menu_dic.items():
            print('一级事项：', first_key)
            second_menu_dic = await get_second_menu(first_href)
            print(second_menu_dic)
            if second_menu_dic[0] == 3:
                for second_key, second_href in second_menu_dic[1].items():
                    print('二级事项：', second_key)
                    m, all_num = await get_page(second_href)
                    _a += m
                    allgk += all_num

            # 没有二级事项
            elif second_menu_dic[0] == 1:
                # 返回1表示没有二级事项且不跳转
                m, all_num = await deal_first_menu_not_direct(first_href, second_menu_dic[1])
                _a += m
                allgk += all_num

            elif second_menu_dic[0] == 2:
                # 返回2表示没有二级事项还跳转了
                m, all_num = await deal_first_menu_direct(first_href)
                _a += m
                allgk += all_num

        area_num_dic[area] = _a
    print(area_num_dic)
    return area_num_dic, allgk

if __name__ == '__main__':
    asyncio.run(startMain())