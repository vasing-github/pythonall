import time
from copyreg import pickle

import requests


def get_course():
    cookies = {
        'JSESSIONID': '3707332DDE8759B16A7DD9340AE3144D',
        '__root_domain_v': '.uestcedu.com',
        '_qddaz': 'QD.248224846529360',
        '_qdda': '3-1.15t87d',
        '_qddab': '3-aco2jk.m0dt37v9',
        '77544ED4C32D75F181EEE4BE197D3345': 'xJnd%2bxGMyyxKbLso9tpphImyBQ6DH1WOoOISE0w%2b%2bAvR0PxwSky6nvrvdrwpDexSESMeLfgCYM46B2UnHW3z%2fdnQABk6UYrTXYWDrG2SoXvRQ3VEpfdoq%2fFjtKrtRC%2fM8cfFhWviED14%2bX2A%2fTRfM5y3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8E1fgZL0GkTkdIPkpErffl0F%2bpJX7sKWlEmD2WR5d2lh%2b83V3Uey%2bqrFQRFDJskMuKd3fdPoS%2bBx7zVDS9Gn3g%2fciA4FiQMn97pFkOoERLxL4V6Zjehx7vYfS%2fsuepnH5LnLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bSuzI5tBnEv1F1y4Oh95hS3cmfCSKrSAf5x2JC7KRRYk4bP2C9ATV%2bU0gmM4SBNW3jeeVas6zcTuqe1wPIG26XKkn2AYRiOiWGDojL7GKNnVCaVISatqZ1Doun21IXeXNsict5zaPzMrpwPwYcUjRwX4Y%2fLX2Nu6m7csMRtSdphWQA%3d%3d',
        '5CC081377012BE0C81B147E9EFFBEE75': 'xJnd%2bxGMyyxKbLso9tpphL%2ba5MvfO5VQKhBg6fYpm8wi50DbOOq1t8K6P3v6sYFeTSCCQRZ%2baPxOIaH5W4O6NNxYx%2bX18s2SUBWTYKnHSgVAD%2bympe7qlj9nW6LXcOBdAyax6NI76Ez%2fwtmbJ28QKZy3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8Eq4UcQT9lOt5gh6d7zvXbIrkpr37FJcUH33ne%2fUMZBsb9BMPJmcmRtkvI5MCypHALBsA8yrgoOKJmY5f0WQwjGG3wrSe9IpxOHu15eXkTaZU%2fSqAoGmMLLT7LQ22wbI6knLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bSv3cym9YBzBKLEEP9r9Q7xjhgdLWTskN3xu6yG3cEOSgo6BbTo0lpVKhkFbElrYWM%2bXPkIu5O1PF3W2h40oyEFsLWTMBHjRFEZfLcGVF5kIq0aNHKNgh3mY69uqrQ5fr5uct5zaPzMrpwPwYcUjRwX4JHG1gSyK29SBAYcXQ%2fSb9xFmVK%2fdtSCIcCWnEBKlHZWaabpNNC2FTYAjE%2bQTOI4sk8BVYSv6vFShfIt%2b9j7A4KwjOGzeHup5cVgD12JdU3PkVzs14L5%2f5VKXTsnL3oRzJcoSBHZ5kig9snKtaAXkaUEQIKrCoTPIj1XTG1FneQrU0axxjaE%2f5GQYnsjhH241J5FvmIYNgYPWHzIc1UzxMCF9eoM6Rw9aqyOKW7cb0qJoqt5bVhoX%2b9n1lJ9W43nBbvPTz0oDhqthGFRB2ZvVdBZfMOpRq3tMH40YCvYyac%2bsuOFw8UAX2FVAxtrGArDfQRAgqsKhM8iPVdMbUWd5Co%2bsWAPK0TzvznpzSjEqONPrdU46Ih3H5Sa1xd%2fBGIWOl2yETJi3tzlDNVwp09QJ9ZcXpC1zu2at%2bO8HAF1jq5QCAGg6%2bNRDhau8DASBlqrdehBzfZwuu8PtN%2bikPGZXrDbzYDoff%2b1ENziEmFm86JxBECCqwqEzyI9V0xtRZ3kKuPWDHezK8kWSG1kdLbA3XQ%3d%3d',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        # 'Cookie': 'JSESSIONID=3707332DDE8759B16A7DD9340AE3144D; __root_domain_v=.uestcedu.com; _qddaz=QD.248224846529360; _qdda=3-1.15t87d; _qddab=3-aco2jk.m0dt37v9; 77544ED4C32D75F181EEE4BE197D3345=xJnd%2bxGMyyxKbLso9tpphImyBQ6DH1WOoOISE0w%2b%2bAvR0PxwSky6nvrvdrwpDexSESMeLfgCYM46B2UnHW3z%2fdnQABk6UYrTXYWDrG2SoXvRQ3VEpfdoq%2fFjtKrtRC%2fM8cfFhWviED14%2bX2A%2fTRfM5y3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8E1fgZL0GkTkdIPkpErffl0F%2bpJX7sKWlEmD2WR5d2lh%2b83V3Uey%2bqrFQRFDJskMuKd3fdPoS%2bBx7zVDS9Gn3g%2fciA4FiQMn97pFkOoERLxL4V6Zjehx7vYfS%2fsuepnH5LnLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bSuzI5tBnEv1F1y4Oh95hS3cmfCSKrSAf5x2JC7KRRYk4bP2C9ATV%2bU0gmM4SBNW3jeeVas6zcTuqe1wPIG26XKkn2AYRiOiWGDojL7GKNnVCaVISatqZ1Doun21IXeXNsict5zaPzMrpwPwYcUjRwX4Y%2fLX2Nu6m7csMRtSdphWQA%3d%3d; 5CC081377012BE0C81B147E9EFFBEE75=xJnd%2bxGMyyxKbLso9tpphL%2ba5MvfO5VQKhBg6fYpm8wi50DbOOq1t8K6P3v6sYFeTSCCQRZ%2baPxOIaH5W4O6NNxYx%2bX18s2SUBWTYKnHSgVAD%2bympe7qlj9nW6LXcOBdAyax6NI76Ez%2fwtmbJ28QKZy3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8Eq4UcQT9lOt5gh6d7zvXbIrkpr37FJcUH33ne%2fUMZBsb9BMPJmcmRtkvI5MCypHALBsA8yrgoOKJmY5f0WQwjGG3wrSe9IpxOHu15eXkTaZU%2fSqAoGmMLLT7LQ22wbI6knLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bSv3cym9YBzBKLEEP9r9Q7xjhgdLWTskN3xu6yG3cEOSgo6BbTo0lpVKhkFbElrYWM%2bXPkIu5O1PF3W2h40oyEFsLWTMBHjRFEZfLcGVF5kIq0aNHKNgh3mY69uqrQ5fr5uct5zaPzMrpwPwYcUjRwX4JHG1gSyK29SBAYcXQ%2fSb9xFmVK%2fdtSCIcCWnEBKlHZWaabpNNC2FTYAjE%2bQTOI4sk8BVYSv6vFShfIt%2b9j7A4KwjOGzeHup5cVgD12JdU3PkVzs14L5%2f5VKXTsnL3oRzJcoSBHZ5kig9snKtaAXkaUEQIKrCoTPIj1XTG1FneQrU0axxjaE%2f5GQYnsjhH241J5FvmIYNgYPWHzIc1UzxMCF9eoM6Rw9aqyOKW7cb0qJoqt5bVhoX%2b9n1lJ9W43nBbvPTz0oDhqthGFRB2ZvVdBZfMOpRq3tMH40YCvYyac%2bsuOFw8UAX2FVAxtrGArDfQRAgqsKhM8iPVdMbUWd5Co%2bsWAPK0TzvznpzSjEqONPrdU46Ih3H5Sa1xd%2fBGIWOl2yETJi3tzlDNVwp09QJ9ZcXpC1zu2at%2bO8HAF1jq5QCAGg6%2bNRDhau8DASBlqrdehBzfZwuu8PtN%2bikPGZXrDbzYDoff%2b1ENziEmFm86JxBECCqwqEzyI9V0xtRZ3kKuPWDHezK8kWSG1kdLbA3XQ%3d%3d',
        'Referer': 'https://pcc.uestcedu.com/play/player.html?_V=2021&course_id=382&course_uuid=13f9bbb0-7677-49ce-a4f5-3cc745b18859&lesson_id=983&_V=20210917',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'course_id': '382',
        'course_uuid': '13f9bbb0-7677-49ce-a4f5-3cc745b18859',
        'client_type': '99',
    }

    response = requests.get('https://pcc.uestcedu.com/rest/course/detail', params=params, cookies=cookies, headers=headers)
    print(response.text)


