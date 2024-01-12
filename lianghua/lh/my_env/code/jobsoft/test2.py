
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:\\Users\\龙\\Desktop\\python\\lianghua\\lh\my_env\\Lib\\site-packages\\PyQt5\\Qt5\\plugins'

from PyQt5.QtGui import QFont,QIcon
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QSpacerItem, QDesktopWidget
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        # 最大化窗口
        self.showMaximized()
        desktop = QDesktopWidget()

        # 获取显示器的大小
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

        self.layout = QVBoxLayout()
        # 创建垂直布局

        # 第一个组件：标题
        title = QLabel('居民社会保险信息智慧查询系统')
        title.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(title)
        # 设置标题字体大小
        font = QFont()
        font.setPointSize(40)
        title.setFont(font)

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


        # 第三个组件：查询结果
        self.result_widget = QWidget()
        result_layout = QHBoxLayout()
        result_layout.addStretch()
        self.id_label = QLabel('身份证号码：')
        self.name_label = QLabel('姓名：')
        self.gender_label = QLabel('性别：')
        self.address_label = QLabel('居住地址：')
        self.retired_label = QLabel('是否退休：')
        self.retire_time_label = QLabel('退休时间：')
        self.salary_label = QLabel('工资待遇：')
        result_layout.addWidget(self.id_label)
        result_layout.addWidget(self.name_label)
        result_layout.addWidget(self.gender_label)
        result_layout.addWidget(self.address_label)
        result_layout.addWidget(self.retired_label)
        result_layout.addWidget(self.retire_time_label)
        result_layout.addWidget(self.salary_label)
        result_layout.addStretch()
        self.result_widget.setLayout(result_layout)
        self.layout.addWidget(self.result_widget)
        # 创建表格布局
        # table_layout = QVBoxLayout()
        # row1 = QHBoxLayout()
        # id_number = '1234567890'  # 查询结果中的身份证号码
        # self.id_label = QLabel(f'身份证号码：{id_number}')
        # row1.addWidget(self.id_label)
        #
        #
        # row1.addWidget(QLabel('姓名：'))
        # row1.addWidget(QLabel('性别：'))
        # table_layout.addLayout(row1)
        # row2 = QHBoxLayout()
        # row2.addWidget(QLabel('居住地址：'))
        # row2.addWidget(QLabel('是否退休：'))
        # row2.addWidget(QLabel('退休时间：'))
        # table_layout.addLayout(row2)
        # row3 = QHBoxLayout()
        # row3.addWidget(QLabel('工资待遇：'))
        # table_layout.addLayout(row3)
        #
        # self.result_widget.setLayout(table_layout)
        # # 设置查询结果组件的最小高度
        # self.result_widget.setMinimumHeight(200)

        # 设置查询结果组件默认不可见
        # self.result_widget.setVisible(False)
        # 设置查询结果组件的样式
        self.result_widget.setStyleSheet('''
            QWidget {
                border: 2px solid gray;
                border-radius: 10px;
                background-color: rgba(255, 255, 255, 200);
            }
        ''')
        # self.layout.addLayout(self.result_widget)
        # 连接按钮的信号和槽函数
        self.search_button.clicked.connect(self.on_search)
        self.reset_button.clicked.connect(self.on_reset)

        # 设置窗口布局
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def on_search(self):
         # 查询按钮点击事件处理函数
         # 在这里添加查询逻辑，更新查询结果组件中的标签内容
         # 例如：
         id_number = '1234567890'
         name = '张三'
         gender = '男'
         address = '北京市朝阳区'
         retired = '是'
         retire_time = '2023-08-01'
         salary = '8000元/月'
         self.id_label.setText(f'身份证号码：{id_number}')
         # self.name_label.setText(f'姓名：{name}')
         # ...
         index1 = self.layout.indexOf(self.spacer1)
         if index1 != -1:
             item1 = self.layout.takeAt(index1)
             item1.spacerItem().changeSize(0, 0)
             del item1


         self.result_widget.setVisible(True)

    def on_reset(self):
         # 重置按钮点击事件处理函数
         # 重置按钮点击事件处理函数
         self.input.clear()


         # 显示弹簧
         self.spacer1.changeSize(20, int(self.screen_height * 0.3))
         self.layout.insertSpacerItem(2, self.spacer1)
         self.result_widget.setVisible(False)



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
