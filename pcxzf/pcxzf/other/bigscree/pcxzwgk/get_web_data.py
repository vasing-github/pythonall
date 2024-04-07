# -*- coding: utf-8 -*-
import conf
import asyncio
import jczwgk
import datetime
import re

from datetime import datetime, timedelta
async def get_ywdt_num():
    return await get_news_num_dic(conf.ywdt_dic)
    # return {'公示公告': '949', '基层动态': '6019', '部门工作': '5884', '热点关注': '717', '便民信息': '393', '平昌要闻': '16959'}

async def count_a(href):
    a = await get_num(href)
    if isinstance(a, str):
        a = int(a)
    return a
    # all_gk_dic['all_gk'] = all_gk_dic.get('all_gk') + a

async def getzfxxpages():
    bumenList = await getAllbumen()
    bumen_Mennu_list = {}
    for key, value in bumenList.items():
        menuDic = await getMenniu(None, value)
        bumen_Mennu_list[key] = menuDic

    # 这是第三步找更新时间
    count = 0
    day = 0
    week = 0
    mon = 0
    for key, value in bumen_Mennu_list.items():
        print(key)
        if key == '平昌县人民政府办公室':
            continue
        _a = 0
        for menu, href in value.items():
            print(menu)
            time_list = []
            upTime = await getkeywork(None, href, time_list)
            print('uptime', upTime)
            print(len(time_list))
            _a += get_li_num(time_list, False)
            day_li, week_li, mon_li = get_li_num2(time_list)
            day += day_li
            week += week_li
            mon += mon_li
        count += _a
    return count, day, week, mon

async def get_all_gk_num():
    # return {"要闻动态": 30938, "基础信息": 4000, "重点领域1": 2799, "重点领域2": 2583, "专题专栏": 1461, "所有政府信息": 11507, "当天政府信息": 9, "本周政府信息": 9, "本月政府信息": 133}
    all_gk_dic = {}
    # 要闻动态计数
    _a = 0
    for href in conf.ywdt_dic.values():
        _a += await count_a(href)
    all_gk_dic['要闻动态'] = _a

    # 基础信息公开计数
    _a = 0
    for href in conf.jichu_dic.values():
        _a += await count_a(href)
    all_gk_dic['基础信息'] = _a

    # 重点领域不跳转部分计数
    _a = 0
    for href in conf.height_area_with_total_dic.values():
        _a += await count_a(href)
    all_gk_dic['重点领域1'] = _a

    # 重点领域跳转部分计数
    _a = 0
    for key, href in conf.height_area_redirct_dic.items():
        time_list = []
        await getkeywork(None, href, time_list)
        _a += get_li_num(time_list, False)
    all_gk_dic['重点领域2'] = _a

    # 专题专栏部分 计数
    _a = 0
    for href in conf.zhuanti_total_list:
        _a += await count_a(href)
    all_gk_dic['专题专栏'] = _a

    # 政府信息部分计数
    all,day,week,mon = await getzfxxpages()
    all_gk_dic['所有政府信息'] = all
    all_gk_dic['当天政府信息'] = day
    all_gk_dic['本周政府信息'] = week
    all_gk_dic['本月政府信息'] = mon


    print('count', all_gk_dic)
    return all_gk_dic
async def getMenniu(prox,bumen):
    if not bumen.startswith('http'):
        bumen = 'http://www.scpc.gov.cn' + bumen

    response, soup = await conf.make_request_get(bumen)
    # 以 Beautiful Soup 解析 HTML 程序码

    # 提取 id 为 fdzd_gknr 的 div 标签下的所有 a 标签
    a_elements = soup.find('div', {'id': 'fdzd_gknr'}).find_all('a')
    # 输出所有 a 标签的文本内容和链接地址
    menuList={}
    for a in a_elements:
        # print(f'{a.text}: {a["href"]}')
        if a is not None:
            title = a.text
            href = a["href"]
            menuList[title] = href
    return menuList

async def getAllbumen():
    url = 'http://www.scpc.gov.cn/public/column/6601841?type=4&action=rel'
    # data = {}
    # headers = {
    #     'Accept': '*/*',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #     'Connection': 'keep-alive',
    #     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    # }
    response, soup = await conf.make_request_get(url,)

    # 提取所有 ul 标签下的所有 li 元素
    li_elements = []
    for ul in soup.find_all('ul', class_='clearfix'):
        li_elements += ul.find_all('li')

    # 将 li 元素转换为字典
    bumenList = {}
    for li in li_elements:
        a_element = li.find('a')
        if a_element is not None:
            title = a_element.get('title')
            href = a_element.get('href')
            bumenList[title] = href

    # 输出字典
    print(bumenList)
    return bumenList

