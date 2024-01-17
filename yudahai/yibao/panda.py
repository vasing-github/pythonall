# -*- coding: utf-8 -*-

import pandas as pd
import openpyxl
from datetime import datetime

def modify_date(s):
    # 解析日期

    s = next(iter(s))

    dt = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')

    # 提取年月日
    year = dt.year
    month = dt.month
    day = dt.day

    return year,month,day


def start():
    # 读取Excel文件
    df = pd.read_excel('changshou10.xlsx')

    # 按照医保流水号分类，然后转换为字典
    dict_df = {k: v for k, v in df.groupby("医保流水号")}

    # 遍历字典
    for i, (key, value) in enumerate(dict_df.items()):
        money = 0
        # 打开Excel文件
        workbook = openpyxl.load_workbook('chufangtemp.xlsx')

        # 获取当前活动的工作表
        sheet = workbook.active
        for j, (index, row) in enumerate(value.iterrows()):

            # print(f'第{i+1}个医保流水号，第{j+1}行，金额：{row["金额"]}')
            if j == 0:
                sheet['b4'] = next(iter({row["姓名"]}))
                sheet['e4'] = next(iter({row["性别"]}))
                sheet['g4'] = next(iter({row["年龄"]}))

                s = {row["销售日期"]}
                print(s)
                y,m,d =modify_date(s)
                sheet['c5'] = str(y)+'年'
                sheet['d5'] = ' '+str(m)+'月'
                sheet['E5'] = d

            r = j + 9
            # print(r)
            # print(next(iter({row["姓名"]})))
            sheet[f'b{r}'] = next(iter({row["商品名称"]}))+'   '+next(iter({row["规格"]}))
            sheet[f'i{r}'] = next(iter({row["销售数量"]}))

            money = money + int(next(iter({row["金额"]})))
        sheet['f18'] = money
        # 保存为新的Excel文件
        workbook.save(f'./changshou10/chufang{i}.xlsx')


if __name__ == '__main__':
    start()