import logging
from typing import Tuple

from PyQt5.QtWidgets import QPlainTextEdit


def f(x) -> float:
    """Целевая функция: 3 * x^4 + (x - 1)^2"""
    return 3 * x ** 4 + (x - 1) ** 2


def half_divide(
        lineEdit: QPlainTextEdit,
        a: float, b: float,
        sigma: float, epsilon: float,
        round_number=3,
) -> Tuple[float, float]:
    """Метод половинного деления"""
    lineEdit.appendPlainText('Запущен метод половинного сечения. '
                             'Интервал: [{}, {}]; sigma = {}; epsilon = {}'.format(a, b, sigma, epsilon))
    delta = b - a
    iter_count = 1

    while abs(delta) > 2 * epsilon:
        c = (a + b) / 2
        x_1 = c - (sigma / 2)
        x_2 = c + (sigma / 2)
        f_x_1 = f(x_1)
        f_x_2 = f(x_2)
        if f_x_1 < f_x_2:
            b = x_2
        elif f_x_1 > f_x_2:
            a = x_1

        lineEdit.appendPlainText('Итерация {}; Интервал: [{}, {}]; '
                                 'c = {}; x_1 = {}; x_2 = {}; f(x_1) = {}; f(x_2) = {}.'.format(
            iter_count,
            round(a, round_number),
            round(b, round_number),
            round(c, round_number),
            round(x_1, round_number),
            round(x_2, round_number),
            round(f_x_1, round_number),
            round(f_x_2, round_number),
        ))

        delta = b - a
        iter_count += 1

    result = float(a + b) / 2
    f_result = f(result)
    lineEdit.appendPlainText('Результат метода половинного сечения: {}\n\n'.format(round(result, round_number)))
    return result, f_result

# half_divide(0.3, 2, sigma, epsilon)
# half_divide(interval[0], interval[1], sigma, epsilon)
