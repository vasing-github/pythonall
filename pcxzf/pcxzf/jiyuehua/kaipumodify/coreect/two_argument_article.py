from datetime import datetime
from jiyuehua.kaipumodify.cfg import conf
import requests


def getcontent(organId, contentId, bzid, jid):
    cookies = {
        'authenticatecenterjsessionid': jid,
        conf.jiyuehua_bzgov_shriojid: bzid,
        'historyCookie': '%E5%B9%B3%E6%98%8C%E5%99%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%87%AA%E7%84%B6%E8%B5%84%E6%BA%90%E5%92%8C%E8%A7%84%E5%88%92%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%86%9C%E4%B8%9A%E5%86%9C%E6%9D%91%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%B4%A2%E6%94%BF%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%9E%8D%E5%AA%92%E4%BD%93%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E7%A4%BA%E8%8C%83%E5%B9%BC%E5%84%BF%E5%9B%AD%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B1%9F%E5%8F%A3%E6%B0%B4%E4%B9%A1%E6%B0%B4%E5%88%A9%E9%A3%8E%E6%99%AF%E5%8C%BA%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%B1%80%2C%E5%8E%BF%E5%86%9C%E4%B8%9A%E5%86%9C%E6%9D%91%E5%B1%80',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        # 'Cookie': 'authenticatecenterjsessionid=NDYzMDcxZWItOTlkOC00ZDA4LTg3Y2UtZDQyOGM2NmM2NDdi; bz_govc_SHIROJSESSIONID=1aee0a6d-3f13-44bd-9a17-dfd99b0ed07a; historyCookie=%E5%B9%B3%E6%98%8C%E5%8E%BF%E9%95%87%E9%BE%99%E9%95%87%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%87%AA%E7%84%B6%E8%B5%84%E6%BA%90%E5%92%8C%E8%A7%84%E5%88%92%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%86%9C%E4%B8%9A%E5%86%9C%E6%9D%91%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%B4%A2%E6%94%BF%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%9E%8D%E5%AA%92%E4%BD%93%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E7%A4%BA%E8%8C%83%E5%B9%BC%E5%84%BF%E5%9B%AD%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B1%9F%E5%8F%A3%E6%B0%B4%E4%B9%A1%E6%B0%B4%E5%88%A9%E9%A3%8E%E6%99%AF%E5%8C%BA%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%B1%80%2C%E5%8E%BF%E5%86%9C%E4%B8%9A%E5%86%9C%E6%9D%91%E5%B1%80',
        'Referer': 'http://10.15.3.133:82/todolist/showDetail?typeCode=public_content&columnId=6603181&id=13940017&isOpen=true&_=1715850502563',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'contentId': contentId,
        'organId': organId,
        'attribute': '',
        'IsAjax': '1',
        'dataType': 'JSON',
        '_': '1715850503020',
    }
    url = 'http://10.15.3.133:' + conf.jiyuehua_port + '/public/content/getPublicContent'
    response = requests.get(
        url,
        params=params,
        cookies=cookies,
        headers=headers,
        verify=False,
    )

    return response.json()


def get_current_time():
    # 获取当前时间
    now = datetime.now()
    # 格式化时间为指定格式
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


