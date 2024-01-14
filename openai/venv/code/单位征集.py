import requests
import ast
import xlrd
import xlwt


def dosubmit(d):

    url = 'http://10.160.7.216:9954/csi_sc/publicBusiness/organizationPay/employerPayArrearageAction!toSave.do'
    data = {
             "dto['yaa017']": 1,
        "dto['curMenuid']": "5000146722",
       " dto['yaa017_desc']": "完成流程",
        "dto['systime']":"2023-07-06 10:43:17.0" ,
        "dto['aab001']": "5000142604",
        "dto['aae042']": "202212",


    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '1280',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
         'Host': '10.160.7.216:9954',
        'Origin': 'http://10.160.7.216:9954',
        'Referer': 'http://10.160.7.216:9954/csi_sc/publicBusiness/organizationPay/employerPayArrearageAction.do?businesstype=null&menuid=60371204&___businessId=60371204',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.post(url, headers=headers, data=data)

    print(response.text)

def searchList():
    global cookie
    url = 'http://10.160.7.216:9963/scfxfk/fengkong/checks/nk02RandomYwAction!query.do'
    data = {
        "dto['gridId']": 'ywVerifyList',
        "dto['aae036_start']": '',
        "dto['aae036_end']": '',
        "dto['yab003']": '511923',
        "dto['yab003_desc']": '巴中市平昌县',
        "dto['aaa123']": '',
        "dto['aaa123_desc']": '',
        "dto['aaa121']": '',
        "dto['aaa121_desc']": '',
        "dto['aaa028']": '',
        "dto['aaa028_desc']": '',
        "dto['ynk023_start']": '',
        "dto['ynk023_end']": '',
        "gridInfo['issueList_limit']": '9',
        "gridInfo['issueList_start']": '0',
        "gridInfo['ywVerifyList_limit']": '900',
        "gridInfo['ywVerifyList_start']": '0',
        "gridInfo['finishList_limit']": '9',
        "gridInfo['finishList_start']": '0',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '594',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
        'Host': '10.160.7.216:9963',
        'Origin': 'http://10.160.7.216:9963',
        'Referer': 'http://10.160.7.216:9963/scfxfk/fengkong/checks/nk02RandomYwAction.do?businesstype=null&menuid=85515349&___businessId=85515349',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.post(url, headers=headers, data=data)
    data = response.json()['lists']['ywVerifyList']['list']
    return data


cookie = 'JSESSIONID=Kyoo_Q1hb-kOdOHkDZbRPOX5HXmDvZJx-yD5xNLR_mVlqG6_Z7Qb!480609823; _FaceSkin=deepBlue; hint_01=hint_01; BIGipServertongYiMenHuDanDianDengLu=3893141514.17183.0000; BIGipServertymhjcpt=3926695946.18719.0000; BIGipServerzskglzyzxt=3775701002.17695.0000; BIGipServerB10.160.7.216_9954=1192534026.17183.0000'
dosubmit(cookie)
# data = searchList()
# for d in data:
#     dosubmit(d)