async def get_num(href):
    response, soup = await conf.make_request_get(href)
    print(href)
    scripts = soup.find_all("script")
    for script in scripts:
        if script.string is not None:
            if 'Ls.pagination' in script.string:
                pattern = re.compile(r"total: (\d+)")
                total_match = pattern.search(script.string)
                if total_match:
                    total = total_match.group(1)
                    print(total)
                    return total

                else:
                    page_count_match = re.search(r'pageCount:(\d+)', script.string)
                    if page_count_match:
                        page_count = page_count_match.group(1)
                        return page_count * 18
    return 0


async def get_news_num_dic(dic):
    news_num_dic = {}
    for menu, href in dic.items():
        news_num_dic[menu] = await get_num(href)
    print(news_num_dic)
    return news_num_dic


def is_same_day(date1, date2):
    return date1.year == date2.year and date1.month == date2.month and date1.day == date2.day


def is_same_week(date1, date2):
    return date1.isocalendar()[1] == date2.isocalendar()[1]


def count_dates(dates, now):
    count_day = sum(is_same_day(date, now) for date in dates)
    count_week = sum(is_same_week(date, now) for date in dates)
    count_month = len(dates)
    return count_day, count_week, count_month


async def get_day_week_mon_dic():
    # return {'当天': 20, '本周': 40, '本月': 598}

    list_pages =[]
    # 要闻动态计数
    for href in conf.ywdt_dic.values():
        list_pages.extend(await get_page(href))

    # 基础信息公开计数
    for href in conf.jichu_dic.values():
        list_pages.extend(await get_page(href))

    # 重点领域不跳转部分计数
    for href in conf.height_area_with_total_dic.values():
        list_pages.extend(await get_page(href))

    # 专题专栏部分计数
    for href in conf.zhuanti_total_list:
        list_pages.extend(await get_page(href))

    count_day, count_week, count_month = count_dates(list_pages, datetime.now())

    count_dic = {}
    count_dic['当天'] = count_day
    count_dic['本周'] = count_week
    count_dic['本月'] = count_month
    print(count_dic)
    return count_dic

async def deal_page(page_count, url):
    list_all_page = []
    flag = False
    for i in range(1, int(page_count) + 1):
        if flag:
            break
        new_url = url + str(i)
        # print(new_url)
        res = await conf.make_request_get(new_url)
        # 如果这里的网页请求不到，说明就是在基层政务公开这个专栏发的，没有跳转到其他地方链接，这个时候要用网页里面获取页面内容的js方法请求
        # 有些页面加了pageindex仍然能访问，但实际却并不会跳转，这一部分再上面处理
        if res[0].status != 404:

            div_elment = res[1].find('div', {'class': 'listnews'})
            if div_elment is not None:
                li_elment = div_elment.find_all('li')
                for li in li_elment:

                    if li.find('span', class_='right date') is not None:
                        date = li.find('span', class_='right date').text
                        # 使用 strptime 方法将字符串转换为 datetime 对象
                        date_obj = datetime.strptime(date, '%Y-%m-%d')  # 你需要根据你的日期字符串的实际格式来调整这个值
                        # 获取当前的日期
                        now = datetime.now()
                        # 判断日期是否在当前月份
                        if date_obj.month != now.month or date_obj.year != now.year:
                            flag = True
                            break
                        list_all_page.append(date_obj)
        # else:
            # deal_has_sencond_not_redict(url, list_all_page)

    return list_all_page

async def get_page(url):
    # 正则表达式
    pattern = r'www\.scpc\.gov\.cn(.*)'
    # 搜索匹配的路径
    match = re.search(pattern, url)
    if match:
        url = match.group(1)
    res = await conf.make_request_get(url)
    # 二级事项跳转目录不尽相同，如果div有listnews，直接在这个页面找，并且有些会翻页,第一步找含有listnews的能否翻页，第二部找是否有listnews，第三步找没有listnews的
    # 找到包含pageCount的<script>标签
    script_tag = res[1].find('script', string=re.compile('pageCount'))
    # 使用正则表达式从<script>标签的内容中提取pageCount的值
    if script_tag is not None:
        page_count_match = re.search(r'pageCount\s*:\s*(\d+)', script_tag.string)
        page_count = page_count_match.group(1)
        script_tag = res[1].find('script', string=re.compile(r"http://www.scpc.gov.cn/content/column/\d+\?pageIndex="))

        # 使用正则表达式从<script>标签的内容中提取URL的值
        if script_tag is not None:
            url_match = re.search(r"(http://www.scpc.gov.cn/content/column/\d+\?pageIndex=)", script_tag.string)
            if url_match:
                url = url_match.group(1)
                print(f"提取的URL是: {url}")
                return await deal_page(page_count, url)
    else:
        # 如果没有pagecount，可能是只有一页，所以传值1，但也可能是不跳转，所以没有pagecount，这个时候在基层政务公开这个页面找右侧列表
        div_elment = res[1].find('div', {'class': 'navjz clearfix'})
        if div_elment is not None:
            a_element = div_elment.find_all('a')
            page_news_dic = {}
            if a_element is not None:
                for _a in a_element:
                    title = _a.get('title')
                    href = _a.get('href')
                    page_news_dic[title] = href
                return deal_area_page_news(page_news_dic)
        else:
            return await deal_page(1, url)