def saveorupdate(content, item, bzid, jid):
    cookies = {
        'authenticatecenterjsessionid': jid,
        conf.jiyuehua_bzgov_shriojid: bzid,

    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'authenticatecenterjsessionid=ODU3OWEyNWYtZmUxMS00NDI4LTllN2UtZjIyN2FlNGQyZTQ0; bz_govc_SHIROJSESSIONID=3f0fb94f-46d9-49d8-b40b-2becc90873a9; historyCookie=%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%A1%8C%E6%94%BF%E5%AE%A1%E6%89%B9%E5%92%8C%E6%95%B0%E6%8D%AE%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%B4%E5%88%A9%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%AC%E5%AE%89%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%B8%8D%E5%8A%A8%E4%BA%A7%E7%99%BB%E8%AE%B0%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E5%B1%80%2C%E4%B8%AD%E5%9B%BD%E6%94%BF%E5%BA%9C%E7%BD%91%2C%E5%8E%BF%E5%8D%AB%E7%94%9F%E5%81%A5%E5%BA%B7%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E6%B3%93%E6%BA%90%E5%B8%B8%E9%9D%92%E5%85%AC%E7%94%A8%E4%BA%8B%E4%B8%9A%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8',
        'Origin': 'http://10.15.3.133:' + conf.jiyuehua_port,
        'Referer': 'http://10.15.3.133:' + conf.jiyuehua_port + '/todolist/showDetail?typeCode=public_content&columnId=' + str(
            content['data']['organId']) + '&id=' + str(content['data']['contentId']) + '&isOpen=true&_=1716198448001',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'IsAjax': '1',
        'dataType': 'JSON',
        '_': '0.753297256002835',
    }

    data = {
        'siteId': content['data']['siteId'],
        'id': content['data']['id'],
        'summarize': correct_string(content['data']['summarize'], item) if content['data']['summarize'] else
        content['data']['summarize'],
        'organId': content['data']['organId'],
        'contentId': content['data']['contentId'],
        'type': content['data']['type'],

        'sortNum': content['data']['sortNum'],
        'attachSavedName': content['data']['attachSavedName'],
        'attachRealName': content['data']['attachRealName'],
        'attachSize': content['data']['attachSize'],
        'catId': content['data']['catId'],
        'indexNum': content['data']['indexNum'],
        'fileNum': content['data']['fileNum'],
        'classIds': '',
        'parentClassIds': content['data']['parentClassIds'],
        'classNames': content['data']['siteId'],
        'synColumnIds': content['data']['synColumnIds'],
        'synColumnNames': content['data']['synColumnNames'],
        'synOrganCatIds': content['data']['synOrganCatIds'],
        'synOrganCatNames': content['data']['synOrganCatNames'],
        'synMsgCatIds': content['data']['synMsgCatIds'],
        'synMsgCatNames': content['data']['synMsgCatNames'],
        'effective': content['data']['effective'],
        'effectiveDate': content['data']['effectiveDate'],
        'repealDate': content['data']['repealDate'],
        'writtenDate': content['data']['writtenDate'],
        'title': correct_string(content['data']['title'], item),
        'keyWords': content['data']['keyWords'],
        'publishDate': content['data']['publishDate'],
        'createDate': content['data']['createDate'],
        'content': correct_string(content['data']['content'], item),
        'isPublish': '1',
        'isTop': content['data']['isTop'],
        'author': content['data']['author'],
        'resources': content['data']['resources'],
        'redirectLink': content['data']['redirectLink'],
        'remarks': correct_string(content['data']['remarks'], item) if content['data']['remarks'] else
        content['data']['remarks'],
        'sortDate': content['data']['sortDate'],
        'hit': content['data']['hit'],
        'link': content['data']['link'],
        'catName': content['data']['catName'],
        'organName': content['data']['organName'],
        'process': content['data']['process'],
        'counts': content['data']['counts'],
        'isInvalid': content['data']['isInvalid'],
        'invalidReason': content['data']['invalidReason'],
        'filePath': content['data']['filePath'],
        'relContentId': content['data']['relContentId'],
        'attribute': content['data']['attribute'],
        'titleColor': content['data']['titleColor'],
        'isBold': content['data']['isBold'],
        'isUnderline': content['data']['isUnderline'],
        'isTilt': content['data']['isTilt'],
        'subTitle': content['data']['subTitle'],
        'article': content['data']['article'],
        'isAllowComments': content['data']['isAllowComments'],
        'videoStatus': content['data']['videoStatus'],
        'oldSchemaId': content['data']['oldSchemaId'],
        'logStr': content['data']['logStr'],
        'referedNews': content['data']['referedNews'],
        'referNews': content['data']['referNews'],
        'explainType': content['data']['explainType'],
        'relContentIds': content['data']['relContentIds'],
        'relLink': content['data']['relLink'],
        'relContentTitles': content['data']['relContentTitles'],
        'isPush': content['data']['isPush'],
        'invalidType': content['data']['invalidType'],
        'invalidFileType': content['data']['invalidFileType'],
        'updateDate': '',
        'readFileType': content['data']['readFileType'],
        'relInfo': content['data']['relInfo'],
        'topTitle': content['data']['topTitle'],
        'relExplainType': content['data']['relExplainType'],
        'explainId': content['data']['explainId'],
        'isSpecial': content['data']['isSpecial'],
        'themeNote': content['data']['themeNote'],
        'wordDocName': content['data']['wordDocName'],
        'wordDocPath': content['data']['wordDocPath'],
        'pdfDocName': content['data']['pdfDocName'],
        'pdfDocPath': content['data']['pdfDocPath'],
        'publishDepartment': content['data']['publishDepartment'],
        'startDate': content['data']['startDate'],
        'endDate': content['data']['endDate'],
        'publicYear': content['data']['publicYear'],
        'organCode': content['data']['organCode'],
        'imageLink': content['data']['imageLink'],
        'regNo': content['data']['regNo'],
        'pubMode': content['data']['pubMode'],
        'pubRange': content['data']['pubRange'],
        'abolishDate': content['data']['abolishDate'],
        'writeDate': content['data']['writeDate'],
        'regDate': content['data']['regDate'],
        'pubOrg': content['data']['pubOrg'],
        'cateCode': content['data']['cateCode'],
        'appendixPath': content['data']['appendixPath'],
        'appendixName': content['data']['appendixName'],
        'ownerDept': content['data']['ownerDept'],
        'explainTypes': content['data']['explainTypes'],
        'explainTitles': content['data']['explainTitles'],
        'explainLinks': content['data']['explainLinks'],
        'docExplainRelateJson': content['data']['docExplainRelateJson'],
        'pushStatus': content['data']['pushStatus'],
        'sourcesInfoId': content['data']['sourcesInfoId'],
        'sourcesClassId': content['data']['sourcesClassId'],
        'opeStatus': content['data']['opeStatus'],
        'ectLevel': content['data']['ectLevel'],
        'resClassifyArray': content['data']['resClassifyArray'],
        'isNormalPolicy': content['data']['isNormalPolicy'],
        'policyPushStatus': content['data']['policyPushStatus'],
        'valid': content['data']['valid'],
        'isCurSite': content['data']['isCurSite'],
        'domain': content['data']['domain'],
        'policyCash': content['data']['policyCash'],
        'remoteContent': content['data']['content'],
    }

    response = requests.post(
        'http://10.15.3.133:' + conf.jiyuehua_port + '/public/content/saveOrUpdate',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )

    return response.json()


