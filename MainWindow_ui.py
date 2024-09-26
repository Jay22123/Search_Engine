# Form implementation generated from reading ui file 'c:\Users\jay\Desktop\Search_Engine\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.file_list = QtWidgets.QListWidget(parent=self.centralwidget)
        self.file_list.setObjectName("file_list")
        self.verticalLayout_3.addWidget(self.file_list)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 7)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.Load = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Load.sizePolicy().hasHeightForWidth())
        self.Load.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Load.setFont(font)
        self.Load.setStyleSheet(" QPushButton {\n"
"                border: 1px solid #199909;\n"
"                border-radius: 15px;\n"
"                color: white;\n"
"                font: bold;\n"
"                padding-left:10px;\n"
"                padding-right:10px;\n"
"                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0.86,stop: 0 #24B375, stop: 1 #7CB31B);\n"
"               \n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #6A4005;\n"
"                border: 7px dashed #09940E;\n"
"                border-radius: 15px;\n"
"                padding-left:10px;\n"
"                padding-right:10px;\n"
"                color: white;\n"
"                font: bold;\n"
"                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0.86,stop: 0 #24B375, stop: 1 #7CB31B);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                border: 1px solid #333333;\n"
"                background-color: #127005;\n"
"                padding-left:10px;\n"
"                padding-right:10px;\n"
"                color: white;\n"
"                font: bold;\n"
"                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0.67, stop: 0 #127005, stop: 1 #127005);\n"
"            }\n"
"             QPushButton:checked {\n"
"                border: 1px solid #333333;\n"
"                padding-left:10px;\n"
"                padding-right:10px;\n"
"                color: white;\n"
"                font: bold;\n"
"            }\n"
"")
        self.Load.setObjectName("Load")
        self.horizontalLayout_3.addWidget(self.Load)
        self.Delete = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Delete.sizePolicy().hasHeightForWidth())
        self.Delete.setSizePolicy(sizePolicy)
        self.Delete.setStyleSheet(" QPushButton {\n"
"                border: 1px solid #199909;\n"
"                border-radius: 15px;\n"
"                color: white;\n"
"                font: bold;\n"
"                padding-left:10px;\n"
"                padding-right:10px;\n"
"                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0.86,stop: 0 #24B375, stop: 1 #7CB31B);\n"
"               \n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #6A4005;\n"
"                border: 7px dashed #09940E;\n"
"                border-radius: 15px;\n"
"                padding-left:10px;\n"
"                padding-right:10px;\n"
"                color: white;\n"
"                font: bold;\n"
"                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0.86,stop: 0 #24B375, stop: 1 #7CB31B);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                border: 1px solid #333333;\n"
"                background-color: #127005;\n"
"                padding-left:10px;\n"
"                padding-right:10px;\n"
"                color: white;\n"
"                font: bold;\n"
"                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0.67, stop: 0 #127005, stop: 1 #127005);\n"
"            }\n"
"             QPushButton:checked {\n"
"                border: 1px solid #333333;\n"
"                padding-left:10px;\n"
"                padding-right:10px;\n"
"                color: white;\n"
"                font: bold;\n"
"            }\n"
"")
        self.Delete.setObjectName("Delete")
        self.horizontalLayout_3.addWidget(self.Delete)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("")
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout_5.addWidget(self.title)
        self.Content_analyze = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Content_analyze.setFont(font)
        self.Content_analyze.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Content_analyze.setObjectName("Content_analyze")
        self.verticalLayout_5.addWidget(self.Content_analyze)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_4.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.Search = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Search.sizePolicy().hasHeightForWidth())
        self.Search.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Search.setFont(font)
        self.Search.setStyleSheet(" QPushButton {\n"
"                border: 1px solid #199909;\n"
"                border-radius: 15px;\n"
"                color: white;\n"
"                font: bold;\n"
"                padding-left:10px;\n"
"                padding-right:10px;\n"
"                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0.86,stop: 0 #24B375, stop: 1 #7CB31B);\n"
"               \n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #6A4005;\n"
"                border: 7px dashed #09940E;\n"
"                border-radius: 15px;\n"
"                padding-left:10px;\n"
"                padding-right:10px;\n"
"                color: white;\n"
"                font: bold;\n"
"                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0.86,stop: 0 #24B375, stop: 1 #7CB31B);\n"
"            }\n"
"            QPushButton:pressed {\n"
"                border: 1px solid #333333;\n"
"                background-color: #127005;\n"
"                padding-left:10px;\n"
"                padding-right:10px;\n"
"                color: white;\n"
"                font: bold;\n"
"                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0.67, stop: 0 #127005, stop: 1 #127005);\n"
"            }\n"
"             QPushButton:checked {\n"
"                border: 1px solid #333333;\n"
"                padding-left:10px;\n"
"                padding-right:10px;\n"
"                color: white;\n"
"                font: bold;\n"
"            }\n"
"")
        self.Search.setObjectName("Search")
        self.horizontalLayout_2.addWidget(self.Search)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Exit = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Exit.sizePolicy().hasHeightForWidth())
        self.Exit.setSizePolicy(sizePolicy)
        self.Exit.setText("")
        self.Exit.setObjectName("Exit")
        self.verticalLayout_2.addWidget(self.Exit)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 7)
        self.horizontalLayout_2.setStretch(1, 9)
        self.horizontalLayout_2.setStretch(2, 3)
        self.horizontalLayout_2.setStretch(3, 5)
        self.horizontalLayout_2.setStretch(4, 1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setStyleSheet("QTextEdit {\n"
"                background-color: rgba(255, 255, 255, 180); \n"
"                border: 1px solid #ccc;\n"
"                color: black; /* 設定文字顏色 */\n"
"                font-size: 24px;\n"
"                font-weight: bold; /* 設定字體粗體 */\n"
"                border-radius: 5px;\n"
"            }")
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_7.addWidget(self.textEdit)
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setStyleSheet("QTextEdit {\n"
"                background-color: rgba(255, 255, 255, 180); \n"
"                border: 1px solid #ccc;\n"
"                color:black; /* 設定文字顏色 */\n"
"                font-size: 24px;\n"
"                font-weight: bold; \n"
"                border-radius: 5px;\n"
"            }\n"
"")
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_7.addWidget(self.textEdit_2)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 9)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "已上傳檔案"))
        self.Load.setText(_translate("MainWindow", "載入資料"))
        self.Delete.setText(_translate("MainWindow", "刪除資料"))
        self.title.setText(_translate("MainWindow", "文章title"))
        self.Content_analyze.setText(_translate("MainWindow", "文字統計"))
        self.Search.setText(_translate("MainWindow", "搜尋"))
