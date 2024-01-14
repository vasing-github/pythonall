import requests
import ast
import xlrd
import xlwt


def dosubmit(d):

    url = 'http://10.160.7.216:9963/scfxfk/fengkong/checks/nk02RandomYwAction!saveYwVerify.do'
    data = {
               "dto['yyw010']": '',
               "dto['ynk031']": '14',
               "dto['aaz002']": d['aaz002'],
               "dto['ypz002']": d['ypz002'],
               # "dto['aaa028']": '20',
               # "dto['aaa028_desc']": '人员',
               # "dto['ypz003']": '01',
               "dto['ypz003_desc']": '身份证',
               "dto['ypz007']": d['ypz007'],
               # "dto['ygz006']": 'scsi',
               # "dto['ygz006_desc']": '城镇职工',
               # "dto['aaa121']": '125523_sq',
               # "dto['aaa121_desc']": '企业养老退休待遇核定(事中)',
               # "dto['aae011']": '81513051',
               # "dto['aae011_desc']": '杨苓英',
               # "dto['aae036']": '2023-05-05',
               # "dto['yab003']": '511923',
               "dto['yab003_desc']": '巴中市平昌县',
               # "dto['ynk044']": '2023-05-05',
               # "dto['ynk041']": '4',
               "dto['ynk041_desc']": '无问题',
               "dto['violations']": '0',
               "dto['recovers']": '0',
               "dto['ynk033_1']": '',
               "dto['ynk033_1_desc']": '',
               "dto['ynk034_1']": '',
               "dto['ynk043']": '经核实无问题',
               "dto['ynk033']": '0',
               "dto['ynk033_desc']": '通过',
               # "dto['ynk034']": '',
               # "dto['msgWarn']": '00',
               # "dto['ynk040']": '1000884164',
               # "dto['fileInfoDivTag']": '1',
               # "dto['hidenUpload']": '0',
               # "dto['gz08List']": '',
               # "dto.ynk031": 14
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '1280',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
         'Host': '10.160.7.216:9963',
        'Origin': 'http://10.160.7.216:9963',
        'Referer': 'http://10.160.7.216:9963/scfxfk/fengkong/checks/nk02RandomYwAction!getYwVerifyRandom.do?dto.aaz002=20230221150102737829_sq',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.post(url, headers=headers, data=data)

    print(response.json())

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


cookie = 'JSESSIONID=1viRKFwZceREE94iM2-GQGR46VCO_eWjbac5jhpb31N2zZDgkfBF!-1195317490; _FaceSkin=deepBlue; hint_01=hint_01; BIGipServertongYiMenHuDanDianDengLu=2500632586.19743.0000; BIGipServertymhjcpt=3943473162.18207.0000; BIGipServerzskglzyzxt=3792478218.17695.0000; BIGipServerB10.160.7.216_9963=1058381834.18207.0000'
data = searchList()
for d in data:
    dosubmit(d)