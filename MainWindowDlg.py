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
        self.showMaximized()
        self.fillColor = QColor(30, 30, 30, 120)
        self.penColor = QColor("333333")
        
        #記錄載入的檔案的所有資訊
        self.file = {}
       


         # 檔案列表區域
        self.__ui.file_list.setFont(QFont("Arial", 12))
        self.__ui.file_list.itemSelectionChanged.connect(self.display_file_content)

       

        self._processor = Processor()
        self._reader = Reader()

        self.setup_control()

    def setup_control(self):
        self.__ui.Load.clicked.connect(self.bnt_load_Clicked)
        self.__ui.Search.clicked.connect(self.bnt_Search_Clicked)
       

    def bnt_load_Clicked(self):
        self._processor.Clear()
       
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self, "選擇 XML 檔案", "./data", "XML Files (*.xml);;All Files (*)", options=options)
        if files:
            for file_path in files:
                file_name = file_path.split('/')[-1]
                data = self._reader.ReadDocument(file_path)
                #統計文章字數,句數等
                result = self._processor.Normalize(data) 
                self.file[file_name] = result
                self.__ui.file_list.addItem(file_name)

    
    def display_file_content(self):
        # 顯示選擇的檔案內容
        selected_item = self.__ui.file_list.currentItem()
        if selected_item:
            file_name = selected_item.text()
            content = self.files.get(file_name, "")
            self.textEdit.setText(content)
    

    def bnt_Search_Clicked(self):
        self.__ui.Search_result.clear()

        
        self._dictionary = self._processor.Normalize(str(self.__ui.lineEdit.text()))

        for item in self._dictionary:
            self.__ui.comboBox.insertItem(0, (item['Path']))

        if str(self.__ui.lineEdit.text()):
            result = self._processor.Search(str(self.__ui.lineEdit.text()))
            dispaly = ""
            for key, concordance_list in result.items():  # 分別對個別文件取收尋結果key = 文件title
                dispaly += f'<span style="color:#0023F5;">[{key}]</span><br>' + "<br>".join(concordance_list) + "<br>"

            self.__ui.Search_result.setText(dispaly)
            self.__ui.Search_result.setOpenExternalLinks(True)

   

    def paintEvent(self, event):
        s = self.size()
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing, True)
        qp.setPen(self.penColor)
        qp.setBrush(self.fillColor)
        qp.drawRect(0, 0, s.width(), s.height())
