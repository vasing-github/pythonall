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
        return '6ed7ab2a5e4a42c2b1f950fec0ba1665'



    elif year == '10':
        return 'd5c11e27a6be4b88b7d0daa6f7cdf89a'
    elif year == '11':
        return '5ae898a409f146478d8cb11094493601'
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

    {'name': 'yibin', 'year': [10],
     'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTExNTAyMjAwMDEyMDU4NDM1QDE1MiIsIm1vYmlsZSI6IjE3NjI4MTQxNTY4IiwidXNlck5hbWUiOiJMSkgxMjMzMiIsInVzZXJJZCI6IjFhMDc5NDMwYzYxNTQ0MTA4OWU2NmYwODA2YzUwZDBlIiwiaWF0IjoxNzI4NTU4ODYxLCJqdGkiOiI2NzFiNmJjZTFmZWU0YmFhOTM0YTMwZjc3NDhlOWZhZSJ9.r7oQJVYTovkViZeZ3KGuAaW1YxJ0NNmNk6je9u0coTc'},

    #  {'name': 'he1', 'year': [11],
    #   'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk4NjAxMjc0Nzk4QDE1MSIsIm1vYmlsZSI6IjEzNTQ3MzA1MjUyIiwidXNlck5hbWUiOiI1MTM3MjMxOTg2MDEyNzQ3OTgiLCJ1c2VySWQiOiJwMXM1XzI1NzVlZTkwLTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcyODU0MTc5NywianRpIjoiZWYyNGY5ODY0MjcyNDUwYTllZGZmMmQzNTY3NTAwNTUifQ.2q1A_R5aOPQ4VDvQkRCCp6hnow0xXGlTuEXbUSQXvdI'},
    #
    # {'name': 'he2', 'year': [23],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk4MjAxMTkzOTgwQDE1MSIsIm1vYmlsZSI6IjE1ODI4OTQwNzA4IiwidXNlck5hbWUiOiI1MTM3MjMxOTgyMDExOTM5ODAiLCJ1c2VySWQiOiJwMHMzXzIyYjllNWVlLTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcyODU2NTgzMSwianRpIjoiMDFiOWFjNjU0OWI2NDU1Y2FhMDg4YzcyNDdhNGJjZTAifQ.k95C8v4oddJBUYaoQ1HcJE_HxmszV11s8hKKMtLr1o0'},
    #
    # {'name': 'he3', 'year': [24],
    #  'cookie': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk4MzA4MTczNzAxQDE1MSIsIm1vYmlsZSI6IjE4Mzk4MjQ1ODc4IiwidXNlck5hbWUiOiI1MTM3MjMxOTgzMDgxNzM3MDEiLCJ1c2VySWQiOiJwMXM0XzIzMDM3YWE2LTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcyODU2NjE4NiwianRpIjoiMWQzNGRlMGY1ZTEwNDM3YmFiMDJjZjM5MGFkYTBiZDEifQ.gPMNvfeOSwjgHb7aOF1x6wm5jM-DKZunps9ARl7cbTE'},

]
