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
        return '429db59ff85d4cf4935c1f5b5f3f34c8'
    elif year == '24':
        return '97624af4fdea4442890d4c257dbe83f2'
    elif year == '25':
        return '6ed7ab2a5e4a42c2b1f950fec0ba1665'



    elif year == '10':
        return '4f8ff6814938448e8ea6e36933b86e66'
    elif year == '11':
        return 'd0af473b813a47758e0a4fffb7053517'
    elif year == '12':
        return '4fa3a091c9634608b96efaf74c432a06'
    elif year == '13':
        return 'c8f2fb13640647b2ad082098c740bdba'
    elif year == '14':
        return '578c78426b91414096f0f94d26f335e6'


jessionid = '2FBFE1F6184436312EB4751C84A2FE13'

# 8.23 更新  现在需要去爬每年的plantid，每个课程不一样了
# 8.25 更新 现在专业课也不需要换符号了

cookies = [

    {'name': '王菊', 'year': [24, 13, 12, 10],
     'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk4NjAxMjc0Nzk4QDE1MSIsIm1vYmlsZSI6IjEzNTQ3MzA1MjUyIiwidXNlck5hbWUiOiI1MTM3MjMxOTg2MDEyNzQ3OTgiLCJ1c2VySWQiOiJwMXM1XzI1NzVlZTkwLTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcyODQ1Nzk4MCwianRpIjoiYzdlNmVjZmZkMjcwNDFjNzk5Y2UzZmI3N2EzYzA0ZjcifQ.06Mppve6tt_zGdHPNjnXw6o5Zwi4hmLt-_HeI_62wfQ'},

    {'name': '60那个', 'year': [11],
     'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIyMTk5MTAxMDMxMjk2QDE1MSIsIm1vYmlsZSI6IjE4MjgyNzQ4ODU1IiwidXNlck5hbWUiOiI1MTM3MjIxOTkxMDEwMzEyOTYiLCJ1c2VySWQiOiI5NjBmMTFlNS01N2IwLTRlMjYtOTdiZS00ZjIwNDJiOTZkZTQiLCJpYXQiOjE3Mjg0NTU2MjcsImp0aSI6IjQyYjI2YmQ2ZGU3ZDRkNDhhYjFmM2Q5MzgyMzMzODExIn0.YPbnNzbOyJ2m7zhKFXWW6AW_QRpn_AC_HOQzjsGm3IE'},
    #
    #  {'name': '慢刷给20的', 'year': [24],
    #   'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzMDI1MTk2OTA0MjQwMDEzQDE1MSIsIm1vYmlsZSI6IjEzMTgzNTM1Nzg5IiwidXNlck5hbWUiOiI1MTMwMjUxOTY5MDQyNDAwMTMiLCJ1c2VySWQiOiJwMnM5XzIzNGYzNDc4LTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcyNzQwMzAwOSwianRpIjoiMmE2NWFlZDUzNTAxNDMwYTg5NDc3ZmFmMDllN2VlNGUifQ.tRnmLQb76gffZfIZrTWP3neFuL_AZTfJFiztRVP_86U'},

    # {'name': '两个90的2', 'year': [13, 14],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzOTAxMTk4ODAzMDgxMDMwQDE1MSIsIm1vYmlsZSI6IjE4NTgwNjU2MTUxIiwidXNlck5hbWUiOiJqaWFuMmRhbiIsInVzZXJJZCI6InAxczlfZTU3ODNiYjgtMTYzOC00NGNjLWEyMDctMTdiMDNlZjE2MjU1IiwiaWF0IjoxNzI3MzQ1NTM2LCJqdGkiOiIyNWRlMzEwYmQ0ZjY0OTE5ODEyMDQ3OTA1NmMwNzM3NSJ9.GCkCbt_klT1XMpAYxoyuc4TZxC9tVq15XkOnVbWp8CY'},

    # {'name': '第五个', 'year': [24],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk4OTEwMDE5MTkyQDE1MSIsIm1vYmlsZSI6IjE4MzgyNzAwNzcxIiwidXNlck5hbWUiOiI1MTM3MjMxOTg5MTAwMTkxOTIiLCJ1c2VySWQiOiJwMnMzXzRlZjY5NTBiLTM2MDQtNGQxYS05NzA4LWFjMjk5MWUyNDlhNyIsImlhdCI6MTcyNzE3NjI2MCwianRpIjoiZGNmZWQzZDhkODcxNDMyNGI3OTMxNzYyNThlMzU4ODYifQ.YDAZnJ-VIvLIFOhkwVTA0ncEPH0L_dANTUNcpOrwgdg'},

]
