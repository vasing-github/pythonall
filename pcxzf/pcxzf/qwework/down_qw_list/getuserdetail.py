# -*- coding: utf-8 -*-

import conf
import conf2
import requests
import pymysql

def get_access_token():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + conf.qy_id + '&corpsecret=' + conf.secret_szpc
    response = requests.get(url, )
    print(response.text)
    token = response.json()['access_token']
    # token = 'Bi0-HT5bwQFmGp57jKjnHQa7hRotK4jIJf5eO3HIT1-gOZsX-8FYItzhKFErA4vAbLW4QUaP_UDPE37B6dY3Rt-3fWwzzr0Wp3imB8XghqMJOBGGHwZL16Kesjm9wQNYUgEl8rmFeklyPEt2DyIcCLv08wWSBn6ppUPN-1gzZxHCtFDbzezRnwZzKhvOROcaMnTYXBeYYjVZQuePoVr6mw'
    save_token(token)
    return token

def save_token(token):
    with open('conf2.py', 'w') as f:
        f.write('access_token = \'' + token + '\'\n')


def get_user_detail(tk):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/auth/getuserdetail?access_token='+tk
    data= {
        # 'access_token': tk,
        'user_ticket': 'yPdgIOidIkbQHPc3u5aC0ucU1b_fSa3t_d4qhwB4rP9L_eqpSk2OYMNZSXomeNrup2yy7b5ffxRmYk0uEyyeNkUs_Vc2-xQrb-up2Y70ptY',
    }
    response = requests.post(url, json=data)
    print(response.text)
    print(response.json())



if __name__ == '__main__':
    # get_access_token()
    tk = 'K4AxYszwU49gnvFWC1i_REQ4elcGO37uaFNDhMl4Tzmv9mhRCc_FopwD2UMDngsicUSPa_OCx0SKXaoZv-DE9dZ1etoLEbpjBazicEgapk9Q1_k8XGhWE_DFrsO_o4ZJ_ZfjvoTsDF6AZg9olCMR7WcPlosV-IbqKwQR22zSs9mkXhrR2ZxVanOOPRdSKCie5cPPM08LDjsiAMRjycwsig'
    get_user_detail(tk)
    # test_inser_user()
