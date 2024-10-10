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
        return '03834387382247f991819b6a610d217d'
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

    {'name': '慢刷给20的', 'year': [24],
     'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk4NzA1MTU3NTAyQDE1MSIsIm1vYmlsZSI6IjE1MjgyNzYzMzY1IiwidXNlck5hbWUiOiI1MTM3MjMxOTg3MDUxNTc1MDIiLCJ1c2VySWQiOiJwMXM1XzI0NmNkNWNjLTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcyODUxNDU5NiwianRpIjoiMmViOTAxZTQzNjkxNGQyMWJmM2I2ZjY4ZDJjZTMzYjEifQ.Euhqho9RiNS-KLG-mxWkAOzq1m4TAlP9plpQD4WPLN4'},

    # {'name': 'chenzhou', 'year': [14, 13],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzMDI4MTk4NzA0MDU0NDMzQDE1MSIsIm1vYmlsZSI6IjE1OTA4NDQ3OTk3IiwidXNlck5hbWUiOiI1MTMwMjgxOTg3MDQwNTQ0MzMiLCJ1c2VySWQiOiJwMXM2XzgyNDljMGNiLTllNzQtNGNmNC1hYjcyLTUwODM3Nzc0MjYxZiIsImlhdCI6MTcyODQ2OTc1NSwianRpIjoiZjFlYTc3NWY5OGRkNGRkZmE2NzM0ZmQ0MDllZWM4NzUifQ.YErOKJhVvzGVJet9l1pJfKgi90wikKuI4lkEPvNwP1k'},
    #
    # {'name': 'qiao', 'year': [13, 14],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTExMzI0MTk5NzEyMDcxMzVYQDE1MSIsIm1vYmlsZSI6IjE1NjgxMDMwMzEzIiwidXNlck5hbWUiOiIxNTY4MTAzMDMxMyIsInVzZXJJZCI6ImY1ZWE0NDU5YzZmZTRiMjg4MTg2YjA3M2ExMGNiYjJmIiwiaWF0IjoxNzI4NDY5OTczLCJqdGkiOiIxY2QyOGJmOGZlMWY0MmZmOGI3MjRkOTk3YzRjMTEzMCJ9.K56cuJxxQyIiCFVigjwxdW6o85gPGC1qIG9QTz7I_bI'},


    # {'name': '两个90的2', 'year': [13, 14],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzOTAxMTk4ODAzMDgxMDMwQDE1MSIsIm1vYmlsZSI6IjE4NTgwNjU2MTUxIiwidXNlck5hbWUiOiJqaWFuMmRhbiIsInVzZXJJZCI6InAxczlfZTU3ODNiYjgtMTYzOC00NGNjLWEyMDctMTdiMDNlZjE2MjU1IiwiaWF0IjoxNzI3MzQ1NTM2LCJqdGkiOiIyNWRlMzEwYmQ0ZjY0OTE5ODEyMDQ3OTA1NmMwNzM3NSJ9.GCkCbt_klT1XMpAYxoyuc4TZxC9tVq15XkOnVbWp8CY'},

    # {'name': '第五个', 'year': [24],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk4OTEwMDE5MTkyQDE1MSIsIm1vYmlsZSI6IjE4MzgyNzAwNzcxIiwidXNlck5hbWUiOiI1MTM3MjMxOTg5MTAwMTkxOTIiLCJ1c2VySWQiOiJwMnMzXzRlZjY5NTBiLTM2MDQtNGQxYS05NzA4LWFjMjk5MWUyNDlhNyIsImlhdCI6MTcyNzE3NjI2MCwianRpIjoiZGNmZWQzZDhkODcxNDMyNGI3OTMxNzYyNThlMzU4ODYifQ.YDAZnJ-VIvLIFOhkwVTA0ncEPH0L_dANTUNcpOrwgdg'},

]
