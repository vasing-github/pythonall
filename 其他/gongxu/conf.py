# 24年的id
# trainplanId= '97624af4fdea4442890d4c257dbe83f2'

# 23年课程id
# trainplanId = 'b34287b27e1142fb9f00d0046e6a9ee9'

def get_year_planid(year):
    if year == 22:
        return 'be50251f5ca649fa9411ae9b7e0e0083'
    elif year == 23:
        return 'b34287b27e1142fb9f00d0046e6a9ee9'
    elif year == 24:
        return '578c78426b91414096f0f94d26f335e6'

    elif year == 10:
        return '4f8ff6814938448e8ea6e36933b86e66'
    elif year == 11:
        return '578c78426b91414096f0f94d26f335e6'
    elif year == 12:
        return '578c78426b91414096f0f94d26f335e6'


jessionid = '2FBFE1F6184436312EB4751C84A2FE13'


# 8.23 更新  现在需要去爬每年的plantid，每个课程不一样了
# 8.25 更新 现在专业课也不需要换符号了

cookies = [


    # {'name': 'edge', 'year': [22],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzMDI3MTk3MjEwMTc1ODI0QDE1MSIsIm1vYmlsZSI6IjE4MDkwMjA5OTc2IiwidXNlck5hbWUiOiI1MTMwMjcxOTcyMTAxNzU4MjQiLCJ1c2VySWQiOiJwMXMzXzI1YzViNjc4LTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcyNDk3ODk5NywianRpIjoiM2QwMTNjZDI2MGEwNDEzNTk4MjIyOTkwOTU4ZDYzZjUifQ.qxgkwCk1wVF2rnccHa6GsD6-LhMsf3csbx5H9_njegM'},


    {'name': 'guge', 'year': [10],
    'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzMDI4MTk3ODEyMjM3NjU0QDE1MSIsIm1vYmlsZSI6IjE1OTgyNzkwMDg4IiwidXNlck5hbWUiOiI1MTMwMjgxOTc4MTIyMzc2NTQiLCJ1c2VySWQiOiJwMXM4XzIyYmUzNGJlLTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcyNTAxNTk3OSwianRpIjoiOWFhNTM5OTI5NDYyNDE2ZGE0ZjA1NzhlOTE1NjE5YmEifQ.Gb7J65Ye1McfpW0n5nrmN5aotFVM_ZtFXo9d1g2nlDU'},

   # {'name': 'guge', 'year': [23],
    # 'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNDIzMTk5ODExMDkwMDIwQDE1MSIsIm1vYmlsZSI6IjE4MjI3NTU2MDUxIiwidXNlck5hbWUiOiIxODIyNzU1NjA1MSIsInVzZXJJZCI6ImYxNzUyMGM2NTM3ODQwOTRhMDhjNjgyYjcyMzI3OWRhIiwiaWF0IjoxNzI0OTQyNzQ3LCJqdGkiOiIwYWZmYTFjZjE5ZmU0MDU5YjdhODQ3ZDEwM2E2YmM3MSJ9.QOjjir5tsMU8tv0DjeZbjmeOiFcx_Hgtp32FkEdEBzE'},


  #    {'name': 'wangli', 'year': [24],
  # 'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEwNzI3MTk5NjEwMjQxNDE4QDE1MSIsIm1vYmlsZSI6IjE1ODg0NjE4MTAwIiwidXNlck5hbWUiOiLpu4TmlododyIsInVzZXJJZCI6IjY3MTM0ZjcyMWMwNDRiNzM4YTRkNWY3OTY0YzRmNjFhIiwiaWF0IjoxNzI0OTIyODUwLCJqdGkiOiI0ZmI3ODE1ZDlhNTk0YjExOWRkYjhiNzY3MTc1YzJhYSJ9.hLiYMRCGG9WhULRqH3C-USZnW8mqGqg-Y73v3KYZTL4'},

     # {'name': 'wenjing', 'year': [24],
     #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEwNzI3MTk5NDA5MTMwODIwQDE1MSIsIm1vYmlsZSI6IjE4MjgxNjIwNjEyIiwidXNlck5hbWUiOiLmlofpnZlXSiIsInVzZXJJZCI6ImZmNmEzMjE0NDQwNDQwMGM5MjVhYmY3NWYyYzhiOTQxIiwiaWF0IjoxNzI0OTc4NTY5LCJqdGkiOiJlMmM3MGI0ZmM2YjY0ZDdjYTQ5MDVlYmJkOTMxY2E3OSJ9.2-qQrryLmEHY-Oz9TFxcJDyrTSRskX9Z_RGVsFNG7ME'},


]
