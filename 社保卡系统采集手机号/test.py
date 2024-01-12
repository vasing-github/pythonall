import requests
import xlrd
import xlwt


def getinfo(str):
    url = 'http://10.160.1.18:9002/cardmgt/cardStatisticAnalysis/g01/g0128Rest/queryAc47'
    data = {
        'pageNumber': 1,
        'pageSize': 10,
        'aac058': '01',
        'aac147': str,
        'frontUrl': 'http://10.160.1.18:9002/cardmgt/template/g01Module.html#/g0128?_modulePartId_=186224896'
    }

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'insert_cookie=26236291; JSESSIONID=lR-C5Rqfinok6ZipyMOBzE_-INFCNbsByJvb3gIcB6-GS5an9f3U!385196851',
        'Host': '10.160.1.18:9002',
        'Origin': 'http://10.160.1.18:9002',
        'Referer': 'http://10.160.1.18:9002/cardmgt/template/g01Module.html',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-N9100 Build/LRX21V) > AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 > Chrome/37.0.0.0 Mobile Safari/537.36 > MicroMessenger/6.0.2.56_r958800.520 NetType/WIFI Edg/116.0.0.0'
    }
    response = requests.post(url, headers=headers, data=data,timeout=10)
    print(response.json()['data']['pageBean']['list'][0]['aac067'])
    print(response.json()['data']['pageBean']['list'][0]['aac010'])
    return response.json()['data']['pageBean']['list'][0]['aac067'],response.json()['data']['pageBean']['list'][0]['aac010']

if __name__ == '__main__':
    data = xlrd.open_workbook(r'test.xlsx')
    print(data.nsheets)
    sheet1 = data.sheet_by_index(0)  # 通过索引获取表格
    # 创建新的 Excel 文件
    new_data = xlwt.Workbook()
    new_sheet = new_data.add_sheet('Sheet1')
    maxrows = sheet1.nrows
    for i in range(maxrows):
        rows = sheet1.row_values(i)
        print(i, rows[0])
        try:
            info = getinfo(rows[0])
        except Exception as e:
            print("错了一个")
            continue
        new_sheet.write(i, 0, rows[0])
        new_sheet.write(i, 1, info[0])
        new_sheet.write(i, 2, info[1])

    # 保存新的 Excel 文件
    new_data.save('phoneadress.xls')
