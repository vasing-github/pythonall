import requests

url = "http://hcp.sczwfw.gov.cn/app/api/evaluate/getChannel"

payload = "{\"areaCode\":\"\",\"shardKey\":\"5100\",\"dataTime\":\"2022-09\"}"
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json;charset=UTF-8',
  'Cookie': 'JSESSIONID=D977D7750763AD70C1E9D240C65B51A0',
  'Origin': 'http://hcp.sczwfw.gov.cn',
  'Referer': 'http://hcp.sczwfw.gov.cn/evaluateArea/evaluateIndex?areaCode=510000000000',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
