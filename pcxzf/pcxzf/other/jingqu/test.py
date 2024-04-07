import requests
from bs4 import BeautifulSoup
import os

# 网页的URL
url = 'http://www.pcbygz.com/#'

# 发送GET请求获取网页内容
response = requests.get(url)

# 创建一个目录来保存网页和相关文件
os.makedirs('website', exist_ok=True)

# 检查请求是否成功
if response.status_code == 200:
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 保存HTML源代码
    with open('website/index.html', 'w', encoding='utf-8') as file:
        file.write(response.text)

    # 查找并下载所有CSS文件
    for link in soup.find_all('link', {'rel': 'stylesheet'}):
        href = link.get('href')
        if href:
            css_response = requests.get(href)
            if css_response.status_code == 200:
                css_path = os.path.join('website', os.path.basename(href))
                with open(css_path, 'w', encoding='utf-8') as file:
                    file.write(css_response.text)

    # 查找并下载所有JS文件
    for script in soup.find_all('script'):
        src = script.get('src')
        if src:
            js_response = requests.get(src)
            if js_response.status_code == 200:
                js_path = os.path.join('website', os.path.basename(src))
                with open(js_path, 'w', encoding='utf-8') as file:
                    file.write(js_response.text)

    print('网页和相关文件已成功保存到website目录')
else:
    print(f'获取网页失败，状态码：{response.status_code}')
