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
        'user_ticket': 'Y1vdkx4En8um9i5UjCdADSl48KIFoUllRhgBUBGSP-zSaWPCijJJBeDRLxNtTRjAQy4603xkCZU7uOjB27JKcpv-aUYoPb3ea8C4-5dNBUE',
    }
    response = requests.post(url, json=data)
    print(response.text)
    print(response.json())




if __name__ == '__main__':
    # get_access_token()
    tk = '3bfs1ajknrBOwPFQHY0qz4ktqah06zYotrJxCaVobYcUID9gxEXN_TBEzV5ESnwo_iX98XJFy7VOvG60ISvHdoD-8STw_PzvNvdjbPNOnaBdOUhakpGyZOD6EuzMKGqK5lXuQe8dhEM6aC_sgVV7OsfZCk13bGgxrhjeSJ2_8d8xL6tkEEhhmDCrFvRuyiSMInwmT6H7d4EP5mgUZuWAgw'
    get_user_detail(tk)
    # test_inser_user()
