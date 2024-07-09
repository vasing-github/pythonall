import requests

from bs4 import BeautifulSoup


# 请求网页得到信件id
def get_message_id(url):
    # URL of the webpage

    # Send an HTTP request to fetch the webpage content
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the element containing the message ID
    message_id_element = soup.find("td", class_="nr")

    # Extract the message ID
    message_id = message_id_element.text.strip()

    # Print the extracted message ID
    print("Message ID:", message_id)

    shuji_el = soup.find("a", title="书记信箱")
    xianzhang_el = soup.find("a", title="县长信箱")

    # Extract the text
    if shuji_el:
        result = 1
    elif xianzhang_el:
        result = 0
    else:
        result = "无法区分书记信箱还是县长信箱报错"

    print(result)

    return message_id, result


def search_message_by_id(message_id, is_shuji, bz_gov_id, jid):
    cookies = {
        'msgsubmitjsessionid': 'Y2Q3NTQ4ZTEtMTY5My00NzllLTliM2YtNzQ2ODI2NjE2ZDNj',
        'authenticatecenterjsessionid': jid,
        'bz_govc_SHIROJSESSIONID': bz_gov_id,
        'historyCookie': '%E5%8E%BF%E5%8D%AB%E7%94%9F%E5%81%A5%E5%BA%B7%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E6%B3%93%E6%BA%90%E5%B8%B8%E9%9D%92%E5%85%AC%E7%94%A8%E4%BA%8B%E4%B8%9A%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%9E%8D%E5%AA%92%E4%BD%93%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%B0%E8%8D%89%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E6%96%B0%E5%8D%8E%E7%A4%BE%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E9%9D%92%E4%BA%91%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%B7%B4%E5%B1%B1%E5%A4%A9%E9%A6%99%E8%8A%B1%E6%A4%92%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%8D%8E%E6%96%87%E5%85%AC%E5%85%B1%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        # 'Cookie': 'msgsubmitjsessionid=Y2Q3NTQ4ZTEtMTY5My00NzllLTliM2YtNzQ2ODI2NjE2ZDNj; authenticatecenterjsessionid=NTA2N2Y2ZDgtZGQ0YS00ZjFkLWE1YzgtYjcyYjBiYWM1OWQz; bz_govc_SHIROJSESSIONID=c1fe79d0-4665-4908-b249-a8a13f86a598; historyCookie=%E5%8E%BF%E5%8D%AB%E7%94%9F%E5%81%A5%E5%BA%B7%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E6%B3%93%E6%BA%90%E5%B8%B8%E9%9D%92%E5%85%AC%E7%94%A8%E4%BA%8B%E4%B8%9A%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%9E%8D%E5%AA%92%E4%BD%93%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%B0%E8%8D%89%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E6%96%B0%E5%8D%8E%E7%A4%BE%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E9%9D%92%E4%BA%91%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%B7%B4%E5%B1%B1%E5%A4%A9%E9%A6%99%E8%8A%B1%E6%A4%92%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%8D%8E%E6%96%87%E5%85%AC%E5%85%B1%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8',
        'Referer': 'http://10.15.3.133:83/index;JSESSIONID=9cadc447-8ab6-4315-b0f9-a31ffa1314de?s=1716965667820&siteId=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'IsAjax': '1',
        'dataType': 'JSON',
        '_': '1716965668846',
        'pageIndex': '0',
        'pageSize': '10',
        'dataFlag': '1',
        'columnId': '6790321' if is_shuji else '6790331',
        'title': '',
        'docNum': message_id,
        'personName': '',
        'isPublish': '',
        'dealStatus': '',
        'classCode': '',
        'receiveUnitId': '',
        'receiveUserCode': '',
        'receiveDepartId': '',
        'st': '',
        'ed': '',
    }

    response = requests.get('http://10.15.3.133:83/messageBoard/getPage', params=params, cookies=cookies,
                            headers=headers, verify=False)

    return response.json()
    # if response.json()['total'] != 1:
    #     print("通过信件编号找到多条信息")
    #     return
    # return response.json()['data'][0]
    # for message in data:
    #     id = message['id']
    #     baseContentId = message['baseContentId']
    #     messageBoardContent = message['messageBoardContent']
    #     for reply in message['replyVOList']:
    #         replyContent = reply['replyContent']
    #         messageBoardId = reply['messageBoardId']
    #         break
    # print(id, baseContentId, messageBoardContent, replyContent, messageBoardId)
    # return id, baseContentId, messageBoardContent, replyContent, messageBoardId


