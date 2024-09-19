# 24年的id
# trainplanId= '97624af4fdea4442890d4c257dbe83f2'

# 23年课程id
# trainplanId = 'b34287b27e1142fb9f00d0046e6a9ee9'

def get_year_planid(year):
    if year == '21':
        return '27535dc4b3294ec49fe2a0c11f6bf853'
    elif year == '22':
        return 'be50251f5ca649fa9411ae9b7e0e0083'
    elif year == '23':
        return '429db59ff85d4cf4935c1f5b5f3f34c8'
    elif year == '24':
        return '6ed7ab2a5e4a42c2b1f950fec0ba1665'
    elif year == '25':
        return '6ed7ab2a5e4a42c2b1f950fec0ba1665'


    elif year == '10':
        return '4f8ff6814938448e8ea6e36933b86e66'
    elif year == '11':
        return 'd0af473b813a47758e0a4fffb7053517'
    elif year == '12':
        return 'f2c16584e5ef40b5821250309dd9238a'
    elif year == '13':
        return '03834387382247f991819b6a610d217d'
    elif year == '14':
        return '578c78426b91414096f0f94d26f335e6'


jessionid = '2FBFE1F6184436312EB4751C84A2FE13'

# 8.23 更新  现在需要去爬每年的plantid，每个课程不一样了
# 8.25 更新 现在专业课也不需要换符号了

cookies = [

    # {'name': '唐志鹏', 'year': [21,22,23,24],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEwMTI1MTk5MjEyMDMwMDExQDE1MSIsIm1vYmlsZSI6IjE4MjI4ODUyMjk5IiwidXNlck5hbWUiOiJ0enAxMjM0IiwidXNlcklkIjoiMmU5YTIyYmVlMzg1NDkyMGIwMDNiMjhlNjdiYmU0YzkiLCJpYXQiOjE3MjUzMjU5MDUsImp0aSI6IjE2MWEyYTFhZjc1YTRiNzA4ZmNhYmRkYjVmNjk2ZjFiIn0.cWVrwzRAc9LjJJPAdxVkEXFKpBaxm48c_YqyNpVXcb0'},
    #
    #
    {'name': '陈陆军', 'year': [13],
     'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzAxMTk5ODA4MTcwNzE0QDE1MSIsIm1vYmlsZSI6IjE3ODgzMjk4MjAzIiwidXNlck5hbWUiOiJuaWRlcGVuZ3lvdWFuZGVsaWUiLCJ1c2VySWQiOiJjMzZkYTM4NGJjMmI0NzFlOGE4N2Q3YWM1NmJhYTk5NSIsImlhdCI6MTcyNjY0MDQwMCwianRpIjoiN2JiYTI3MTk4N2FhNDhlNWJmYmE2YzFiNjYwOGRiYTcifQ._qPYZL7JCjaZmkUAl-leagkV4qKtzmXSk7Tqf3OlXh4'},

    # {'name': '王菊', 'year': [24],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTExMDIyMTk3MTA5MjUwMDQ4QDE1MSIsIm1vYmlsZSI6IjE1MjgyMjIxMTkzIiwidXNlck5hbWUiOiI1MTEwMjIxOTcxMDkyNTAwNDgiLCJ1c2VySWQiOiJwMHMxX2Y0MjVkNmQ4LTIxNTMtNDJmMi1hNWUwLTlmYmQxYmE1ZWUzOCIsImlhdCI6MTcyNjYyNzA0NywianRpIjoiM2M4NGU0Y2Y4Y2ExNGE2Yjk0Mzg4Y2Q0ZjFlNWQ0YzQifQ.rd41dUAB8B_tffHJjPEEqEuGU-HXpwySTNLl1Jhuur8'},

    #  {'name': '核武', 'year': [21,22,23,24],
    # 'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEwNzI3MTk4OTA3MTUwMDEwQDE1MSIsIm1vYmlsZSI6IjEzNTQ4NDE0OTM0IiwidXNlck5hbWUiOiJodzEyMzQ0IiwidXNlcklkIjoiOGNkZDZhZmQ0NmU5NDUwNjgyNzM4NmZkNTRmY2JkZjUiLCJpYXQiOjE3MjUzMjYyNDIsImp0aSI6ImY5N2RiNTNjNmNhYTQ1MTNiMDUwMzdmMWZkY2I4ZDJiIn0.alKSppsxjJGO8E0xqKE-9ni-6csH4XiZ_oELe9-n1LA'},

]
