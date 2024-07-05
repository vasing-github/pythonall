import requests
from bs4 import BeautifulSoup

def make_request_get(url):

    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        return response,soup
    else:
        print('网络波动，休眠2秒再试')
        return make_request_get(url)


# 当日期小于目标不再爬取
target_date = '2023-9-11'
# 来源是这些排除
out_comp = [
			'融媒体',

			]
#表格名称
pcyw_excel_name = '平昌要闻.xlsx'
bmgz_excel_name = '部门工作.xlsx'
jcdt_excel_name = '基层动态.xlsx'

# 往前搜索多少天
before_date = 5

cn_num = {
    "一":1, "二":2, "三":3, "四":4, "五":5,
    "六":6, "七":7, "八":8, "九":9, "十":10,
    "十一":11, "十二":12, "十三":13, "十四":14, "十五":15,
    "十六":16, "十七":17, "十八":18, "十九":19, "二十":20,
    "二十一":21, "二十二":22, "二十三":23, "二十四":24, "二十五":25,
    "二十六":26, "二十七":27, "二十八":28, "二十九":29, "三十":30
}

num_cn = {v: k for k, v in cn_num.items()}
# 县政府常务会url
zf_cw_url = f'http://www.scpc.gov.cn/zwgk/xzfcwh/index.html'
# 县委常委会url
xw_cw_url = f'http://www.scpc.gov.cn/zwgk/xwcwh/index.html'

# 测试小群的key
key_cs = '425a53f6-696e-46c1-9d4a-fae8940b136f'
# 正式群key
key_zs = '6c00ba33-68ab-403e-bab2-2b9134a7d7f6'

database_cs = {
    "host": "yuxiaohaishidalao.shop",
    "user": "root",
    "password": "vas9624..",
    "database": "smartpc"
}
database_zs_nat = {
    "host": "10.167.39.125",
    "user": "kfvasing",
    "password": "vas9624..",
    "database": "smartpingchangdb"
}
database_zs_net = {
    "host": "222.215.24.208",
    "user": "kfvasing",
    "password": "vas9624..",
    "database": "smartpingchangdb"
}
database = database_zs_nat