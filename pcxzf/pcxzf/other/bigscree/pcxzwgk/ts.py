# -*- coding: utf-8 -*-
import asyncio
from datetime import datetime

# 获取事件循环对象
loop = asyncio.get_running_loop()

# 获取当前的UTC时间
now = datetime.utcnow()

# 将秒数转换为UTC时间的datetime对象
dt = datetime.fromtimestamp(loop.time(), tz=datetime.timezone.utc)

# 将datetime对象格式化为字符串
s = dt.strftime("%Y-%m-%d %H:%M:%S.%f")
print(s)
print(now)
