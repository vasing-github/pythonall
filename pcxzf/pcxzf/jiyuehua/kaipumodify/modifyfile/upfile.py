import requests

# 文件路径
file_path = 'path/to/your/rBUtImZdJn2Aaj5GAAEeAIUXQEc028.xls'

# 请求的 URL
url = 'http://10.15.3.133:83/content/updateFileByPath'

# 请求头部
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data',
    'Origin': 'http://10.15.3.133:83',
    'Referer': 'http://10.15.3.133:83/fileCenter/uploadPage?uploadType=1&s=0.27547134292630027&isOpen=true&_=1717397696247',
    'User-Agent': 'your_user_agent'
}

# 请求体中的文件和其他参数
files = {
    'Filedata': ('rBUtImZdJn2Aaj5GAAEeAIUXQEc028.xls', open(file_path, 'rb'), 'application/vnd.ms-excel')
}

data = {
    'siteId': '6787191',
    'sessionId': '3fd411c9-8b33-4c78-93ee-9c8d7a85ddad',
    'type': 'application/vnd.ms-excel',
    'title': '平昌县2024年防汛责任人公示',
    'contentId': '13945499',
    'filePath': '/group3/M00/11/AA/rBUtImZdJn2Aaj5GAAEeAIUXQEc028.xls',
    'fileName': '附件4：平昌县2024年水库防汛责任人名单.xls',
    'id': 'WU_FILE_0',
    'name': 'rBUtImZdJn2Aaj5GAAEeAIUXQEc028.xls',
    'lastModifiedDate': 'Mon Jun 03 2024 14:54:37 GMT+0800 (中国标准时间)',
    'size': '73216'
}

# 发送请求
response = requests.post(url, headers=headers, files=files, data=data, verify=False)

# 打印响应
print(response.text)
