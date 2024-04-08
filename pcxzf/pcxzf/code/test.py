import requests

url = 'https://szpc.pcxzf.cn:8080/farmer/farmernotoken/countfarmer'
response = requests.get(url)
print(response.text)