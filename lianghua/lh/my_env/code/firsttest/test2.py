import tushare as ts
import pandas as pd
# 设置tushare API令牌
ts.set_token('75e3f4b8fe02b2fee3d57e952c94804e9062ce4076850af35894bb70')

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
with open("chagnchengqiche_data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # 跳过第一行表头
    for row in reader:
        data.append(row)
lowpoints = []  # 存储低点
highpoints = [] #和高点的列表
lowPricePoint,highPricePoint = (0,0)
start = 0
starts = []
ends = []

def mainsearch(start,data):
    starts.append(start)
    global lowPricePoint,highPricePoint
    for i in range(start, len(data)):
        if data[i][6] >= data[highPricePoint][6]:
            highPricePoint = i
        if data[i][6] <= data[lowPricePoint][6]:
            lowPricePoint = i
        if i - start == 30:
            ends.append(i)
            break
    if  data[start][6] <  data[i][6]:
        lowpoints.append(lowPricePoint)

        start = highPricePoint
        lowPricePoint = highPricePoint
    else:
        highpoints.append(highPricePoint)

        start = lowPricePoint
        highPricePoint = lowPricePoint
    if i != len(data)-1:
        mainsearch(start,data)

mainsearch(0,data)
print("low:", lowpoints)
print("high:",highpoints)
print("starts:",starts)
print("ends:",ends)
# 假设您的数据存储在一个名为data的二维数组中
# 提取第2列和第6列的数据
x_data = [row[2] for row in data]
y_data = [float(row[6]) for row in data]

# 使用plot函数绘制折线图
plt.plot(x_data, y_data)

# 标记特定的点
x_highPoints = []
y_highPoints = []
for point in highpoints:
    x_highPoints.append(data[point][2])
    y_highPoints.append(float(data[point][6]))
plt.scatter(x_highPoints, y_highPoints, color='red')

x_lowPoints = []
y_lowPoints = []
for point in lowpoints:
    x_lowPoints.append(data[point][2])
    y_lowPoints.append(float(data[point][6]))
plt.scatter(x_lowPoints, y_lowPoints, color='black')

x_starts = []
y_starts = []
for point in starts:
    x_starts.append(data[point][2])
    y_starts.append(float(data[point][6]))
# plt.scatter(x_starts, y_starts, color='green', marker='x')

x_ends = []
y_ends = []
for point in ends:
    x_ends.append(data[point][2])
    y_ends.append(float(data[point][6]))
plt.scatter(x_ends, y_ends, color='green', marker='x')


# 显示图形
plt.show()


