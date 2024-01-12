#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import requests


url = 'http://hcp.sczwfw.gov.cn/app/api/evaluationFileHandler'
#content = {"anonymous":1,"busiCode":"511923-20220921-001628","evalChannel":"3","evalSource":"2","objType":"2","evaluationChildren":[],"instructions":"","objCode":"code-001","praise":[],"publish":1,"score":5,"maxBadClassifyFlag":""}
data = {"content":("anonymous",1,"busiCode","511923-20220919-000581","evalChannel","3","evalSource","2","objType","2","evaluationChildren",[],"instructions","","objCode","code-001","praise",[],"publish",1,"score",5,"maxBadClassifyFlag","")}
data1={'content':{"anonymous":1,"busiCode":"511923-20220921-001628","evalChannel":"3","evalSource":"2","objType":"2","evaluationChildren":[],"instructions":"","objCode":"code-001","praise":[],"publish":1,"score":5,"maxBadClassifyFlag":""}}

print(type(data1))
print(type(data1['content']))
headers ={'Accept':'application/json, text/plain, */*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Content-Length': '359',
#'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarytlDbYgCxKA6eOkJd',
'Host':'hcp.sczwfw.gov.cn',
'Origin':'http://hcp.sczwfw.gov.cn',
'Referer': 'http://hcp.sczwfw.gov.cn/appEval/index.html',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
response = requests.post(url,headers=headers,data=data1)
print(response.text)
