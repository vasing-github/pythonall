from bs4 import BeautifulSoup
import requests
import json
import datetime


def getTime(prox,menu):
    if not menu.startswith('http'):
        menu = 'http://www.scpc.gov.cn' + menu

    data = {}
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    response = requests.get(menu, headers=headers, data=data,proxies=prox)

    # 以 Beautiful Soup 解析 HTML 程序码
    soup = BeautifulSoup(response.text, 'html.parser')
    li_elements = soup.find_all('li', {'class': 'rq'})
    print(li_elements)
    if len(li_elements) ==1:
        return '无'
    second_li_element = li_elements[1]

    return second_li_element.text

if __name__ == '__main__':
    import requests

    # 你的webhook URL
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=425a53f6-696e-46c1-9d4a-fae8940b136f&debug=1"

    # 你的文件路径
    filename = 'msg.txt'

    # 读取文件内容
    with open(filename, 'rb') as f:
        file_content = f.read()

    # 准备文件数据
    files = {'file': (filename, file_content)}

    # 发送文件
    response = requests.post(url, files=files)

    # 检查响应
    if response.status_code == 200:
        print("文件已成功发送！")
        print(response.text)
    else:
        print(f"发送文件时出错，状态码：{response.status_code}")
