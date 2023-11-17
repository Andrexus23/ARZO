from enum import Enum
from typing import Optional

from PyQt5.QtWidgets import QMainWindow


class Alogithm(Enum):
    """Энам."""
    HALF_DIVIDE = 'Метод половинного деления'
    GOLD_SECTION = 'Метод золотого сечения'
    MID_POINT = 'Метод средней точки'
    NEWTON_RAPFSON = 'Метод Ньютона-Рафсона'
    CHORDS = 'Метод хорд'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.epsilon: Optional[float] = None
        self.sigma: Optional[float] = None
        self.a: Optional[float] = None
        self.b: Optional[float] = None
        self.func = None

    def initUi(self, ui):
        self.ui = ui
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.ui.doubleSpinBoxEps.valueChanged.connect(self.updateEps)
        self.show()

    def updateEps(self):
        self.epsilon = self.ui.doubleSpinBoxEps.value()
        print(self.epsilon)
