# -*- coding: utf-8 -*-
import requests
import gethtml
import re
from bs4 import BeautifulSoup
def get_study_code_and_recordid(courceid,selectionid,ck,planid):
    # 注意这里，如果是专业课就把获取html请求 改为 /   如果是学公需就是-
    url = gethtml.get_url(courceid,selectionid,ck,planid)
    cookies = {
        'JSESSIONID': '94B5F0D142D88EFE3E6DC4DF1376764F',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        # 'Cookie': 'JSESSIONID=94B5F0D142D88EFE3E6DC4DF1376764F',
        'Referer': 'https://edu.chinahrt.com/',
        'Sec-Fetch-Dest': 'iframe',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get(url, cookies=cookies, headers=headers)
    response.encoding = 'utf-8'


    soup = BeautifulSoup(response.text, 'lxml')

    # 找到所有的script标签
    scripts = soup.find_all('script')

    # 遍历所有的script标签
    for script in scripts:
        # 获取script标签的内容
        script_content = script.string
        if script_content is not None:
            # 使用正则表达式查找你需要的数据
            recordId = re.search(r'recordId = "(.*?)"', script_content)
            studyCode = re.search(r'studyCode = "(.*?)"', script_content)
            if recordId and studyCode:
                # print('recordId:', recordId.group(1))
                # print('studyCode:', studyCode.group(1))
                return recordId.group(1),studyCode.group(1),url

# 8.25 测试代码
    # Find the script tag containing the token
    # script_tag = soup.find('script', string=lambda text: text and 'token' in text)
    #
    # # Extract the token value
    #
    # token_match = re.search(r"token:\s*'([^']+)'", script_tag.string)
    # token = token_match.group(1) if token_match else None
    #
    # print("Token:", token)
    # return token



if __name__ == '__main__':
    url = 'https://videoadmin.chinahrt.com/videoPlay/playEncrypt?param=M6FUERTovrwJKhmQd7T7TyNBK%2BVNxhzqSH0PXmorPcZ3rSPEh3uIvka%2FyE3InQ%2F4KQ10ZDPXDfHpXIXR%2BcI5FbEJzxuiNJ27XTKne2kfX8TwXayEpRR%2BBx2qNm6PaNCE53UxECkhSGHXaE2JZNesZcBB1Bq7RHzNHSfUBuJKLjfmarzBgbbLGN2syT6eiq6vwEyaN4d0RseygKNXisXChNY0p7ylVdk4v1dbWewWqZtVdu0J73xZQ7r7FzhTOuZFKAKA5DApDeVet0oKX%2B1T72HaonAl7xEwaRjJS0sISh%2Bx7hh085VbEYnbGOQzwAzt9r1PD1nveiK0F9ElfMXEfEeJyD7Rp3BoP0ox3i7gbmDBdHvIAYusrm%2BSxGJiw0Cwc0%2BSk8b5h7GxnJEpTQXmIReBKmZhOABCb%2BY2hniYaUOl%2FTxpl4WF6VJgWq3%2F1Q8YXijcMrgL52mkVlvg8mqH7cyZbps%2BlrlncBvgPNhLrrNSvvrEkj0fD410nf6%2BhpH3XBetjVoLZsL6rWZWCnCYf7y%2Bnj80svW0Z5mRLrpEIlCx2TbYW7cXm6HH5bm72JZvdG60uUzu7oRWDgG5ktYBWHA12AysCwUbOXI%2FOYgb7umfzgG4VuyeZZui%2Bdf6jOfFTR7bR%2FE%2BZkyUgySSYhJVzH6maf3CZoIW33gLpPrVYuVKAIyrGQl1ojC7moQAF25v'
    cookies = {
        'JSESSIONID': '94B5F0D142D88EFE3E6DC4DF1376764F',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        # 'Cookie': 'JSESSIONID=94B5F0D142D88EFE3E6DC4DF1376764F',
        'Referer': 'https://edu.chinahrt.com/',
        'Sec-Fetch-Dest': 'iframe',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get(url, cookies=cookies, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    # 找到所有的script标签
    scripts = soup.find_all('script')

    # 遍历所有的script标签
    for script in scripts:
        # 获取script标签的内容
        script_content = script.string
        if script_content is not None:
            # 使用正则表达式查找你需要的数据
            recordId = re.search(r'recordId = "(.*?)"', script_content)
            studyCode = re.search(r'studyCode = "(.*?)"', script_content)
            if recordId and studyCode:
                print('recordId:', recordId.group(1))
                print('studyCode:', studyCode.group(1))


