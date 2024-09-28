# 24年的id
# trainplanId= '97624af4fdea4442890d4c257dbe83f2'

# 23年课程id
# trainplanId = 'b34287b27e1142fb9f00d0046e6a9ee9'

def get_year_planid(year):
    if year == '20':
        return '1d53989388a4433f9f4ed1805979261b'
    elif year == '21':
        return '27535dc4b3294ec49fe2a0c11f6bf853'
    elif year == '22':
        return 'be50251f5ca649fa9411ae9b7e0e0083'
    elif year == '23':
        return 'b34287b27e1142fb9f00d0046e6a9ee9'
    elif year == '24':
        return '97624af4fdea4442890d4c257dbe83f2'
    elif year == '25':
        return '7126ee35589148268176f025da0dfcf6'



    elif year == '10':
        return '03834387382247f991819b6a610d217d'
    elif year == '11':
        return 'd0af473b813a47758e0a4fffb7053517'
    elif year == '12':
        return 'f2c16584e5ef40b5821250309dd9238a'
    elif year == '13':
        return '03834387382247f991819b6a610d217d'
    elif year == '14':
        return '3281756fd5e44257bb9ad443f55843f3'


jessionid = '2FBFE1F6184436312EB4751C84A2FE13'

# 8.23 更新  现在需要去爬每年的plantid，每个课程不一样了
# 8.25 更新 现在专业课也不需要换符号了

cookies = [

   {'name': '王菊', 'year': [13,12,11],
    'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzMTI3MTk5MzA5MTkwMjFYQDE1MSIsIm1vYmlsZSI6IjE4MzgwNDEwNDY4IiwidXNlck5hbWUiOiJhMTMwOTA4ODIyMSIsInVzZXJJZCI6ImZmYmU3NThhYjliZTQ3MzFiMTk3ZjhmMGQxOTEzOTlhIiwiaWF0IjoxNzI3NDQyMDI0LCJqdGkiOiJhZWNhNzY1NTY0NzQ0YTRlOTk0MjgyODk3ZGZkMjBjNiJ9.aQhK1kfxIHpoVMU83K9M9TfPZBTfUNPRtwvznCKgekM'},

   # {'name': '60那个', 'year': [12,13,22,23],
   #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTExOTAyMTk5MjAyMDcwMTQwQDE1MSIsIm1vYmlsZSI6IjE4ODAwOTU3MDAzIiwidXNlck5hbWUiOiJhbW91cmxqMTIzIiwidXNlcklkIjoiMDk0ZTFiYTYtNWRhNi00MmVkLThhYmYtMDE3NWIwMTI5M2EwIiwiaWF0IjoxNzI3NDAzMDY2LCJqdGkiOiI2YjU4MTY0ZjI3ZGU0NzU0YWMzYmNmMzY0MzAzZDI1ZCJ9.uVBznA_Hsq35p8-9jGtg1euStuccLCyKBiCNCyJ0huo'},
   #
   #  {'name': '慢刷给20的', 'year': [24],
   #   'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzMDI1MTk2OTA0MjQwMDEzQDE1MSIsIm1vYmlsZSI6IjEzMTgzNTM1Nzg5IiwidXNlck5hbWUiOiI1MTMwMjUxOTY5MDQyNDAwMTMiLCJ1c2VySWQiOiJwMnM5XzIzNGYzNDc4LTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcyNzQwMzAwOSwianRpIjoiMmE2NWFlZDUzNTAxNDMwYTg5NDc3ZmFmMDllN2VlNGUifQ.tRnmLQb76gffZfIZrTWP3neFuL_AZTfJFiztRVP_86U'},


    # {'name': '两个90的2', 'year': [13, 14],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzOTAxMTk4ODAzMDgxMDMwQDE1MSIsIm1vYmlsZSI6IjE4NTgwNjU2MTUxIiwidXNlck5hbWUiOiJqaWFuMmRhbiIsInVzZXJJZCI6InAxczlfZTU3ODNiYjgtMTYzOC00NGNjLWEyMDctMTdiMDNlZjE2MjU1IiwiaWF0IjoxNzI3MzQ1NTM2LCJqdGkiOiIyNWRlMzEwYmQ0ZjY0OTE5ODEyMDQ3OTA1NmMwNzM3NSJ9.GCkCbt_klT1XMpAYxoyuc4TZxC9tVq15XkOnVbWp8CY'},

    # {'name': '第五个', 'year': [24],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk4OTEwMDE5MTkyQDE1MSIsIm1vYmlsZSI6IjE4MzgyNzAwNzcxIiwidXNlck5hbWUiOiI1MTM3MjMxOTg5MTAwMTkxOTIiLCJ1c2VySWQiOiJwMnMzXzRlZjY5NTBiLTM2MDQtNGQxYS05NzA4LWFjMjk5MWUyNDlhNyIsImlhdCI6MTcyNzE3NjI2MCwianRpIjoiZGNmZWQzZDhkODcxNDMyNGI3OTMxNzYyNThlMzU4ODYifQ.YDAZnJ-VIvLIFOhkwVTA0ncEPH0L_dANTUNcpOrwgdg'},

]
