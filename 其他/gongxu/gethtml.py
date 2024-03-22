# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import conf
def get_src(courceid,selectionid,ck,planid):
    cookies = {
        'PLATFORM_INFO__': '151',
        'chrt_token_151': ck,
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'PLATFORM_INFO__=151; chrt_token_151=eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk4MDAzMjgzMzM2QDE1MSIsIm1vYmlsZSI6IjEzNTY4NDcxMjY2IiwidXNlck5hbWUiOiI1MTM3MjMxOTgwMDMyODMzMzYiLCJ1c2VySWQiOiJwMXMwXzI1MzIyZTEyLTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcwOTc5NTAzMSwianRpIjoiMmMzMjNkNjkyOTQ2NGRlY2E0NzMxNmY2YWY1MThkNmQifQ.WF2xw43lxx9w_bJlf0S0DWNx4oqxS7OEXMNKNKFOQZw',
        'Referer': 'https://edu.chinahrt.com/151/learning_center/trainplan_detail/b34287b27e1142fb9f00d0046e6a9ee9/2c9ff022029b4d0fa3a64948fc00a73c',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'sectionId': selectionid,
    }

    response = requests.get(
        'https://edu.chinahrt.com/151/play_video/'+planid+'-'+courceid,
        params=params,
        cookies=cookies,
        headers=headers,
    )


    soup = BeautifulSoup(response.text, 'lxml')  # 使用lxml来解析HTML

    # 找到所有的iframe标签
    iframes = soup.find_all('iframe')

    # 遍历所有的iframe标签
    for iframe in iframes:
        # 获取src属性
        src = iframe.get('src')
        # 检查src是否以"https://videoadmin.chinahrt.com"开头
        if src and src.startswith('https://videoadmin.chinahrt.com'):
            # print(src)
            return src


if __name__ == '__main__':
    get_src()