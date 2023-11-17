from enum import Enum

from PyQt5.QtWidgets import QMainWindow

class Alogithm(Enum):

    HALF_DIVIDE = 'Метод половинного деления'
    GOLD_SECTION = 'Метод золотого сечения'
    MID_POINT = 'Метод средней точки'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def initUi(self, ui):
        self.ui = ui
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        self.show()

    def updateParams(self):
        self.algo


