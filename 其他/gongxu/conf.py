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
        return 'b34287b27e1142fb9f00d0046e6a9ee9'
    elif year == '24':
        return '97624af4fdea4442890d4c257dbe83f2'
    elif year == '20':
        return '1d53989388a4433f9f4ed1805979261b'


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

    {'name': '第一个', 'year': [20,21,22,23,24],
     'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIxMTk4OTA3MDkyNzI0QDE1MSIsIm1vYmlsZSI6IjEzMzIwNjEzNjc3IiwidXNlck5hbWUiOiJ3YW5nbGkxMDAzNjUiLCJ1c2VySWQiOiJwMHM4XzhlODk5NDkwLTY0OTItNGRkNy05NTliLTgzOGNiZjFiOGU1NyIsImlhdCI6MTcyNzIzNzUyMSwianRpIjoiMDM0MDAxOTk1MDUxNGUxOTkwOWVmOTQ4YTg2NjYzNTcifQ.VvaWdi1gqGtVsWz7hMtGSdWvupt4TKyOkVAEB18_IYk'},

    # {'name': '陈陆军', 'year': [24],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNDM0MTk4NTEwMDMzNDIyQDE1MSIsIm1vYmlsZSI6IjEzNTU4NTY1MTc1IiwidXNlck5hbWUiOiI1MTM0MzQxOTg1MTAwMzM0MjIiLCJ1c2VySWQiOiJwMnM3XzIyZjgyODM2LTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcyNzE3NjU2OSwianRpIjoiMDY2NjYxYzg1M2VlNDE0NDg1NDljZWQ3MmUxZGE1OWEifQ.i6_fU42tu4dKedTHqiQKrJ-evT-nyHneUxBgzJ1Q-N4'},
    #
    # {'name': '王菊', 'year': [24],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTExMTIzMTk4MDAxMjc1MDEyQDE1MSIsIm1vYmlsZSI6IjEzODgxNjYxMDY3IiwidXNlck5hbWUiOiI1MTExMjMxOTgwMDEyNzUwMTIiLCJ1c2VySWQiOiJwMnM4XzI0OWE4YzYwLTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcyNzE3NjY5NSwianRpIjoiZjhiNDQwZGUyNDhiNDI0M2I3MzliZDA4MTA5NzM4YmUifQ.ENWBSLe-_STCwmNX7d5zCW6QIJpZqxNO3hVx17p358w'},

    #  {'name': '核武', 'year': [21,22,23,24],
    # 'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEwNzI3MTk4OTA3MTUwMDEwQDE1MSIsIm1vYmlsZSI6IjEzNTQ4NDE0OTM0IiwidXNlck5hbWUiOiJodzEyMzQ0IiwidXNlcklkIjoiOGNkZDZhZmQ0NmU5NDUwNjgyNzM4NmZkNTRmY2JkZjUiLCJpYXQiOjE3MjUzMjYyNDIsImp0aSI6ImY5N2RiNTNjNmNhYTQ1MTNiMDUwMzdmMWZkY2I4ZDJiIn0.alKSppsxjJGO8E0xqKE-9ni-6csH4XiZ_oELe9-n1LA'},

]


