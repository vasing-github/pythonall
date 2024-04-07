from datetime import datetime, timedelta

# 获取当前的日期和时间
now = datetime.now()

# 计算一周的开始和结束时间
start_week = now - timedelta(days=now.weekday(), hours=now.hour, minutes=now.minute, seconds=now.second, microseconds=now.microsecond)
end_week = start_week + timedelta(days=6, hours=23, minutes=59, seconds=59)

print("start_week", start_week)
print('end_week', end_week)