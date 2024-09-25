# -*- coding: utf-8 -*-
import os
import re
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目的根目录
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
# 将项目根目录添加到 sys.path
sys.path.append(project_root)
import kaipumodify.cfg.text as text
import getcontent2, getcontent
from kaipumodify.search import jiyuehuasearch

token = text.token

bz_gov_id = text.bz_gov_id
jid = text.jid


def extract_numbers(url):
    # 用斜杠截取 URL
    parts = url.split('/')
    numbers = []

    # 遍历每个部分
    for part in parts:
        # 检查部分是否以数字开头并且长度大于4
        match = re.match(r'^\d{5,}', part)
        if match:
            numbers.append(match.group())

    return numbers


if __name__ == '__main__':
    wrong_words = ['、谢江鸿', '谢江鸿、', '，副县长谢江鸿', ',副县长谢江鸿', '副县长谢江鸿一同调研。', '副县长谢江鸿出席会议。', '，谢江鸿', ',谢江鸿', '、县人民政府副县长谢江鸿',
                   '副县长谢江鸿陪同调研。', '，副县长、推演指挥长谢江鸿主持推演。', '县领导谢江鸿参加调研。', '副县长谢江鸿应邀参加视察。','县领导谢江鸿参加。','县领导谢江鸿出席会议。'
                   ,'副县长谢江鸿在平昌分会场参加会议。','副县长谢江鸿参加汇报会。','副县长、县生态环境保护委员会副主任谢江鸿出席会议。','副县长谢江鸿陪同。']

    urls = jiyuehuasearch.get_url_searched("谢江鸿", bz_gov_id)
    for url in urls:

        numbers = extract_numbers(url)
        # 将提取出的数字转换为整数
        numbers = [int(num) for num in numbers]

        if len(numbers) == 1:
            res = getcontent2.getcontent(numbers[0], bz_gov_id, jid)
            res_save = getcontent2.savearticnews2(res, wrong_words, '', bz_gov_id, jid)
            print(res_save)
        elif len(numbers) == 2:
            res = getcontent.getcontent(numbers[0], numbers[1], bz_gov_id, jid)
            res_save = getcontent.saveorupdate2(res, wrong_words, '', bz_gov_id, jid)
            print(res_save)
        else:
            print("未知情况")
