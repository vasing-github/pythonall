import time

import requests
import conf
import test_get_recordid
import takerecord
def get_cource_detail(courceid):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Hrttoken': conf.cookie,
        'Origin': 'https://edu.chinahrt.com',
        'Referer': 'https://edu.chinahrt.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        'appid': 'gp6-1',
        'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'courseId': courceid,
        'trainplanId': 'b34287b27e1142fb9f00d0046e6a9ee9',
        'platformId': '151',
    }

    response = requests.get('https://gp.chinahrt.com/gp6/lms/stu/course/courseDetail', params=params, headers=headers, verify=False)
    chapter_list = response.json()['data']['course']['chapter_list']
    all_cource = []
    for chapter in chapter_list:
        for selction in chapter['section_list']:

            all_cource.append(selction)

    return all_cource
if __name__ == '__main__':
    list_cource = [
       '09f49a3bbc0d4d89a422550a366a9a18',
       '2c9ff022029b4d0fa3a64948fc00a73c',
        '2gPauPN1AgJXV4v6wJsX5',
       #  '6fidE1rl-j1plKeBNSFAk',
       #  '8f1fbd28c2ce43c983c51c1030a80c63',
       #  'd536937a57be45f38233a245496a976c',
       #  'd8d7128ffd984e95960c8daf31540638',
        'e0QdGP6T7NPtjbW3Ec8ud',
        'ed4db77a25954589b7732bd044618f0d',
         'Mq1UUdk8k-GqsQqMUVEVF',
    ]
    cource_selection_dic = {}
    for cource in list_cource:
        list_selection = get_cource_detail(cource)
        cource_selection_dic[cource] = list_selection
    print(cource_selection_dic)
    # cource_selection_dic = {'6fidE1rl-j1plKeBNSFAk': ['6fidE1rl-j1plKeBNSFAk1-1', '6fidE1rl-j1plKeBNSFAk1-2', '6fidE1rl-j1plKeBNSFAk1-3', '6fidE1rl-j1plKeBNSFAk1-4'], '8f1fbd28c2ce43c983c51c1030a80c63': ['8f1fbd28c2ce43c983c51c1030a80c631-1', '8f1fbd28c2ce43c983c51c1030a80c631-2', '8f1fbd28c2ce43c983c51c1030a80c631-3', '8f1fbd28c2ce43c983c51c1030a80c631-4'], 'd536937a57be45f38233a245496a976c': ['d536937a57be45f38233a245496a976c1-1', 'd536937a57be45f38233a245496a976c1-2', 'd536937a57be45f38233a245496a976c1-3', 'd536937a57be45f38233a245496a976c1-4', 'd536937a57be45f38233a245496a976c1-5'], 'd8d7128ffd984e95960c8daf31540638': ['d8d7128ffd984e95960c8daf315406381-1', 'd8d7128ffd984e95960c8daf315406381-2', 'd8d7128ffd984e95960c8daf315406381-3']}
    for courceid,selctions in cource_selection_dic.items():
        print(courceid)
        for selction in selctions:
            recordid , studydoce ,src = test_get_recordid.get_study_code_and_recordid(courceid,selction['id'])
            study_time = selction['study_time']
            total_time = selction['total_time']
            print(selction['name'])

            if study_time < 0.85 * total_time:
                takerecord.taskrecord(recordid,studydoce,src,selction['id'],0.85 * total_time)
            else:
                takerecord.taskrecord(recordid, studydoce, src, selction['id'], total_time - 30)
            time.sleep(10)
