import tushare as ts
import pandas as pd
# 设置tushare API令牌
ts.set_token('75e3f4b8fe02b2fee3d57e952c94804e9062ce4076850af35894bb70')


# 初始化tushare接口
pro = ts.pro_api()

 # 获取股票代码为300357的历史交易数据
df = pro.daily(ts_code='601633.SH', start_date='20200101', end_date='20231231')
df.to_csv("chagnchengqiche_data.csv")