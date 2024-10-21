# -*- coding: utf-8 -*-
import asyncio
import get_cource
import get_cource_detail
import test_get_recordid
import takerecord
import exam
import getssion
import conf
import txt
import datetime
import json
import schedule
import time

user_record = txt.record_user


def save_data():
    global user_record
    with open('txt.py', 'w', encoding='utf-8') as f:
        # 将字典转换为 JSON 格式的字符串
        record_user_json = json.dumps(user_record, ensure_ascii=False)

        # 将 JSON 字符串写入文件
        f.write('record_user = ' + record_user_json + '\n')


def start_learn(ck, planid, userid):
    list_cource = get_cource.get_all_cource(ck, planid)
    print('所有课程id：', list_cource)
    cource_selection_dic = {}
    for cource in list_cource:
        list_selection = get_cource_detail.get_cource_detail(cource, ck, planid)
        cource_selection_dic[cource] = list_selection
    print('所有章节：', cource_selection_dic)

    for courceid, selctions in cource_selection_dic.items():

        for selction in selctions:
            print(courceid, selction['id'])

            study_time = selction['study_time']
            total_time = selction['total_time']
            print(selction['name'])
            print(study_time, total_time, selction['study_status'])
            if selction['study_status'] == '已学完':
                continue

            token = test_get_recordid.get_study_code_and_recordid2(courceid, selction['id'], ck,planid)

            takerecord.one_course_ing(token,study_time,total_time)


            # code = takerecord.takeRecode2(token, '%.4f' % (study_time))
            # time.sleep(1)
            # code = takerecord.takeRecode2(token,'%.4f' % (study_time + 30))
            # time.sleep(1)
            # code = takerecord.takeRecode2(token, '%.4f' % (study_time + 60))
            # time.sleep(1)
            # code = takerecord.takeRecode2(token, '%.4f' % (study_time + 90))
            # time.sleep(1)
            # code = takerecord.takeRecode2(token, '%.4f' % (study_time + 100))

            print()

    # 如果学完了返回1修改状态，记录时间
    list_cource = get_cource.get_all_cource(ck, planid)
    # 如果 list_cource 为空，返回 True，否则返回 Fals
    return not list_cource


def start_exam(ck):
    examid = exam.get_exam_id(ck)
    if not examid:
        return
    this_exam_id, pager = exam.get_exam_list(examid, ck)
    que_ans_dic = exam.modify_list(this_exam_id, pager)
    exam.submit_answer(this_exam_id, que_ans_dic, ck)


def end_exam(ck):
    examid = exam.get_exam_id(ck)
    this_exam_id, pager = exam.get_exam_list(examid, ck)
    que_ans_dic = exam.modify_list(this_exam_id, pager)
    exam.submit_all(this_exam_id, que_ans_dic, ck)


def add_user_record(userid, realname, year):
    global user_record
    # 获取当前日期和时间
    now = datetime.datetime.now()

    if user_record.get(userid) != None:
        user_year_list = user_record.get(userid)
    else:
        user_year_list = {}
    user_year_list[year] = {'stage': 1, 'time': now.strftime("%Y-%m-%d %H:%M:%S"), 'realname': realname}
    user_record[userid] = user_year_list
    save_data()


def modify_user_stage(stage, userid, realname, year):
    global user_record
    now = datetime.datetime.now()
    user_record[userid][year] = {'stage': stage, 'time': now.strftime("%Y-%m-%d %H:%M:%S"), 'realname': realname}
    save_data()


def job(task, year):
    print("开始执行")
    print(task['name'],year)

    try:
        userid, realname = getssion.getssion(task['cookie'])
    except Exception as e:
        print('cookie过期', task['name'])
    if user_record.get(userid) == None or user_record[userid].get(year) == None:
        add_user_record(userid, realname, year)

        is_modify_stage =  start_learn(task['cookie'], conf.get_year_planid(year), userid)
        if is_modify_stage:
            modify_user_stage(2, userid, realname, year)
            if year == '10' or year == '11' or year == '12' or year == '13' or year == '14':
                return
            start_exam(task['cookie'])
    else:
        if user_record[userid][year]['stage'] == 1:
            now = datetime.datetime.now()
            time_obj = datetime.datetime.strptime(user_record[userid][year]['time'], '%Y-%m-%d %H:%M:%S')

            if (now - time_obj).total_seconds() >= 10:
                modify_user_stage(1, userid, realname, year)
                is_modify_stage =  start_learn(task['cookie'], conf.get_year_planid(year), userid)

                if is_modify_stage:
                    modify_user_stage(2, userid, realname, year)
                    if year == '10' or year == '11' or year == '12' or year == '13' or year == '14':
                        return
                    start_exam(task['cookie'])
        elif user_record[userid][year]['stage'] == 2:
            if year == '10' or year == '11' or year == '12' or year == '13' or year == '14':
                return

            now = datetime.datetime.now()
            time_obj = datetime.datetime.strptime(user_record[userid][year]['time'], '%Y-%m-%d %H:%M:%S')
            if (now - time_obj).total_seconds() >= 10:
                modify_user_stage(3, userid, realname, year)

                end_exam(task['cookie'])


async def main():
    tasks = []
    for task in conf.cookies:
        for year in task['year']:
            # 创建一个新的协程，并将它添加到任务列表中
            year = str(year)
            tasks.append(job(task, year))
    # 使用 asyncio.gather 来启动所有的协程
    await asyncio.gather(*tasks)


def do_run():
    asyncio.run(main())


if __name__ == '__main__':
    while True:
        for task in conf.cookies:
            for year in task['year']:
                year = str(year)
                job(task, year)
