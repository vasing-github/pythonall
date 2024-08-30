import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://smartedu.gdtextbook.com',
    'Referer': 'https://smartedu.gdtextbook.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'token': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJhcHBJZFwiOlwic3lzdGVtLWFwcGxpY2F0aW9uLXRlYWNoZXJcIixcImNsaWVudElkXCI6XCJuYXRpb25hbF9zbWFydF9lZHVjYXRpb25cIixcImNsaWVudFR5cGVcIjpcIndlYlwiLFwicm9sZUlkc1wiOltcInRlYWNoZXJcIl0sXCJ1c2VySWRcIjpcIjhhODA4MzlhNTdkMDVlM2UwMTU3ZGZhOTZhZjMzYjkwXCJ9IiwiaWF0IjoxNzI0NjUzODU5fQ.z-T1-sFePUMZpX0hvnbaueIDO1wwY547y888h0Wqdzo',
}

json_data = {
    'userId': '8a80839a57d05e3e0157dfa96af33b90',
    'curriculumId': '496b65d74fed4d7d9f492a9d39b70c53',
    'chapterId': '12c8e09b67c04fee841878cce37e33d4',
    'watchStatus': 0,
    'durationTime': 201.253,
}

response = requests.post(
    'https://gateway-gray.gdtextbook.com/opengateway/research/auth/uuas-research/v1/curriculum/watch/add/user',
    headers=headers,
    json=json_data,
)

print(response.text)