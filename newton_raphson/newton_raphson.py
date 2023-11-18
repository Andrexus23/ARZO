import logging
import warnings

from PyQt5.QtWidgets import QPlainTextEdit

warnings.filterwarnings("ignore", category=DeprecationWarning)
from scipy.misc import derivative

# file = '../newton_raphson.log'
# logging.basicConfig(format='%(message)s', filename=file, encoding='utf-8', level=logging.INFO)

DX = 1e-6
ROUND_NUMBER = 3


def f(x: float) -> float:
    """Целевая функция: 3 * x ^ 4 + (x - 1) ^ 2"""
    return 3 * (x ** 4) + (x - 1) ** 2


def newton_raphson(lineEdit: QPlainTextEdit, b: float, sigma: float) -> tuple[float, float]:
    """Метод Ньютона-Рафсона"""
    k = 0
    x_k = b
    lineEdit.appendPlainText("Запущен метод Ньютона-Рафсона. x_k = {}, sigma = {}".format(b, sigma))
    while True:
        df_x_k = derivative(f, x_k, dx=DX)
        ddf_x_k = derivative(f, x_k, dx=DX, n=2)
        lineEdit.appendPlainText("Итерация №{}.\nx_k = {}, df_x_k = {}, ddf_x_k = {}".format(
            k,
            round(x_k, ROUND_NUMBER),
            round(df_x_k, ROUND_NUMBER),
            round(ddf_x_k, ROUND_NUMBER)
        ))
        if abs(df_x_k) <= sigma:
            break
        x_k = x_k - df_x_k / ddf_x_k
        k += 1
    f_x = f(x_k)
    lineEdit.appendPlainText("Результат работы алгоритма: x = {}, f(x) = {}\n".format(
        round(x_k, ROUND_NUMBER),
        round(f_x, ROUND_NUMBER)
    ))
    return x_k, f_x


# x, y = newton_raphson(4.0, 0.01)
