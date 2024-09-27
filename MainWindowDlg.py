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
        # 設定無邊框視窗
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.__ui.Exit.setStyleSheet("""
            QPushButton {
            background-color: transparent;
            border-image: url('./Exit.png');
            border: none;
            }
        """)

        self.__ui.Content_analyze.setWordWrap(True)  # 啟用自動分行
        # self.__ui.Content_analyze.setFixedSize(288, 477)  # 設定 QLabel 的固定寬度與高度

        self.__ui.Search_input.setPlaceholderText('輸入搜尋關鍵字...')
        self.__ui.Search_input.textChanged.connect(
            self.highlight_text)  # 當文字改變時執行搜尋

        self.__ui.ccb_Page1.currentIndexChanged.connect(
            self.update_Page1)  # 當選項改變時更新 QTextEdit1
        self.__ui.ccb_Page2.currentIndexChanged.connect(
            self.update_Page2)  # 當選項改變時更新 QTextEdit1

        self.fillColor = QColor(30, 30, 30, 120)
        self.penColor = QColor("333333")

        # 記錄載入的檔案的所有資訊
        self.file = {}

        # 檔案列表區域
        self.__ui.file_list.setFont(QFont("Arial", 12))
        self.__ui.file_list.itemSelectionChanged.connect(
            self.display_file_Analysis)

        self._processor = Processor()
        self._reader = Reader()

        self.setup_control()

    def setup_control(self):
        self.__ui.Load.clicked.connect(self.bnt_load_Clicked)
        self.__ui.Delete.clicked.connect(self.delete_selected_file)
        self.__ui.Exit.clicked.connect(self.close_application)

    def close_application(self):
        # 關閉程式
        self.close()

    def bnt_load_Clicked(self):
        self.__ui.ccb_Page1.clear()
        self.__ui.ccb_Page2.clear()
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(
            self, "選擇 XML 檔案", "./data", "XML Files (*.xml);;All Files (*)", options=options)
        if files:
            for file_path in files:
                file_name = file_path.split('/')[-1]
                data = self._reader.ReadDocument(file_path)
                # 統計文章字數,句數等
                result = self._processor.Normalize(data)
                self.file[file_name] = result
                self.__ui.file_list.addItem(file_name)
                self.__ui.ccb_Page1.addItem(file_name, result)
                self.__ui.ccb_Page2.addItem(file_name, result)

    def display_file_Analysis(self):
        # 顯示選擇檔案的統計資料
        selected_item = self.__ui.file_list.currentItem()
        if selected_item:
            file_name = selected_item.text()
            char_count_including_spaces = self.file[file_name]["char_count_including_spaces"]
            char_count_excluding_spaces = self.file[file_name]["char_count_excluding_spaces"]
            word_count = self.file[file_name]["word_count"]
            sentence_count = self.file[file_name]["sentence_count"]
            non_ascii_char_coun = self.file[file_name]["non_ascii_char_count"]
            non_ascii_word_count = self.file[file_name]["non_ascii_word_count"]
            # 將多個變數值組合成一個字串
            combined_text = (
                f"[ {self.file[file_name]["Title"]}]\n"
                f"char_count_including_spaces: {char_count_including_spaces}\n"
                f"char_count_excluding_spaces: {char_count_excluding_spaces}\n"
                f"word_count: {word_count}\n"
                f"sentence_count: {sentence_count}\n"
                f"non_ascii_char_coun: {non_ascii_char_coun}\n"
                f"non_ascii_word_count: {non_ascii_word_count}\n"
            )

            self.__ui.Content_analyze.setText(combined_text)

    def delete_selected_file(self):
        # 刪除選擇的檔案
        selected_item = self.__ui.file_list.currentItem()
        if selected_item:
            file_name = selected_item.text()
            reply = QMessageBox.question(
                self, "確認刪除", f"確定要刪除 {file_name} 嗎？",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                # 移除檔案
                self.file.pop(file_name, None)
                self.__ui.file_list.takeItem(
                    self.__ui.file_list.row(selected_item))
                self.__ui.textEdit.clear()

    def update_Page1(self):
        selected_item = self.__ui.ccb_Page1.currentData()
        if selected_item:
            text = selected_item
            # 顯示內容於 QTextEdit1 中
            search_word = self.__ui.Search_input.text().strip().lower()
            self._processor.Search(text['Content'], search_word)
            self.__ui.textEdit.setPlainText(f"內容:\n{text['Content']}")

    def update_Page2(self):
        selected_item = self.__ui.ccb_Page2.currentData()
        if selected_item:
            text = selected_item
            # 顯示內容於 QTextEdit1 中
            self.__ui.textEdit_2.setPlainText(f"內容:\n{text['Content']}")

    def highlight_text(self):
        # 取得使用者輸入的搜尋關鍵字
        search_word = self.__ui.Search_input.text().strip().lower()

        # 高亮顯示 QTextEdit1 中的關鍵字
        self.highlight_in_text_edit(self.__ui.textEdit, search_word)

        # 高亮顯示 QTextEdit2 中的關鍵字
        self.highlight_in_text_edit(self.__ui.textEdit_2, search_word)

    def highlight_in_text_edit(self, text_edit, search_word):
        if not search_word:
            return

        # 取得 QTextEdit 的文字內容
        text = text_edit.toPlainText()

       # result = self._processor.GetToken(text.lower(),search_word)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("./background.jpg")
        painter.drawPixmap(0, 0, self.width(), self.height(), pixmap)
