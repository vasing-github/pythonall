import requests
from nanjiang.kaipumodify.cfg import conf
def getcontent(id,bzid,jid):
    cookies = {
        'authenticatecenterjsessionid': jid,
        conf.jiyuehua_bzgov_shriojid: bzid,
        'historyCookie': '%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%A1%8C%E6%94%BF%E5%AE%A1%E6%89%B9%E5%92%8C%E6%95%B0%E6%8D%AE%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%B4%E5%88%A9%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%AC%E5%AE%89%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%B8%8D%E5%8A%A8%E4%BA%A7%E7%99%BB%E8%AE%B0%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E5%B1%80%2C%E4%B8%AD%E5%9B%BD%E6%94%BF%E5%BA%9C%E7%BD%91%2C%E5%8E%BF%E5%8D%AB%E7%94%9F%E5%81%A5%E5%BA%B7%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E6%B3%93%E6%BA%90%E5%B8%B8%E9%9D%92%E5%85%AC%E7%94%A8%E4%BA%8B%E4%B8%9A%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        # 'Cookie': 'authenticatecenterjsessionid=ODU3OWEyNWYtZmUxMS00NDI4LTllN2UtZjIyN2FlNGQyZTQ0; bz_govc_SHIROJSESSIONID=3f0fb94f-46d9-49d8-b40b-2becc90873a9; historyCookie=%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%A1%8C%E6%94%BF%E5%AE%A1%E6%89%B9%E5%92%8C%E6%95%B0%E6%8D%AE%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%B4%E5%88%A9%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%AC%E5%AE%89%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%B8%8D%E5%8A%A8%E4%BA%A7%E7%99%BB%E8%AE%B0%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E5%B1%80%2C%E4%B8%AD%E5%9B%BD%E6%94%BF%E5%BA%9C%E7%BD%91%2C%E5%8E%BF%E5%8D%AB%E7%94%9F%E5%81%A5%E5%BA%B7%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E6%B3%93%E6%BA%90%E5%B8%B8%E9%9D%92%E5%85%AC%E7%94%A8%E4%BA%8B%E4%B8%9A%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8',
        'Referer': 'http://10.15.3.133:'+conf.jiyuehua_port+'/todolist/showDetail?typeCode=articleNews&columnId=6790051&id=13650431&isOpen=true&_=1716191454907',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'IsAjax': '1',
        'dataType': 'JSON',
        '_': '1716191455319',
        'id': id,
        'recordStatus': 'Normal',
    }

    response = requests.get(
        'http://10.15.3.133:'+conf.jiyuehua_port+'/articleNews/getArticleContent',
        params=params,
        cookies=cookies,
        headers=headers,
        verify=False,
    )

    return response.json()


