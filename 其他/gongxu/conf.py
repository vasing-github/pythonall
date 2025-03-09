# 24年的id
# trainplanId= '97624af4fdea4442890d4c257dbe83f2'

# 23年课程id
# trainplanId = 'b34287b27e1142fb9f00d0046e6a9ee9'

def get_year_planid(year):
    if year == '20':
        return 'SC_2f9c3f94-022e-4cdc-a9b8-ea13f9c98955'
    elif year == '21':
        return '27535dc4b3294ec49fe2a0c11f6bf853'
    elif year == '22':
        return 'be50251f5ca649fa9411ae9b7e0e0083'
    elif year == '23':
        return 'b34287b27e1142fb9f00d0046e6a9ee9'
    elif year == '24':
        return '97624af4fdea4442890d4c257dbe83f2'
    elif year == '25':
        return 'b9f7d3f65d2d4d6e8c73ef1e96c7777f'
    elif year == '26':
        return '3fc370eb4a37420fab9fc8951fbfa978'



    elif year == '10':
        return '4f8ff6814938448e8ea6e36933b86e66'
    elif year == '11':
        return 'f67022a48f3b4852b28e2e6656510836'
    elif year == '12':
        return '4a97ca27c56b4441aec5f38931126bbd'
    elif year == '13':
        return 'e669841922334a98bfb4405118d59da2'
    elif year == '14':
        return '4ceeca79e0374c2d9f1e775b3ea264b6'
    elif year == '15':
        return '51ed19a6f9ae49f5aa1e147e10fd41ec'


jessionid = '2FBFE1F6184436312EB4751C84A2FE13'

# 8.23 更新  现在需要去爬每年的plantid，每个课程不一样了
# 8.25 更新 现在专业课也不需要换符号了

cookies = [

    # {'name': 'diyige', 'year': [25],
    #   'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEwMTg0MTk4MTA5MDMwMDZYQDE1MSIsIm1vYmlsZSI6IjE1MjgxODczMzUwIiwidXNlck5hbWUiOiI1MTAxODQxOTgxMDkwMzAwNlgiLCJ1c2VySWQiOiJwMnM4XzIwMWQ2MjIwLTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTc0MTE2NTQ3NCwianRpIjoiNzZlN2YwMjA5ZTQzNDRjN2E1NzFiMDNhYzNhY2YzMWYifQ.qTr4W-tsZt38i3c4r62ID4or4ha__CLq2NVzXI24Lkw'},
    #
    #
    # {'name': 'er', 'year': [25],
    #   'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzMDMwMTk4NjA0MTE2OTQyQDE1MSIsIm1vYmlsZSI6IjE1ODgxODAyNTUwIiwidXNlck5hbWUiOiI1MTMwMzAxOTg2MDQxMTY5NDIiLCJ1c2VySWQiOiJwMXM1XzIwMGU2Mjg0LTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTc0MTE2NDQ0NSwianRpIjoiNTUzZDVjOWYxMDQwNDZjMjhlYzNkNzYzZmEyNDUzNWYifQ.LDzTtO1SeFLjA1NxX3nGKGyhpYJDKKy8k_Pb9zCCZBg'},
    # #
    # #
    # {'name': 'san', 'year': [25],
    #   'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzMDMwMTk3MzEwMjUzODQwQDE1MSIsIm1vYmlsZSI6IjEzNTY4MTgxMDAxIiwidXNlck5hbWUiOiI1MTMwMzAxOTczMTAyNTM4NDAiLCJ1c2VySWQiOiJwMHM2XzFmYTFlNzA4LTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTc0MTE2NTM5NiwianRpIjoiODBiM2Y4NjE5ZjUxNDUyMDg0NjA4MjNjNTI1ZTNkNmMifQ.iAwCtW4D9jy8kShOVhFGCNAWkuiAQN2AE5JSwTVVVhQ'},

    # {'name': 'diyige', 'year': [26],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk4ODA1MTMwMDMyQDE1MSIsIm1vYmlsZSI6IjE4Nzg0MjY4NTQ4IiwidXNlck5hbWUiOiI1MTM3MjMxOTg4MDUxMzAwMzIiLCJ1c2VySWQiOiJjNWU2MTIxNGQ1NjA0OTNjYWE2MDI4NGIzNTdkODMwNyIsImlhdCI6MTc0MTIyMTE4OSwianRpIjoiYTU4NmE5MDM4NjY5NGJkYzk5YzlhYTU5MGUyMjM4NzEifQ.Lu352QcAjQBO9e3Dz7kzF3DP01y5CsLFjt1q7l7FeIM'},

    {'name': 'er', 'year': [25],
     'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzMDMwMTk2ODEwMDgwNjExQDE1MSIsIm1vYmlsZSI6IjEzNDU4MTk2Mjg2IiwidXNlck5hbWUiOiI1MTMwMzAxOTY4MTAwODA2MTEiLCJ1c2VySWQiOiI2ZjhkMTAwNy00MTZhLTQzM2ItODY4MC1mMDhmYjJiMGU5ODciLCJpYXQiOjE3NDEzMDg5MDcsImp0aSI6IjE0OGRjMDE2NWI4NTQyNTI5YzRjODY1NDdhMTFhYjgzIn0.p7jmiQuDa_ri1tZZpSIxL_kYImDIXyh8B00HDa4lgIM'},
    #
]
