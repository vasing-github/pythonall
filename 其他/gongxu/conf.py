# 24年的id
# trainplanId= '97624af4fdea4442890d4c257dbe83f2'

# 23年课程id
# trainplanId = 'b34287b27e1142fb9f00d0046e6a9ee9'

def get_year_planid(year):
    if year == '22':
        return 'be50251f5ca649fa9411ae9b7e0e0083'
    elif year == '23':
        return 'b34287b27e1142fb9f00d0046e6a9ee9'
    elif year == '24':
        return '6ed7ab2a5e4a42c2b1f950fec0ba1665'

    elif year == '10':
        return '4f8ff6814938448e8ea6e36933b86e66'
    elif year == '11':
        return '5124bf763af34f8c9db8f2e064c3990a'
    elif year == '12':
        return 'e5784e46c9ac4338bf47d904ab101290'
    elif year == '13':
        return '0985ef8ae5494f2eae0a5f8fe5ee18ee'
    elif year == '14':
        return '578c78426b91414096f0f94d26f335e6'


jessionid = '2FBFE1F6184436312EB4751C84A2FE13'


# 8.23 更新  现在需要去爬每年的plantid，每个课程不一样了
# 8.25 更新 现在专业课也不需要换符号了

cookies = [


    # {'name': 'dege', 'year': [14],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEwNzAzMTk4NzAzMTIxMTEwQDE1MSIsIm1vYmlsZSI6IjEzNTE4MzExNDEzIiwidXNlck5hbWUiOiJndWFuZ3RvdSIsInVzZXJJZCI6InAwczNfOWQ1MjBiNzUtYWUwOS00ZGU2LWE4ZmEtYzc3NGJjYWMyZTIxIiwiaWF0IjoxNzI1MTk4NDc4LCJqdGkiOiJlOTA3MmRlZmU3ZTI0MTRkODYxMTQzZTQ2ZmI1MzM5YyJ9.REaKkQtU2v2LnKip-xEjsT72bCBW3uT6QF7EyqLCB8M'},


    {'name': 'guge', 'year': [24],
    'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzMDMwMTk4ODEyMDc4MTE5QDE1MSIsIm1vYmlsZSI6IjE1Nzc1Njk5ODk3IiwidXNlck5hbWUiOiI1MTMwMzAxOTg4MTIwNzgxMTkiLCJ1c2VySWQiOiJwMHMyXzFmNzVhOGQyLTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcyNTE5ODY3NCwianRpIjoiNmRiZTJkOTJlY2Q3NDllOWJlYjFhYzYyMzQyYzIyNDcifQ.LjgyZUAQSNq5r2Mr7Qgz8CuNipsREAVDmFW6nrqbUJA'},

   # {'name': 'guge', 'year': [23],
    # 'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNDIzMTk5ODExMDkwMDIwQDE1MSIsIm1vYmlsZSI6IjE4MjI3NTU2MDUxIiwidXNlck5hbWUiOiIxODIyNzU1NjA1MSIsInVzZXJJZCI6ImYxNzUyMGM2NTM3ODQwOTRhMDhjNjgyYjcyMzI3OWRhIiwiaWF0IjoxNzI0OTQyNzQ3LCJqdGkiOiIwYWZmYTFjZjE5ZmU0MDU5YjdhODQ3ZDEwM2E2YmM3MSJ9.QOjjir5tsMU8tv0DjeZbjmeOiFcx_Hgtp32FkEdEBzE'},


  #    {'name': 'wangli', 'year': [24],
  # 'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEwNzI3MTk5NjEwMjQxNDE4QDE1MSIsIm1vYmlsZSI6IjE1ODg0NjE4MTAwIiwidXNlck5hbWUiOiLpu4TmlododyIsInVzZXJJZCI6IjY3MTM0ZjcyMWMwNDRiNzM4YTRkNWY3OTY0YzRmNjFhIiwiaWF0IjoxNzI0OTIyODUwLCJqdGkiOiI0ZmI3ODE1ZDlhNTk0YjExOWRkYjhiNzY3MTc1YzJhYSJ9.hLiYMRCGG9WhULRqH3C-USZnW8mqGqg-Y73v3KYZTL4'},

     # {'name': 'wenjing', 'year': [24],
     #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEwNzI3MTk5NDA5MTMwODIwQDE1MSIsIm1vYmlsZSI6IjE4MjgxNjIwNjEyIiwidXNlck5hbWUiOiLmlofpnZlXSiIsInVzZXJJZCI6ImZmNmEzMjE0NDQwNDQwMGM5MjVhYmY3NWYyYzhiOTQxIiwiaWF0IjoxNzI0OTc4NTY5LCJqdGkiOiJlMmM3MGI0ZmM2YjY0ZDdjYTQ5MDVlYmJkOTMxY2E3OSJ9.2-qQrryLmEHY-Oz9TFxcJDyrTSRskX9Z_RGVsFNG7ME'},


]


