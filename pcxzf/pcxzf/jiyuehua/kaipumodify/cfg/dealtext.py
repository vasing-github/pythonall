# -*- coding: utf-8 -*-

import requests
from kaipumodify.cfg import text
from kaipumodify.loginwz import getjsseion
import os

token = text.token
# wait_fix = text.wait_fix
# text_yinsi_num = text.text_yinsi_num
# text_out_num = text.text_out_num
# text_link_use_num = text.text_link_use_num
bz_gov_id = text.bz_gov_id
jid = text.jid




def modify_token(newtoken):
    global token
    token = newtoken


def modify_cookie(new_bz_gov_id, new_jid):
    global bz_gov_id, jid
    bz_gov_id = new_bz_gov_id
    jid = new_jid


def save_data():
    # 构建正确的文件路径
    # 获取脚本所在目录的绝对路径
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 构建 text.py 文件的绝对路径
    file_path = os.path.join(script_dir,  'text.py')

    with open(file_path, 'w') as f:
        f.write('token = \'' + token + '\'\n')
        # f.write('wait_fix = ' + str(wait_fix) + '\n')
        # f.write('text_yinsi_num = ' + str(text_yinsi_num) + '\n')
        # f.write('text_out_num = ' + str(text_out_num) + '\n')
        # f.write('text_link_use_num = ' + str(text_link_use_num) + '\n')
        f.write('bz_gov_id = \'' + bz_gov_id + '\'\n')
        f.write('jid = \'' + jid + '\'\n')


def get_new_token():
    cookies = {
        'HWWAFSESID': '40854762319bc867f7',
        'HWWAFSESTIME': '1703639525975',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': 'Basic dWNhcC1jbG91ZC1uZXdtZWRpYS13ZWItYXBwOnVjYXA=',
        'Connection': 'keep-alive',
        # 'Cookie': 'HWWAFSESID=40854762319bc867f7; HWWAFSESTIME=1703639525975',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'isToken': 'false',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'grant_type': 'custcode',
        'scope': 'server',
        'custCode': '5119230005',
        'custPassWord': 'gPMVQsFEv2EeGOCuhua3ZKEJYtPSYIod94HM341mnctbt6gl72Yl2QvzwUngHgOH4AaWXE1K3MIA1cu02+VpsW7U+2ncYyG8fArt6u9xSm+Zgh+34UfWu3EhMT24MhOVokS2A17Mdnvs6AG6ich2DndAAXd7b0LQvXUUAfV4kGo=',
    }

    response = requests.get('https://datais.ucap.com.cn/auth/oauth/token', params=params, cookies=cookies,
                            headers=headers)

    return response.json()["access_token"]


def jiyue_token():
    print("bz_gov_id token press...........")
    new_bz_gov_id, new_jid = getjsseion.get_new_cookie()
    modify_cookie(new_bz_gov_id, new_jid)
    save_data()
    return new_bz_gov_id, new_jid


def deal_kaipu_token():
    print("get new token ..........")
    new_token = get_new_token()
    modify_token(new_token)
    save_data()
    return new_token


if __name__ == '__main__':
    jiyue_token()