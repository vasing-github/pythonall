# -*- coding: utf-8 -*-
# return {'水质监测': 18, '不动产登记': 6, '征地信息': 4, '财政资金直达基层': 2, '环评公示': 2, '助企纾困': 1, '公共资源交易': 1, '价格信息': 1, '卫生健康': 1, '食品药品监管': 1}
menu_num_dic = {'水质监测': 18, '不动产登记': 6, '征地信息': 4, '财政资金直达基层': 2, '环评公示': 2, '助企纾困': 1, '公共资源交易': 1, '价格信息': 1, '卫生健康': 1, '食品药品监管': 1}
# 使用 sorted 函数对字典按值排序，并取前10个项目
sorted_items = sorted(menu_num_dic.items(), key=lambda item: item[1], reverse=True)[:10]

# 将排序后的元组列表转换为字典
sorted_dict = dict(sorted_items)

# 打印排序后的字典
print(sorted_dict)
converted_list = [{"name": item[0], "value": item[1]} for item in sorted_items]
print(converted_list)
