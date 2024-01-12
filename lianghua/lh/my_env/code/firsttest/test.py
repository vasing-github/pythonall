import tushare as ts
import pandas as pd

# 设置tushare API令牌
ts.set_token('75e3f4b8fe02b2fee3d57e952c94804e9062ce4076850af35894bb70')
import sys
sys.setrecursionlimit(3000)
import matplotlib.pyplot as plt
# 初始化tushare接口
pro = ts.pro_api()

# # 获取股票代码为300357的历史交易数据
# df = pro.daily(ts_code='515790.SH', start_date='20200101', end_date='20231231')
# df.to_csv("guangfu_data.csv")


# 读取csv文件，假设文件名是stock.csv
# data = pd.read_csv("stock_data.csv")
import csv
data = []
with open("stock_data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # 跳过第一行表头
    for row in reader:
        data.append(row)

# 假设您的数据存储在一个名为data的二维数组中
# 提取第2列和第6列的数据
x_data = [row[2] for row in data]
y_data = [float(row[6]) for row in data]

# 使用plot函数绘制折线图
plt.plot(x_data, y_data)


# 标记特定的点
plt.scatter([x_data[0], x_data[2]], [y_data[0], y_data[2]], color='red')

# 显示图形
plt.show()