def savearticnews2(content, wrong_words, right,bz_id,jid):
    cookies = {
        'authenticatecenterjsessionid': jid,
        conf.jiyuehua_bzgov_shriojid: bz_id,
        'historyCookie': '%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%A1%8C%E6%94%BF%E5%AE%A1%E6%89%B9%E5%92%8C%E6%95%B0%E6%8D%AE%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%B4%E5%88%A9%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%AC%E5%AE%89%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%B8%8D%E5%8A%A8%E4%BA%A7%E7%99%BB%E8%AE%B0%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E5%B1%80%2C%E4%B8%AD%E5%9B%BD%E6%94%BF%E5%BA%9C%E7%BD%91%2C%E5%8E%BF%E5%8D%AB%E7%94%9F%E5%81%A5%E5%BA%B7%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E6%B3%93%E6%BA%90%E5%B8%B8%E9%9D%92%E5%85%AC%E7%94%A8%E4%BA%8B%E4%B8%9A%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'authenticatecenterjsessionid=ODU3OWEyNWYtZmUxMS00NDI4LTllN2UtZjIyN2FlNGQyZTQ0; bz_govc_SHIROJSESSIONID=3f0fb94f-46d9-49d8-b40b-2becc90873a9; historyCookie=%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%A1%8C%E6%94%BF%E5%AE%A1%E6%89%B9%E5%92%8C%E6%95%B0%E6%8D%AE%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%B4%E5%88%A9%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%AC%E5%AE%89%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%B8%8D%E5%8A%A8%E4%BA%A7%E7%99%BB%E8%AE%B0%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E5%B1%80%2C%E4%B8%AD%E5%9B%BD%E6%94%BF%E5%BA%9C%E7%BD%91%2C%E5%8E%BF%E5%8D%AB%E7%94%9F%E5%81%A5%E5%BA%B7%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E6%B3%93%E6%BA%90%E5%B8%B8%E9%9D%92%E5%85%AC%E7%94%A8%E4%BA%8B%E4%B8%9A%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8',
        'Origin': 'http://10.15.3.133:'+conf.jiyuehua_port,
        'Referer': 'http://10.15.3.133:'+conf.jiyuehua_port+'/todolist/showDetail?typeCode=articleNews&columnId=6789801&id=13448751&isOpen=true&_=1716193031308',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'IsAjax': '1',
        'dataType': 'JSON',
        '_': '0.6454915144417703',
    }

    tittle = content['data']['article']['title']
    subTitle = content['data']['article']['subTitle']
    shortTitle = content['data']['article']['shortTitle']
    remarks = content['data']['article']['remarks']
    content1 = content['data']['content']
    for wrong in wrong_words:
        tittle = tittle.replace(wrong, right)
        subTitle = subTitle.replace(wrong, right) if subTitle else None
        shortTitle = shortTitle.replace(wrong, right) if shortTitle else None
        remarks = remarks.replace(wrong, right) if remarks else None
        content1 = content1.replace(wrong, right)

    data = {
        'remoteContent': content['data']['content'],
        'fromIndex': '',
        'id': content['data']['article']['id'] if content and content.get('data') and content['data'].get('article') and content['data']['article'].get('id') else None,
        'columnId': content['data']['article']['columnId'] if content and content.get('data') and content['data'].get(
            'article') and content['data']['article'].get('columnId') else None,
        'siteId': content['data']['article']['siteId'] if content and content.get('data') and content['data'].get(
            'article') and content['data']['article'].get('siteId') else None,

        'title': tittle,

        'subTitle': subTitle,

        'shortTitle': shortTitle,
        'author': content['data']['article']['author'],
        'responsibilityEditor': content['data']['article']['responsibilityEditor'],
        'resources': content['data']['article']['resources'],
        'redirectLink': content['data']['article']['redirectLink'],
        'imageLink': content['data']['article']['imageLink'],
        'isNew': content['data']['article']['isNew'],
        'isTop': content['data']['article']['isTop'],
        # 'topValidDate': '',
        'isBold': '0',
        'isUnderline': '0',
        'isTilt': '0',
        'titleColor': '',
        'remarks': remarks,
        'content': content1,
        'isPublish': content['data']['article']['isPublish'],
        'publishDate': content['data']['article']['publishDate'],
        'typeCode': content['data']['article']['typeCode'],
        'isAllowComments': content['data']['article']['isAllowComments'],
        'quoteStatus': content['data']['article']['quoteStatus'],
        'recordStatus': content['data']['article']['recordStatus'],
        'workFlowStatus': content['data']['article']['workFlowStatus'],
        'videoStatus': content['data']['article']['videoStatus'],
        # 'allImgSrc': '',
        # 'flag': 'true',
        # 'imgNum': '0',
        'subIsBold': content['data']['article']['subIsBold'],
        'subIsTilt': content['data']['article']['subIsTilt'],
        'subIsUnderline': content['data']['article']['subIsUnderline'],
        'subTitleColor': content['data']['article']['subTitleColor'],
        'topTitle': content['data']['article']['topTitle'],
        'topIsBold': content['data']['article']['topIsBold'],
        'topIsTilt': content['data']['article']['topIsTilt'],
        'topIsUnderline': content['data']['article']['topIsUnderline'],
        'topTitleColor': content['data']['article']['topTitleColor'],
        'smallTitle': content['data']['article']['smallTitle'],
        'smallIsBold': content['data']['article']['smallIsBold'],
        'smallIsTilt': content['data']['article']['smallIsTilt'],
        'smallIsUnderline': content['data']['article']['smallIsUnderline'],
        'smallTitleColor': content['data']['article']['smallTitleColor'],
        'qsYear': content['data']['article']['qsYear'],
        'qsMonth': content['data']['article']['qsMonth'],
        'qsNum': content['data']['article']['qsNum'],
        'isLight': content['data']['article']['isLight'],
        'smallLinkUrl': content['data']['article']['smallLinkUrl'],
        'smallLinkTitle': content['data']['article']['smallLinkTitle'],
        'picUrl': content['data']['article']['picUrl'],
        'normalUrl': content['data']['article']['normalUrl'],
        'recommend': content['data']['article']['recommend'],
        'keyWords': content['data']['article']['keyWords'],
        # 'reportType': '',
        # 'interviewContentId': '',
        # 'newsThemeType': '',
        'createOrganId': content['data']['article']['createOrganId'],
        # 'pubTime': '',
        # 'explainOrgan': '',
        # 'explainTypes': '',
        # 'explainForms': '',
        # 'explainTitles': '',
        # 'explainLinks': '',
        # 'editor': '',
        'num': content['data']['article']['num'],
        'member': content['data']['article']['member'],
        'memberConStu': content['data']['article']['memberConStu'],
        'backReason': content['data']['article']['backReason'],
        # 'memPutDate': '',
        # 'interviewInfoId': '',
        # 'isLink': '0',
        # 'articleText': ' 11月2日上午，县养路段召开学习贯彻中国共产党平昌县第十四次代表大会精神专题会议。\n 会议要求，全体干部职工要自觉把思想和行动统一到县第十四次党代会精神上来，把智慧和力量凝聚到落实党代会提出的目标任务上来，依托会前学、集中学、自学等形式，沉下心来认真学习，学深悟透，入脑入心，努力推动县第十四次党代会精神在平昌公路养护领域落地生效。\n 会议强调，结合公路养护工作实际，以第十四次党代会精神为引领，紧盯目标任务，强化工作推进，进一步在工作标准上再提高，进一步在工作效率上再提升，进一步在作风建设上再严密，进一步在精神状态上再提振，着力以更高的效率统筹协调、更高的质量督促落实、更高的标准强化保障，全面完成县委县政府及市县主管部门交办的各项目标任务，为平昌公路养护事业高质量发展贡献公路人力量，以优异的成绩为县委县政府交上一份满意的答卷。.\n \n \n \n',
        # 'hit': '0',
    }

    response = requests.post(
        'http://10.15.3.133:'+conf.jiyuehua_port+'/articleNews/saveArticleNews',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )

    return response.json()

