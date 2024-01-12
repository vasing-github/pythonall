
import conf
import requests

Authorization = conf.Authorization

def get_list():

    url = 'http://59.225.201.162:8086/api/approval/wf/task/upcoming'
    #data = '{"page":1,"rows":'+str(conf.query_num)+',"orderBy":{"updateTime":"desc"},"affairName":null,"likeMap":{},"between":{},"in":{"bizStatus":["21","22","23","24","25","26","27,","28","31","33"]}}'
    data = '{"page":1,"rows":'+str(conf.query_num)+',"orderBy":{"updateTime":"desc"},"affairName":null,"likeMap":{},"between":{},"in":{"bizStatus":["41","32","34"]}}'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': Authorization,
        'Content-Length':'168',
        'Content-Type':'application/json;charset=UTF-8',
        'Cookie':'route=7e955e553605b1ea9a7034e978d0c40a',
        'Host':'59.225.201.162:8086',
        'Origin': 'http://59.225.201.162:8086',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://59.225.201.162:8086/db_work',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    response = requests.post(url, headers=headers,data=data)
    records = response.json()['data']['records']
    ids = [x['busiId'] for x in records]
    return ids
def submitAffair(busiId):
    url = 'http://59.225.201.162:8086/api/approval/dth/affair/submitAffair'
    # data = '{"affairId":"'+busiId+'","shardKey":"5119","handleType":6,"auditAdviceInfo":null,"base64Json":"","auditAdvice":1,"attIds":""}'
    data = '{"affairId": "'+busiId+'", "shardKey": "5119", "handleType": 7, "auditAdvice": "1","auditAdviceInfo": "同意", "base64Json": "", "attIds": ""}'
    data = data.encode("utf-8")
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Authorization': Authorization,
        'Content-Length': '168',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'route=7e955e553605b1ea9a7034e978d0c40a',
        'Host': '59.225.201.162:8086',
        'Origin': 'http://59.225.201.162:8086',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://59.225.201.162:8086/db_work',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    response = requests.post(url, headers=headers, data=data)
    code = response.json()['code']
    succ = response.json()['success']
    name = response.json()['data']['affair']['applicantName']
    print("code:",code,"succ:",succ,"name:",name)
ids = get_list()
_a = 1
j = 0
for each in ids:
    print("star:%d", _a)
    try:
        submitAffair(each)
        _a += 1
    except Exception as e:
        j = +1
        print('错了几个？', j)

    print("\n")





