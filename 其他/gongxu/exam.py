import time
import answer
import requests
import conf
import re
import json
def get_exam_id(ck):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Hrttoken': ck,
        # 'Hrttoken': 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk4MDAzMjgzMzM2QDE1MSIsIm1vYmlsZSI6IjEzNTY4NDcxMjY2IiwidXNlck5hbWUiOiI1MTM3MjMxOTgwMDMyODMzMzYiLCJ1c2VySWQiOiJwMXMwXzI1MzIyZTEyLTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcwOTgxMDQ5MywianRpIjoiYjFhNTZmNGRiZTVlNDFhYzlmY2VlOWM3ZmFhMGQyNWIifQ._-vPg34GmRITc8Vlni6K75HDOWQpwjrFFCvFIRitmpk',

        'Origin': 'https://edu.chinahrt.com',
        'Referer': 'https://edu.chinahrt.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        'appid': 'gp6-1',
        'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'curPage': '1',
        'pageSize': '10',
        'order_sequence': 'up',
        'order_type': 'time',
        'isHistory': '0',
        'examResult': '103001',
    }

    response = requests.get('https://gp.chinahrt.com/gp6/exam/stu/exam/examList', params=params, headers=headers, verify = False)

    # print(response.json()['data']['data'][0]['id'])
    if len(response.json()['data']['data'][0]['id']) == 0:
        return 0
    return response.json()['data']['data'][0]['id']

def get_exam_list(examid,ck):

    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Origin': 'https://edu.chinahrt.com',
        'Referer': 'https://edu.chinahrt.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
        'accept': 'application/json',
        'appid': 'gp6-1',
        'content-type': 'application/x-www-form-urlencoded',
        'hrttoken': ck,
        'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'examId': examid,
        'isExercise': '0',
    }

    response = requests.post('https://gp.chinahrt.com/gp6/exam/stu/exam/go_exam', headers=headers, data=data, verify = False)
    print(response.json()['data']['pager']['id'])
    this_exam_id = response.json()['data']['pager']['id']
    return this_exam_id,response.json()['data']['pager']

def modify_list(this_exam_id,pager):
    que_ans_dic = {}

    # print(response.json()['data']['pager']['single_list'])

    single_list = pager['single_list']
    for single in single_list:
        question = single['question']
        single_id = single['id']
        ans = getanswer(1, question)
        que_ans_dic[single_id] = ans

    multi_list = pager['multi_list']
    for multi in multi_list:
        question = multi['question']
        muti_id = multi['id']
        ans = getanswer(2, question)
        que_ans_dic[muti_id] = ans

    judge_list = pager['judge_list']
    for ju in judge_list:
        question = ju['question']
        ju_id = ju['id']
        ans = getanswer(3, question)
        if ans == 'A':
            que_ans_dic[ju_id] = '1'
        else:
            que_ans_dic[ju_id] = '0'

    return que_ans_dic


    # submit_all(this_exam_id, que_ans_dic)


def submit_all(this_exam_id,que_ans_dic,ck):


    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Origin': 'https://edu.chinahrt.com',
        'Referer': 'https://edu.chinahrt.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
        'accept': 'application/json',
        'appid': 'gp6-1',
        'content-type': 'application/x-www-form-urlencoded',
        'hrttoken': ck,
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    answers = [{'id': id, 'mark': '1', 'answer': answer} for id, answer in que_ans_dic.items()]
    # 创建data字典
    data = {
        'paperId': this_exam_id,
        'answers': json.dumps(answers)
    }
    response = requests.post('https://gp.chinahrt.com/gp6/exam/stu/exam/submit_exam_all_answer', headers=headers,
                             data=data,verify = False)
    print(response.text)


def getanswer(type,question):
    for ans in answer.answerList:
        if ans['title'] == question:
            result = re.search(r'正确答案：(\w+)', ans['answer'])
            if result:
                # print(ans['answer'])
                # print("提取的答案是", result.group(1))
                return result.group(1)

    if type == 1:
        return 'A'
    elif type == 2:
        return "ABC"
    else:
        return "1"


def submit_answer(this_exam_id,que_ans_dic,ck):

    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Origin': 'https://edu.chinahrt.com',
        'Referer': 'https://edu.chinahrt.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
        'accept': 'application/json',
        'appid': 'gp6-1',
        'content-type': 'application/x-www-form-urlencoded',
        'hrttoken': ck,
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }


    answers = [{'id': id, 'mark': '1', 'answer': answer} for id, answer in que_ans_dic.items()]
    # 创建data字典
    data = {
        'paperId': this_exam_id,
        'answers': json.dumps(answers)  # 将answers转换为字符串
    }

    # 发送POST请求
    print(data)

    response = requests.post('https://gp.chinahrt.com/gp6/exam/stu/exam/submit_exam_answer', headers=headers, data=data, verify = False)
    print(response.text)

if __name__ == '__main__':
    examid = get_exam_id()
    get_exam_list(examid)

    # que_ans_dic = {}
    # multi_list = answer.que_list_test['data']['pager']['multi_list']
    # for multi in multi_list:
    #     question = multi['question']
    #     muti_id = multi['id']
    #     ans = getanswer(2,question)
    #     que_ans_dic[muti_id] = ans
    # print(que_ans_dic)