import logging
import warnings

from PyQt5.QtWidgets import QPlainTextEdit

warnings.filterwarnings("ignore", category=DeprecationWarning)
from scipy.misc import derivative

# file = '../mid_point.log'
# logging.basicConfig(format='%(message)s', filename=file, encoding='utf-8', level=logging.INFO)

DX = 1e-6
ROUND_NUMBER = 3


def f(x: float) -> float:
    """Целевая функция: 3 * x ^ 4 + (x - 1) ^ 2"""
    return 3 * (x ** 4) + (x - 1) ** 2


def mid_point(lineEdit: QPlainTextEdit, a: float, b: float, sigma: float, epsilon: float) -> tuple[float, float]:
    """Метод средней точки"""
    lineEdit.appendPlainText('Запущен метод средней точки. '
                             'Интервал: [{}, {}]; sigma = {}; epsilon = {}'.format(a, b, sigma, epsilon))
    iter_count = 0
    lineEdit.appendPlainText("Начало работы алгоритма.\nInterval = [{}, {}], epsilon = {}, sigma = {}".format(
        round(a, ROUND_NUMBER),
        round(b, ROUND_NUMBER),
        epsilon,
        sigma
    ))
    while abs(b - a) > 2 * epsilon:
        iter_count += 1
        x_0 = (a + b) / 2
        df_x_0 = derivative(f, x_0, dx=DX)
        lineEdit.appendPlainText("Итерация №{}.\nx_0 = {}, df_x_0 = {}".format(
            iter_count,
            round(x_0, ROUND_NUMBER),
            round(df_x_0, ROUND_NUMBER)
        ))
        if df_x_0 > sigma:
            b = x_0
            lineEdit.appendPlainText("df_x_0 > {}, Interval = [{}, {}]".format(
                sigma,
                round(a, ROUND_NUMBER),
                round(b, ROUND_NUMBER)
            ))
        elif df_x_0 < -sigma:
            a = x_0
            lineEdit.appendPlainText("df_x_0 < {}, Interval = [{}, {}]".format(
                -sigma,
                round(a, ROUND_NUMBER),
                round(b, ROUND_NUMBER)
            ))
        elif abs(df_x_0) <= sigma:
            break
    result = (a + b) / 2
    f_x = f(result)
    lineEdit.appendPlainText("Результат работы алгоритма: x = {}, f(x) = {}\n".format(
        round(result, ROUND_NUMBER),
        round(f_x, ROUND_NUMBER)
    ))
    return result, f_x


# x, y = mid_point(0.0, 4.0, 0.01, 0.01)
