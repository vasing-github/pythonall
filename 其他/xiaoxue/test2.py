import requests

cookies = {
    'JSESSIONID': '2549CCCB5F8C8B8D3A2F1B704F028831',
    '5CC081377012BE0C81B147E9EFFBEE75': 'tZ8j9Fpml9e1jJpXBIY39zA59fbTcO7UHqiXZPv%2bZvLVv%2b1WYyDBu9TFn5nzD9AgfvxidR2ziNOkab2LFvQ8ElBujRrbFyDN2eLr4DDX7Bg2L%2fkyx6T7DC8k0gjqIrvy2hL3EH2fLe4jRaLT7tTiWEEQIKrCoTPIj1XTG1FneQrU0axxjaE%2f5GQYnsjhH2417xhAwGUXs%2fTL0ye8EQDEzL2zdfIzK9xe1z83P%2bAcPZqZm1YiEzaS6umqYqXBXlSqghUDF2uucpXMA9TRpd2sSJBy5drSd618PwZobsrmjqPQgY4vZ1xqhzGBX4eRJmyuQRAgqsKhM8iPVdMbUWd5Co%2bsWAPK0TzvznpzSjEqONM6f5VHHceAz8cFaAKz5kddFPrMtYnrZ7wVMbiH%2b%2fZ%2boNYZfSxeqS23ymYqsFEpebKWyQya6qLyFaCNv6y8ZzhGrEOaGxTfKHl3zaWipxCkF31R3TceMM30nFscv8lYsfxBECCqwqEzyI9V0xtRZ3kKuPWDHezK8kWSG1kdLbA3XQ%3d%3d',
    '__root_domain_v': '.uestcedu.com',
    '_qddaz': 'QD.163024830625477',
    '_qdda': '3-1.15t87d',
    '_qddab': '3-pll25d.m0djmccg',
    '77544ED4C32D75F181EEE4BE197D3345': 'xJnd%2bxGMyyxKbLso9tpphEhJgIccyXIRRcvnXPIMWfwy1fxOf6r3vd3GT8I6x4indya40qInoUiUoR5TjdaFLs7%2baWTdKyRKxVgu95Kb0MDCUXA%2ff0NN4ff9TU61%2beG5yjGfWW9NfkL8V5SAvzVwqZy3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8ETTPCE%2bAsVeFSRPie0dbEJGu200cHbPbXGhUr3LcZhJN3lkNqBTigIxBHzSOQzMB9ti%2bSIyTHl6VhEwVeL8Fb%2fd4oOXEsLG06bmQyrxCoO%2bJfkqfYsv67nYWOEhmEG5F%2fnLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bSvXEojuB%2fjjJ%2fPHXB0WqWWNIUiLkruZQG1Vk7eeADwE9%2fV%2fEcB35Cdwj%2frC55V71CKebhvELDQsWf5HfKpyhPN8RESFAlZx2gqNiC1V0nNk9ttqUkPPMgJgbjfbl7hz2sGct5zaPzMrpwPwYcUjRwX4Y%2fLX2Nu6m7csMRtSdphWQA%3d%3d',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'JSESSIONID=2549CCCB5F8C8B8D3A2F1B704F028831; 5CC081377012BE0C81B147E9EFFBEE75=tZ8j9Fpml9e1jJpXBIY39zA59fbTcO7UHqiXZPv%2bZvLVv%2b1WYyDBu9TFn5nzD9AgfvxidR2ziNOkab2LFvQ8ElBujRrbFyDN2eLr4DDX7Bg2L%2fkyx6T7DC8k0gjqIrvy2hL3EH2fLe4jRaLT7tTiWEEQIKrCoTPIj1XTG1FneQrU0axxjaE%2f5GQYnsjhH2417xhAwGUXs%2fTL0ye8EQDEzL2zdfIzK9xe1z83P%2bAcPZqZm1YiEzaS6umqYqXBXlSqghUDF2uucpXMA9TRpd2sSJBy5drSd618PwZobsrmjqPQgY4vZ1xqhzGBX4eRJmyuQRAgqsKhM8iPVdMbUWd5Co%2bsWAPK0TzvznpzSjEqONM6f5VHHceAz8cFaAKz5kddFPrMtYnrZ7wVMbiH%2b%2fZ%2boNYZfSxeqS23ymYqsFEpebKWyQya6qLyFaCNv6y8ZzhGrEOaGxTfKHl3zaWipxCkF31R3TceMM30nFscv8lYsfxBECCqwqEzyI9V0xtRZ3kKuPWDHezK8kWSG1kdLbA3XQ%3d%3d; __root_domain_v=.uestcedu.com; _qddaz=QD.163024830625477; _qdda=3-1.15t87d; _qddab=3-pll25d.m0djmccg; 77544ED4C32D75F181EEE4BE197D3345=xJnd%2bxGMyyxKbLso9tpphEhJgIccyXIRRcvnXPIMWfwy1fxOf6r3vd3GT8I6x4indya40qInoUiUoR5TjdaFLs7%2baWTdKyRKxVgu95Kb0MDCUXA%2ff0NN4ff9TU61%2beG5yjGfWW9NfkL8V5SAvzVwqZy3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8ETTPCE%2bAsVeFSRPie0dbEJGu200cHbPbXGhUr3LcZhJN3lkNqBTigIxBHzSOQzMB9ti%2bSIyTHl6VhEwVeL8Fb%2fd4oOXEsLG06bmQyrxCoO%2bJfkqfYsv67nYWOEhmEG5F%2fnLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bSvXEojuB%2fjjJ%2fPHXB0WqWWNIUiLkruZQG1Vk7eeADwE9%2fV%2fEcB35Cdwj%2frC55V71CKebhvELDQsWf5HfKpyhPN8RESFAlZx2gqNiC1V0nNk9ttqUkPPMgJgbjfbl7hz2sGct5zaPzMrpwPwYcUjRwX4Y%2fLX2Nu6m7csMRtSdphWQA%3d%3d',
    'Origin': 'https://pcc.uestcedu.com',
    'Referer': 'https://pcc.uestcedu.com/play/player.html?_V=2021&course_id=382&course_uuid=13f9bbb0-7677-49ce-a4f5-3cc745b18859&lesson_id=983',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'course_id': '382',
    'course_uuid': '13f9bbb0-7677-49ce-a4f5-3cc745b18859',
    'client_type': '99',
    'lesson_id': '983',
    'finish_len': '10',
    'video_position': '780',
}

response = requests.post('https://pcc.uestcedu.com/rest/user/course/lesson/onexit', cookies=cookies, headers=headers, data=data)

print(response.text)