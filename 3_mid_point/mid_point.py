import logging
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
from scipy.misc import derivative

file = '../mid_point.log'
logging.basicConfig(format='%(message)s', filename=file, encoding='utf-8', level=logging.INFO)

DX = 1e-6
ROUND_NUMBER = 3


def f(x: float) -> float:
    return 3 * (x ** 4) + (x - 1) ** 2


def mid_point(a: float, b: float, epsilon: float, sigma: float) -> tuple[float, float]:
    """Метод средней точки"""
    iter_count = 0
    logging.info(f"Начало работы алгоритма.\nInterval = [{round(a, ROUND_NUMBER)}, {round(b, ROUND_NUMBER)}], epsilon = {epsilon}, sigma = {sigma}")
    while abs(b - a) > 2 * epsilon:
        iter_count += 1
        x_0 = (a + b) / 2
        df_x_0 = derivative(f, x_0, dx=DX)
        logging.info(f"Итерация №{iter_count}.\nx_0 = {round(x_0, ROUND_NUMBER)}, df_x_0 = {round(df_x_0, ROUND_NUMBER)}")
        if df_x_0 > sigma:
            b = x_0
            logging.info(f"df_x_0 > {sigma}, Interval = [{round(a, ROUND_NUMBER)}, {round(b, ROUND_NUMBER)}]")
        elif df_x_0 < -sigma:
            a = x_0
            logging.info(f"df_x_0 < {-sigma}, Interval = [{round(a, ROUND_NUMBER)}, {round(b, ROUND_NUMBER)}]")
        elif abs(df_x_0) <= sigma:
            break
    result = (a + b) / 2
    f_x = f(result)
    logging.info(f"Результат работы алгоритма: x = {round(result, ROUND_NUMBER)}, f(x) = {round(f_x, ROUND_NUMBER)}\n")
    return result, f_x


x, y = mid_point(0.0, 4.0, 0.01, 0.01)