def saveorupdate2(content, wrong_words, right, bzid, jid):
    cookies = {
        'authenticatecenterjsessionid': jid,
        conf.jiyuehua_bzgov_shriojid: bzid,
        'historyCookie': '%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%A1%8C%E6%94%BF%E5%AE%A1%E6%89%B9%E5%92%8C%E6%95%B0%E6%8D%AE%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%B4%E5%88%A9%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%AC%E5%AE%89%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%B8%8D%E5%8A%A8%E4%BA%A7%E7%99%BB%E8%AE%B0%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E5%B1%80%2C%E4%B8%AD%E5%9B%BD%E6%94%BF%E5%BA%9C%E7%BD%91%2C%E5%8E%BF%E5%8D%AB%E7%94%9F%E5%81%A5%E5%BA%B7%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E6%B3%93%E6%BA%90%E5%B8%B8%E9%9D%92%E5%85%AC%E7%94%A8%E4%BA%8B%E4%B8%9A%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'authenticatecenterjsessionid=ODU3OWEyNWYtZmUxMS00NDI4LTllN2UtZjIyN2FlNGQyZTQ0; bz_govc_SHIROJSESSIONID=3f0fb94f-46d9-49d8-b40b-2becc90873a9; historyCookie=%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%A1%8C%E6%94%BF%E5%AE%A1%E6%89%B9%E5%92%8C%E6%95%B0%E6%8D%AE%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%B4%E5%88%A9%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%AC%E5%AE%89%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%B8%8D%E5%8A%A8%E4%BA%A7%E7%99%BB%E8%AE%B0%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E5%B1%80%2C%E4%B8%AD%E5%9B%BD%E6%94%BF%E5%BA%9C%E7%BD%91%2C%E5%8E%BF%E5%8D%AB%E7%94%9F%E5%81%A5%E5%BA%B7%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E6%B3%93%E6%BA%90%E5%B8%B8%E9%9D%92%E5%85%AC%E7%94%A8%E4%BA%8B%E4%B8%9A%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8',
        'Origin': 'http://10.15.3.133:' + conf.jiyuehua_port,
        'Referer': 'http://10.15.3.133:' + conf.jiyuehua_port + '/todolist/showDetail?typeCode=public_content&columnId=6602061&id=13939642&isOpen=true&_=1716198448001',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'IsAjax': '1',
        'dataType': 'JSON',
        '_': '0.4361940897591683',
    }

    data = {
        'siteId': content['data']['siteId'],
        'id': content['data']['id'],
        'summarize': content['data']['summarize'],
        'organId': content['data']['organId'],
        'contentId': content['data']['contentId'],
        'type': content['data']['type'],

        'sortNum': content['data']['sortNum'],
        'attachSavedName': content['data']['attachSavedName'],
        'attachRealName': content['data']['attachRealName'],
        # 'attachSize': content['data']['attachSize'],
        'catId': content['data']['catId'],
        'indexNum': content['data']['indexNum'],
        'fileNum': content['data']['fileNum'],
        # 'classIds': content['data']['classIds'],
        # 'parentClassIds': content['data']['parentClassIds'],
        # 'classNames': content['data']['siteId'],
        'synColumnIds': content['data']['synColumnIds'],
        # 'synColumnNames': content['data']['siteId'],
        'synOrganCatIds': content['data']['synOrganCatIds'],
        # 'synOrganCatNames': content['data']['siteId'],
        'synMsgCatIds': content['data']['synMsgCatIds'],
        # 'synMsgCatNames': content['data']['siteId'],
        # 'effective': content['data']['siteId'],
        'effectiveDate': content['data']['effectiveDate'],
        'repealDate': content['data']['repealDate'],
        # 'writtenDate': content['data']['siteId'],
        'title': correct_string2(content['data']['title'], wrong_words, right),
        'keyWords': content['data']['keyWords'],
        'publishDate': content['data']['publishDate'],
        'createDate': content['data']['createDate'],
        'content': correct_string2(content['data']['content'], wrong_words, right),
        'isPublish': content['data']['isPublish'],
        'isTop': content['data']['isTop'],
        'author': content['data']['author'],
        'resources': content['data']['resources'],
        'redirectLink': content['data']['redirectLink'],
        'remarks': correct_string2(content['data']['remarks'], wrong_words, right) if content['data']['remarks'] else
        content['data']['remarks'],
        'sortDate': content['data']['sortDate'],
        'hit': content['data']['hit'],
        # 'link': content['data']['isTop'],
        'catName': content['data']['catName'],
        'organName': content['data']['organName'],
        # 'process':content['data']['isTop'],
        # 'counts': content['data']['isTop'],
        'isInvalid': content['data']['isInvalid'],
        'invalidReason': content['data']['invalidReason'],
        # 'filePath': content['data']['isTop'],
        # 'relContentId': content['data']['isTop'],
        # 'attribute': content['data']['isTop'],
        # 'titleColor': content['data']['isTop'],
        'isBold': content['data']['isBold'],
        'isUnderline': content['data']['isUnderline'],
        'isTilt': content['data']['isTilt'],
        'subTitle': content['data']['subTitle'],
        # 'article': content['data']['isTop'],
        'isAllowComments': content['data']['isAllowComments'],
        'videoStatus': content['data']['videoStatus'],
        # 'oldSchemaId': content['data']['isTop'],
        # 'logStr': content['data']['isTop'],
        'referedNews': content['data']['referedNews'],
        'referNews': content['data']['referNews'],
        'explainType': content['data']['explainType'],
        # 'relContentIds':content['data']['isTop'],
        # 'relLink': content['data']['isTop'],
        # 'relContentTitles':content['data']['isTop'],
        'isPush': content['data']['isPush'],
        # 'invalidType': content['data']['isTop'],
        # 'invalidFileType': content['data']['isTop'],
        'updateDate': get_current_time(),
        'readFileType': content['data']['readFileType'],
        # 'relInfo': content['data']['isTop'],
        'topTitle': content['data']['topTitle'],
        # 'relExplainType': content['data']['relExplainType'],
        # 'explainId': content['data']['isPush'],
        # 'isSpecial': content['data']['isPush'],
        'themeNote': content['data']['themeNote'],
        'wordDocName': content['data']['wordDocName'],
        'wordDocPath': content['data']['wordDocPath'],
        'pdfDocName': content['data']['pdfDocName'],
        'pdfDocPath': content['data']['pdfDocPath'],
        'publishDepartment': content['data']['publishDepartment'],
        # 'startDate': content['data']['isPush'],
        # 'endDate': content['data']['isPush'],
        'publicYear': content['data']['publicYear'],
        # 'organCode': content['data']['isPush'],
        'imageLink': content['data']['imageLink'],
        'regNo': content['data']['regNo'],
        'pubMode': content['data']['pubMode'],
        'pubRange': content['data']['pubRange'],
        # 'abolishDate': content['data']['isPush'],
        # 'writeDate': content['data']['isPush'],
        # 'regDate': content['data']['isPush'],
        'pubOrg': content['data']['pubOrg'],
        'cateCode': content['data']['cateCode'],
        'appendixPath': content['data']['appendixPath'],
        'appendixName': content['data']['appendixName'],
        'ownerDept': content['data']['ownerDept'],
        'explainTypes': content['data']['explainTypes'],
        'explainTitles': content['data']['explainTitles'],
        'explainLinks': content['data']['explainLinks'],
        'docExplainRelateJson': content['data']['docExplainRelateJson'],
        # 'pushStatus': '',
        # 'sourcesInfoId': '',
        # 'sourcesClassId': '',
        # 'opeStatus': '',
        # 'ectLevel': '',
        # 'resClassifyArray': '',
        'isNormalPolicy': content['data']['isNormalPolicy'],
        # 'policyPushStatus': '',
        # 'valid': '',
        'isCurSite': content['data']['isCurSite'],
        # 'domain': '',
        # 'policyCash': '',
        'remoteContent': content['data']['content'],
    }

    response = requests.post(
        'http://10.15.3.133:' + conf.jiyuehua_port + '/public/content/saveOrUpdate',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )

    return response.json()


