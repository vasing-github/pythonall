import datetime
import json
import os
import re
import sys

import conf
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目的根目录
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
# 将项目根目录添加到 sys.path
sys.path.append(project_root)
from kaipumodify.cfg import dealtext
from kaipumodify.search import jiyuehuasearch
import kaipumodify.cfg.text as text

bz_gov_id = text.bz_gov_id
jid = text.jid


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

        if not deal_res(response, pcyw_news_list, None):
            break

        page_index += 1
    return pcyw_news_list


def deal_li_elment(s):
    num = re.findall(r'\d+', s)  # 提取阿拉伯数字
    chn_num = re.findall(r'(十[一二三四五六七八九]?|二十[一二三四五六七八九十]?)', s)  # 提取中文数字
    if len(num) != 1 or len(chn_num) != 1:
        return '', ''
    return int(num[0]), chn_num[0]


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


def re_result(data, cw_dup):
    for item in data:
        title = item[0]
        chn_num = re.findall(r'(十[一二三四五六七八九]?|二十[一二三四五六七八九十]?)', title)  # 提取中文数字
        num = re.findall(r'\d+', title)

        if chn_num and num:
            chn_num = chn_num[0]
            num = int(num[0])

            if chn_num == cw_dup[1] and cw_dup[0] < num <= cw_dup[0] + 5:
                return title, chn_num, num
            elif chn_num == puls_ch_num(cw_dup[1]) and 1 <= num <= 5:
                return title, chn_num, num


def sendMsg(id, title):
    # 定义要发送的消息内容
    _url = 'http://www.scpc.gov.cn/content/article/' + str(id)
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": f"自动保障栏目-常务会/常委会，请人工核实。\n\n\n[{title}]({_url})\n\n\n{_url}\n\n\n<@WuXiaoLong>\n<@MingFengWangBaoNing>"
        }
    }

    key = conf.key_cs
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=" + key
    # 发送HTTP POST请求
    response = requests.post(url, data=json.dumps(data))

    # 输出响应结果
    print(response.text)


def deal_cw_jugement(pcyw_list, url):
    cw_dup = get_new_cw_or_cw_buisines(url)
    print(cw_dup)
    result = re_result(pcyw_list, cw_dup)
    return result


def get_new_bzid_jid():
    global bz_gov_id, jid
    bz_gov_id, jid = dealtext.jiyue_token()


def copy_content(titlle, newtittle, cloumid):
    res = jiyuehuasearch.search(titlle, bz_gov_id)
    if 'status' in res and res['status'] == -9:
        get_new_bzid_jid()
        res = jiyuehuasearch.search(titlle, bz_gov_id)
    if len(res['data']) != 0:

        search_tittle = res['data'][0]['title']
        if search_tittle == titlle:
            id = res['data'][0]['id']
            content = jiyuehuasearch.get_search_content(id, jid, bz_gov_id)

            save_response = save_new_cwh(content['data']['article'], content['data']['content'], newtittle, cloumid)
            sendMsg(save_response['data'], newtittle)


