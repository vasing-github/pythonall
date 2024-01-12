class Person:
    def __init__(self, xianzhongleixing, shenfenzheng, name, age, sex, cbzt, moneylevel, joinDate, phone, bank, standard, startTime, account, adres):
        self.xianzhongleixing = xianzhongleixing
        self.shenfenzheng = shenfenzheng
        self.name = name
        self.age = age
        self.sex = sex
        self.cbzt = cbzt
        self.moneylevel = moneylevel
        self.joinDate = joinDate
        self.phone = phone
        self.bank = bank
        self.standard = standard
        self.startTime = startTime
        self.account = account
        self.adres = adres

    def __str__(self):
        return f'Person(xianzhongleixing={self.xianzhongleixing}, shenfenzheng={self.shenfenzheng}, name={self.name}, age={self.age}, sex={self.sex}, cbzt={self.cbzt}, moneylevel={self.moneylevel}, joinDate={self.joinDate}, phone={self.phone}, bank={self.bank}, standard={self.standard}, startTime={self.startTime}, account={self.account}, adres={self.adres})'

import pandas as pd

def read_data_from_excel(file_path):
    # 读取 Excel 文件
    df = pd.read_excel(file_path, na_values=[''],dtype=str)
    df = df.fillna('')

    # 创建一个空字典
    data = {}

    # 遍历每一行数据
    for index, row in df.iterrows():
        # 创建一个 Person 对象
        person = Person(
            row['险种类型'],
            row['证件号码'],
            row['姓名'],
            row['年龄'],
            row['性别'],
            row['参保状态'],
            row['缴费档次'],
            row['参保日期'],
            row['联系电话'],
            row['银行名称'],
            row['当月领取标准'],
            row['待遇享受开始时间'],
            row['发放账号'],
            row['地址']
        )

        # 将 Person 对象添加到字典中
        data[row['证件号码']] = person

    return data
# data = read_data_from_excel('./asses/social.xlsx')
# print(data['51232219741125416X'].__str__())
