import time

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
    url = 'http://10.160.7.216:9963/scfxfk/fengkong/checks/nk04RandomYwAction!query.do'
    data = {
        'dto[gridId]': 'rectifyList',
        'dto[aae036_start]': '',
        'dto[aae036_end]': '',
        'dto[user_yab003]': '511923',
        'dto[yab003]': '511923',
        'dto[yab003_desc]': '巴中市平昌县',
        'dto[ygz010]': '',
        'dto[ygz010_desc]': '',
        'dto[ygz020]': '',
        'dto[ygz020_desc]': '',
        'dto[ygz101]': '',
        'dto[ygz101_desc]': '',
        'dto[aaa028]': '',
        'dto[aaa028_desc]': '',
        'dto[ynk023_start]': '',
        'dto[ynk023_end]': '',
        'dto[cxfs]': '',
        'dto[cxfs_desc]': '',
        'dto[randomNum]': '',
        'dto[rzid]': '',
        'dto[scale]': '',
        'dto[scale_desc]': '',
        'gridInfo[warnList_limit]': 10,
        'gridInfo[warnList_start]': 0,
        'gridInfo[issueList_limit]': 10,
        'gridInfo[issueList_start]': 0,
        'gridInfo[fkVerifyList_limit]': 10,
        'gridInfo[fkVerifyList_start]': 0,
        'gridInfo[finishList_limit]': 10,
        'gridInfo[finishList_start]': 0
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',

        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'JSESSIONID=VX0aszR1TNfb2R2VTgXeL2zNjeJ9Qv7IX4tiPHFYLctUSfXdXDzy!283645343; DWRSESSIONID=AkKtnijdQGnydRbd7iOm0AgQvcBE!CQIqAo; hint_01=hint_01; BIGipServertongYiMenHuDanDianDengLu=2483855370.18207.0000; BIGipServertymhjcpt=1041145866.17695.0000; BIGipServerzskglzyzxt=3742146570.18207.0000; BIGipServerB10.160.7.216_9963=1058381834.17183.0000',
        'Host': '10.160.7.216:9963',
        'Origin': 'http://10.160.7.216:9963',
        'Referer': 'http://10.160.7.216:9963/scfxfk/fengkong/checks/nk02RandomFkAction!handleFk.do?businesstype=null&menuid=88029003&___businessId=88029003',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0',
        'X-Requested-With': 'XMLHttpRequest'
    }

    response = requests.post(url, headers=headers, data=data)
    print(response.text)
    # data = response.json()['lists']['fkVerifyList']['list']
    return data


cookie = 'JSESSIONID=TToZasHP5zHetTqIV0GmCHrlN7y0VP3Rpe2DbByHY5o-8OFH1997!1192646186; _FaceSkin=deepBlue; hint_01=hint_01; BIGipServertongYiMenHuDanDianDengLu=3876364298.19743.0000; BIGipServertymhjcpt=2550964234.17183.0000; BIGipServerzskglzyzxt=2399969290.17183.0000; BIGipServerB10.160.7.216_9963=1041604618.18207.0000'
data = searchList()
time.sleep(3)
data = searchList()
for d in data:
    dosubmit(d)