def save_new_cwh(a, c, newtittle, cloumid):
    cookies = {
        'historyCookie': '%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%B4%E5%88%A9%E5%B1%80%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%86%9C%E4%B8%9A%E5%86%9C%E6%9D%91%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%8F%B8%E6%B3%95%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%91%E6%94%BF%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%9E%8D%E5%AA%92%E4%BD%93%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%BA%94%E6%80%A5%E7%AE%A1%E7%90%86%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E7%BA%A2%E5%8D%81%E5%AD%97%E4%BC%9A%2C%E5%8F%8C%E6%A1%A5%E6%B0%B4%E5%BA%93',
        'authenticatecenterjsessionid': jid,
        'bz_govc_SHIROJSESSIONID': bz_gov_id,
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'historyCookie=%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%B4%E5%88%A9%E5%B1%80%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%86%9C%E4%B8%9A%E5%86%9C%E6%9D%91%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%8F%B8%E6%B3%95%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%91%E6%94%BF%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%9E%8D%E5%AA%92%E4%BD%93%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%BA%94%E6%80%A5%E7%AE%A1%E7%90%86%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E7%BA%A2%E5%8D%81%E5%AD%97%E4%BC%9A%2C%E5%8F%8C%E6%A1%A5%E6%B0%B4%E5%BA%93; authenticatecenterjsessionid=NDUxOTYyYjYtM2Q3MC00NzI3LTgwYjktZTNiZGVmNTgyODJl; bz_govc_SHIROJSESSIONID=0ce819a7-3c2f-44fe-a58b-6fff5a1cd493',
        'Origin': 'http://10.15.3.133:83',
        'Referer': 'http://10.15.3.133:83/index;JSESSIONID=174d640d-7a0c-40d1-91e6-98555ee1b259?s=1719891291645&siteId=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'IsAjax': '1',
        'dataType': 'JSON',
        '_': '0.4627731254650349',
    }

    data = {
        'remoteContent': '',
        'fromIndex': '',
        'id': '',
        'columnId': cloumid,
        'siteId': '6787191',
        'title': newtittle,
        'subTitle': '',
        'shortTitle': '',
        'author': '',
        'responsibilityEditor': a['responsibilityEditor'],
        'resources': a['resources'],
        'redirectLink': '',
        'imageLink': '',
        'isNew': '0',
        'isTop': '0',
        'topValidDate': '',
        'isBold': '0',
        'isUnderline': '0',
        'isTilt': '0',
        'titleColor': '',
        'remarks': a['remarks'],
        'content': c,
        'isPublish': '1',
        'publishDate': a['publishDate'],
        'typeCode': a['typeCode'],
        'isAllowComments': '0',
        'quoteStatus': '0',
        'recordStatus': 'Normal',
        'workFlowStatus': '',
        'videoStatus': '100',
        'allImgSrc': '',
        'flag': 'true',
        'imgNum': '0',
        'subIsBold': '0',
        'subIsTilt': '0',
        'subIsUnderline': '0',
        'subTitleColor': '',
        'topTitle': '',
        'topIsBold': '0',
        'topIsTilt': '0',
        'topIsUnderline': '0',
        'topTitleColor': '',
        'smallTitle': '',
        'smallIsBold': '0',
        'smallIsTilt': '0',
        'smallIsUnderline': '0',
        'smallTitleColor': '',
        'qsYear': '',
        'qsMonth': '',
        'qsNum': '',
        'isLight': '0',
        'smallLinkUrl': '',
        'smallLinkTitle': '',
        'picUrl': '',
        'normalUrl': '',
        'recommend': '0',
        'keyWords': '',
        'reportType': '',
        'interviewContentId': '',
        'newsThemeType': '',
        'isLink': '0',
        'articleText': '',
        'hit': '0',
    }

    response = requests.post(
        'http://10.15.3.133:83/articleNews/saveArticleNews',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )
    print(response.text)
    return response.json()


def startMain():
    # pcyw_list = [('十四届县委常委会召开会议专题传达学习省委十二届四次全会精神', '2023-12-07', '平昌县融媒体中心', ''), ('杜小兵主持召开县政府十九届第44次常务会议', '2023-12-04', '县融媒体中心', ''), ('张勋主持召开十四届县委常委会第80次会议', '2023-12-01', '县融媒体中心', ''), ('县政府十九届第43次常务会议召开', '2023-11-28', '县融媒体中心', '')]
    pcyw_list = get_pcyw()
    print(pcyw_list)
    # pcyw_list = [('县政府十九届第44次常务会议召开', '2023-12-20', '县融媒体中心', ''), ('十四届县委常委会召开会议专题传达学习省委十二届四次全会精神', '2023-12-07', '平昌县融媒体中心', ''), ('杜小兵主持召开县政府十九届第42次常务会议', '2023-12-04', '县融媒体中心', ''), ('张勋主持召开十四届县委常委会第80次会议', '2023-12-01', '县融媒体中心', ''), ('县政府十九届第43次常务会议召开', '2023-11-28', '县融媒体中心', '')]

    result = deal_cw_jugement(pcyw_list, conf.zf_cw_url)
    result2 = deal_cw_jugement(pcyw_list, conf.xw_cw_url)

    if result is not None:
        title, chn_num, num = result
        new_titlle = '县政府' + chn_num + '届第' + str(num) + '次常务会议召开'
        copy_content(title, new_titlle, '6790961')
    if result2 is not None:
        title, chn_num, num = result2
        new_titlle = '县委' + chn_num + '届常委会第' + str(num) + '次会议召开'
        copy_content(title, new_titlle, '6790951')


def jugedate(date):
    date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
    date_target = datetime.datetime.now() - datetime.timedelta(days=conf.before_date)
    return date_obj < date_target


def deal_news_href(href):
    if not href.startswith('http://www.scpc.gov.cn'):
        return 1, ""
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
            return 0, info['来源'], info['作者'] if '作者' in info else ""
    return 1, ""


def deal_tittle(str, pcyw_list):
    tittle = str.split('【')[-1].split('】')[-1]

    if '常务会' in tittle or '常委会' in tittle:
        return 0, tittle
    return 1, ''


def deal_res(response, news_list, pcyw_list):
    # 这里返回假则不再翻页
    div_elment = response[1].find('div', {'class': 'listnews'})
    if div_elment is not None:
        li_elment = div_elment.find_all('li')
        for li in li_elment:
            if li.find('span', class_='right date') is not None:
                date = li.find('span', class_='right date').text
                if jugedate(date):
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
                news_list.append((title_deal[1], date, newsinfo[1], newsinfo[2]))

    # 第一页测试结束这里改为真

    return True


if __name__ == '__main__':
    startMain()
    # sendMsg(13951138,'县委十四届常委会第103次会议召开')