async def deal_area_page_news(page_news_dic):
    list_all_page = []
    for title, url in page_news_dic.items():
        res = await conf.make_request_get(url)
        div_elment = res[1].find('div', {'class': 'newsinfo clearfix'})
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

        list_all_page.append(date_obj)

    return list_all_page

async def get_jczwgk_dic():
    # return [
    # {"name": "自规局", "value": 14},
    # {"name": "教科体局", "value": 9},
    # {"name": "民政局", "value": 1},
    # {"name": "应急局", "value": 1},
    # {"name": "文广旅局", "value": 0},
    # {"name": "人社局", "value": 0},
    # {"name": "农业局", "value": 0},
    # {"name": "市监局", "value": 0},
    # {"name": "卫健局", "value": 0},
    # {"name": "司法局", "value": 0}
    # ],2489

    area_num_dic, allgk = await jczwgk.startMain()
    comp_num_dic = {}

    for area, comp in conf.jczwgk_area_comp_dic.items():
        # 如果单位还没有在字典中，就添加它并设置初始数量为0
        if comp not in comp_num_dic:
            comp_num_dic[comp] = 0
        # 将领域的数量加到单位的数量上
        comp_num_dic[comp] += area_num_dic.get(area, 0)

    # 对字典按值（即数量）进行降序排序
    sorted_comp_num = sorted(comp_num_dic.items(), key=lambda x: x[1], reverse=True)

    # 取前十个元素
    top_ten = sorted_comp_num[:10]

    print(top_ten)
    converted_list = [{"name": item[0], "value": item[1]} for item in top_ten]
    print(allgk)
    return converted_list, allgk

def get_li_num2(list_tags):
    # 获取当前的年份和月份
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day

    # 获取当前周的开始和结束日期
    # 计算一周的开始和结束时间
    start_week = now - timedelta(days=now.weekday(), hours=now.hour, minutes=now.minute, seconds=now.second,
                                 microseconds=now.microsecond)
    end_week = start_week + timedelta(days=6, hours=23, minutes=59, seconds=59)

    # 初始化计数器
    count_day = 0
    count_week = 0
    count_month = 0

    for tag_str in list_tags:
        tag = tag_str.text

        # 检查标签的内容是否是日期
        try:
            date = datetime.strptime(tag, '%Y-%m-%d')
            # 如果是本月的日期，就增加计数器
            if date.year == current_year and date.month == current_month:
                count_month += 1
            # 如果是本周的日期，就增加计数器
            if start_week <= date <= end_week:
                count_week += 1
            # 如果是当天的日期，就增加计数器
            if date.year == current_year and date.month == current_month and date.day == current_day:
                count_day += 1

        except ValueError:
            pass  # 当不能转换为日期时，忽略错误并继续遍历剩下的标签

    print(f"Today's count: {count_day}")
    print(f"This week's count: {count_week}")
    print(f"This month's count: {count_month}")
    return count_day, count_week, count_month


def get_li_num(list_tags,is_month):
    # 获取当前的年份和月份
    now = datetime.now()
    current_year = now.year
    current_month = now.month

    # 初始化计数器
    count = 0

    for tag_str in list_tags:

        tag = tag_str.text

        # 检查标签的内容是否是日期
        try:
            date = datetime.strptime(tag, '%Y-%m-%d')
            # 如果是本月的日期，就增加计数器
            if is_month:
                if date.year == current_year and date.month == current_month:
                    count += 1
            else:
                count += 1
        except ValueError:
            pass  # 当不能转换为日期时，忽略错误并继续遍历剩下的标签

    print(f"本月的标签数量：{count}")
    return count

