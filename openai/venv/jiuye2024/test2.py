import time

import requests
import pandas as pd

def insert(idcard,shouru,name,huji,changzhu,zhuanyi,lianxidianhua,zhuanyitype,zhuanyihangye):
    url = "http://10.160.7.100:8000/jyback/jy105/jy105_emp02"
    headers = {
        "Host": "10.160.7.100:8000",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://10.160.7.100:8000",
        "Referer": "http://10.160.7.100:8000/jyback/template/ruralLaborers.html",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
         "Cookie": cookie,
        "Accept-Encoding": "gzip, deflate",
        # "Content-Length": "1063"
    }

    data = {
        # "aac001": info1['aac001'],
        # "aac147": info1['aac147'],
        # "aac058": info1['aac058'],
        "aac003": name,
        # "aac004": info1['aac004'],  # 性别1男，2女
        # "aac006": info1['aac006'],
        # "aac005": info1.get('aac005') or "01",
        # "aac024": info1.get('aac024') or "13", # 政治面貌 13群众 03共青团员

        # "aac011": info1['aac011'],  # 文化程度 10研究生以上 11博士  14硕士 21本科  31专科 41中等 44高中 47技工 61普通中学  71初级中学 81小学 90其他
        "aae005": lianxidianhua,
        # "aac009": info1['aac009'],
        "acc316": "0",  # 人
        "aab301": huji,  # 户籍地 查出来是多个斜杠，插入只填最后一个
        # "aac010": info1.get('aac010') or " ",  # 户籍地详细地址  汉字
        "aab299": changzhu,  # 常住地，查出来是多个斜杠，插入只填最后一个
        # "aae006": info1.get('aae006') or " ",  # 常住地 详细地址，这是汉字
        # "acc520": info1['acc520'],
        "aac316": "03",  # 人口资源分类，03适龄劳动 01未满16  02年满十六周岁  04判刑劳改   05现役军人  06出国定居  07法定退休或农村老人 08丧失劳动力 09死亡 10 失踪
        "acc987": "04",  # 农村劳动力转移就业状况 04外出务工， 99无转移状态 02务农  03返乡未就业 05自主创业 06农合吸纳  07灵活就业 06本市县就业
         "acc458": "0",
         "aac369": "0",
        "ycc0ov": "0",
    "ycc0ox": "0",
    "acc333": "0",
    "acc455": "2",  # 转移就业方式 1政府组织转移  2自发转移  3企业组织  5就业扶贫车间  6农村劳务 7其他
        # "aab004": info1['aab004'],
        # "acc454": info1['acc454'],
        "acc457": zhuanyihangye,
        "acc452": zhuanyitype,
        "acc328": shouru,  # 收入
        "aab301Desc": zhuanyi,
        # "aae013": info1['aae013'],
        "cc55Jsonstr": "[]",
        # "aac180": info1['aac180'],
        # "aac181": info1['aac181'],
        # "aac183": info1['aac183'],
        "_modulePartId_": "1000241649",
        "frontUrl": "http://10.160.7.100:8000/jyback/template/ruralLaborers.html#/ruralLaborersManage?_modulePartId_=1000241649"
    }

    response = requests.post(url, headers=headers, data=data)

    print(response.status_code)
    # print(response.text)


def getinfo1(idcard):

    url = "http://10.160.7.100:8000/jyback/jy001/jy001_base03"
    headers = {
        "Host": "10.160.7.100:8000",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://10.160.7.100:8000",
        "Referer": "http://10.160.7.100:8000/jyback/template/ruralLaborers.html",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": cookie,
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "189"
    }

    data = {
        "aac147": idcard,
        "_modulePartId_": "1000241649",
        "frontUrl": "http://10.160.7.100:8000/jyback/template/ruralLaborers.html#/ruralLaborersManage?_modulePartId_=1000241649"
    }

    response = requests.post(url, headers=headers, data=data)

    print(response.status_code)
    # print(response.text)
    return response.json()['data']['result'][0]

def getinfo2():


    url = "http://10.160.7.100:8000/jyback/jy105/jy105_emp14"
    headers = {
        "Host": "10.160.7.100:8000",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://10.160.7.100:8000",
        "Referer": "http://10.160.7.100:8000/jyback/template/ruralLaborers.html",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": cookie,
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "671"
    }

    data = {
        "aac001": "1035733301",
        "aac002": "513723199811243556",
        "aae100": "1",
        "aac005": "01",
        "aac006": "1998-11-24",
        "aac003": "孙小东",
        "aac004": "1",
        "aac009": "20",
        "aac010": "宝塔村一社62号",
        "aac011": "90",
        "aac058": "01",
        "aac183": "52011600",
        "aac024": "13",
        "aac180": "专科",
        "aac181": "2019-06-30",
        "aae006": "天府三街1111号",
        "aab299": "510000000000/510100000000/510199000000",
        "aae005": "13540433474",
        "aac147": "513723199811243556",
        "aab301": "510000000000/511900000000/511923000000",
        "age": "26",
        "aac316": "03",
        "_modulePartId_": "1000241649",
        "frontUrl": "http://10.160.7.100:8000/jyback/template/ruralLaborers.html#/ruralLaborersManage?_modulePartId_=1000241649"
    }

    response = requests.post(url, headers=headers, data=data)

    print(response.status_code)
    print(response.text)

def getinfo3():


    url = "http://10.160.7.100:8000/jyback/jy007/jy007_com01"
    headers = {
        "Host": "10.160.7.100:8000",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://10.160.7.100:8000",
        "Referer": "http://10.160.7.100:8000/jyback/template/ruralLaborers.html",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie": cookie,
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "197"
    }

    data = {
        "arealevel": "5",
        "areacode": "350122000000",
        "_modulePartId_": "1000241649",
        "frontUrl": "http://10.160.7.100:8000/jyback/template/ruralLaborers.html#/ruralLaborersManage?_modulePartId_=1000241649"
    }

    response = requests.post(url, headers=headers, data=data)

    print(response.status_code)
    print(response.text)


def readexcel():
    # 读取Excel文件
    file_path = 'worker.xlsx'
    df = pd.read_excel(file_path)

    # 遍历每个单元格并打印内容
    for row in df.itertuples(index=False):

        idcard = getattr(row, '身份证号码')
        name = getattr(row, '姓名')
        shouru = getattr(row, '月收入')
        huji = getattr(row,"户籍地址")
        changzhu = getattr(row,"常住地址")
        zhuanyi = getattr(row,"转移就业地点")
        lianxidianhua = getattr(row,"联系电话")
        zhuanyitype = getattr(row,"转移就业产业类别")
        zhuanyihangye = getattr(row,"转移就业从事行业")
        # print(f'列名1: {value1}, 列名2: {value2}')
        # info1 = getinfo1(idcard)
        print(name)
        insert(idcard,shouru,name,huji,changzhu,zhuanyi,lianxidianhua,zhuanyitype,zhuanyihangye)
        time.sleep(1)


cookie = 'SESSION=NzZhMGZhOTYtMmQ0Ni00ODk5LTlkMzMtYjRmNmMxMTFmYTJi; BIGipServer10.160.7.100:8000=34775050.12661.0000'
if __name__ == '__main__':
    getinfo1('511923202202070112')
    # print("=============================================\n")
    # getinfo2()
    # print("=============================================\n")
    # getinfo3()
    # insert()
    # readexcel()