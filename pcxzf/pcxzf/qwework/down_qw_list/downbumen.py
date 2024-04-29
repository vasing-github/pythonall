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
    save_token(token)
    return token

def save_token(token):
    with open('conf2.py', 'w') as f:
        f.write('access_token = \'' + token + '\'\n')


def get_department(tk):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token='+tk
    response = requests.get(url, )
    print(response.text)
    print(response.json())
    if response.json()["errcode"] == 42001:
        tk = get_access_token()
        return get_department(tk)
    return response.json()["department"]
def insert_department():
    departmen = get_department(conf2.access_token)

    db = pymysql.connect(**conf.database)
    # 创建一个游标对象
    cursor = db.cursor()
    # 构造SQL语句
    values = ', '.join([
        f"({item['id']}, '{item['name']}', {item['parentid']}, {item['order']}, '{','.join(item['department_leader'])}')"
        for item in departmen])
    sql = f"""
        INSERT INTO pc_department (id, name, parentid, order_num, department_leader) 
        VALUES {values} 
        ON DUPLICATE KEY UPDATE 
        name=VALUES(name), parentid=VALUES(parentid), order_num=VALUES(order_num), department_leader=VALUES(department_leader)
        """
    print(sql)
    # 执行SQL语句
    try:
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except pymysql.err.IntegrityError as e:
        print("IntegrityError:", e)
    except Exception as e:
        print("An error occurred:", e)

    # 关闭数据库连接
    db.close()
def insert_user():
    # 连接数据库
    db = pymysql.connect(**conf.database)

    # 创建一个游标对象
    cursor = db.cursor()

    # 构造SQL语句
    sql = "SELECT id FROM pc_department"

    # 执行SQL语句
    cursor.execute(sql)

    # 获取所有返回的行
    rows = cursor.fetchall()

    # 提取所有的部门id
    department_ids = [row[0] for row in rows]

    # 打印所有的部门id
    for id in department_ids:
        if id < 5751:
            continue
        if id == 5752:  #临时分组
            continue
        print(id)
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/list?access_token=' + conf2.access_token + '&department_id=' + str(id) + '&fetch_child=0'

        response = requests.get(url)
        user_list = response.json()['userlist']
        if not user_list:
            continue
        else:
            values = ', '.join([
                f"('{item['userid']}', '{item['name']}', '{','.join(map(str, item['department']))}', '{item['position']}', {item['status']}, {item['main_department']})"
                for item in user_list
            ])
            sql = f"""
                    INSERT INTO pc_qw_user (userid, name, department, position, status, main_department) 
                    VALUES {values} 
                    ON DUPLICATE KEY UPDATE 
                    name=VALUES(name), department=VALUES(department), position=VALUES(position), status=VALUES(status), main_department=VALUES(main_department)
                """
            # 执行SQL语句
            try:
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except pymysql.err.IntegrityError as e:
                print("IntegrityError:", e)
            except Exception as e:
                print("An error occurred:", e)

    # 关闭数据库连接
    db.close()

def test_inser_user():
    members = [{"name":"谭思敏","department":[2572],"position":"副股长","status":1,"enable":1,"isleader":1,"extattr":{"attrs":[]},"hide_mobile":0,"telephone":"","order":[0],"external_profile":{"external_attr":[],"external_corp_name":"","wechat_channels":{"nickname":"平昌发布","status":0}},"main_department":2572,"alias":"","is_leader_in_dept":[1],"userid":"tXiaoYu","direct_leader":[]}]
    for me in members:
        print(me['userid'])

    db = pymysql.connect(**conf.database)

    # 创建一个游标对象
    cursor = db.cursor()
    values = ', '.join([
        f"('{item['userid']}', '{item['name']}', '{','.join(map(str, item['department']))}', '{item['position']}', {item['status']}, {item['main_department']})"
        for item in members
    ])
    sql = f"""
        INSERT INTO pc_qw_user (userid, name, department, position, status, main_department)
        VALUES {values}
        ON DUPLICATE KEY UPDATE
        name=VALUES(name), department=VALUES(department), position=VALUES(position), status=VALUES(status), main_department=VALUES(main_department)
    """
    # 执行SQL语句
    try:
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except pymysql.err.IntegrityError as e:
        print("IntegrityError:", e)
    except Exception as e:
        print("An error occurred:", e)

    db.close()


if __name__ == '__main__':
    # get_access_token()
    insert_user()
    # test_inser_user()
