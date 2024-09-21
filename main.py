
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from MainWindowDlg import MainWindow


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ui = MainWindow()

    ui.show()
    sys.exit(app.exec_())