def onexit(i,cuid):
    import requests

    cookies = {
        'JSESSIONID': '3324DE1C38692CD83F237F98E46DA657',
        '__root_domain_v': '.uestcedu.com',
        '_qddaz': 'QD.388825355743434',
        '_qdda': '3-1.15t87d',
        '_qddab': '3-6mk5jf.m0m89fxq',
        '77544ED4C32D75F181EEE4BE197D3345': 'xJnd%2bxGMyyxKbLso9tpphOD19vH7q2DRE%2fW9EKbvMNfAN8NMYLHHKzQeAyUWyw3uB4cdSl8htSCsQgrhfQ%2fOuHhB3nn5GfrTM%2bYDu7nSCrDHIxDJ%2ftHcnnZ7WRlHdFW6YTOmtoiOvQ4Y%2fr7x7X3M0py3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8EyWbcXhddoUdDPBbtsompV03jbAa0Xp9xjDMO%2fDBWR7ekIy4poNujxuYd%2fwmkLqufOgApiaRTWHv%2fqpfBIMaWo5q8Uo5FJu41LqWuOp4MAEikqqPcCDONoTNCDFFKX3HqnLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bSvD7BtPN72ak%2bxSD8N%2bnCj7dbzkU7rbY%2f%2fg2siv2EqESV5LQFOY0UJGd5jvapeUhLb2pPrp8yt%2bLDXSr3FGLCKpmF03nnbM%2f25N6TeyHe5HuQiTcRiL7R7nWMSTOiHiAzOct5zaPzMrpwPwYcUjRwX4Y%2fLX2Nu6m7csMRtSdphWQA%3d%3d',
        '5CC081377012BE0C81B147E9EFFBEE75': 'xJnd%2bxGMyyxKbLso9tpphOQ5lXaxQh9L8CGitQDBbtbXG4V1qkdLRriJ2AOEFksH40fk8bKUmNDZx1vUxszkmtAk9%2b7pAV3fJiUtROciAPFvk95ctyKleJaqzd%2boP0vcDmShDFnrpboM2LrNnE481py3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8ERmjpsxDA3Da%2f8tHaizsENLpsQSG%2fyNIq8l53b0IukrgXbS50zSq01Rv3aJF8Z5wJS89RIr%2fUTeCydGm1CYEWzKprnFQbgo1h9MgfBVOWTcKGL6BDrwULKE6I1nhoRq7ZnLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bStdMBU0n%2fPhOVHXrueK6pAzxchkdNMjVjkuCggDjqvygmBbK1PEoa3t%2bBKK%2fWDI4U0YTSjHxA0NvlTrajRUIE2DVbJrS0%2f6M%2byPlKEzUP4EOPDeeirfObRQe9DDis26BsKct5zaPzMrpwPwYcUjRwX4JHG1gSyK29SBAYcXQ%2fSb9wy6PyH3rvBuDremQGBQ9mRV%2bsHr0SFu7hYZucXor4PNglUcV05srR6mFHCH0IKmN89hwRJIsSxTaSNKc2%2frMFN0IUQAfGT8T%2f2wTl2KHAvf9zbGtpjbQskDIkAKBrCE10EQIKrCoTPIj1XTG1FneQrU0axxjaE%2f5GQYnsjhH241X3k3rmWJbLKAutGeJ63xxoA4pQrV55CyikHavY9%2fTNKQGcqIe4AmB5v0YBQLR5WPfKzFyqjgYZ1DGdpvEoBm7%2fTt8nm9K5joDnNmE7MyjYLp5h%2fcMqDSkCBaIjpf2fLMQRAgqsKhM8iPVdMbUWd5Co%2bsWAPK0TzvznpzSjEqONMf%2bCyM6RDAFGRGtXP1vK2PHh8pS9BPk8YbM%2fwCcF03VlzYEMUl4BNcP44Ya3V7mL0PWkTfX%2fS%2fzuWhvXHfuMq%2fBqBAVZDJD1qS9xwSAD7gp0CePHeUAzjJWF1yJQ5ULShBECCqwqEzyI9V0xtRZ3kKuPWDHezK8kWSG1kdLbA3XQ%3d%3d',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'JSESSIONID=3324DE1C38692CD83F237F98E46DA657; __root_domain_v=.uestcedu.com; _qddaz=QD.388825355743434; _qdda=3-1.15t87d; _qddab=3-6mk5jf.m0m89fxq; 77544ED4C32D75F181EEE4BE197D3345=xJnd%2bxGMyyxKbLso9tpphOD19vH7q2DRE%2fW9EKbvMNfAN8NMYLHHKzQeAyUWyw3uB4cdSl8htSCsQgrhfQ%2fOuHhB3nn5GfrTM%2bYDu7nSCrDHIxDJ%2ftHcnnZ7WRlHdFW6YTOmtoiOvQ4Y%2fr7x7X3M0py3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8EyWbcXhddoUdDPBbtsompV03jbAa0Xp9xjDMO%2fDBWR7ekIy4poNujxuYd%2fwmkLqufOgApiaRTWHv%2fqpfBIMaWo5q8Uo5FJu41LqWuOp4MAEikqqPcCDONoTNCDFFKX3HqnLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bSvD7BtPN72ak%2bxSD8N%2bnCj7dbzkU7rbY%2f%2fg2siv2EqESV5LQFOY0UJGd5jvapeUhLb2pPrp8yt%2bLDXSr3FGLCKpmF03nnbM%2f25N6TeyHe5HuQiTcRiL7R7nWMSTOiHiAzOct5zaPzMrpwPwYcUjRwX4Y%2fLX2Nu6m7csMRtSdphWQA%3d%3d; 5CC081377012BE0C81B147E9EFFBEE75=xJnd%2bxGMyyxKbLso9tpphOQ5lXaxQh9L8CGitQDBbtbXG4V1qkdLRriJ2AOEFksH40fk8bKUmNDZx1vUxszkmtAk9%2b7pAV3fJiUtROciAPFvk95ctyKleJaqzd%2boP0vcDmShDFnrpboM2LrNnE481py3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8ERmjpsxDA3Da%2f8tHaizsENLpsQSG%2fyNIq8l53b0IukrgXbS50zSq01Rv3aJF8Z5wJS89RIr%2fUTeCydGm1CYEWzKprnFQbgo1h9MgfBVOWTcKGL6BDrwULKE6I1nhoRq7ZnLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bStdMBU0n%2fPhOVHXrueK6pAzxchkdNMjVjkuCggDjqvygmBbK1PEoa3t%2bBKK%2fWDI4U0YTSjHxA0NvlTrajRUIE2DVbJrS0%2f6M%2byPlKEzUP4EOPDeeirfObRQe9DDis26BsKct5zaPzMrpwPwYcUjRwX4JHG1gSyK29SBAYcXQ%2fSb9wy6PyH3rvBuDremQGBQ9mRV%2bsHr0SFu7hYZucXor4PNglUcV05srR6mFHCH0IKmN89hwRJIsSxTaSNKc2%2frMFN0IUQAfGT8T%2f2wTl2KHAvf9zbGtpjbQskDIkAKBrCE10EQIKrCoTPIj1XTG1FneQrU0axxjaE%2f5GQYnsjhH241X3k3rmWJbLKAutGeJ63xxoA4pQrV55CyikHavY9%2fTNKQGcqIe4AmB5v0YBQLR5WPfKzFyqjgYZ1DGdpvEoBm7%2fTt8nm9K5joDnNmE7MyjYLp5h%2fcMqDSkCBaIjpf2fLMQRAgqsKhM8iPVdMbUWd5Co%2bsWAPK0TzvznpzSjEqONMf%2bCyM6RDAFGRGtXP1vK2PHh8pS9BPk8YbM%2fwCcF03VlzYEMUl4BNcP44Ya3V7mL0PWkTfX%2fS%2fzuWhvXHfuMq%2fBqBAVZDJD1qS9xwSAD7gp0CePHeUAzjJWF1yJQ5ULShBECCqwqEzyI9V0xtRZ3kKuPWDHezK8kWSG1kdLbA3XQ%3d%3d',
        'Origin': 'https://pcc.uestcedu.com',
        'Referer': 'https://pcc.uestcedu.com/play/player.html?_V=2021&course_id=382&course_uuid=13f9bbb0-7677-49ce-a4f5-3cc745b18859&lesson_id=983&_V=20210917',
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
        'course_id': '382',
        'course_uuid': '13f9bbb0-7677-49ce-a4f5-3cc745b18859',
        'client_type': '99',
        'lesson_id': i,
        'finish_len': '600',
        'video_position': '691',
    }



    response = requests.post('https://pcc.uestcedu.com/rest/user/course/lesson/onexit', cookies=cookies,
                             headers=headers, data=data)
    print(response.text)

