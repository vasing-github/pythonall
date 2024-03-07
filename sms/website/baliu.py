import requests

def baliu(phoneNum):
    url = 'http://www.810086.com.cn/message/'
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Cache-Control':'max-age=0',
        'Content-Length': '82',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://www.810086.com.cn',
        'Upgrade-Insecure-Requests': '1',
        'Cookie':'lg=cn; PbootSystem=do4b697a0tsptb8kdepc6d4qtt',
        'Host':'www.810086.com.cn',
        'Referer':'http://www.810086.com.cn/contact/',

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'}
    r = requests.get(url, headers=headers)
   # data = {name=%E5%BC%A0&tel=18615708288&email=18615708288%40163.com&content=&checkcode=vkru}

    print('baliu结束：',phoneNum,r.text)
    print("\n")
