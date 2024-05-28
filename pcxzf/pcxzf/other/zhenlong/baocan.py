import requests

# 机器人的Webhook地址
webhook_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=c3077605-b89f-42dc-aafc-07b53e03ff89'

# 要发送的消息内容
message = {
    "msgtype": "text",
    "text": {
        "content": "温馨提示：请各位同事，按时按需报餐，谢谢！"
    }
}

# 发送POST请求
response = requests.post(webhook_url, json=message)

# 检查响应状态码
if response.status_code == 200:
    print("消息发送成功！")
else:
    print(f"消息发送失败，状态码：{response.status_code}")
