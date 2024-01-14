import requests
import ast
import xlrd
import xlwt
# 个人台账查询   从test表中读取身份证，将查询到的结果放入新表，参数可选时间
# ；ll

def serch(basic):

    url = 'http://10.160.7.216:9954/csi_sc/publicBusiness/employeeQuery/employeeIntegrativeQuery/employeeCollectPlanQueryAction!getPersonBaseInfo.do'
    data = {
        "dto['aac001']": basic[0],
        "_aac001": basic[0],
        "dto['aac003']": basic[2],
        "dto['aac002']": basic[1],
        "dto['aae140']": "110",
        "dto['aae140_desc']": "企业职工基本养老保险",
        "dto['aae078']": "",
        "dto['aae078_desc']": "",
        "dto['aae041']": "202201",
        "dto['aae042']": "202212",
        "dto['bz']": "",
        "dto['bz_desc']": "",
        "gridInfo['dgJfmxList_limit']": "200",
        "gridInfo['dgJfmxList_start']": "0",
        "dto._PAGE_AUDIT_DATA_": "{}",
        "__businessId": 170567
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '507',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
        'Host': '10.160.7.216:9954',
        'Origin': 'http://10.160.7.216:9954',
        'Referer': 'http://10.160.7.216:9954/csi_sc/publicBusiness/employeeQuery/employeeIntegrativeQuery/employeeCollectPlanQueryAction.do?businesstype=null&menuid=170567&___businessId=170567',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.post(url, headers=headers, data=data)

    data = response.json()['lists']['dgJfmxList']['list']
    result = set()
    for item in data:
        result.add(item['aab004'])
        result.add(item['aab359'])
        result.add(item['aab360'])
    return result


def basicInform(card):
    url = 'http://10.160.7.216:9954/csi_sc//process/comm/action/suggestFrameworkAction!getByac01All.do'
    data = {
        "gridInfo['dgJfmxList_limit']": "200",
        "gridInfo['dgJfmxList_start']": "0",
        "dto.jstj": card,
        "dto.qstb": "1",
        "dto._PAGE_AUDIT_DATA_": "{}",
        "__businessId": 170567
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '160',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': cookie,
        'Host': '10.160.7.216:9954',
        'Origin': 'http://10.160.7.216:9954',
        'Referer': 'http://10.160.7.216:9954/csi_sc/publicBusiness/employeeQuery/employeeIntegrativeQuery/employeeCollectPlanQueryAction.do?businesstype=null&menuid=170567&___businessId=170567',
        'User-Agent': 'Mozilla/5.',
        'X-Requested-With': 'XMLHttpRequest'
    }

    response = requests.post(url, headers=headers, data=data)
    # print(response.text)
    data = response.json()['fieldData']['data']
    data = data.replace('new Array', '')
    data = ast.literal_eval(data)

    print(data[1][1],data[1][2],data[1][3])
    return data[1][1],data[1][2],data[1][3]



def excel():
    data = xlrd.open_workbook(r'test.xlsx')
    print(data.nsheets)
    sheet1 = data.sheet_by_index(2)  # 通过索引获取表格
    # 创建新的 Excel 文件
    new_data = xlwt.Workbook()
    new_sheet = new_data.add_sheet('Sheet1')
    maxrows = sheet1.nrows
    for i in range(maxrows):
        rows = sheet1.row_values(i)
        print(i,rows[0])
        try:
            basic = basicInform(rows[0])
            ret = serch(basic)
        except Exception as e:
            print("错了一个")
            continue
        new_sheet.write(i, 0, rows[0])
        # 在身份证号码后面插入新数据
        ret_str = ', '.join(map(str, ret))
        new_sheet.write(i, 1, ret_str)
    # 保存新的 Excel 文件
    new_data.save('2022年交通.xls')


cookie = 'JSESSIONID=pzSunnNvcJ4hXvmcV764QXwclkNtNZ2sLW3YKi1wOvCBh-2FJmQm!1603284101; BIGipServertongYiMenHuDanDianDengLu=2483855370.21279.0000; BIGipServertymhjcpt=2550964234.17695.0000; BIGipServerzskglzyzxt=2399969290.17695.0000; BIGipServerB10.160.7.216_9954=1293197322.17183.0000'
excel()




# basic = basicInform(510724199810206140)
# print(basic[0])
# ret = serch(basic)