def onexit2(i):
    cookies = {
        'JSESSIONID': '3324DE1C38692CD83F237F98E46DA657',
        '__root_domain_v': '.uestcedu.com',
        '_qddaz': 'QD.388825355743434',
        '_qdda': '3-1.15t87d',
        '_qddab': '3-6mk5jf.m0m89fxq',
        '77544ED4C32D75F181EEE4BE197D3345': 'xJnd%2bxGMyyxKbLso9tpphOD19vH7q2DRE%2fW9EKbvMNfAN8NMYLHHKzQeAyUWyw3uB4cdSl8htSCsQgrhfQ%2fOuHhB3nn5GfrTM%2bYDu7nSCrDHIxDJ%2ftHcnnZ7WRlHdFW6YTOmtoiOvQ4Y%2fr7x7X3M0py3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8EyWbcXhddoUdDPBbtsompV03jbAa0Xp9xjDMO%2fDBWR7ekIy4poNujxuYd%2fwmkLqufOgApiaRTWHv%2fqpfBIMaWo5q8Uo5FJu41LqWuOp4MAEikqqPcCDONoTNCDFFKX3HqnLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bSvD7BtPN72ak%2bxSD8N%2bnCj7dbzkU7rbY%2f%2fg2siv2EqESV5LQFOY0UJGd5jvapeUhLb2pPrp8yt%2bLDXSr3FGLCKpmF03nnbM%2f25N6TeyHe5HuQiTcRiL7R7nWMSTOiHiAzOct5zaPzMrpwPwYcUjRwX4Y%2fLX2Nu6m7csMRtSdphWQA%3d%3d',
        '5CC081377012BE0C81B147E9EFFBEE75': 'xJnd%2bxGMyyxKbLso9tpphOQ5lXaxQh9L8CGitQDBbtbXG4V1qkdLRriJ2AOEFksH40fk8bKUmNDZx1vUxszkmtAk9%2b7pAV3fJiUtROciAPFvk95ctyKleJaqzd%2boP0vcDmShDFnrpboM2LrNnE481py3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8ERmjpsxDA3Da%2f8tHaizsENLpsQSG%2fyNIq8l53b0IukrgXbS50zSq01Rv3aJF8Z5wJS89RIr%2fUTeCydGm1CYEWzKprnFQbgo1h9MgfBVOWTcKGL6BDrwULKE6I1nhoRq7ZnLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bStdMBU0n%2fPhOVHXrueK6pAzxchkdNMjVjkuCggDjqvygmBbK1PEoa3t%2bBKK%2fWDI4U0YTSjHxA0NvlTrajRUIE2DVbJrS0%2f6M%2byPlKEzUP4EOPDeeirfObRQe9DDis26BsKct5zaPzMrpwPwYcUjRwX4JHG1gSyK29SBAYcXQ%2fSb9wy6PyH3rvBuDremQGBQ9mRV%2bsHr0SFu7hYZucXor4PNglUcV05srR6mFHCH0IKmN89hwRJIsSxTaSNKc2%2frMFN0IUQAfGT8T%2f2wTl2KHAvf9zbGtpjbQskDIkAKBrCE10EQIKrCoTPIj1XTG1FneQrU0axxjaE%2f5GQYnsjhH241X3k3rmWJbLKAutGeJ63xxoA4pQrV55CyikHavY9%2fTNKQGcqIe4AmB5v0YBQLR5WPfKzFyqjgYZ1DGdpvEoBm7%2fTt8nm9K5joDnNmE7MyjYLp5h%2fcMqDSkCBaIjpf2fLMQRAgqsKhM8iPVdMbUWd5Co%2bsWAPK0TzvznpzSjEqONMf%2bCyM6RDAFGRGtXP1vK2PHh8pS9BPk8YbM%2fwCcF03VlzYEMUl4BNcP44Ya3V7mL0PWkTfX%2fS%2fzuWhvXHfuMq%2fBqBAVZDJD1qS9xwSAD7gp0CePHeUAzjJWF1yJQ5ULShBECCqwqEzyI9V0xtRZ3kKuPWDHezK8kWSG1kdLbA3XQ%3d%3d',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'JSESSIONID=3324DE1C38692CD83F237F98E46DA657; __root_domain_v=.uestcedu.com; _qddaz=QD.388825355743434; _qdda=3-1.15t87d; _qddab=3-6mk5jf.m0m89fxq; 77544ED4C32D75F181EEE4BE197D3345=xJnd%2bxGMyyxKbLso9tpphOD19vH7q2DRE%2fW9EKbvMNfAN8NMYLHHKzQeAyUWyw3uB4cdSl8htSCsQgrhfQ%2fOuHhB3nn5GfrTM%2bYDu7nSCrDHIxDJ%2ftHcnnZ7WRlHdFW6YTOmtoiOvQ4Y%2fr7x7X3M0py3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8EyWbcXhddoUdDPBbtsompV03jbAa0Xp9xjDMO%2fDBWR7ekIy4poNujxuYd%2fwmkLqufOgApiaRTWHv%2fqpfBIMaWo5q8Uo5FJu41LqWuOp4MAEikqqPcCDONoTNCDFFKX3HqnLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bSvD7BtPN72ak%2bxSD8N%2bnCj7dbzkU7rbY%2f%2fg2siv2EqESV5LQFOY0UJGd5jvapeUhLb2pPrp8yt%2bLDXSr3FGLCKpmF03nnbM%2f25N6TeyHe5HuQiTcRiL7R7nWMSTOiHiAzOct5zaPzMrpwPwYcUjRwX4Y%2fLX2Nu6m7csMRtSdphWQA%3d%3d; 5CC081377012BE0C81B147E9EFFBEE75=xJnd%2bxGMyyxKbLso9tpphOQ5lXaxQh9L8CGitQDBbtbXG4V1qkdLRriJ2AOEFksH40fk8bKUmNDZx1vUxszkmtAk9%2b7pAV3fJiUtROciAPFvk95ctyKleJaqzd%2boP0vcDmShDFnrpboM2LrNnE481py3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8ERmjpsxDA3Da%2f8tHaizsENLpsQSG%2fyNIq8l53b0IukrgXbS50zSq01Rv3aJF8Z5wJS89RIr%2fUTeCydGm1CYEWzKprnFQbgo1h9MgfBVOWTcKGL6BDrwULKE6I1nhoRq7ZnLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bStdMBU0n%2fPhOVHXrueK6pAzxchkdNMjVjkuCggDjqvygmBbK1PEoa3t%2bBKK%2fWDI4U0YTSjHxA0NvlTrajRUIE2DVbJrS0%2f6M%2byPlKEzUP4EOPDeeirfObRQe9DDis26BsKct5zaPzMrpwPwYcUjRwX4JHG1gSyK29SBAYcXQ%2fSb9wy6PyH3rvBuDremQGBQ9mRV%2bsHr0SFu7hYZucXor4PNglUcV05srR6mFHCH0IKmN89hwRJIsSxTaSNKc2%2frMFN0IUQAfGT8T%2f2wTl2KHAvf9zbGtpjbQskDIkAKBrCE10EQIKrCoTPIj1XTG1FneQrU0axxjaE%2f5GQYnsjhH241X3k3rmWJbLKAutGeJ63xxoA4pQrV55CyikHavY9%2fTNKQGcqIe4AmB5v0YBQLR5WPfKzFyqjgYZ1DGdpvEoBm7%2fTt8nm9K5joDnNmE7MyjYLp5h%2fcMqDSkCBaIjpf2fLMQRAgqsKhM8iPVdMbUWd5Co%2bsWAPK0TzvznpzSjEqONMf%2bCyM6RDAFGRGtXP1vK2PHh8pS9BPk8YbM%2fwCcF03VlzYEMUl4BNcP44Ya3V7mL0PWkTfX%2fS%2fzuWhvXHfuMq%2fBqBAVZDJD1qS9xwSAD7gp0CePHeUAzjJWF1yJQ5ULShBECCqwqEzyI9V0xtRZ3kKuPWDHezK8kWSG1kdLbA3XQ%3d%3d',
        'Origin': 'https://pcc.uestcedu.com',
        'Referer': 'https://pcc.uestcedu.com/play/player.html?_V=2021&course_id=383&course_uuid=7ca27d1a-4efe-459f-9c70-4ccaa5bd370e&lesson_id=1000&_V=20210917',
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
        'course_id': '383',
        'course_uuid': '7ca27d1a-4efe-459f-9c70-4ccaa5bd370e',
        'client_type': '99',
        'lesson_id': i,
        'finish_len': '600',
        'video_position': '22',
    }

    response = requests.post('https://pcc.uestcedu.com/rest/user/course/lesson/onexit', cookies=cookies,
                             headers=headers, data=data)
    print(response.text)
