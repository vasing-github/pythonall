# -*- coding: utf-8 -*-
import requests
import gethtml
import re
from bs4 import BeautifulSoup
def get_study_code_and_recordid(courceid,selectionid,ck,planid):
    # 注意这里，如果是专业课就把获取html请求 改为 /   如果是学公需就是-
    url = gethtml.get_url(courceid,selectionid,ck,planid)
    # print(url)
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
    return '','',url


def get_study_code_and_recordid2(courceid,selectionid,ck,planid):
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
    # 发送请求获取HTML内容
    response = requests.get(url, cookies=cookies, headers=headers)
    response.encoding = 'utf-8'

    # 打印响应内容以进行调试
    # print(response.text)

    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找script标签
    script_tags = soup.find_all('script', type='text/javascript')

    sign_id = None
    # 遍历所有script标签
    for script_tag in script_tags:
        if script_tag.string:
            # 打印script标签内容以进行调试


            # 提取signId值
            sign_id_match = re.search(r'attrset\.signId\s*=\s*"([^"]+)"', script_tag.string)
            if sign_id_match:
                sign_id = sign_id_match.group(1)
                break

    if sign_id:
        print(f'signId: {sign_id}')
        return sign_id
    else:
        print('signId not found')
    return ''

if __name__ == '__main__':


    url = 'https://videoadmin.chinahrt.com/videoPlay/playEncrypt?param=M6FUERTovrwJKhmQd7T7TyNBK%2BVNxhzqSH0PXmorPcZ3rSPEh3uIvka%2FyE3InQ%2F4DeUOXdLAPuFPbuWqM7gto7EJzxuiNJ27XTKne2kfX8TwXayEpRR%2BBx2qNm6PaNCE53UxECkhSGHXaE2JZNesZcBB1Bq7RHzNHSfUBuJKLjfmarzBgbbLGN2syT6eiq6vwEyaN4d0RseygKNXisXChNY0p7ylVdk4v1dbWewWqZuuBDyOjSMk2O24DL5TXVXZXye1%2BqOdFYvD9kO%2Fu%2Bz8Oj81JeICop8ZbzZhMwdpeTR4t90WxoLqIDLXvThch3r497Bog%2F0WEWxJo0Q45XO%2FgnMbH346bgkNOkaJESugyk5g3qKyTh1hrBPKvdUStLHZWf6ATqOukafkePOfTVsE72Wdin2EOP8g71nTG47tn%2FkqZjdlnc5ql%2Bt4TCJov1Mx6c6Nrgir4YLbbwZGklmZ1Dnwwn%2BVRzbLkiALS6FFyYu4brhU3gr%2FLUowarzrA84anZDSZ3MkRcMJ9DVC%2Bd9mFi%2BCJ7Qm5n2W0x8syZAQqbLu%2FBHPS2jN%2F%2BYnFrYVYWaBknTBMgqn%2Fa%2FVKppiSD00vLZDlOnEzQ%2BHt9hibjBB4EIMGcY3OCoKUElK8o%2Fomlz1QidAZXmJy3x6bXBEhbIoMEGHnEgpMK2nE9VKvcCHOAAB%2BNKw5cuPokYJdSJ8LPA%2B'
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
    # 发送请求获取HTML内容
    response = requests.get(url, cookies=cookies, headers=headers)
    response.encoding = 'utf-8'

    # 打印响应内容以进行调试
    # print(response.text)

    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找script标签
    script_tags = soup.find_all('script', type='text/javascript')

    sign_id = None
    # 遍历所有script标签
    for script_tag in script_tags:
        if script_tag.string:
            # 打印script标签内容以进行调试
            print(script_tag.string)

            # 提取signId值
            sign_id_match = re.search(r'attrset\.signId\s*=\s*"([^"]+)"', script_tag.string)
            if sign_id_match:
                sign_id = sign_id_match.group(1)
                break

    if sign_id:
        print(f'signId: {sign_id}')

    else:
        print('signId not found')