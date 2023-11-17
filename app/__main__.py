from ui.ProgramBasicInterface import *
from MainWindow import MainWindow
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.initUi(Ui_MainWindow())
    sys.exit(app.exec())