def onexit3(i):
    cookies = {
        'JSESSIONID': '3324DE1C38692CD83F237F98E46DA657',
        '__root_domain_v': '.uestcedu.com',
        '_qddaz': 'QD.388825355743434',
        '_qdda': '3-1.15t87d',
        '_qddab': '3-6mk5jf.m0m89fxq',
        '77544ED4C32D75F181EEE4BE197D3345': 'xJnd%2bxGMyyxKbLso9tpphOD19vH7q2DRE%2fW9EKbvMNfAN8NMYLHHKzQeAyUWyw3uB4cdSl8htSCsQgrhfQ%2fOuHhB3nn5GfrTM%2bYDu7nSCrDHIxDJ%2ftHcnnZ7WRlHdFW6YTOmtoiOvQ4Y%2fr7x7X3M0py3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8EyWbcXhddoUdDPBbtsompV03jbAa0Xp9xjDMO%2fDBWR7ekIy4poNujxuYd%2fwmkLqufOgApiaRTWHv%2fqpfBIMaWo5q8Uo5FJu41LqWuOp4MAEikqqPcCDONoTNCDFFKX3HqnLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bSvD7BtPN72ak%2bxSD8N%2bnCj7dbzkU7rbY%2f%2fg2siv2EqESV5LQFOY0UJGd5jvapeUhLb2pPrp8yt%2bLDXSr3FGLCKpmF03nnbM%2f25N6TeyHe5HuQiTcRiL7R7nWMSTOiHiAzOct5zaPzMrpwPwYcUjRwX4Y%2fLX2Nu6m7csMRtSdphWQA%3d%3d',
        '5CC081377012BE0C81B147E9EFFBEE75': 'xJnd%2bxGMyyxKbLso9tpphOQ5lXaxQh9L8CGitQDBbtbXG4V1qkdLRriJ2AOEFksH40fk8bKUmNDZx1vUxszkmtAk9%2b7pAV3fJiUtROciAPFvk95ctyKleJaqzd%2boP0vcDmShDFnrpboM2LrNnE481py3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8ERmjpsxDA3Da%2f8tHaizsENLpsQSG%2fyNIq8l53b0IukrgXbS50zSq01Rv3aJF8Z5wJS89RIr%2fUTeCydGm1CYEWzKprnFQbgo1h9MgfBVOWTcKGL6BDrwULKE6I1nhoRq7ZnLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bStdMBU0n%2fPhOVHXrueK6pAzxchkdNMjVjkuCggDjqvygmBbK1PEoa3t%2bBKK%2fWDI4U0YTSjHxA0NvlTrajRUIE2DVbJrS0%2f6M%2byPlKEzUP4EOPDeeirfObRQe9DDis26BsKct5zaPzMrpwPwYcUjRwX4JHG1gSyK29SBAYcXQ%2fSb9wy6PyH3rvBuDremQGBQ9mRV%2bsHr0SFu7hYZucXor4PNglUcV05srR6mFHCH0IKmN89hwRJIsSxTaSNKc2%2frMFN0IUQAfGT8T%2f2wTl2KHAvf9zbGtpjbQskDIkAKBrCE10EQIKrCoTPIj1XTG1FneQrU0axxjaE%2f5GQYnsjhH241X3k3rmWJbLKAutGeJ63xxoA4pQrV55CyikHavY9%2fTNKQGcqIe4AmB5v0YBQLR5WPfKzFyqjgYZ1DGdpvEoBm7%2fTt8nm9K5joDnNmE7MyjYLp5h%2fcMqDSkCBaIjpf2fLMQRAgqsKhM8iPVdMbUWd5Co%2bsWAPK0TzvznpzSjEqONMf%2bCyM6RDAFGRGtXP1vK2PHh8pS9BPk8YbM%2fwCcF03VlzYEMUl4BNcP44Ya3V7mL0PWkTfX%2fS%2fzuWhvXHfuMq%2fBqBAVZDJD1qS9xwSAD7gp0CePHeUAzjJWF1yJQ5ULShBECCqwqEzyI9V0xtRZ3kKuPWDHezK8kWSG1kdLbA3XQ%3d%3d',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'JSESSIONID=3324DE1C38692CD83F237F98E46DA657; __root_domain_v=.uestcedu.com; _qddaz=QD.388825355743434; _qdda=3-1.15t87d; _qddab=3-6mk5jf.m0m89fxq; 77544ED4C32D75F181EEE4BE197D3345=xJnd%2bxGMyyxKbLso9tpphOD19vH7q2DRE%2fW9EKbvMNfAN8NMYLHHKzQeAyUWyw3uB4cdSl8htSCsQgrhfQ%2fOuHhB3nn5GfrTM%2bYDu7nSCrDHIxDJ%2ftHcnnZ7WRlHdFW6YTOmtoiOvQ4Y%2fr7x7X3M0py3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8EyWbcXhddoUdDPBbtsompV03jbAa0Xp9xjDMO%2fDBWR7ekIy4poNujxuYd%2fwmkLqufOgApiaRTWHv%2fqpfBIMaWo5q8Uo5FJu41LqWuOp4MAEikqqPcCDONoTNCDFFKX3HqnLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bSvD7BtPN72ak%2bxSD8N%2bnCj7dbzkU7rbY%2f%2fg2siv2EqESV5LQFOY0UJGd5jvapeUhLb2pPrp8yt%2bLDXSr3FGLCKpmF03nnbM%2f25N6TeyHe5HuQiTcRiL7R7nWMSTOiHiAzOct5zaPzMrpwPwYcUjRwX4Y%2fLX2Nu6m7csMRtSdphWQA%3d%3d; 5CC081377012BE0C81B147E9EFFBEE75=xJnd%2bxGMyyxKbLso9tpphOQ5lXaxQh9L8CGitQDBbtbXG4V1qkdLRriJ2AOEFksH40fk8bKUmNDZx1vUxszkmtAk9%2b7pAV3fJiUtROciAPFvk95ctyKleJaqzd%2boP0vcDmShDFnrpboM2LrNnE481py3nNo%2fMyunA%2fBhxSNHBfgZG1KTS0YPinaS5G8b1I8ERmjpsxDA3Da%2f8tHaizsENLpsQSG%2fyNIq8l53b0IukrgXbS50zSq01Rv3aJF8Z5wJS89RIr%2fUTeCydGm1CYEWzKprnFQbgo1h9MgfBVOWTcKGL6BDrwULKE6I1nhoRq7ZnLec2j8zK6cD8GHFI0cF%2bJSnI9nn9rjiqhYxNjVi%2bStdMBU0n%2fPhOVHXrueK6pAzxchkdNMjVjkuCggDjqvygmBbK1PEoa3t%2bBKK%2fWDI4U0YTSjHxA0NvlTrajRUIE2DVbJrS0%2f6M%2byPlKEzUP4EOPDeeirfObRQe9DDis26BsKct5zaPzMrpwPwYcUjRwX4JHG1gSyK29SBAYcXQ%2fSb9wy6PyH3rvBuDremQGBQ9mRV%2bsHr0SFu7hYZucXor4PNglUcV05srR6mFHCH0IKmN89hwRJIsSxTaSNKc2%2frMFN0IUQAfGT8T%2f2wTl2KHAvf9zbGtpjbQskDIkAKBrCE10EQIKrCoTPIj1XTG1FneQrU0axxjaE%2f5GQYnsjhH241X3k3rmWJbLKAutGeJ63xxoA4pQrV55CyikHavY9%2fTNKQGcqIe4AmB5v0YBQLR5WPfKzFyqjgYZ1DGdpvEoBm7%2fTt8nm9K5joDnNmE7MyjYLp5h%2fcMqDSkCBaIjpf2fLMQRAgqsKhM8iPVdMbUWd5Co%2bsWAPK0TzvznpzSjEqONMf%2bCyM6RDAFGRGtXP1vK2PHh8pS9BPk8YbM%2fwCcF03VlzYEMUl4BNcP44Ya3V7mL0PWkTfX%2fS%2fzuWhvXHfuMq%2fBqBAVZDJD1qS9xwSAD7gp0CePHeUAzjJWF1yJQ5ULShBECCqwqEzyI9V0xtRZ3kKuPWDHezK8kWSG1kdLbA3XQ%3d%3d',
        'Origin': 'https://pcc.uestcedu.com',
        'Referer': 'https://pcc.uestcedu.com/play/player.html?_V=2021&course_id=384&course_uuid=62a30396-8161-446a-99c2-538adfbe5dd0&lesson_id=1006&_V=20210917',
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
        'course_id': '384',
        'course_uuid': '62a30396-8161-446a-99c2-538adfbe5dd0',
        'client_type': '99',
        'lesson_id': i,
        'finish_len': '600',
        'video_position': '7',
    }

    response = requests.post('https://pcc.uestcedu.com/rest/user/course/lesson/onexit', cookies=cookies,
                             headers=headers, data=data)


    print(response.text)
if __name__ == '__main__':
    # get_course()
    while True:
        for i in range(983,999):
            onexit(i,'13f9bbb0-7677-49ce-a4f5-3cc745b18859')
            print(i)

        for i in range(1000,1005):
            onexit2(i)
            print(i)

        for i in range(1006,1010):
            onexit3(i)
            print(i)

        time.sleep(500)