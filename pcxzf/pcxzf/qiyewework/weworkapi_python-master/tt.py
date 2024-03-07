# -*- coding: utf-8 -*-
from wechat_enterprise import WechatEnterprise

we = WechatEnterprise(
    corpid="wwfe9cad0f2c6a4eca",  # 企业 ID
    appid="1000002",  # 企业应用 ID
    corpsecret="oTt-Tn7GQlcDbGjR1YnFyyD5PWFpQ4Yq2H57lzpe4UU",  # 企业应用 Secret
)

receivers = ["WuXiaoLong", "vasing2"]
# 发送 文本
we.send_text("来息 somenzz 的消息", receivers)
# 发送 Markdown
we.send_markdown("# Markdown", receivers)
# 发送图片
# we.send_image("/Users/aaron/Downloads/images.jpeg", receivers)
# # 发送文件
we.send_file("./README.md", receivers)