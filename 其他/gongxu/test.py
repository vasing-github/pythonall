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

if __name__ == '__main__':
    take2()