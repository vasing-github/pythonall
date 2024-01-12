import pymysql

def create_connection():
    """创建并返回一个连接对象和游标对象。"""

    # 创建连接
    connection = pymysql.connect(
        host='yuxiaohaishidalao.shop',
        user='root',
        password='vas9624..',
        database='smartpc'
    )

    # 创建一个游标对象
    cursor = connection.cursor()

    return connection, cursor

def execute_query(connection, cursor, sql, params=None):
    """使用游标执行查询语句，并返回查询结果。"""

    # 执行查询语句
    cursor.execute(sql, params)

    # 获取查询结果
    result = cursor.fetchall()

    return result


def update_data(connection, cursor, sql, params=None):
    """使用游标执行更新语句。"""

    # 执行更新语句
    cursor.execute(sql, params)

    # 提交更新
    connection.commit()


def close_connection(connection, cursor):
    """关闭一个连接对象和游标对象。"""

    # 关闭游标对象
    cursor.close()

    # 归还连接对象到连接池
    connection.close()


if __name__ == '__main__':
    # 创建连接对象和游标对象
    connection, cursor = create_connection()

    # 执行查询语句，获取数据
    # result = execute_query(connection, cursor, "SELECT * FROM recordsth WHERE recordname = 'kaipuyun'")
    # print(result)
    # # 将查询到的数据与您现有的数据进行比较
    # if result[0][1] != 200:
    #     # 执行更新语句，更新数据
    #     update_data(connection, cursor, "UPDATE recordsth SET num_int = 200 WHERE recordname = 'kaipuyun'")
    # result = execute_query(connection, cursor, "SELECT * FROM recordsth WHERE recordname = 'kaipuyun'")
    # print(result)
    # 关闭连接对象和游标对象

    update_data(connection, cursor, "UPDATE recordsth SET num_int = 0 WHERE recordname = 'kaipuyun'")
    close_connection(connection, cursor)