def modify_mesagee(m, bzid, jid, wrong, right):
    cookies = {
        'msgsubmitjsessionid': 'Y2Q3NTQ4ZTEtMTY5My00NzllLTliM2YtNzQ2ODI2NjE2ZDNj',
        'authenticatecenterjsessionid': jid,
        'bz_govc_SHIROJSESSIONID': bzid,
        'historyCookie': '%E5%8E%BF%E5%8D%AB%E7%94%9F%E5%81%A5%E5%BA%B7%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E6%B3%93%E6%BA%90%E5%B8%B8%E9%9D%92%E5%85%AC%E7%94%A8%E4%BA%8B%E4%B8%9A%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%9E%8D%E5%AA%92%E4%BD%93%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%B0%E8%8D%89%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E6%96%B0%E5%8D%8E%E7%A4%BE%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E9%9D%92%E4%BA%91%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%B7%B4%E5%B1%B1%E5%A4%A9%E9%A6%99%E8%8A%B1%E6%A4%92%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%8D%8E%E6%96%87%E5%85%AC%E5%85%B1%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'msgsubmitjsessionid=Y2Q3NTQ4ZTEtMTY5My00NzllLTliM2YtNzQ2ODI2NjE2ZDNj; authenticatecenterjsessionid=NTA2N2Y2ZDgtZGQ0YS00ZjFkLWE1YzgtYjcyYjBiYWM1OWQz; bz_govc_SHIROJSESSIONID=c1fe79d0-4665-4908-b249-a8a13f86a598; historyCookie=%E5%8E%BF%E5%8D%AB%E7%94%9F%E5%81%A5%E5%BA%B7%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E6%B3%93%E6%BA%90%E5%B8%B8%E9%9D%92%E5%85%AC%E7%94%A8%E4%BA%8B%E4%B8%9A%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%9E%8D%E5%AA%92%E4%BD%93%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%B0%E8%8D%89%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E6%96%B0%E5%8D%8E%E7%A4%BE%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E9%9D%92%E4%BA%91%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%B7%B4%E5%B1%B1%E5%A4%A9%E9%A6%99%E8%8A%B1%E6%A4%92%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%8D%8E%E6%96%87%E5%85%AC%E5%85%B1%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8',
        'Origin': 'http://10.15.3.133:83',
        'Referer': 'http://10.15.3.133:83/messageBoard/modify?id=13943256&&columnId=6790321&isOpen=true&_=1716974937394',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'IsAjax': '1',
        'dataType': 'JSON',
        '_': '0.17964781726228374',
    }

    data = {
        # 'receiveUnitId': '6601841',
        'classCode': m['classCode'],
        'personName': m['personName'],
        'personIp': m['personIp'],
        'title': m['title'].replace(wrong, right),
        'messageBoardContent': m['messageBoardContent'].replace(wrong, right),
        'addDate': m['addDate'],
        'id': m['id'],
        # 'forwardId': m['classCode'],
        # 'userId': m['userId'],
        # 'userName': m['userName'],
        # 'responseContent': m['classCode'],
        'isPublic': m['isPublic'],
        'isPublicInfo': m['isPublicInfo'],
        'isSuper': m['isSuper'],
        'personId': m['personId'],
        'type': m['type'],
        'personPhone': m['personPhone'],
        'baseContentId': m['baseContentId'],
        'knowledgeBaseId': m['knowledgeBaseId'],
        'categoryName': m['categoryName'],
        'forwardDate': m['forwardDate'],
        'remarks': m['remarks'],
        'isResponse': m['isResponse'],
        'replyDate': m['replyDate'],
        'password': m['password'],
        'receiveUserCode': m['password'],
        'defaultDays': m['defaultDays'],
        'receiveUnitName': '平昌县人民政府办公室',
        'receiveUserName': m['receiveUserName'],
        'recType': m['recType'],
        'className': m['className'],
        # 'contentClassCode': 'mct_jywb',
        'contentClassName': m['contentClassName'],
        'isPublish': m['isPublish'],
        'dealDays': m['dealDays'],
        'siteId': m['siteId'],
        'columnId': m['columnId'],
        'forwardAttachId': m['forwardAttachId'],
        'forwardCount': m['forwardCount'],
        'attachId': m['attachId'],
        # 'publishDate': m['publishDate'],
        'typeCode': m['typeCode'],
        'link': m['link'],
        'hit': m['hit'],
        'recordStatus': m['recordStatus'],
        # 'createUserId': '192246',
        # 'createOrganId': m['password'],
        'createDate': m['createDate'],
        # 'updateUserId': '6786225',
        # 'updateDate': '2024-05-29 16:15:10',
        'dueDate': m['dueDate'],
        'resourceType': m['resourceType'],
        'openId': m['openId'],
        'randomCode': m['randomCode'],
        'replyUserName': m['replyUserName'],
        'replyUserId': m['replyUserId'],
        'replyUnitName': m['replyUnitName'],
        'replyUnitId': m['replyUnitId'],
        'docNum': m['docNum'],
        'isTimeOut': m['isTimeOut'],
        'commentCode': m['commentCode'],
        'commentName': m['commentName'],
        'uri': m['uri'],
        'dealStatus': m['dealStatus'],
        'dealName': m['dealName'],
        # 'statusName': m['password'],
        'columnName': m['columnName'],
        'createUnitId': m['createUnitId'],
        'attachName': m['attachName'],
        'applyStatus': m['applyStatus'],
        'oldPersonId': m['oldPersonId'],
        'address': m['address'],
        'email': m['email'],
        'oldId': m['oldId'],
        'isBack': m['isBack'],
        'sort': m['sort'],
        'memberId': m['memberId'],
        'memberName': m['memberName'],
        'isPrinted': m['isPrinted'],
        'questionPlace': m['questionPlace'],
        'questionTime': m['questionTime'],
        'reportedUnit': m['reportedUnit'],
        'reportedPerson': m['reportedPerson'],
    }

    response = requests.post(
        'http://10.15.3.133:83/messageBoard/modifySave',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )
    print(response.json())


