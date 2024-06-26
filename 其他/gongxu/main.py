# -*- coding: utf-8 -*-
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

def learn_zhuanyeke():
    trainplanId = '578c78426b91414096f0f94d26f335e6'
    ck = 'eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW0iOiJncDUiLCJpZGVudGl0eUlkIjoiNTEzNzIzMTk3NjEwMjQwMTA2QDE1MSIsIm1vYmlsZSI6IjEzNTY4NDg5ODM4IiwidXNlck5hbWUiOiI1MTM3MjMxOTc2MTAyNDAxMDYiLCJ1c2VySWQiOiJwMXMwXzIyY2YwZDg0LTkyYmUtMTFlMy1iNzdjLWQ0YWU1MjZjNjk1YiIsImlhdCI6MTcxNzczMzgwNCwianRpIjoiNmJkYTcxYWUyZGM5NGUyM2JmYTMyYWUxZTgyODNhNzMifQ.ZuWvzBtNItvTBMkbeqLkCP2OSNP9pKZyKY7F_mhq2Us'

    userid, realname = getssion.getssion(ck)
    list_cource = get_cource.get_all_cource(ck, trainplanId)
    print('所有课程id：', list_cource)
    cource_selection_dic = {}
    for cource in list_cource:
        list_selection = get_cource_detail.get_cource_detail(cource,ck,trainplanId)
        cource_selection_dic[cource] = list_selection
    print('所有章节：', cource_selection_dic)
    for courceid, selctions in cource_selection_dic.items():

        for selction in selctions:
            print(courceid, selction['id'])

            study_time = selction['study_time']
            total_time = selction['total_time']
            print(selction['name'])
            print(study_time, total_time)
            if selction['study_status'] == '已学完':
                continue
             # 注意这里，如果是专业课就把获取html请求 改为 /   如果是学公需就是-
            recordid, studydoce, src = test_get_recordid.get_study_code_and_recordid(courceid, selction['id'],ck,trainplanId)

            if study_time < 0.8 * total_time:
                # if 0.15 * total_time <40:
                #     code = takerecord.taskrecord(recordid, studydoce, src, selction['id'], '%.4f' % (0.6 * total_time),
                #                                  userid, trainplanId)
                # else:
                #     code = takerecord.taskrecord(recordid, studydoce, src, selction['id'], '%.4f' % (0.85 * total_time), userid,trainplanId)
                code = takerecord.taskrecord(recordid, studydoce, src, selction['id'], '%.4f' % (0.85 * total_time),
                                             userid, trainplanId)
            else:
                code = takerecord.taskrecord(recordid, studydoce, src, selction['id'], total_time - 30, userid,trainplanId)

            time.sleep(10)
            if code  == '1':
                break

    #如果学完了返回1修改状态，记录时间
    list_cource = get_cource.get_all_cource(ck, trainplanId)
    # 如果 list_cource 为空，返回 True，否则返回 False
    return not list_cource

def start_learn(ck,planid,userid):

    list_cource = get_cource.get_all_cource(ck, planid)
    print('所有课程id：', list_cource)
    cource_selection_dic = {}
    for cource in list_cource:
        list_selection = get_cource_detail.get_cource_detail(cource,ck,planid)
        cource_selection_dic[cource] = list_selection
    print('所有章节：', cource_selection_dic)


    for courceid, selctions in cource_selection_dic.items():

        for selction in selctions:
            print(courceid, selction['id'])

            study_time = selction['study_time']
            total_time = selction['total_time']
            print(selction['name'])
            print(study_time, total_time)
            if selction['study_status'] == '已学完':
                continue
            recordid, studydoce, src = test_get_recordid.get_study_code_and_recordid(courceid, selction['id'],ck,planid)

            if study_time < 0.8 * total_time:
                if 0.15 * total_time <40:
                    code = takerecord.taskrecord(recordid, studydoce, src, selction['id'], '%.4f' % (0.6 * total_time),
                                                 userid, planid)
                else:
                    code = takerecord.taskrecord(recordid, studydoce, src, selction['id'], '%.4f' % (0.85 * total_time), userid,planid)
            else:
                code = takerecord.taskrecord(recordid, studydoce, src, selction['id'], total_time - 30, userid,planid)

            time.sleep(10)
            if code  == '1':
                break

    #如果学完了返回1修改状态，记录时间
    list_cource = get_cource.get_all_cource(ck, planid)
    # 如果 list_cource 为空，返回 True，否则返回 False
    return not list_cource

def start_exam(ck):
    examid = exam.get_exam_id(ck)
    this_exam_id,pager = exam.get_exam_list(examid,ck)
    que_ans_dic = exam.modify_list(this_exam_id,pager)
    exam.submit_answer(this_exam_id, que_ans_dic,ck)


def end_exam(ck):
    examid = exam.get_exam_id(ck)
    this_exam_id, pager = exam.get_exam_list(examid, ck)
    que_ans_dic = exam.modify_list(this_exam_id, pager)
    exam.submit_all(this_exam_id, que_ans_dic,ck)

def add_user_record(userid,realname):
    global user_record
    # 获取当前日期和时间
    now = datetime.datetime.now()
    user_record[userid] = {'stage': 1, 'time': now.strftime("%Y-%m-%d %H:%M:%S"), 'realname':realname}
    save_data()

def modify_user_stage(stage,userid,realname):
    global user_record
    now = datetime.datetime.now()
    user_record[userid] = {'stage': stage, 'time': now.strftime("%Y-%m-%d %H:%M:%S"), 'realname': realname}
    save_data()

def job():
    print("开始执行")
    for task in conf.cookies:
        for year in task['year']:
            print(task['name'])
            try:
                userid, realname = getssion.getssion(task['cookie'])
            except Exception as e:
                print('cookie过期',task['name'])

            if user_record.get(userid) == None:
                add_user_record(userid,realname)

                is_modify_stage = start_learn(task['cookie'], conf.get_year_planid(year), userid)
                if is_modify_stage:
                    modify_user_stage(2,userid,realname)

                    start_exam(task['cookie'])
            else:
                if user_record[userid]['stage'] == 1:
                    now = datetime.datetime.now()
                    time_obj = datetime.datetime.strptime(user_record[userid]['time'], '%Y-%m-%d %H:%M:%S')
                    if now - time_obj > datetime.timedelta(minutes=30):
                        modify_user_stage(1, userid, realname)
                        is_modify_stage = start_learn(task['cookie'], conf.get_year_planid(year), userid)

                        if is_modify_stage:
                            modify_user_stage(2, userid, realname)

                            start_exam(task['cookie'])
                elif user_record[userid]['stage'] == 2:
                    now = datetime.datetime.now()
                    time_obj = datetime.datetime.strptime(user_record[userid]['time'], '%Y-%m-%d %H:%M:%S')
                    if now - time_obj > datetime.timedelta(minutes=30):

                        modify_user_stage(3, userid, realname)

                        end_exam(task['cookie'])
if __name__ == '__main__':
    # 每隔20分钟执行一次 job 方法
    # schedule.every(10).minutes.do(job)
    # job()
    # while True:
    #     # 运行所有可以运行的任务
    #     schedule.run_pending()

    learn_zhuanyeke()


