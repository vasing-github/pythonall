
import os
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:\\Users\\龙\\Desktop\\python\\lianghua\\lh\my_env\\Lib\\site-packages\\PyQt5\\Qt5\\plugins'

from PyQt5.QtGui import QFont,QIcon
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QSpacerItem, QDesktopWidget,QFormLayout,QGroupBox,QGridLayout,QMessageBox
import socialData
import re
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initTittle(self):
        # 获取显示器的大小
        desktop = QDesktopWidget()
        screen_rect = desktop.screenGeometry()
        self.screen_width = screen_rect.width()
        self.screen_height = screen_rect.height()
        # 隐藏标题栏
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # 设置窗口背景为从粉红色渐变到紫色的渐变背景
        self.setStyleSheet('''
                    QMainWindow {
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                                     stop:0 pink, stop:1 purple);
                    }
                ''')

        # 创建垂直布局
        self.layout = QVBoxLayout()

        # 第一个组件：标题
        title = QLabel('居民社会保险信息智慧查询系统')
        title.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(title)
        # 设置标题字体大小
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(40)
        title.setFont(font)
    def initSearchUi(self):
        # 第二个组件：输入框和按钮
        sub_layout = QHBoxLayout()
        sub_layout.addStretch()
        self.input = QLineEdit()
        self.input.setFixedWidth(int(self.screen_width * 0.4))
        self.search_button = QPushButton('查询')
        self.reset_button = QPushButton('重置')

        sub_layout.addWidget(self.input)
        sub_layout.addWidget(self.search_button)
        sub_layout.addWidget(self.reset_button)
        sub_layout.addStretch()

        # 设置布局的间距和外边距
        sub_layout.setSpacing(10)
        sub_layout.setContentsMargins(0, 0, 0, 0)

        # 设置输入框和按钮的样式
        self.input.setStyleSheet('''
                    QLineEdit {
                        border: 2px solid gray;
                        border-radius: 20px;
                        padding: 0 8px;
                        selection-background-color: darkgray;
                        font-size: 40px;
                    }
                ''')
        self.search_button.setStyleSheet('''
                    QPushButton {
                        border: 2px solid #8f8f91;
                        border-radius: 20px;
                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                          stop:0 #f6f7fa, stop:1 #dadbde);
                        min-width: 80px;
                        min-height: 40px;
                    }
                    QPushButton:pressed {
                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                          stop:0 #dadbde, stop:1 #f6f7fa);
                    }
                ''')
        self.reset_button.setStyleSheet('''
                    QPushButton {
                        border: 2px solid #8f8f91;
                        border-radius: 20px;
                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                          stop:0 #f6f7fa, stop:1 #dadbde);
                        min-width: 80px;
                        min-height: 40px;
                    }
                    QPushButton:pressed {
                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                          stop:<EUGPSCoordinates> #dadbde, stop:<EUGPSCoordinates> #f6f7fa);
                    }
                ''')
        self.layout.addLayout(sub_layout)

        search_icon = QIcon('./asses/serch.jpg')
        self.search_button.setIcon(search_icon)
        # 在第二个组件下面添加两个弹簧
        self.spacer1 = QSpacerItem(20, int(self.screen_height * 0.3))
        self.layout.insertSpacerItem(2, self.spacer1)

    def initFormUi(self):
        # 第三个组件：wangge
        self.form_group = QGroupBox()
        form_layout = QGridLayout()
        form_layout.setSpacing(10)
        form_layout.setContentsMargins(0, 0, 0, 0)

        font = QFont()
        font.setPointSize(20)

        # 险种类型
        xianzhongleixing_label = QLabel('险种类型：')
        xianzhongleixing_label.setFont(font)
        self.xianzhongleixing_input = QLineEdit()
        self.xianzhongleixing_input.setFont(font)
        form_layout.addWidget(xianzhongleixing_label, 0, 0)
        form_layout.addWidget(self.xianzhongleixing_input, 0, 1)

        # 证件号码
        shenfenzheng_label = QLabel('证件号码：')
        shenfenzheng_label.setFont(font)
        self.shenfenzheng_input = QLineEdit()
        self.shenfenzheng_input.setFont(font)
        form_layout.addWidget(shenfenzheng_label, 0, 2)
        form_layout.addWidget(self.shenfenzheng_input, 0, 3)

        # 姓名
        name_label = QLabel('姓名：')
        name_label.setFont(font)
        self.name_input = QLineEdit()
        self.name_input.setFont(font)
        name_label.setAlignment(QtCore.Qt.AlignRight)
        form_layout.addWidget(name_label, 0, 4)
        form_layout.addWidget(self.name_input, 0, 5)

        # 年龄
        age_label = QLabel('年龄：')
        age_label.setFont(font)
        self.age_input = QLineEdit()
        self.age_input.setFont(font)
        age_label.setAlignment(QtCore.Qt.AlignRight)
        form_layout.addWidget(age_label, 0, 6)
        form_layout.addWidget(self.age_input, 0, 7)

        # 性别
        sex_label = QLabel('性别：')
        sex_label.setFont(font)
        self.sex_input = QLineEdit()
        self.sex_input.setFont(font)
        form_layout.addWidget(sex_label, 0, 8)
        form_layout.addWidget(self.sex_input, 0, 9)

        # 参保状态
        cbzt_label = QLabel('参保状态：')
        cbzt_label.setFont(font)
        self.cbzt_input = QLineEdit()
        self.cbzt_input.setFont(font)
        form_layout.addWidget(cbzt_label, 1, 0)
        form_layout.addWidget(self.cbzt_input, 1, 1)

        # 缴费档次
        moneyleve_label = QLabel('缴费档次：')
        moneyleve_label.setFont(font)
        self.moneyleve_input = QLineEdit()
        self.moneyleve_input.setFont(font)
        form_layout.addWidget(moneyleve_label, 1, 2)
        form_layout.addWidget(self.moneyleve_input, 1, 3)

        # 参保日期
        joinDate_label = QLabel('参保日期：')
        joinDate_label.setFont(font)
        self.joinDate_input = QLineEdit()
        self.joinDate_input.setFont(font)
        joinDate_label.setAlignment(QtCore.Qt.AlignRight)
        form_layout.addWidget(joinDate_label, 1, 4)
        form_layout.addWidget(self.joinDate_input, 1, 5)

        # 联系电话
        phone_label = QLabel('联系电话：')
        phone_label.setFont(font)
        self.phone_input = QLineEdit()
        self.phone_input.setFont(font)
        phone_label.setAlignment(QtCore.Qt.AlignRight)
        form_layout.addWidget(phone_label, 1, 6)
        form_layout.addWidget(self.phone_input, 1, 7)

        # 银行名称
        bank_label = QLabel('银行名称：')
        bank_label.setFont(font)
        self.bank_input = QLineEdit()
        self.bank_input.setFont(font)
        form_layout.addWidget(bank_label, 2, 0)
        form_layout.addWidget(self.bank_input, 2, 1,1,2)

        # 当月领取标准
        standard_label = QLabel('当月领取标准：')
        standard_label.setFont(font)
        self.standard_input = QLineEdit()
        self.standard_input.setFont(font)
        form_layout.addWidget(standard_label, 2, 3)
        form_layout.addWidget(self.standard_input, 2, 4)

        # 待遇享受开始时间
        start_time_label = QLabel('待遇享受开始时间：')
        start_time_label.setFont(font)
        self.start_time_input = QLineEdit()
        self.start_time_input.setFont(font)
        form_layout.addWidget(start_time_label, 2, 5)
        form_layout.addWidget(self.start_time_input, 2, 6)

        # 发放账号
        account_label = QLabel('发放账号：')
        account_label.setFont(font)
        self.account_input = QLineEdit()
        self.account_input.setFont(font)
        form_layout.addWidget(account_label, 3, 0)
        form_layout.addWidget(self.account_input, 3, 1,1,2)

        # 地址
        address_label = QLabel('地址：')
        address_label.setFont(font)
        self.address_input = QLineEdit()
        self.address_input.setFont(font)
        address_label.setAlignment(QtCore.Qt.AlignRight)
        form_layout.addWidget(address_label, 3, 3)
        form_layout.addWidget(self.address_input, 3, 4,1,2)

        # 设置查询结果组件的样式
        self.form_group.setStyleSheet('''
             QGroupBox {
                 border: 2px solid gray;
                 border-radius: 10px;
                 background-color: rgba(255,255,255,200);
                 font-size: 50px;
             }
         ''')
        self.form_group.setLayout(form_layout)
        self.layout.addWidget(self.form_group)
        self.form_group.setVisible(False)

    def initUI(self):
        # 最大化窗口
        self.showMaximized()
        self.initTittle()
        self.initSearchUi()
        self.initFormUi()



        # self.layout.addLayout(self.result_widget)
        # 连接按钮的信号和槽函数
        self.search_button.clicked.connect(self.on_search)
        self.reset_button.clicked.connect(self.on_reset)

        # 设置窗口布局
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)
    def mathData(self,data):
        self.xianzhongleixing_input.setText(data.xianzhongleixing if data.xianzhongleixing else ' ')
        self.shenfenzheng_input.setText(data.shenfenzheng if data.shenfenzheng else ' ')
        self.name_input.setText(data.name if data.name else ' ')
        self.age_input.setText(str(data.age) if data.age else ' ')
        self.sex_input.setText(data.sex if data.sex else ' ')
        self.cbzt_input.setText(data.cbzt if data.cbzt else ' ')
        self.moneyleve_input.setText(str(data.moneylevel) if data.moneylevel else ' ')
        self.joinDate_input.setText(str(data.joinDate) if data.joinDate else ' ')
        self.phone_input.setText(str(data.phone) if data.phone else ' ')
        self.bank_input.setText(str(data.bank) if data.bank else ' ')
        self.standard_input.setText(str(data.standard) if data.standard else ' ')
        self.start_time_input.setText(str(data.startTime) if data.startTime else ' ')
        self.account_input.setText(str(data.account) if data.account else ' ')
        self.address_input.setText(data.adres)
    def on_search(self):
        # 获取输入框中的值
        value = self.input.text()
        # 验证身份证号码是否符合格式要求
        pattern = r'^\d{17}[\dxX]$'
        if not re.match(pattern, value):
            QMessageBox.warning(self, '警告', '身份证号码格式不正确')
        # try:
        #     # 执行查询操作
        #     self.name_input.setText(local_data[value].name)
        # except KeyError:
        #     # 如果发生 KeyError 异常，弹出提示框
        #     QMessageBox.warning(self, '警告', '未找到对应的数据')
        elif value not in local_data:
            QMessageBox.warning(self, '警告', '非本社区人员')
        else:
            self.mathData(local_data[value])
            index1 = self.layout.indexOf(self.spacer1)
            if index1 != -1:
              item1 = self.layout.takeAt(index1)
              item1.spacerItem().changeSize(0, 0)
              del item1


            self.form_group.setVisible(True)

    def on_reset(self):
         # 重置按钮点击事件处理函数
         # 重置按钮点击事件处理函数
         self.input.clear()
         if self.form_group.isVisible():
             # 显示弹簧
             self.spacer1.changeSize(20, int(self.screen_height * 0.3))
             self.layout.insertSpacerItem(2, self.spacer1)
             self.form_group.setVisible(False)


if __name__ == '__main__':
    local_data = socialData.read_data_from_excel('./asses/social.xlsx')
    # print(local_data['51232219741125416X'].__str__())
    app = QApplication([])
    app.addLibraryPath("C:/Users/龙/Desktop/python/job/lib/site-packages/PyQt5/Qt5/plugins")
    window = MainWindow()
    window.show()
    app.exec_()
    input("please input any key to exit!")