def correct_string2(content, wrong_list, correct):
    """
    将字符串 content 中的所有 wrong_list 中的词替换为 correct。

    :param content: 原始字符串
    :param wrong_list: 错误字符串的列表
    :param correct: 正确的字符串
    :return: 更正后的字符串
    """
    for wrong in wrong_list:
        content = content.replace(wrong, correct)
    return content

def deal_new_right_words(wrong, right):
    replacements = []
    
    if '疑似时间错误' in right:
        # 使用列表存储需要替换的时间词
        time_words = ['上午', '下午', '晚上', '早上', '晚']
        for word in time_words:
            if word in wrong:
                right = wrong.replace(word, '')
                break
        print("real right", right)
        replacements.append((wrong, right))
    # 处理"两会"的情况
    elif '注意区分是全国两会还是地方两会' in right:
        right = '地方"两会"'
        print("real right", right)
        replacements.append((wrong, right))
    
    elif '涉及到' in wrong:
        right = '涉及'
        print("real right", right)
        replacements.append((wrong, right))
    else:
        # 检查right是否包含wrong
        if wrong in right:
            # 添加原始替换对
            replacements.append((wrong, right))
            # 添加新的替换对
            new_wrong = right.replace(wrong, right)
            replacements.append((new_wrong, right))
        else:
            replacements.append((wrong, right))
            
    return replacements


def correct_string(content, item):
    for replacement in item:
        wrong = replacement['sensitiveWords']
        l = deal_new_right_words(wrong,replacement['recommendUpdate'].split('|')[0])
        for wrong_word, right_word in l:
            content = content.replace(wrong_word, right_word)

    return content


def modify(organId, contentId, wrong, right):
    content = getcontent(organId, contentId)
    saveorupdate(content, wrong, right)


if __name__ == '__main__':
    print(deal_new_right_words("十九届","党的十九届"))
