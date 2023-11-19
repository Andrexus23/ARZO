import logging
from typing import Optional, Tuple

from PyQt5.QtWidgets import QPlainTextEdit
from scipy.misc import derivative
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

# logging.basicConfig(format='%(message)s', filemode="w", filename='chords.log', encoding='utf-8',
#                     level=logging.INFO)

# interval = [0, 1]
# sigma = 0.01
# epsilon = 0.01
ROUND_NUMBER = 3
DX = 1e-6


def f(x) -> float:
    """Целевая функция: 3 * x ^ 4 + (x - 1) ^ 2"""
    return 3 * x ** 4 + (x - 1) ** 2


def chords_method(lineEdit: QPlainTextEdit, func, a: float, b: float, sigma: float, epsilon: float, round_number=3) -> Optional[
    Tuple[float, float]]:
    """Метод хорд"""
    delta = [a, b]
    f_a = derivative(func, a, dx=DX)
    f_b = derivative(func, b, dx=DX)
    if f_a >= 0 or f_b <= 0:
        lineEdit.appendPlainText('Интервал: [{}, {}]; f(a) = {}; f(b) = {}; Требуется корректировка интервала\n'.format(
            round(a, round_number), round(b, round_number), round(f_a, round_number), round(f_b, round_number)
        ))
        return None, None
    iter_count = 1
    while True:
        x_0 = a - (f_a * (b - a) / (f_b - f_a))
        f_x0 = derivative(func, x_0, dx=DX)
        lineEdit.appendPlainText('Итерация: {}; Интервал: [{}, {}]; f_x0 = {}, x_0 = {}'.format(iter_count, round(a, round_number),
                                                                                    round(b, round_number),
                                                                                    round(f_x0, round_number),
                                                                                    round(x_0, round_number)))
        if f_x0 > sigma:
            b = x_0
        elif f_x0 < -sigma:
            a = x_0
        elif abs(f_x0) <= sigma:
            lineEdit.appendPlainText(
                'Итерация: {}; Интервал: [{}, {}]; x_0 = {} - искомая точка минимума, процедура завершена.\n'.format(
                    iter_count, round(a, round_number), round(b, round_number), round(x_0, round_number)))
            return x_0, f(x_0)

        if (b - a) <= 2 * epsilon:
            x_0 = (a + b) / 2
            lineEdit.appendPlainText(
                'Итерация: {}; Интервал: [{}, {}]; x_0 = (a + b)/2 = {} - искомая точка минимума, процедура завершена.\n'.format(
                    iter_count, round(a, round_number), round(b, round_number), round(x_0, round_number)))
            return x_0, f(x_0)
        lineEdit.appendPlainText('Итерация: {}, Интервал: [{}, {}]; epsilon = {}, (b - a) > 2*epsilon'.format(
            iter_count,
            round(a,round_number),
            round(b, round_number),
            round(epsilon, round_number)
        ))
        iter_count += 1

# # chords_method(f, 0.3, 2, sigma, epsilon)
# chords_method(f, interval[0], interval[1], sigma, epsilon)
