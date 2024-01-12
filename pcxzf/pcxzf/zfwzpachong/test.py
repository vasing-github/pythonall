from openpyxl import load_workbook

# 加载现有的Excel文件
wb = load_workbook('msg.xlsx')

# 获取活动工作表
ws = wb.active

# 添加新的数据
new_data = [
    ['NewKey1', 'NewMenu1', 'NewHref1', 'NewDays1'],
    ['NewKey2', 'NewMenu2', 'NewHref2', 'NewDays2'],
    # 更多的数据...
]

for data in new_data:
    ws.append(data)

# 保存文件
wb.save('msg.xlsx')