async def get_height_area():
    # return {'水质监测': 18, '不动产登记': 6, '征地信息': 4, '财政资金直达基层': 2, '环评公示': 2, '助企纾困': 1, '公共资源交易': 1, '价格信息': 1, '卫生健康': 1, '食品药品监管': 1}
    menu_num_dic = {}
    # 重点领域不跳转部分计数
    for key, href in conf.height_area_with_total_dic.items():
        _a = len(await get_page(href))
        menu_num_dic[key] = _a

    # 重点领域跳转部分计数
    for key, href in conf.height_area_redirct_dic.items():
        time_list = []
        await getkeywork(None, href, time_list)
        _a = get_li_num(time_list, True)
        menu_num_dic[key] = _a

    # 使用 sorted 函数对字典按值排序，并取前10个项目
    sorted_items = sorted(menu_num_dic.items(), key=lambda item: item[1], reverse=True)[:10]

    # 将排序后的元组列表转换为字典
    sorted_dict = dict(sorted_items)

    # 打印排序后的字典
    print(sorted_dict)
    converted_list = [{"name": item[0], "value": item[1]} for item in sorted_items]
    return converted_list


# 这个方法不是直接取网页数据了，是取网页中的js方法，以及参数，用它来请求每一页的数据，如果js为空  说明就只有一页数据，那就拿到这一页的日期返回去，如果不为空，就用gettimebypage方法返回所有日期列表
async def getkeywork(prox,menu,time_list):
    if not menu.startswith('http'):
        menu = 'http://www.scpc.gov.cn' + menu

    response,soup = await conf.make_request_get(menu)

    # 查找所有的<script>标签
    scripts = soup.find_all('script')

    # 遍历所有的<script>标签
    for script in scripts:
        # 检查<script>标签的内容是否为None
        if script.string is not None:
            # 检查<script>标签的内容是否包含感兴趣的JavaScript代码
            if 'Ls.pagination' in script.string:
                # 使用正则表达式提取url和data
                url_match = re.search(r'url: "(.*?)"', script.string)
                data_match = re.search(r'data : ({.*?})', script.string, re.DOTALL)
                page_count_match = re.search(r'pageCount:(\d+)', script.string)

                if url_match and data_match and page_count_match:
                    # 提取url
                    url = url_match.group(1)

                    # 提取data
                    data_str = data_match.group(1)

                    page_count = page_count_match.group(1)

                    return await getTimeListByPage(time_list,url,data_str,page_count)


    li_elements = soup.find_all('li', {'class': 'rq'})
    if len(li_elements) == 1:
        return '无'
    time_list.extend(li_elements)
    return time_list


async def getTimeListByPage(time_list,url,data_str,pagecount):
    # 存储所有页面的数据
    # all_pages_data = []
    # 使用正则表达式提取siteId，catId和file
    site_id_match = re.search(r'siteId : "(.*?)"', data_str)
    cat_id_match = re.search(r'catId: "(.*?)"', data_str)
    file_match = re.search(r'file:"(.*?)"', data_str)
    organ_id_match = re.search(r'organId: "(.*?)"', data_str)

    if site_id_match and cat_id_match and file_match and organ_id_match:
        # 提取siteId，catId和file
        site_id = site_id_match.group(1)
        cat_id = cat_id_match.group(1)
        file = file_match.group(1)
        organid = organ_id_match.group(1)
        print(f"siteId: {site_id}, catId: {cat_id}, file: {file}")
        for i in range(1, int(pagecount) + 1):
            # 请求的URL
            if not url.startswith('http'):
                url = 'http://www.scpc.gov.cn' + url
            print(url)
            # 请求的参数
            params = {
                "labelName": "publicInfoList",
                "siteId": site_id,
                "pageSize": "18",
                "pageIndex": i,
                "action": "list",
                "isDate": "true",
                "dateFormat": "yyyy-MM-dd",
                "length": "50",
                "organId": organid,
                "isDetail": "",
                "type": "4",
                "catId": cat_id,
                "cId": "",
                "result": "暂无相关信息",
                "file": file
            }

            # 发送请求
            response, soup = await conf.make_request_get(url, params=params)

            # 检查响应状态码
            if response.status == 200:
                # 将页面数据添加到列表中
                # all_pages_data.append(response.text)

                li_elements = soup.find_all('li', {'class': 'rq'})

                time_list.extend(li_elements)
            else:
                print(f"请求失败，状态码：{response.status}")

    return time_list


async def get_zhuanti_of():

    # return {'主题教育': 237, '预决算': 2868, '两会专题': 225, '乡村振兴': 286, '依法治县': 237, '政府信息公开': 149, '信用双公示': 96, '试点领域': 125}

    zhuan_dic = {}
    for key,hrefs in conf.zhuanti_of_dic.items():
        count = 0
        for href in hrefs:
            count += await count_a(href)
        zhuan_dic[key] = count
    print(zhuan_dic)
    return zhuan_dic

async def main():
    # await get_ywdt_num()
    # await get_all_gk_num()
    # await get_day_week_mon_dic()
    await get_jczwgk_dic()
    await get_zhuanti_of()
    await get_height_area()
if __name__ == '__main__':
    asyncio.run(main())