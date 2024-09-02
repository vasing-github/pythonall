import requests

def test1():
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
    time = str(3024+28*4)
    data = '{"token":"830a38ac9ae6ec92d59dbfbc30d72785","time":'+time+'}'

    response = requests.post(
        'https://videoadmin.chinahrt.com/videoPlay/takeRecordByToken',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.text)

def take2():
    import requests

    cookies = {
        'JSESSIONID': 'F2306DAABB7A6B0B4AAD955DB6E158C3',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'text/html',
        # 'Cookie': 'JSESSIONID=F2306DAABB7A6B0B4AAD955DB6E158C3',
        'Origin': 'https://videoadmin.chinahrt.com',
        'Referer': 'https://videoadmin.chinahrt.com/videoPlay/playEncrypt?param=M6FUERTovrwJKhmQd7T7TyNBK%2BVNxhzqSH0PXmorPcZ3rSPEh3uIvka%2FyE3InQ%2F4KQ10ZDPXDfHpXIXR%2BcI5FbEJzxuiNJ27XTKne2kfX8TwXayEpRR%2BBx2qNm6PaNCE53UxECkhSGHXaE2JZNesZcBB1Bq7RHzNHSfUBuJKLjfmarzBgbbLGN2syT6eiq6vs4M8z3UpUempPee0HIY%2BMdY0p7ylVdk4v1dbWewWqZuuBDyOjSMk2O24DL5TXVXZXye1%2BqOdFYvD9kO%2Fu%2Bz8Oj81JeICop8ZbzZhMwdpeTR4t90WxoLqIDLXvThch3r497Bog%2F0WEWxJo0Q45XO%2FgnMbH346bgkNOkaJESugyk5g3qKyTh1hrBPKvdUStLHZWf6ATqOukafkePOfTVsE72Wdin2EOP8g71nTG47tn%2FkqZjdlnc5ql%2Bt4TCJov1Mx6c6Nrgir4YLbbwZGklmZ1I%2Bro9V8S3Z%2FOLzcw9CYrk%2Fu7rKoCcaQXIi8hXtxYxLR6F4R0mhr2vbSiVyKIgAvgRfcAZSIgTRVUo4CgKSAY2xD3jsazkg1ODgnupPor3lofXwZMfVKy4mpd212HMqxdpvGT2DNkPeVf2Cda%2FQRbjm7EmFWQ%2BxzkPd1SVmjOCA%2Bvk7%2F8phHGfTNgd%2BZn8GpYbGFA4uP52l3vpMYFpXBzud24QExFgUnmsfjzggtZH0r',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = '{"token":"bd502b32e0b3a3cee211f2dac9d6fdaa","time":1031.63942}'

    response = requests.post(
        'https://videoadmin.chinahrt.com/videoPlay/takeRecordByToken',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.text)

def made():
    import requests

    cookies = {
        'p_h5_u': '3AFCAD64-17A5-4264-A77B-B54DB6E981C0',
        'JSESSIONID': 'BD773C1A105EE87CCD67C7D9901D1489',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'p_h5_u=3AFCAD64-17A5-4264-A77B-B54DB6E981C0; JSESSIONID=BD773C1A105EE87CCD67C7D9901D1489',
        'Origin': 'https://videoadmin.chinahrt.com',
        'Referer': 'https://videoadmin.chinahrt.com/videoPlay/playEncrypt?param=M6FUERTovrwJKhmQd7T7TyNBK%2BVNxhzqSH0PXmorPcZ3rSPEh3uIvka%2FyE3InQ%2F4KQ10ZDPXDfHpXIXR%2BcI5FbEJzxuiNJ27XTKne2kfX8TwXayEpRR%2BBx2qNm6PaNCE53UxECkhSGHXaE2JZNesZcBB1Bq7RHzNHSfUBuJKLjfmarzBgbbLGN2syT6eiq6vwEyaN4d0RseygKNXisXChNY0p7ylVdk4v1dbWewWqZtVdu0J73xZQ7r7FzhTOuZFKAKA5DApDeVet0oKX%2B1T72HaonAl7xEwaRjJS0sISh%2Bx7hh085VbEYnbGOQzwAzt9r1PD1nveiK0F9ElfMXEfEeJyD7Rp3BoP0ox3i7gbmDBdHvIAYusrm%2BSxGJiw0Cwc0%2BSk8b5h7GxnJEpTQXmIReBKmZhOABCb%2BY2hniYaUOl%2FTxpl4WF6VJgWq3%2F1Q8YXijcMrgL52mkVlvg8mqH7cyZbps%2BlrlncBvgPNhLrrNsjz3cyvD0RW3mTa368Q8fUuWMPT6449QfCV7ilALMbE8o2yDNUywJcElVlGe8fcxf4lSNZzxh2lv%2BWg8D9ciziQKKeZNaFptUUVZChnxY7hKoscShIVFLh8usrrLp4D6I9ZcUrtaOqTbpeN5B%2B12%2FMK9be4N56ZXvt6mKiOGpZ9LXxe0E28M88RmC8ob5m25%2Bpmn9wmaCFt94C6T61WLlSgCMqxkJdaIwu5qEABdubw%3D%3D',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'recordUrl': 'https://cloud.chinahrt.com/gp6/lms/api/course/update_learn_record',
        'updateRedisMap': '1',
        'sectionId': '1190963f61614009a2f6120af1c5567e1-19',
        'signId': '151#0985ef8ae5494f2eae0a5f8fe5ee18ee#p1s8_22be34be-92be-11e3-b77c-d4ae526c695b',
        'time': '568.522422',
        'businessId': 'gp5',
        'token': 'nerc',
    }

    response = requests.post('https://videoadmin.chinahrt.com/videoPlay/takeRecord', cookies=cookies, headers=headers,
                             data=data)
    print(response.text)

def xiaozhong():
    import requests

    cookies = {
        'Hm_lvt_75ba3a52fde3150c4f38ab6f87ef712a': '1725034518',
        'HMACCOUNT': '00B831FE7E9B92EF',
        'Hm_lpvt_75ba3a52fde3150c4f38ab6f87ef712a': '1725034929',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': 'Hm_lvt_75ba3a52fde3150c4f38ab6f87ef712a=1725034518; HMACCOUNT=00B831FE7E9B92EF; Hm_lpvt_75ba3a52fde3150c4f38ab6f87ef712a=1725034929',
        'id': '3190183',
        'origin': 'https://v3.dconline.net.cn',
        'priority': 'u=1, i',
        'referer': 'https://v3.dconline.net.cn/student.html',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'token': '554d23ab7e1a23cd21c1d9ee9b4165c6',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
    }

    json_data = {
        'msg': 's%2BlO8XDhHo9FxwcKDsDiJ2C8idtTpu%2BQ7bojryqNtpftXuxXLhZL8MK2tuGW%2FgZ6%2FSyQqzgsiGGs9LvpO%2BVednCJNIxmUVwgM%2F48VQnspLA%3D',
    }

    response = requests.post('https://v3.dconline.net.cn/api/v1/courseVideo/compV3', cookies=cookies, headers=headers,
                             json=json_data)
    print(response.text)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    # data = '{"msg":"s%2BlO8XDhHo9FxwcKDsDiJ2C8idtTpu%2BQ7bojryqNtpftXuxXLhZL8MK2tuGW%2FgZ6%2FSyQqzgsiGGs9LvpO%2BVednCJNIxmUVwgM%2F48VQnspLA%3D"}'
    # response = requests.post('https://v3.dconline.net.cn/api/v1/courseVideo/compV3', cookies=cookies, headers=headers, data=data)
if __name__ == '__main__':
    # made()
    xiaozhong()