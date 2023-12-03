from enum import Enum
from typing import Optional, Any
from PyQt5.QtWidgets import QGridLayout
from matplotlib import pyplot as plt
from app.Canvas import MplCanvas
from build_plot import PlotBuilder
from PyQt5.QtWidgets import QMainWindow
from constants import f
from half_divide import half_divide
from golden_section import golden_section
from mid_point import mid_point
from chords import chords_method
from newton_raphson import newton_raphson
from constants.constants import *


class Algorithm(Enum):
    """Энам для алгоритмов."""
    HALF_DIVIDE = 'Метод половинного деления'
    GOLD_SECTION = 'Метод золотого сечения'
    MID_POINT = 'Метод средней точки'
    NEWTON_RAPFSON = 'Метод Ньютона-Рафсона'
    CHORDS = 'Метод хорд'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvas = None
        self.plotWindowLayout = None
        self.plotWindow = None
        self.epsilon: Optional[float] = None
        self.sigma: Optional[float] = None
        self.a: Optional[float] = None
        self.b: Optional[float] = None
        self.algo: Algorithm = Algorithm.HALF_DIVIDE
        self.func = lambda x: 3 * x ** 4 + (x - 1) ** 2
        self.textFunc = "3 * x ** 4 + (x - 1) ** 2"
        self.plt = plt

    def initPlotWindow(self):
        """Инициализация окна графика."""
        self.plotWindow: QMainWindow = QMainWindow(self)
        self.plotWindowLayout = QGridLayout(self.plotWindow)
        self.plotWindow.setLayout(self.plotWindowLayout)
        self.plotWindow.setFixedSize(800, 600)
        self.plotBuilder = PlotBuilder(self.plt, dpi=DPI, round_number=ROUND_NUMBER)
        self.plotWindow.setWindowTitle('График работы метода')

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
        self.ui.logTextEdit.setReadOnly(True)
        self.ui.doubleSpinBoxEps.setValue(EPS)
        self.ui.doubleSpinBoxSigma.setValue(SIGMA)
        self.ui.doubleSpinBox_A.setValue(A)
        self.ui.doubleSpinBox_B.setValue(B)
        self.epsilon = self.ui.doubleSpinBoxEps.value()
        self.sigma = self.ui.doubleSpinBoxSigma.value()
        self.a = self.ui.doubleSpinBox_A.value()
        self.b = self.ui.doubleSpinBox_B.value()
        self.initPlotWindow()
        self.ui.lineEditFunc.textChanged.connect(self.updateFunc)
        self.ui.lineEditFunc.setText(self.textFunc)
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
        self.ui.logTextEdit.clear()
        if not self.checkParams():
            return
        plot_tmp = None
        target_func = lambda x: eval(self.textFunc)
        x, fx, plot_tmp = None, None, None
        try:
            if self.algo == Algorithm.HALF_DIVIDE:
                x, fx, plot_tmp = self.plotBuilder.build_plot(
                    lineEdit=self.ui.logTextEdit,
                    a=self.a,
                    b=self.b,
                    sigma=self.sigma,
                    epsilon=self.epsilon,
                    method=half_divide,
                    target_function=target_func,
                    target_function_text=self.textFunc
                )
            elif self.algo == Algorithm.GOLD_SECTION:
                x, fx, plot_tmp = self.plotBuilder.build_plot(
                    lineEdit=self.ui.logTextEdit,
                    a=self.a,
                    b=self.b,
                    sigma=None,
                    epsilon=self.epsilon,
                    method=golden_section,
                    target_function=target_func,
                    target_function_text=self.textFunc
                )
            elif self.algo == Algorithm.MID_POINT:
                x, fx, plot_tmp = self.plotBuilder.build_plot(
                    lineEdit=self.ui.logTextEdit,
                    a=self.a,
                    b=self.b,
                    sigma=self.sigma,
                    epsilon=self.epsilon,
                    method=mid_point,
                    target_function=target_func,
                    target_function_text=self.textFunc
                )
            elif self.algo == Algorithm.NEWTON_RAPFSON:
                x, fx, plot_tmp = self.plotBuilder.build_plot(
                    lineEdit=self.ui.logTextEdit,
                    a=None,
                    b=self.b,
                    sigma=self.sigma,
                    epsilon=None,
                    method=newton_raphson,
                    target_function=target_func,
                    target_function_text=self.textFunc
                )
            elif self.algo == Algorithm.CHORDS:
                x, fx, plot_tmp = self.plotBuilder.build_plot(
                    lineEdit=self.ui.logTextEdit,
                    a=self.a,
                    b=self.b,
                    sigma=self.sigma,
                    epsilon=self.epsilon,
                    method=chords_method,
                    target_function=target_func,
                    target_function_text=self.textFunc
                )
        except (SyntaxError, TypeError, NameError):
            self.ui.logTextEdit.appendPlainText('Целевая функция введена некорректно')
        if x is None and fx is None:
            return
        self.plt = plot_tmp
        self.canvas = MplCanvas(figure=self.plt.gcf())
        self.plotWindow.setCentralWidget(self.canvas)
        self.plotWindow.show()

    def checkParams(self):
        if self.sigma >= 2 * self.epsilon and self.algo not in [Algorithm.GOLD_SECTION, Algorithm.NEWTON_RAPFSON]:
            self.ui.logTextEdit.appendPlainText("Недопустимое сочетание параметров: sigma >= 2 * epsilon")
            return False
        if self.a >= self.b and self.algo != Algorithm.NEWTON_RAPFSON:
            self.ui.logTextEdit.appendPlainText("Недопустимое значение параметров: a >= b")
            return False
        return True

    def updateFunc(self):
        txt = self.ui.lineEditFunc.text()
        self.textFunc = self.ui.lineEditFunc.text()