def muti_argument_replace(content,item, str):

    # 遍历列表并替换
    if content and content.get('data') and content['data'].get('article') and content['data']['article'].get(str):
        new_argu = content['data']['article'][str]
        for replacement in item:
            wrong = replacement['sensitiveWords']
            right = replacement['recommendUpdate'].split('|')[0]
            new_argu = new_argu.replace(wrong, right)
    else:
        return None

    return new_argu

def repalce_content(content,item):
    new_argu = content['data']['content']
    for replacement in item:
        wrong = replacement['sensitiveWords']
        right = replacement['recommendUpdate'].split('|')[0]
        new_argu = new_argu.replace(wrong, right)
    return new_argu


def savearticnews(content,item, bz_id,jid):
    cookies = {
        'authenticatecenterjsessionid': jid,
        conf.jiyuehua_bzgov_shriojid: bz_id,
        'historyCookie': '%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%A1%8C%E6%94%BF%E5%AE%A1%E6%89%B9%E5%92%8C%E6%95%B0%E6%8D%AE%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%B4%E5%88%A9%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%AC%E5%AE%89%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%B8%8D%E5%8A%A8%E4%BA%A7%E7%99%BB%E8%AE%B0%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E5%B1%80%2C%E4%B8%AD%E5%9B%BD%E6%94%BF%E5%BA%9C%E7%BD%91%2C%E5%8E%BF%E5%8D%AB%E7%94%9F%E5%81%A5%E5%BA%B7%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E6%B3%93%E6%BA%90%E5%B8%B8%E9%9D%92%E5%85%AC%E7%94%A8%E4%BA%8B%E4%B8%9A%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'authenticatecenterjsessionid=ODU3OWEyNWYtZmUxMS00NDI4LTllN2UtZjIyN2FlNGQyZTQ0; bz_govc_SHIROJSESSIONID=3f0fb94f-46d9-49d8-b40b-2becc90873a9; historyCookie=%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E5%8A%9E%E5%85%AC%E5%AE%A4%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E8%A1%8C%E6%94%BF%E5%AE%A1%E6%89%B9%E5%92%8C%E6%95%B0%E6%8D%AE%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E6%B0%B4%E5%88%A9%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E5%85%AC%E5%AE%89%E5%B1%80%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%B8%8D%E5%8A%A8%E4%BA%A7%E7%99%BB%E8%AE%B0%E4%B8%AD%E5%BF%83%2C%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93%E5%B1%80%2C%E4%B8%AD%E5%9B%BD%E6%94%BF%E5%BA%9C%E7%BD%91%2C%E5%8E%BF%E5%8D%AB%E7%94%9F%E5%81%A5%E5%BA%B7%E5%B1%80%2C%E5%9B%9B%E5%B7%9D%E6%B3%93%E6%BA%90%E5%B8%B8%E9%9D%92%E5%85%AC%E7%94%A8%E4%BA%8B%E4%B8%9A%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%2C%E5%9B%BD%E7%BD%91%E5%B9%B3%E6%98%8C%E5%8E%BF%E4%BE%9B%E7%94%B5%E5%85%AC%E5%8F%B8',
        'Origin': 'http://10.15.3.133:'+conf.jiyuehua_port,
        'Referer': 'http://10.15.3.133:'+conf.jiyuehua_port+'/todolist/showDetail?typeCode=articleNews&columnId=6789801&id=13448751&isOpen=true&_=1716193031308',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        'IsAjax': '1',
        'dataType': 'JSON',
        '_': '0.6454915144417703',
    }

    data = {
        'remoteContent': content['data']['content'],
        'fromIndex': '',
        'id': content['data']['article']['id'] if content and content.get('data') and content['data'].get('article') and content['data']['article'].get('id') else None,
        'columnId': content['data']['article']['columnId'] if content and content.get('data') and content['data'].get(
            'article') and content['data']['article'].get('columnId') else None,
        'siteId': content['data']['article']['siteId'] if content and content.get('data') and content['data'].get(
            'article') and content['data']['article'].get('siteId') else None,


        'title':muti_argument_replace(content, item, 'title'),
        'subTitle': muti_argument_replace(content, item, 'subTitle'),

        'shortTitle': muti_argument_replace(content, item, 'shortTitle'),
        'author': content['data']['article']['author'],
        'responsibilityEditor': content['data']['article']['responsibilityEditor'],
        'resources': content['data']['article']['resources'],
        'redirectLink': content['data']['article']['redirectLink'],
        'imageLink': content['data']['article']['imageLink'],
        'isNew': content['data']['article']['isNew'],
        'isTop': content['data']['article']['isTop'],
        # 'topValidDate': '',
        'isBold': '0',
        'isUnderline': '0',
        'isTilt': '0',
        'titleColor': '',
        'remarks': muti_argument_replace(content, item, 'remarks'),
        'content': repalce_content(content, item),
        'isPublish': '1',
        'publishDate': content['data']['article']['publishDate'],
        'typeCode': content['data']['article']['typeCode'],
        'isAllowComments': content['data']['article']['isAllowComments'],
        'quoteStatus': content['data']['article']['quoteStatus'],
        'recordStatus': content['data']['article']['recordStatus'],
        'workFlowStatus': content['data']['article']['workFlowStatus'],
        'videoStatus': content['data']['article']['videoStatus'],
        # 'allImgSrc': '',
        # 'flag': 'true',
        # 'imgNum': '0',
        'subIsBold': content['data']['article']['subIsBold'],
        'subIsTilt': content['data']['article']['subIsTilt'],
        'subIsUnderline': content['data']['article']['subIsUnderline'],
        'subTitleColor': content['data']['article']['subTitleColor'],
        'topTitle': content['data']['article']['topTitle'],
        'topIsBold': content['data']['article']['topIsBold'],
        'topIsTilt': content['data']['article']['topIsTilt'],
        'topIsUnderline': content['data']['article']['topIsUnderline'],
        'topTitleColor': content['data']['article']['topTitleColor'],
        'smallTitle': content['data']['article']['smallTitle'],
        'smallIsBold': content['data']['article']['smallIsBold'],
        'smallIsTilt': content['data']['article']['smallIsTilt'],
        'smallIsUnderline': content['data']['article']['smallIsUnderline'],
        'smallTitleColor': content['data']['article']['smallTitleColor'],
        'qsYear': content['data']['article']['qsYear'],
        'qsMonth': content['data']['article']['qsMonth'],
        'qsNum': content['data']['article']['qsNum'],
        'isLight': content['data']['article']['isLight'],
        'smallLinkUrl': content['data']['article']['smallLinkUrl'],
        'smallLinkTitle': content['data']['article']['smallLinkTitle'],
        'picUrl': content['data']['article']['picUrl'],
        'normalUrl': content['data']['article']['normalUrl'],
        'recommend': content['data']['article']['recommend'],
        'keyWords': content['data']['article']['keyWords'],
        # 'reportType': '',
        # 'interviewContentId': '',
        # 'newsThemeType': '',
        'createOrganId': content['data']['article']['createOrganId'],
        # 'pubTime': '',
        # 'explainOrgan': '',
        # 'explainTypes': '',
        # 'explainForms': '',
        # 'explainTitles': '',
        # 'explainLinks': '',
        # 'editor': '',
        'num': content['data']['article']['num'],
        'member': content['data']['article']['member'],
        'memberConStu': content['data']['article']['memberConStu'],
        'backReason': content['data']['article']['backReason'],
        # 'memPutDate': '',
        # 'interviewInfoId': '',
        # 'isLink': '0',
        # 'articleText': ' 11月2日上午，县养路段召开学习贯彻中国共产党平昌县第十四次代表大会精神专题会议。\n 会议要求，全体干部职工要自觉把思想和行动统一到县第十四次党代会精神上来，把智慧和力量凝聚到落实党代会提出的目标任务上来，依托会前学、集中学、自学等形式，沉下心来认真学习，学深悟透，入脑入心，努力推动县第十四次党代会精神在平昌公路养护领域落地生效。\n 会议强调，结合公路养护工作实际，以第十四次党代会精神为引领，紧盯目标任务，强化工作推进，进一步在工作标准上再提高，进一步在工作效率上再提升，进一步在作风建设上再严密，进一步在精神状态上再提振，着力以更高的效率统筹协调、更高的质量督促落实、更高的标准强化保障，全面完成县委县政府及市县主管部门交办的各项目标任务，为平昌公路养护事业高质量发展贡献公路人力量，以优异的成绩为县委县政府交上一份满意的答卷。.\n \n \n \n',
        # 'hit': '0',
    }

    response = requests.post(
        'http://10.15.3.133:'+conf.jiyuehua_port+'/articleNews/saveArticleNews',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )

    return response.json()

def modify(id, wrong, right):
    content = getcontent(id)

    savearticnews(content, wrong, right)


if __name__ == '__main__':
    # content = getcontent(13945499,text.bz_gov_id,text.jid)
    # if content['status'] == -9:
    #     print("jjj")
    # print(content)
    pass