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


# 当日期小于目标不再爬取 包含
target_date = '2023-9-11'
# 当日期大于目标继续翻页  包含
after_date = '2023-12-31'
# 来源是这些排除
out_comp = ['团委',
			'日报',
			'融媒体',
			'人大',
			'县人民政府',
			'工会',
			'政法委',
			'政协',
			'宣传',
			'纪委',
			'统战部',
			]
#表格名称
pcyw_excel_name = '平昌要闻.xlsx'
bmgz_excel_name = '部门工作.xlsx'
jcdt_excel_name = '基层动态.xlsx'