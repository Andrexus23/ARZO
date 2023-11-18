import sys
import random
import matplotlib
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, figure):
        super(MplCanvas, self).__init__(figure)
