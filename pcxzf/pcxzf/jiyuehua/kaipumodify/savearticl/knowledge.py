import requests
import os
import sys
import json
import conf

current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目的根目录
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
# 将项目根目录添加到 sys.path
sys.path.append(project_root)
from kaipumodify.cfg import dealtext
import kaipumodify.cfg.text as text

bz_gov_id = text.bz_gov_id
jid = text.jid

from datetime import datetime
now = datetime.now()

# 格式化时间为字符串
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

def getpage_type(knowledge_type):
    cookies = {
        'historyCookie': '%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E6%95%99%E8%82%B2%E9%83%A8%2C%E4%BA%BA%E6%B0%91%E6%97%A5%E6%8A%A5%2C%E5%8E%BF%E8%87%AA%E7%84%B6%E8%B5%84%E6%BA%90%E5%92%8C%E8%A7%84%E5%88%92%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E7%9C%81%E6%95%99%E8%82%B2%E8%80%83%E8%AF%95%E9%99%A2%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E4%BA%BA%E6%B0%91%E7%BD%91%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%8F%B8%E6%B3%95%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E7%BB%BC%E5%90%88%E8%A1%8C%E6%94%BF%E6%89%A7%E6%B3%95%E5%B1%80',
        'authenticatecenterjsessionid': jid,
        'bz_govc_SHIROJSESSIONID': bz_gov_id,
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'historyCookie=%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E6%95%99%E8%82%B2%E9%83%A8%2C%E4%BA%BA%E6%B0%91%E6%97%A5%E6%8A%A5%2C%E5%8E%BF%E8%87%AA%E7%84%B6%E8%B5%84%E6%BA%90%E5%92%8C%E8%A7%84%E5%88%92%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E7%9C%81%E6%95%99%E8%82%B2%E8%80%83%E8%AF%95%E9%99%A2%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E4%BA%BA%E6%B0%91%E7%BD%91%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%8F%B8%E6%B3%95%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E7%BB%BC%E5%90%88%E8%A1%8C%E6%94%BF%E6%89%A7%E6%B3%95%E5%B1%80; authenticatecenterjsessionid=OTRhZjJjMzYtODUxOC00ZmU0LTk3YzgtNjM0MDljNjNjODM2; bz_govc_SHIROJSESSIONID=2441cf52-0f9a-43ee-bfac-9debd1b0fb9b',
        'Origin': 'http://10.15.3.133:83',
        'Referer': 'http://10.15.3.133:83/index;JSESSIONID=0e5d40fe-e04a-4347-9afb-e3ac6d335567?s=1722236533349&siteId=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'isAjax': '1',
        'dataType': 'json',
    }

    data = {
        'columnId': '6790391',
        'siteId': '6787191',
        'typeCode': 'knowledgeBase',
        'condition': '',
        'title': '',
        'dataFlag': '1',
        'pageIndex': '0',
        'pageSize': '100',
        'sortField': '',
        'sortOrder': '',
        'categoryCode': knowledge_type,
    }

    response = requests.post(
        'http://10.15.3.133:83/knowledgeBase/getPage',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )
    return response.json()


def get_new_bzid_jid():
    global bz_gov_id, jid
    bz_gov_id, jid = dealtext.jiyue_token()

