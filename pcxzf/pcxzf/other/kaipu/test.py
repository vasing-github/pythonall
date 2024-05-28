import uuid
from datetime import datetime


def generate_random_strings(n):
    """
    生成 n 个随机的 UUID 字符串。

    :param n: 要生成的字符串数量
    :return: 包含 n 个随机字符串的列表
    """
    random_strings = [str(uuid.uuid4()) for _ in range(n)]
    return random_strings

print(str(uuid.uuid4()))
endDate = datetime.now()
print(endDate)