# 24年的id
# trainplanId= '97624af4fdea4442890d4c257dbe83f2'

# 23年课程id
# trainplanId = 'b34287b27e1142fb9f00d0046e6a9ee9'

def get_year_planid(year):
    if year == '20':
        return 'SC_2f9c3f94-022e-4cdc-a9b8-ea13f9c98955'
    elif year == '21':
        return 'SC_ebc875206fc44194883fe06ec90f1fe9'
    elif year == '22':
        return 'SC_92c5753d65e34f05982adf6fddd7492f'
    elif year == '23':
        return '429db59ff85d4cf4935c1f5b5f3f34c8'
    elif year == '24':
        return '97624af4fdea4442890d4c257dbe83f2'
    elif year == '25':
        return '6ed7ab2a5e4a42c2b1f950fec0ba1665'
    elif year == '26':
        return '429db59ff85d4cf4935c1f5b5f3f34c8'



    elif year == '10':
        return '4f8ff6814938448e8ea6e36933b86e66'
    elif year == '11':
        return 'f67022a48f3b4852b28e2e6656510836'
    elif year == '12':
        return '621fa92897c74f429d39de9d4808e323'
    elif year == '13':
        return '03834387382247f991819b6a610d217d'
    elif year == '14':
        return '578c78426b91414096f0f94d26f335e6'


jessionid = '2FBFE1F6184436312EB4751C84A2FE13'

# 8.23 更新  现在需要去爬每年的plantid，每个课程不一样了
# 8.25 更新 现在专业课也不需要换符号了

cookies = [
 

    # {'name': 'yaodaimade', 'year': [20,21,22],
    #   'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzMDMwMTk4OTExMDY4NTMwQDE1MSIsIm1vYmlsZSI6IjE3ODI4ODcxNTIwIiwidXNlck5hbWUiOiJoZWFueWluZzA4MDEyNSIsInVzZXJJZCI6Ijc4MDdhNTQ1N2I3OTRlYzg5MWFjYzg0ZTliMzY4NTE1IiwiaWF0IjoxNzM1NjEyMDA1LCJqdGkiOiI2M2I5MTVjOWU0MDQ0NjdkOTRmNTNmNzgyODdlY2E2YyJ9.xfXXJ-jp7kkt1KsRY_8E8R_mF-dNeBrsntCGqZeuMw0'},
    #
    {'name': 'yaodaimade', 'year': [23],
     'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTExOTIzMTk5NTA5MTAzOTczQDE1MSIsIm1vYmlsZSI6IjE3MzExMDY3MjU1IiwidXNlck5hbWUiOiJ2YXNpbmciLCJ1c2VySWQiOiIyZmExOTdkNzg3ZmM0OTY0OThjZmUxYWJhYjUwNThmYSIsImlhdCI6MTczNjgzNjg2NCwianRpIjoiNjBmOGJlYjMwNDZlNDlhYWJmMmRkZDJmZTU1NjdhNTMifQ.Uqc23nezFQye9VlYqjlfSoGu96Ro3UZaBJYHjIfbYKo'},
    #
    # {'name': 'yaodaimade', 'year': [24],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIyMTk5MzEwMDEyMTQ3QDE1MSIsIm1vYmlsZSI6IjEzMzMwNjcyMzQ4IiwidXNlck5hbWUiOiI1MTM3MjIxOTkzMTAwMTIxNDciLCJ1c2VySWQiOiI5NTBmNTViYi1lZTM4LTRmNmQtYTZlYS0zMjIzZmFlNzA5OWYiLCJpYXQiOjE3MzU2NTYzMzQsImp0aSI6IjI5ZWZiMjUzZTBiOTQ0MmJhNGI3YjkzMDYwOWVhNjg2In0.C7oYhzK-R2dDMGFBo7b64heh4iAj_LRFslo5VsjOg3M'},
    #
    # {'name': 'yaoda2imade', 'year': [24],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzMDI2MTk3NzA3MjYzNDAxQDE1MSIsIm1vYmlsZSI6IjE4MDg2OTM4OTQ3IiwidXNlck5hbWUiOiI1MTMwMjYxOTc3MDcyNjM0MDEiLCJ1c2VySWQiOiJwMHMzXzIzN2RkYzU2LTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTczNTY1MzM5MCwianRpIjoiNGQ3Zjg5YjllZTM5NDkzYjlkZTk0YTJkYzE0ZWI0YjkifQ._soY4M0XkOw3267rdd5V60tlga5R7vOqMCmTYj9RGUM'},

    # {'name': '2ge', 'year': [23, 24],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzAxMTk5NDAzMTAxNjE0QDE1MSIsIm1vYmlsZSI6IjE3NzI2NTU2ODYxIiwidXNlck5hbWUiOiI1MTM3MDExOTk0MDMxMDE2MTQiLCJ1c2VySWQiOiIwYzQ4ZTljOC1kOTQ3LTQ2NDItYjAzMi0zYTMyZTgxNjllNzIiLCJpYXQiOjE3MzU2MjEzMjcsImp0aSI6IjMwOTFmMDQzMTQxMDQ4Y2E5OTc1YzgwMGFlMjliMzI4In0.59U-QLM8JiHs_ucG0jeGoC9vd4StEpXvvyo1CMCUAxY'},

]
