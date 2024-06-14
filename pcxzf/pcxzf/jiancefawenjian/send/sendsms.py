import pymysql
import requests
from urllib.parse import quote

from jiancefawenjian import conf


def send_sms(login_name, password, fee_type, mobile, content, sign_name, timing_date=None, ext_code=None):
    base_url = "https://dxsdk.028lk.com:8082/Api/SendSms"

    # URL编码content和sign_name
    content_encoded = quote(content.encode('utf-8'))
    sign_name_encoded = quote(sign_name.encode('utf-8'))

    # 构建请求URL
    url = f"{base_url}?LoginName={login_name}&Pwd={password}&FeeType={fee_type}&Mobile={mobile}&Content={content_encoded}&SignName={sign_name_encoded}"

    # 如果有定时发送的时间或者扩展号，加入到URL中
    if timing_date:
        url += f"&TimingDate={timing_date}"
    if ext_code:
        url += f"&ExtCode={ext_code}"

    # 发送请求
    response = requests.get(url)

    return response.text


def sendsmsmethod(res):
    for row in res:
        print(row[0],row[1])
        sendmsg(row[0], row[1], )



def sendmsg(comp,score):

    login_name = "DSC2610021"
    password = "pc@2023"
    fee_type = "2"
    mobile = "17311067255"
    phont_list = conf.bumen_phone.get(comp)

    content = f"{comp}，你单位本周政务公开考核扣{abs(score)}分，请及时进入数字平昌政务微信或登录数字平昌综合治理后台处理。"
    sign_name = "【平政哨兵】"
    if phont_list != None:
        for phone in phont_list:
            mobile = phone[0]
            # 发送短信
            result = send_sms(login_name, password, fee_type, mobile, content, sign_name)
            print(result)


def sendtest():
    connection = pymysql.connect(**conf.database)
    cursor = connection.cursor()
    sql = """
                SELECT company_name, SUM(score) AS total_score
                FROM assessment_record
                WHERE date = '2024-5-20'
                GROUP BY company_name;
                """
    cursor.execute(sql)
    # 获取查询结果
    result = cursor.fetchall()

    sendsmsmethod(result)
    cursor.close()
    connection.close()


if __name__ == '__main__':
    # 调用函数
    sendtest()
