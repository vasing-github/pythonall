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
        return '03834387382247f991819b6a610d217d'
    elif year == '11':
        return 'f2c16584e5ef40b5821250309dd9238a'
    elif year == '12':
        return 'd0af473b813a47758e0a4fffb7053517'
    elif year == '13':
        return '03834387382247f991819b6a610d217d'
    elif year == '14':
        return '578c78426b91414096f0f94d26f335e6'


jessionid = '2FBFE1F6184436312EB4751C84A2FE13'

# 8.23 更新  现在需要去爬每年的plantid，每个课程不一样了
# 8.25 更新 现在专业课也不需要换符号了

cookies = [

   # {'name': '王菊', 'year': [24],
   #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzMDI4MTk3MzAzMDI5MTUyQDE1MSIsIm1vYmlsZSI6IjEzNTUwNDgyMDA4IiwidXNlck5hbWUiOiI1MTMwMjgxOTczMDMwMjkxNTIiLCJ1c2VySWQiOiJwMXM4XzI1NjVkMmY4LTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcyNzIzMDU0NCwianRpIjoiZTJiMzE2OTkyOWQzNDI2MWFkMmEzZWZjOGZlYzc0M2YifQ.aveYvzo_ivNJvk-qIkGJPv6AI-k59TP7je_CPtqUMnM'},

    {'name': 'shun', 'year': [24],
     'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzMDIzMTk4MTAyMjIzMzE0QDE1MSIsIm1vYmlsZSI6IjEzNTY4NDY5NjM4IiwidXNlck5hbWUiOiI1MTMwMjMxOTgxMDIyMjMzMTQiLCJ1c2VySWQiOiJwMXM2XzI0YjJiMGNlLTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcyNzI0NDQ5NywianRpIjoiYTY5YTExNGQ5YTcxNDE2NzliODQzMWJlMDBlMjJlNjEifQ.35-cSalRGlUSXfpw-l6GrqSEf6Xr9Zrk99fq9oJUX9w'},

    #  {'name': '核武', 'year': [24],
    # 'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzMDI4MTk3NDA2MTUwMDM1QDE1MSIsIm1vYmlsZSI6IjE4NzI4NzM1Nzg3IiwidXNlck5hbWUiOiI1MTMwMjgxOTc0MDYxNTAwMzUiLCJ1c2VySWQiOiJwMnM2XzIyYmE3MjhlLTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcyNzIzNDY3OCwianRpIjoiYmU0MTc1N2NjZjkyNDZiZWE2NzE0MThkZmU4Y2FmNWYifQ.5lm2egKtvOltmmJ2ZXcozFWQxzacfbPAqBRuXuV9TuY'},

    # {'name': '唐志鹏', 'year': [24],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk4MjAxMTQwMDM3QDE1MSIsIm1vYmlsZSI6IjE1OTgzOTUyOTgwIiwidXNlck5hbWUiOiI1MTM3MjMxOTgyMDExNDAwMzciLCJ1c2VySWQiOiJwMHMwXzI1M2Q1Y2Q4LTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcyNzE3NDI2MiwianRpIjoiMWIyODE3ZThkODkxNDk3ZWIyNmJmMWI4ZTUxM2UxYjMifQ.x4Wp5ukZfpf2i9p7Qw3YFiCyP1ZvgHgG8xRpzStImOI'},

    # {'name': '第五个', 'year': [24],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk4OTEwMDE5MTkyQDE1MSIsIm1vYmlsZSI6IjE4MzgyNzAwNzcxIiwidXNlck5hbWUiOiI1MTM3MjMxOTg5MTAwMTkxOTIiLCJ1c2VySWQiOiJwMnMzXzRlZjY5NTBiLTM2MDQtNGQxYS05NzA4LWFjMjk5MWUyNDlhNyIsImlhdCI6MTcyNzE3NjI2MCwianRpIjoiZGNmZWQzZDhkODcxNDMyNGI3OTMxNzYyNThlMzU4ODYifQ.YDAZnJ-VIvLIFOhkwVTA0ncEPH0L_dANTUNcpOrwgdg'},

]
