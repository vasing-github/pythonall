import base64
import json
from kaipumodify.cfg import conf
import requests
import os
def hello():
    print('hello')
def getindex():
    # 请求的URL
    url = 'http://10.15.3.133/authenticate/login'

    # 请求头部
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }

    # 发送请求
    response = requests.get(url, headers=headers, verify=False)

    # 获取cookie中的authenticatecenterjsessionid
    cookie_jessionid = response.cookies.get('authenticatecenterjsessionid')

    # 输出authenticatecenterjsessionid
    print(f'authenticatecenterjsessionid: {cookie_jessionid}')
    return cookie_jessionid


def getcode(jid):
    # 请求的URL
    url = 'http://10.15.3.133/authenticate/login/getCode'

    # 请求头部
    headers = {
        'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'authenticatecenterjsessionid=' + jid,
        'Referer': 'http://10.15.3.133/authenticate/login',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }

    # 发送GET请求
    response = requests.get(url, headers=headers, verify=False)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 构建 text.py 文件的绝对路径
    file_path = os.path.join(script_dir,  'verify_code.png')

    # 将验证码图片保存到本地文件
    with open(file_path, 'wb') as f:
        f.write(response.content)

    print('验证码图片已保存为 verify_code.png')


def getjsessionid2(jid, code):
    # 登录请求的URL
    cookies = {
        'rememberUID': '0',
        'username': '',
        'authenticatecenterjsessionid': jid,
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'rememberUID=0; username=; authenticatecenterjsessionid=MWM4ODg2NDYtYmM4NC00ZDhmLTliMWQtODk3YTMyOTY0ZjZi',
        'Origin': 'http://10.15.3.133',
        'Referer': 'http://10.15.3.133/authenticate/login',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'IsAjax': '1',
        'dataType': 'JSON',
        '_': '0.24409118044898892',
    }

    data = {
        'username': conf.jiyuehua_user,
        'password': conf.jiyuehua_password,
        'code': code,
        'isEncryption': 'true',
    }

    response = requests.post(
        'http://10.15.3.133/authenticate/loginPost',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )
    # 从响应中获取cookie
    cookies = response.cookies.get_dict()

    # 打印authenticatecenterjsessionid
    print(f'authenticatecenterjsessionid: {cookies.get("authenticatecenterjsessionid")}')
    return cookies.get("authenticatecenterjsessionid")


def getloginurl(jid):
    cookies = {
        'rememberUID': '0',
        'username': '',
        'authenticatecenterjsessionid': jid,
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'rememberUID=0; username=; authenticatecenterjsessionid=NGJiM2JiY2YtMTI0MS00ODczLWJkYWEtYmVjZDk3OTc2YmUz',
        'Origin': 'http://10.15.3.133',
        'Referer': 'http://10.15.3.133/authenticate/index',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'IsAjax': '1',
        'dataType': 'JSON',
        '_': '0.6624885375774627',
    }

    data = {
        'type': 'cms',
    }

    response = requests.post(
        'http://10.15.3.133/authenticate/loginForType',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )

    # 打印响应内容
    print(response.json()['data'])
    return response.json()['data']


def get_finaly_code(url, jid):
    # 创建一个Session对象
    session = requests.Session()

    # 设置初始cookies
    session.cookies.set('authenticatecenterjsessionid', jid, domain='10.15.3.133')

    # 设置请求头部
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'http://10.15.3.133/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    }

    # 发送GET请求
    response = session.get(url, headers=headers, verify=False)

    # 从响应中获取cookie
    cookies = session.cookies.get_dict()

    # 打印bz_govc_SHIROJSESSIONID
    print(f'bz_govb_SHIROJSESSIONID: {cookies.get(conf.jiyuehua_bzgov_shriojid)}')
    return cookies.get(conf.jiyuehua_bzgov_shriojid)


def base64_api(img):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": 'vasing', "password": 'vas9624', "typeid": 3, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

def get_new_cookie():
    jid = getindex()
    getcode(jid)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建 text.py 文件的绝对路径
    file_path = os.path.join(script_dir,  'verify_code.png')
    code = base64_api(file_path)
    print("识别的验证码为：", code)
    new_jid = getjsessionid2(jid, code)
    url = getloginurl(new_jid)
    bz_gov_id = get_finaly_code(url, new_jid)
    return bz_gov_id, new_jid


if __name__ == '__main__':
    jid = getindex()
    getcode(jid)
    code = base64_api('verify_code.png')
    print("识别的验证码为：", code)
    new_jid = getjsessionid2(jid, code)
    url = getloginurl(new_jid)
    a_id = get_finaly_code(url, new_jid)
