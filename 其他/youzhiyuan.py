
import requests

url = 'https://uwf7de983aad7a717eb.youzy.cn/youzy.dms.basiclib.api.college.query'
data ='{"keyword":"","provinceNames":[],"natureTypes":[],"eduLevel":"","categories":[],"features":[],"pageIndex":1,"pageSize":20,"sort":11}'

headers ={
'u-sign': '643ff9499febb3ee34c95ffe0bb29cb0',
 'Content-Type': 'application/json',
    }
response = requests.post(url,headers=headers,data=data)
print(response.json())
