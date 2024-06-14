# -*- coding: utf-8 -*-
import requests
import gethtml
import re
from bs4 import BeautifulSoup
def get_study_code_and_recordid(courceid,selectionid,ck,planid):
    # 注意这里，如果是专业课就把获取html请求 改为 /   如果是学公需就是-
    url = gethtml.get_src(courceid,selectionid,ck,planid)
    print(url)
    response = requests.get(url, )


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
                return recordId.group(1),studyCode.group(1),url





