import math
from typing import Any, Tuple, Optional
from matplotlib import pyplot
from numpy import linspace
from PyQt5.QtWidgets import QPlainTextEdit

from constants.constants import RANGE, ROUND_NUMBER
from half_divide import half_divide
from golden_section import golden_section
from mid_point import mid_point
from chords import chords_method
from newton_raphson import newton_raphson

class PlotBuilder:
    """Класс построения графиков для алгоритмов."""

    def __init__(self,
                 plt: pyplot,
                 dpi: int = 300,
                 round_number=3):
        """Конструктор"""
        self.round_number = ROUND_NUMBER
        self._plt: pyplot = plt
        self._dpi:int = dpi

    def build_plot(self,
                   lineEdit: QPlainTextEdit,
                   a: Optional[float],
                   b: Optional[float],
                   sigma: Optional[float],
                   epsilon: Optional[float],
                   method: Any,
                   target_function: Any,
                   target_function_text: str,
                   ):
        """Построение графика для half_divide."""


        x_0 = None
        f_x0 = None
        sigma_output = None
        if method is half_divide:
            x_0, f_x0 = method(lineEdit, target_function, a, b, sigma, epsilon)
        elif method is golden_section:
            x_0, f_x0, sigma_output = method(lineEdit, target_function, a, b, epsilon)
        elif method is mid_point:
            x_0, f_x0 = method(lineEdit, target_function, a, b, sigma, epsilon)
        elif method is chords_method:
            x_0, f_x0 = method(lineEdit, target_function, a, b, sigma, epsilon)
        elif method is newton_raphson:
            x_0, f_x0 = method(lineEdit, target_function, b, sigma)
        range_x = 0
        if method is not newton_raphson:
            range_x = float(abs(b - a) / 2)
        else:
            range_x = RANGE

        self._plt.clf()

        if x_0 is None and f_x0 is None or math.isnan(x_0) or math.isnan(f_x0):
            return None, None, self._plt

        visible_range = [x_0 - range_x, x_0 + range_x]
        x_array = linspace(visible_range[0], visible_range[1], int((visible_range[1] - visible_range[0]) * 100))
        y_array = [target_function(x_value) for x_value in x_array]

        self._plt.grid(True)
        self._plt.plot(x_array, y_array)
        self._plt.xlabel('x')
        self._plt.ylabel('y')
        title_arg = method.__doc__ + '\n' + target_function_text + '\n'
        if method in [half_divide, mid_point, chords_method]:
            title_arg += \
                'Интервал: [{}, {}]; '.format(round(a, self.round_number), round(b, self.round_number)) + \
                'Sigma = {}; '.format(sigma) + \
                'Epsilon = {}; '.format(epsilon)
        elif method is golden_section:
            title_arg += \
                'Интервал: [{}, {}]; '.format(round(a, self.round_number), round(b, self.round_number)) + \
                'Sigma = {}; '.format(sigma_output) + \
                'Epsilon = {}; '.format(epsilon)
        elif method is newton_raphson:
            title_arg += \
                'x_0: {}; '.format(round(b, self.round_number)) + \
                'Sigma = {}; '.format(sigma)

        self._plt.title(title_arg)
        self._plt.plot(x_0, f_x0, marker='o', color='red', ms = 8)
        self._plt.text(x_0 - 0.15, f_x0 + 1, s='(' + str(round(x_0, self.round_number)) + ', ' + str(round(f_x0, self.round_number)) + ')')
        # self._plt.savefig(im_path, dpi=self._dpi)
        return x_0, f_x0, self._plt









