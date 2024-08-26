import requests
import conf
from pcxzf.pcxzf.other.shizhengfu.text import token


def taskrecord(recordid,studycode,src,sectionid,studytime, userid,planid):
    cookies = {
        'JSESSIONID': conf.jessionid,
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'JSESSIONID=2CB53C6C9987FBB99B324B1EB2B5C971',
        'Origin': 'https://videoadmin.chinahrt.com',
        'Referer': src,
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'studyCode': studycode,
        'updateRedisMap': '1',
        'recordId': recordid,
        'sectionId': sectionid,
        'signId': '151#'+planid+'#'+userid,
        # 'signId': '151#97624af4fdea4442890d4c257dbe83f2#db94e12f4a9d45a19936bc304cbe26c4',

        'time': studytime,
        'businessId': 'gp5',
    }
    # print(data)

    response = requests.post('https://videoadmin.chinahrt.com/videoPlay/takeRecord', cookies=cookies, headers=headers, data=data)
    print(response.text)
    return response.json()['status']

def takeRecode2(token,time):

    cookies = {
        'JSESSIONID': 'AE60F152BBDE09F155A5B6B7B9F27B8B',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'text/html;charset=UTF-8',
        # 'Cookie': 'JSESSIONID=AE60F152BBDE09F155A5B6B7B9F27B8B',
        'Origin': 'https://videoadmin.chinahrt.com',
        'Referer': 'https://videoadmin.chinahrt.com/videoPlay/playEncrypt?param=M6FUERTovrwJKhmQd7T7TyNBK%2BVNxhzqSH0PXmorPcZ3rSPEh3uIvka%2FyE3InQ%2F4KQ10ZDPXDfHpXIXR%2BcI5FbEJzxuiNJ27XTKne2kfX8TwXayEpRR%2BBx2qNm6PaNCE53UxECkhSGHXaE2JZNesZcBB1Bq7RHzNHSfUBuJKLjfmarzBgbbLGN2syT6eiq6vwEyaN4d0RseygKNXisXChNY0p7ylVdk4v1dbWewWqZtVdu0J73xZQ7r7FzhTOuZFKAKA5DApDeVet0oKX%2B1T72HaonAl7xEwaRjJS0sISh%2Bx7hh085VbEYnbGOQzwAzt9r1PD1nveiK0F9ElfMXEfEeJyD7Rp3BoP0ox3i7gbmDBdHvIAYusrm%2BSxGJiw0Cwc0%2BSk8b5h7GxnJEpTQXmIReBKmZhOABCb%2BY2hniYaUOl%2FTxpl4WF6VJgWq3%2F1Q8YXijcMrgL52mkVlvg8mqH7cyZbps%2BlrlncBvgPNhLrrOo9kO2k75yQTm0dzRmozuW0%2F5sJFqBNZjYpo5CyZCMYRqV0Q%2FjjPxjz1UGS4QC8vPiIJRYsT1QQu6nnsNRfmS%2B1o4u7rFTctZ6Ls1SaZC7lorRPqUm%2FzT2xlnLpHplMhASbF7nYQDQ8sO19IkBmLv0%2FiDypQkzVpVSNPUQHydQFFRfACVqtJwfAb0xBV3nh8t%2FsyVkl0d8IlLLNAhEDVzSduEBMRYFJ5rH484ILWR9Kw%3D%3D',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = '{"token":'+token+',"time":'+time+'}'

    response = requests.post(
        'https://videoadmin.chinahrt.com/videoPlay/takeRecordByToken',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.text)
    return response.json()['status']