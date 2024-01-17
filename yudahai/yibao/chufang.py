# -*- coding: utf-8 -*-

import openpyxl

# 打开Excel文件
workbook = openpyxl.load_workbook('chufang.xlsx')

# 获取当前活动的工作表
sheet = workbook.active

# 修改单元格的内容
sheet['b4'] = '新的内容'  # 修改A1单元格的内容

# 保存为新的Excel文件
workbook.save('chufang2.xlsx')
