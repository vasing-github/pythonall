# -*- coding: utf-8 -*-
import random
import string

def generate_random_string(length):
    # 定义所有可能的字符，包括大写字母、小写字母和数字
    all_chars = string.ascii_letters + string.digits
    # 使用random.choices随机选择字符，然后使用join连接成一个字符串
    random_string = ''.join(random.choices(all_chars, k=length))
    return random_string

# 生成长度为20的随机字符串
random_string = generate_random_string(20)
print(random_string)