def modify_reply(r, bzid, jid, wrong, right):
    cookies = {
        'historyCookie': '%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%9E%8D%E5%AA%92%E4%BD%93%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%B0%E8%8D%89%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E6%96%B0%E5%8D%8E%E7%A4%BE%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E9%9D%92%E4%BA%91%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%B7%B4%E5%B1%B1%E5%A4%A9%E9%A6%99%E8%8A%B1%E6%A4%92%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%8D%8E%E6%96%87%E5%85%AC%E5%85%B1%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%B7%B4%E4%B8%AD%E5%B8%82%E7%BB%8F%E6%B5%8E%E5%92%8C%E4%BF%A1%E6%81%AF%E5%8C%96%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E9%98%B2%E6%B1%9B%E6%8A%97%E6%97%B1%E6%8C%87%E6%8C%A5%E9%83%A8',
        'authenticatecenterjsessionid': jid,
        'bz_govc_SHIROJSESSIONID': bzid,
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'historyCookie=%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%9E%8D%E5%AA%92%E4%BD%93%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%B0%E8%8D%89%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E6%96%B0%E5%8D%8E%E7%A4%BE%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E9%9D%92%E4%BA%91%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%B7%B4%E5%B1%B1%E5%A4%A9%E9%A6%99%E8%8A%B1%E6%A4%92%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%8D%8E%E6%96%87%E5%85%AC%E5%85%B1%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%B7%B4%E4%B8%AD%E5%B8%82%E7%BB%8F%E6%B5%8E%E5%92%8C%E4%BF%A1%E6%81%AF%E5%8C%96%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E9%98%B2%E6%B1%9B%E6%8A%97%E6%97%B1%E6%8C%87%E6%8C%A5%E9%83%A8; authenticatecenterjsessionid=ZTIyMDgzMWYtNGEzNS00MGU1LThmZWEtMGJjZGZlMWFjODcx; bz_govc_SHIROJSESSIONID=25b7de0f-8d36-4ba7-91f5-268ac7ca6773',
        'Origin': 'http://10.15.3.133:83',
        'Referer': 'http://10.15.3.133:83/messageBoard/updateReply?id=510578&&columnId=6790321&isOpen=true&_=1717493851031',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = {
        'dealStatus': r['dealStatus'],
        'receiveName': r['receiveName'],
        'replyContent': r['replyContent'].replace(wrong, right),
        'attachId': r['attachId'],
        'attachName': r['attachName'],
        'replyDate': r['replyDate'],
        'id': r['id'],
        'messageBoardId': r['messageBoardId'],
        'baseContentId': r['baseContentId'],
        'ip': r['ip'],
        'username': r['username'],
        'resourceType': r['resourceType'],
        'recType': r['recType'],
        'commentCode': r['commentCode'],
        'receiveUserCode': r['receiveUserCode'],
        'isSuper': r['isSuper'],
        'columnId': r['columnId'],
        'addDate': r['addDate'],
        'createDate': r['createDate'],
        'recordStatus': r['recordStatus'],
        'createUserId': r['createUserId'],
        'createOrganId': r['createOrganId'],
        'updateDate': r['updateDate'],
        'updateUserId': r['updateUserId'],
    }

    params = {
        'IsAjax': '1',
        'dataType': 'JSON',
        '_': '0.0782943084828458',
    }
    response = requests.post(
        'http://10.15.3.133:83/messageBoard/reply',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )
    print(response.text)


def start_kaipu(cuomin, bz_gov_id, jid):
    message_id, is_shuji = get_message_id(cuomin['url'])
    res = search_message_by_id(message_id, is_shuji, bz_gov_id, jid)
    if 'status' in res and res['status'] == -9:
        return 1

    print(res['data'][0]['replyVOList'][0])
    modify_mesagee(res['data'][0], bz_gov_id, jid, cuomin['sensitiveWords'], cuomin['recommendUpdate'].split('|')[0], )
    modify_reply(res['data'][0]['replyVOList'][0], bz_gov_id, jid, cuomin['sensitiveWords'], cuomin['recommendUpdate'].split('|')[0], )
    return 0


if __name__ == '__main__':
    # res = search_message_by_id('20240531190254941', 1, text.bz_gov_id, text.jid)
    # print(res['replyVOList'][0])
    # modify_mesagee(res, text.bz_gov_id, text.jid, '谢谢.', '谢谢。')
    #
    # modify_reply(res['replyVOList'][0], text.bz_gov_id, text.jid, '生活愉快。。', '生活愉快。')
    pass