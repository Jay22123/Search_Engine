from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os
from Ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
from Read_Engine import Reader
from DataProcess import Processor


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        self.fillColor = QColor(30, 30, 30, 120)
        self.penColor = QColor("333333")

        self.__ui.title.setWordWrap(True)
        self.__ui.title.setFixedWidth(400)
        self.__ui.title.setStyleSheet(
            "border: 2px solid red; padding: 5px;")

        self.__ui.Search_result.setWordWrap(True)
        self.__ui.Search_result.setFixedWidth(600)

        self._processor = Processor()
        self._reader = Reader()

        self.setup_control()

    def setup_control(self):
        self.__ui.Load.clicked.connect(self.bnt_load_Clicked)
        self.__ui.Search.clicked.connect(self.bnt_Search_Clicked)
        self.__ui.comboBox.currentIndexChanged.connect(self.ccb_Clicked)

    def bnt_load_Clicked(self):
        self._processor.Clear()
        self.__ui.comboBox.clear()
        filenames, filetype = QFileDialog.getOpenFileNames(
            self, "Open file", "./data")
        for filename in filenames:
            if os.path.isfile(filename):
                data = self._reader.ReadDocument(filename)
                self._processor.LoadData(data)

    def bnt_Search_Clicked(self):
        self._dictionary = self._processor.Normalize(
            str(self.__ui.lineEdit.text()))
        for item in self._dictionary:
            self.__ui.comboBox.insertItem(0, (item['Path']))

        if str(self.__ui.lineEdit.text()):
            result = self._processor.Search(str(self.__ui.lineEdit.text()))
            dispaly = ""
            for key, concordance_list in result.items():  # 分別對個別文件取收尋結果key = 文件title
                dispaly += f"[{key}]<br>" + \
                    "<br>".join(concordance_list) + "<br>"

            self.__ui.Search_result.setText(dispaly)
            self.__ui.Search_result.setOpenExternalLinks(True)

    def ccb_Clicked(self):
        num = self.__ui.comboBox.currentIndex()
        data = self._dictionary[num]
        self.__ui.title.setText(data['Title'])

        remove = ["Title", "Content", "Path"]

        dict_text = "\n".join(
            [f"{key}: {value}" for key, value in data.items() if key not in remove])
        self.__ui.Content_analyze.setText(dict_text)

    def paintEvent(self, event):
        s = self.size()
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setPen(self.penColor)
        qp.setBrush(self.fillColor)
        qp.drawRect(0, 0, s.width(), s.height())
