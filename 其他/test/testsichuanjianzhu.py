import requests
import time
def shua(s):

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'text/plain',
        'Origin': 'https://px.scbuilder.com',
        'Referer': 'https://px.scbuilder.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    # data = '{"data":{"core":{"primaryKey":"65287618fc9e43f58a230fd1c678eab2","courseRecordId":"989d62670b0d40dca0945bf4752987ab","coursewareRecordId":"4335a45f04f04bd2b6f412d93e946508","lessonId":"2c9881ce90449bb001905ce7d19c23fd","lessonLocation":"","studyMode":1,"studyLastScale":2659.51013,"studyCurrentScale":1875,"studySchedule":100,"timingMode":"schedule","studyStatus":1,"lessonStatus":"not attempted","token":"90e031508d3e40a487d6833ee2ae7380","intervalTime":30},"extend":{"test":false,"markers":[{"key":"SchemeId","value":"2c9880c9907395560190ca60862d459d"},{"key":"LearningId","value":"2c9880c9907395560190ca6086f0459e"},{"key":"ChooseRuleId","value":"2c98807e90bb160b0190ca5d34060537"},{"key":"PackageId","value":"c7b93f8f1448442f8b241b97acd8b621"}],"objectList":[{"objectId":"2c9880c9907395560190ca60862d459d","type":"SchemeId"},{"objectId":"2c9880c9907395560190ca6086f0459e","type":"LearningId"},{"objectId":"2c98807e90bb160b0190ca5d34060537","type":"ChooseRuleId"},{"objectId":"c7b93f8f1448442f8b241b97acd8b621","type":"PackageId"}],"guid":"307301feece4467883d34c79c81a0077","plmId":"40289b7c601f2d9701601f2ff93f0000","pvmId":"40289b7c601f2d9701601f2ff9a60001","prmId":"40289b7c601f731801601f75222b0001","subPrmId":"40289b7c601f731801601f75227f0003","unitId":"-1","orgId":"-1","dataProjectId":"40289b7c601f731801601f75222b0001","dataPlatformVersionId":"40289b7c601f2d9701601f2ff9a60001","originalAbilityId":"40289b7c601f2d9701601f2ff9a60001"}},"head":{"appVersion":"1.0.0","osPlatform":"web","requestTime":'+str(s)+'}}'
    # data = '{"data":{"core":{"primaryKey":"299257e367e4497b87e3a1b9229a13b6","courseRecordId":"989d62670b0d40dca0945bf4752987ab","coursewareRecordId":"19b831bbb4f6455b8f3fb7ac240051a1","lessonId":"2c9881ce90449bb001905ce7d19c23fd","lessonLocation":"","studyMode":1,"studyLastScale":2400.390251,"studyCurrentScale":99,"studySchedule":100,"timingMode":"schedule","studyStatus":1,"lessonStatus":"not attempted","token":"5d4ad1582e2246d4bd2a9838277e689f","intervalTime":30},"extend":{"test":false,"markers":[{"key":"SchemeId","value":"2c9880c9907395560190ca60862d459d"},{"key":"LearningId","value":"2c9880c9907395560190ca6086f0459e"},{"key":"ChooseRuleId","value":"2c98807e90bb160b0190ca5d34060537"},{"key":"PackageId","value":"c7b93f8f1448442f8b241b97acd8b621"}],"objectList":[{"objectId":"2c9880c9907395560190ca60862d459d","type":"SchemeId"},{"objectId":"2c9880c9907395560190ca6086f0459e","type":"LearningId"},{"objectId":"2c98807e90bb160b0190ca5d34060537","type":"ChooseRuleId"},{"objectId":"c7b93f8f1448442f8b241b97acd8b621","type":"PackageId"}],"guid":"ad91c41cfe86445b89e1cf15248dfc83","plmId":"40289b7c601f2d9701601f2ff93f0000","pvmId":"40289b7c601f2d9701601f2ff9a60001","prmId":"40289b7c601f731801601f75222b0001","subPrmId":"40289b7c601f731801601f75227f0003","unitId":"-1","orgId":"-1","dataProjectId":"40289b7c601f731801601f75222b0001","dataPlatformVersionId":"40289b7c601f2d9701601f2ff9a60001","originalAbilityId":"40289b7c601f2d9701601f2ff9a60001"}},"head":{"appVersion":"1.0.0","osPlatform":"web","requestTime":'+str(s)+'}}'
    data = '{"data":{"core":{"primaryKey":"110834efbc524c2cbfc7eb67e979d7f8","courseRecordId":"989d62670b0d40dca0945bf4752987ab","coursewareRecordId":"1e26ae97f6634c6e9edacd0b5aa0487d","lessonId":"2c9881ce90449bb001905ce7d19c23fd","lessonLocation":"","studyMode":1,"studyLastScale":2880.725341,"studyCurrentScale":0,"studySchedule":100,"timingMode":"schedule","studyStatus":1,"lessonStatus":"not attempted","token":"b35ab1abe69d4da3b662a91ed7405f4c","intervalTime":30},"extend":{"test":false,"markers":[{"key":"SchemeId","value":"2c9880c9907395560190ca60862d459d"},{"key":"LearningId","value":"2c9880c9907395560190ca6086f0459e"},{"key":"ChooseRuleId","value":"2c98807e90bb160b0190ca5d34060537"},{"key":"PackageId","value":"c7b93f8f1448442f8b241b97acd8b621"}],"objectList":[{"objectId":"2c9880c9907395560190ca60862d459d","type":"SchemeId"},{"objectId":"2c9880c9907395560190ca6086f0459e","type":"LearningId"},{"objectId":"2c98807e90bb160b0190ca5d34060537","type":"ChooseRuleId"},{"objectId":"c7b93f8f1448442f8b241b97acd8b621","type":"PackageId"}],"guid":"15772803b82c4ab98277cd64a6b5158e","plmId":"40289b7c601f2d9701601f2ff93f0000","pvmId":"40289b7c601f2d9701601f2ff9a60001","prmId":"40289b7c601f731801601f75222b0001","subPrmId":"40289b7c601f731801601f75227f0003","unitId":"-1","orgId":"-1","dataProjectId":"40289b7c601f731801601f75222b0001","dataPlatformVersionId":"40289b7c601f2d9701601f2ff9a60001","originalAbilityId":"40289b7c601f2d9701601f2ff9a60001"}},"head":{"appVersion":"1.0.0","osPlatform":"web","requestTime":1727530988617}}'
    response = requests.post('https://hwstudyv1.59iedu.com//api/LearningMarker/Timing', headers=headers, data=data)
    print(response.text)
    print(response.json()['data']['core']['coursewareSchedule'])

if __name__ == '__main__':
    for i in range(1,1111):
        current_timestamp_ms = int(time.time() * 1000)

        print("当前时间戳（毫秒）:", current_timestamp_ms)

        shua(current_timestamp_ms)
        time.sleep(1)

