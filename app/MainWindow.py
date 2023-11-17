from enum import Enum
from typing import Optional

from PyQt5.QtWidgets import QMainWindow


class Algorithm(Enum):
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
        self.algo: Algorithm = Algorithm.HALF_DIVIDE
        self.func = lambda x: 3 * x ** 4 + (x - 1) ** 2

    def initUi(self, ui):
        self.ui = ui
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.ui.doubleSpinBoxEps.valueChanged.connect(self.updateEps)
        self.ui.doubleSpinBoxSigma.valueChanged.connect(self.updateSigma)
        self.ui.doubleSpinBox_A.valueChanged.connect(self.updateLeft)
        self.ui.doubleSpinBox_B.valueChanged.connect(self.updateRight)
        self.ui.runButton.clicked.connect(self.runAlgo)
        self.ui.AlgoComboBox.currentIndexChanged.connect(self.updateAlgo)
        self.show()

    def updateEps(self):
        self.epsilon = self.ui.doubleSpinBoxEps.value()

    def updateSigma(self):
        self.sigma = self.ui.doubleSpinBoxSigma.value()

    def updateLeft(self):
        self.a = self.ui.doubleSpinBox_A.value()

    def updateRight(self):
        self.b = self.ui.doubleSpinBox_B.value()

    def updateAlgo(self):
        text = self.ui.AlgoComboBox.currentText()
        if text == Algorithm.HALF_DIVIDE.value:
            self.algo = Algorithm.HALF_DIVIDE
        elif text == Algorithm.GOLD_SECTION.value:
            self.algo = Algorithm.GOLD_SECTION
        elif text == Algorithm.MID_POINT.value:
            self.algo = Algorithm.MID_POINT
        elif text == Algorithm.NEWTON_RAPFSON.value:
            self.algo = Algorithm.NEWTON_RAPFSON
        elif text == Algorithm.CHORDS.value:
            self.algo = Algorithm.CHORDS

    def runAlgo(self):
        """Запуск вычислительного алгоритма."""
        if self.algo == Algorithm.HALF_DIVIDE:
            pass
        elif self.algo == Algorithm.GOLD_SECTION:
            pass
        elif self.algo == Algorithm.MID_POINT:
            pass
        elif self.algo == Algorithm.NEWTON_RAPFSON:
            pass
        elif self.algo == Algorithm.CHORDS:
            pass
        # ...
