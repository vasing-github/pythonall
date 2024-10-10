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


async def start_learn(ck, planid, userid):
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
            exitList = ['2bc16638cb5a4ff8af74600ead46a662','1190963f61614009a2f6120af1c5567e','359fa533ba6c49028778f9b94e1755c7','303cf1cd2e2148a9b99beb9daf39c24d',
                        '99c7a177bf77475198045803903d65b4','4b959b2650014a799b78547e6078c45d','a7c0705774d748469e8e2ea771b61cad','9bf9ff4f-7e45-40c1-861e-833b57a9c6e1',
                        'ce33fe4340de41999f2d79ed778319b6','e149cd5b91e84cc1bce0a1bbece9349d','ce33fe4340de41999f2d79ed778319b6','a88e9094acd84063895e46399d7ad443',
                        '45443e93895946b1882bdceb24b9f211','6cf866c6fe65460ab13c0cfe67a62cd8']
            if courceid in exitList:
                continue
            study_time = selction['study_time']
            total_time = selction['total_time']
            print(selction['name'])
            print(study_time, total_time, selction['study_status'])
            if selction['study_status'] == '已学完':
                continue

            recordid, studydoce, src = test_get_recordid.get_study_code_and_recordid(courceid, selction['id'], ck,planid)

            # take = test_get_recordid.get_study_code_and_recordid(courceid, selction['id'], ck,
            #                                                                          planid)
            # if study_time < 0.8 * total_time:
            #     if 0.15 * total_time < 40:
            #         code = takerecord.takeRecode2(take,'%.4f' % (0.6 * total_time))
            #     else:
            #         code = takerecord.takeRecode2(take,'%.4f' % (28))
            # else:
            #     code = takerecord.takeRecode2(take,total_time -30)

            # time.sleep(2)

            # if selction['study_status'] == '未学习' or study_time == 0:
            #     code = takerecord.taskrecord(recordid, studydoce, src, selction['id'], 28, userid, planid)
            # else:
            #     if study_time < 0.8 * total_time:
            #         if 0.15 * total_time <40:
            #             code = takerecord.taskrecord(recordid, studydoce, src, selction['id'], '%.4f' % (0.6 * total_time),
            #                                          userid, planid)
            #         else:
            #             code  = takerecord.taskrecord(recordid, studydoce, src, selction['id'], '%.4f' % (0.85 * total_time), userid,planid)
            #     else:
            #         code = takerecord.taskrecord(recordid, studydoce, src, selction['id'], total_time - 30, userid,planid)

            if selction['study_status'] == '未学习' or study_time == 0:
                code = takerecord.taskrecord(recordid, studydoce, src, selction['id'], 28, userid, planid)
            else:
                if study_time < 0.8 * total_time:
                    if study_time + 28 * 11 < total_time:
                        code = takerecord.taskrecord(recordid, studydoce, src, selction['id'],
                                                     '%.4f' % (study_time + 28 * 11),
                                                     userid, planid)
                    else:
                        code = takerecord.taskrecord(recordid, studydoce, src, selction['id'],
                                                     '%.4f' % (0.9 * total_time), userid, planid)
                else:
                    code = takerecord.taskrecord(recordid, studydoce, src, selction['id'], total_time - 30, userid,
                                                 planid)

            await asyncio.sleep(2)
            # if code  == '1':
            #     break

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


async def job(task, year):
    print("开始执行")
    print(task['name'],year)
    time.sleep(2)
    try:
        userid, realname = getssion.getssion(task['cookie'])
    except Exception as e:
        print('cookie过期', task['name'])
    if user_record.get(userid) == None or user_record[userid].get(year) == None:
        add_user_record(userid, realname, year)

        is_modify_stage = await start_learn(task['cookie'], conf.get_year_planid(year), userid)
        if is_modify_stage:
            modify_user_stage(2, userid, realname, year)
            if year == '10' or year == '11' or year == '12' or year == '13' or year == '14':
                return
            start_exam(task['cookie'])
    else:
        if user_record[userid][year]['stage'] == 1:
            now = datetime.datetime.now()
            time_obj = datetime.datetime.strptime(user_record[userid][year]['time'], '%Y-%m-%d %H:%M:%S')

            if (now - time_obj).total_seconds() >= 170:
                modify_user_stage(1, userid, realname, year)
                is_modify_stage = await start_learn(task['cookie'], conf.get_year_planid(year), userid)

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
            if now - time_obj >= datetime.timedelta(minutes=3):
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
    schedule.every(3).minutes.do(do_run)
    do_run()
    while True:
        # 运行所有可以运行的任务
        schedule.run_pending()