def save_article(v):

    cookies = {
        'historyCookie': '%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E6%95%99%E8%82%B2%E9%83%A8%2C%E4%BA%BA%E6%B0%91%E6%97%A5%E6%8A%A5%2C%E5%8E%BF%E8%87%AA%E7%84%B6%E8%B5%84%E6%BA%90%E5%92%8C%E8%A7%84%E5%88%92%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E7%9C%81%E6%95%99%E8%82%B2%E8%80%83%E8%AF%95%E9%99%A2%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E4%BA%BA%E6%B0%91%E7%BD%91%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%8F%B8%E6%B3%95%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E7%BB%BC%E5%90%88%E8%A1%8C%E6%94%BF%E6%89%A7%E6%B3%95%E5%B1%80',
        'authenticatecenterjsessionid': jid,
        'bz_govc_SHIROJSESSIONID': bz_gov_id,
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'historyCookie=%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E6%95%99%E8%82%B2%E9%83%A8%2C%E4%BA%BA%E6%B0%91%E6%97%A5%E6%8A%A5%2C%E5%8E%BF%E8%87%AA%E7%84%B6%E8%B5%84%E6%BA%90%E5%92%8C%E8%A7%84%E5%88%92%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E7%9C%81%E6%95%99%E8%82%B2%E8%80%83%E8%AF%95%E9%99%A2%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E4%BA%BA%E6%B0%91%E7%BD%91%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%8F%B8%E6%B3%95%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E7%BB%BC%E5%90%88%E8%A1%8C%E6%94%BF%E6%89%A7%E6%B3%95%E5%B1%80; authenticatecenterjsessionid=OTRhZjJjMzYtODUxOC00ZmU0LTk3YzgtNjM0MDljNjNjODM2; bz_govc_SHIROJSESSIONID=2441cf52-0f9a-43ee-bfac-9debd1b0fb9b',
        'Origin': 'http://10.15.3.133:83',
        'Referer': 'http://10.15.3.133:83/index;JSESSIONID=0e5d40fe-e04a-4347-9afb-e3ac6d335567?s=1722236533349&siteId=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'IsAjax': '1',
        'dataType': 'JSON',
        '_': '0.017764141833287228',
    }

    data = {
        'columnId': '6790391',
        'siteId': '6787191',
        'knowledgeBaseId': v['knowledgeBaseId'],
        'contentId': v['contentId'],
        'typeCode': 'knowledgeBase',
        'title': v['title'],
        'subTitle': v['subTitle'],
        'author': v['author'],
        'publishDate': formatted_time,
        'categoryCode': v['categoryCode'],
        'categoryName': v['categoryName'],
        'content': v['content'],
        'replyContent': v['replyContent'],

        'redirectLink':  v['redirectLink'],
        'isNew': v['isNew'],
        'isTop':  v['isTop'],
        'topValidDate':  v['topValidDate'],
        'isBold':  v['isBold'],
        'isUnderline':  v['isUnderline'],
        'isTilt':  v['isTilt'],
        'titleColor':  v['titleColor'],
        'organDn':  v['organDn'],
        'organName':  v['organName'],

        'recordStatus': 'Normal',

        'createOrganId':  v['createOrganId'],
        'clickBtn': '1',

        'isPublish': '1',
        'resources': '答问知识库',
        'isLink': '0',
    }

    response = requests.post(
        'http://10.15.3.133:83/knowledgeBase/save',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )
    return response.json()

def sendmsg():
    _url = 'http://www.scpc.gov.cn/hdjl/wdzsk/index.html'

    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": f"自动保障栏目-每周二自动更新答问知识库成功，请人工核实。\n\n\n[答问知识库]({_url})\n\n\n{_url}\n\n\n<@WuXiaoLong>\n<@MingFengWangBaoNing>"
        }
    }


    key = conf.key_cs
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=" + key
    # 发送HTTP POST请求
    response = requests.post(url, data=json.dumps(data))

    # 输出响应结果
    print(response.text)


def send_err():
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": f"自动更新答问知识库失败-请检查配置文件。\n\n<@WuXiaoLong>\n<@MingFengWangBaoNing>"
        }
    }
    key = conf.key_cs
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=" + key
    # 发送HTTP POST请求
    response = requests.post(url, data=json.dumps(data))

    # 输出响应结果
    print(response.text)


if __name__ == '__main__':
    knowledges = conf.knowleges
    for ty in knowledges:

        res = getpage_type(ty)
        if 'status' in res and res['status'] == -9:
            get_new_bzid_jid()
        last_value = res["data"][-1]
        # print(last_value)
        ret = save_article(last_value)
        print(ret)
        if 'status' in res and res['status'] != 1:
            send_err()
            break
    sendmsg()