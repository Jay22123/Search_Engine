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

        self._processor = Processor()
        self._reader = Reader()

        self.setup_control()

    def setup_control(self):
        self.__ui.Load.clicked.connect(self.bnt_load_Clicked)
        self.__ui.Search.clicked.connect(self.bnt_Search_Clicked)

    def bnt_load_Clicked(self):
        filename, filetype = QFileDialog.getOpenFileName(
            self, "Open file", "./data")
        if os.path.isfile(filename):
            data = self._reader.ReadDocument(filename)
            self._processor.LoadData(data)

    def bnt_Search_Clicked(self):
        result = self._processor.Search(str(self.__ui.lineEdit.text()))
        print(result)
        self._processor.Normalize(str(self.__ui.lineEdit.text()))
        # self.__ui.label_3.setText(result)

    def paintEvent(self, event):
        s = self.size()
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setPen(self.penColor)
        qp.setBrush(self.fillColor)
        qp.drawRect(0, 0, s.width(), s.height())
