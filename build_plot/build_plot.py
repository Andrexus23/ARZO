from typing import Any, Tuple, Optional

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

from half_divide.half_divide import half_divide, f


class PlotBuilder:
    """Класс построения графиков для алгоритмов."""

    def __init__(self,
                 plt: matplotlib.pyplot,
                 dpi: int = 300,
                 round_number=3):
        """Конструктор"""
        self.round_number = 3
        self._plt:matplotlib.pyplot = plt
        self._dpi:int = dpi

    def build_for_half_divide(self, a: float, b: float, visible_range: Tuple, sigma: Optional[float],
                              epsilon: float,
                              method: Any,
                              target_function: Any,
                              im_path = 'half_divide.png'):
        """Построение графика для half_divide."""

        fig, ax = self._plt.subplots()

        x_array = np.linspace(visible_range[0], visible_range[1], int((visible_range[1] - visible_range[0]) * 100))
        y_array = [target_function(x_value) for x_value in x_array]

        x_0, f_x0 = method(a, b, sigma, epsilon, self.round_number)

        self._plt.grid(True)
        self._plt.plot(x_array, y_array)
        self._plt.xlabel('x')
        self._plt.ylabel('y')
        plt.plot(x_0, f_x0, marker='o', color='red', ms = 8)
        plt.text(x_0 - 0.15, f_x0 + 1, s='(' + str(round(x_0, self.round_number)) + ', ' + str(round(f_x0, self.round_number)) + ')')
        self._plt.savefig(im_path, dpi = self._dpi)


plotBuilder = PlotBuilder(plt)
plotBuilder.build_for_half_divide(0, 4, (-1, 1.5), 0.001, 0.1, half_divide, f)





