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
        return '3fc370eb4a37420fab9fc8951fbfa978'
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
        return '1df424185068498797cb91345df5e879'


jessionid = '2FBFE1F6184436312EB4751C84A2FE13'

# 8.23 更新  现在需要去爬每年的plantid，每个课程不一样了
# 8.25 更新 现在专业课也不需要换符号了

cookies = [

    #  {'name': 'er', 'year': [25],
    #   'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTExOTIxMTk4OTA2MjI0NTI4QDE1MSIsIm1vYmlsZSI6IjE4MDk2MzQzOTI2IiwidXNlck5hbWUiOiI1MTE5MjExOTg5MDYyMjQ1MjgiLCJ1c2VySWQiOiJwMXM2XzdjNDA0YzJmLWMxNWItNGZjZS04NDlhLTgwMjc3MjM4NTFiMCIsImlhdCI6MTc0Mjg4MDQ5MiwianRpIjoiZjA1NWJlMmRkMDc1NDZjYmE1YmQ2M2MzZjZjMjIwMTAifQ.SvE7GUgiwP41w9LBYTIAjKqAQW3icdTPXDfCYkXp_vY'},

    # {'name': 'san', 'year': [25],
    #   'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTExMzIxMTk4NTA4MjA3NzM4QDE1MSIsIm1vYmlsZSI6IjEzNzc4Nzg1OTQ1IiwidXNlck5hbWUiOiIxMDUwMTc0MDcxcnd5IiwidXNlcklkIjoicDBzMV8wYTZiNzY5NC00MTBiLTQ0ZjQtOWQ5Mi1mZjExNGU2YTFmOTAiLCJpYXQiOjE3NDI4ODEyNTUsImp0aSI6IjkwMmU1NThjZTdlODQyNDA4MjBlMzc2ZDdjY2RlODRjIn0.oJRwZY4lH1XVIfRUI_pYC0ZqG4H6ZdQ8Cma3aXexsDU'},

 
    # {'name': 'er', 'year': [25],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIxMTk4NTAzMTIzMzAxQDE1MSIsIm1vYmlsZSI6IjE4OTE5NTUzNTkzIiwidXNlck5hbWUiOiJsZWlsaWxpbmciLCJ1c2VySWQiOiJwMHM2X2U2NmI2OGFmLTFkZmQtNGU5My05Mjc0LWQ3NWJiYTNkMzUwZSIsImlhdCI6MTc0Mjg4MTM5MywianRpIjoiNTkyNmRiNTU1YWZmNDc5MzhjN2Q0YzAxMjM1ZDJlN2IifQ.fIKaZbY1LX-FG7wTwMKttmcM7wMY08j6EEudyRBmseg'},
    #
     {'name': 'diyige', 'year': [25],
      'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIxMTk4NjA1MTAwMDIwQDE1MSIsIm1vYmlsZSI6IjE1NjgxMjU4MTExIiwidXNlck5hbWUiOiJnb3Vlbmh1YSIsInVzZXJJZCI6InAxczdfMjQyMWEwZDAtZjYzYi00OGEzLWI0MWUtZGY0YWQ1YzI1NDIxIiwiaWF0IjoxNzQyODgwNjMzLCJqdGkiOiI0MTQ1NzRkZWY3NWI0MmU3YjQxMWFlMDNkYWM3NWJmMiJ9.S18bKmijyUx_iCz5gGQL0CYbPEuFmcDUDjpD7memAZU'},
    #
]
