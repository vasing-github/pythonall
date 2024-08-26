# 24年的id
# trainplanId= '97624af4fdea4442890d4c257dbe83f2'

# 23年课程id
# trainplanId = 'b34287b27e1142fb9f00d0046e6a9ee9'

def get_year_planid(year):
    if year == 23:
        return 'b34287b27e1142fb9f00d0046e6a9ee9'
    elif year == 24:
        return '0bfc0819d26944b19d29b70197efedff'

jessionid = '2FBFE1F6184436312EB4751C84A2FE13'


# 8.23 更新  现在需要去爬每年的plantid，每个课程不一样了
# 8.25 更新 现在专业课也不需要换符号了

cookies = [

    {'name': '24年', 'year': [24],
     'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk5NTA2MDU3NjQyQDE0NyIsIm1vYmlsZSI6IjE3ODA4MzI0NjE4IiwidXNlck5hbWUiOiJMRDE3ODA4MzI0NjE4IiwidXNlcklkIjoiMTBkNjMxMTUxM2FmNDc5YTg1ZTg3NGRmOGY0YmJiYzgiLCJpYXQiOjE3MjQ1Nzk1NzksImp0aSI6ImZmNzQ1ZGY0MWE1YTRkZGI4ZDU3ZjFjOTExMWQ4NDYwIn0.QDjN3rWXeKdkmdkeFYs6s9E3rMarAryUo_zrD0gyBV8'},

    {'name': '第二个', 'year': [24],
     'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNDYwMDAzMTk5MzA4MTQ3NjM4QDE0NyIsIm1vYmlsZSI6IjE1Mjk4MDkwMDE3IiwidXNlck5hbWUiOiLpmYjkupXmj7RjankiLCJ1c2VySWQiOiJhMWUyOWViNDVhYmU0NjI2OThlNWIzMDdmNGQ3ODgwOSIsImlhdCI6MTcyNDU4MDE2OSwianRpIjoiNjMzMmQ2NzFlNDJkNDBiMzgyY2E1YzExYTQ5YmI2ZDkifQ.U6cqEPpF5PyazZKaeBsbeuDxao7-1YkokgbTYc0XMMo'},

]
