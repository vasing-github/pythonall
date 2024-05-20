import requests
from urllib.parse import quote


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


if __name__ == '__main__':
    # 调用函数
    login_name = "DSC2610021"
    password = "pc@2023"
    fee_type = "2"
    mobile = "17311067255"
    content = "平昌县医保局，你单位本月政务公开考核扣9分，请及时处理。"
    sign_name = "【数字平昌】"

    # 发送短信
    result = send_sms(login_name, password, fee_type, mobile, content, sign_name)
    print(result)
