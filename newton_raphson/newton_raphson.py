import warnings
from typing import Tuple, Optional

from PyQt5.QtWidgets import QPlainTextEdit

from constants.constants import MAX_ITER_COUNT

warnings.filterwarnings("ignore", category=DeprecationWarning)
from scipy.misc import derivative

# file = '../newton_raphson.log'
# logging.basicConfig(format='%(message)s', filename=file, encoding='utf-8', level=logging.INFO)

DX = 1e-6
ROUND_NUMBER = 3



def newton_raphson(lineEdit: QPlainTextEdit, func, b: float, sigma: float) -> Tuple[Optional[float], Optional[float]]:
    """Метод Ньютона-Рафсона"""
    k = 0
    x_k = b
    lineEdit.appendPlainText("Запущен метод Ньютона-Рафсона. x_k = {}, sigma = {}".format(b, sigma))
    while k < MAX_ITER_COUNT:
        df_x_k = derivative(func, x_k, dx=DX)
        ddf_x_k = derivative(func, x_k, dx=DX, n=2)
        lineEdit.appendPlainText("Итерация №{}.\nx_k = {}, df_x_k = {}, ddf_x_k = {}".format(
            k,
            round(x_k, ROUND_NUMBER),
            round(df_x_k, ROUND_NUMBER),
            round(ddf_x_k, ROUND_NUMBER)
        ))
        if abs(df_x_k) <= sigma:
            break
        elif k >= MAX_ITER_COUNT:
            lineEdit.appendPlainText("Итерация №{} Некорректные данные. Алгоритм не может быть завершен.\nx_k = {}, df_x_k = {}, ddf_x_k = {}".format(
            k,
            round(x_k, ROUND_NUMBER),
            round(df_x_k, ROUND_NUMBER),
            round(ddf_x_k, ROUND_NUMBER)
            ))
            return None, None
        x_k = x_k - df_x_k / ddf_x_k
        k += 1
    f_x = func(x_k)
    lineEdit.appendPlainText("Результат работы алгоритма: x = {}, f(x) = {}\n".format(
        round(x_k, ROUND_NUMBER),
        round(f_x, ROUND_NUMBER)
    ))
    return x_k, f_x
