import requests

cookies = {
    'token': 'BearereyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3MzQwNzQ4LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3MzMzNTQ4LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.Fuhkr4BREawOWOux82MegrnysprJr3LVHD3TjHYcPvA',
    'refreshToken': 'eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NDE5OTQ4LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3MzMzNTQ4LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.wl7dE5T8EIx6guiozv8A9VnTPXgTbF7cBN6kenlhvco',
    'x-token': '6cab50c9-e0b1-409b-b88c-de521170ef1a',
    'JSESSIONID': 'AE3F03BD3DB67EF0DB6B7E4FDDD1FA39',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Aspxauth': 'BearereyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3MzQwNzQ4LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3MzMzNTQ4LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.Fuhkr4BREawOWOux82MegrnysprJr3LVHD3TjHYcPvA',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'token=BearereyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3MzQwNzQ4LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3MzMzNTQ4LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.Fuhkr4BREawOWOux82MegrnysprJr3LVHD3TjHYcPvA; refreshToken=eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NDE5OTQ4LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3MzMzNTQ4LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.wl7dE5T8EIx6guiozv8A9VnTPXgTbF7cBN6kenlhvco; x-token=6cab50c9-e0b1-409b-b88c-de521170ef1a; JSESSIONID=AE3F03BD3DB67EF0DB6B7E4FDDD1FA39',
    'Origin': 'https://www.hngbzx.gov.cn',
    'Referer': 'https://www.hngbzx.gov.cn/wechat',
    'Refreshtoken': 'eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoi572X55C85qKFIiwicm9sZSI6bnVsbCwiZXhwIjoxNzI3NDE5OTQ4LCJ1c2VyaWQiOjIyNjE1MSwiaWF0IjoxNzI3MzMzNTQ4LCJ1c2VybmFtZSI6ImxxbTEzNjM3NjQ2MzYwIn0.wl7dE5T8EIx6guiozv8A9VnTPXgTbF7cBN6kenlhvco',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'courseId': '14123',
    'timeNode': '005959',
}

response = requests.post('https://www.hngbzx.gov.cn/api/mobile/uploadTimeNode', cookies=cookies, headers=headers, json=json_data)
print(response.text)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"courseId":"14123","timeNode":"001256"}'
#response = requests.post('https://www.hngbzx.gov.cn/api/mobile/uploadTimeNode', cookies=cookies, headers=headers, data=data)