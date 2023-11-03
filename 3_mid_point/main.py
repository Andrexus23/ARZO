import logging
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
from scipy.misc import derivative

logging.basicConfig(format='%(message)s', filename='../mid_point.log', encoding='utf-8', level=logging.INFO)


def f(x: float) -> float:
    return 3 * (x ** 4) + (x - 1) ** 2


def mid_point(a: float, b: float, epsilon: float, sigma: float) -> float:
    """Метод средней точки"""
    iter_count = 0
    logging.info(f"Начало работы алгоритма.\na = {a}, b = {b}, epsilon = {epsilon}, sigma = {sigma}\n")
    while abs(b - a) > 2 * epsilon:
        iter_count += 1
        x_0 = (a + b) / 2
        df_x_0 = derivative(f, x_0, dx=1e-6)
        logging.info(f"Итерация №{iter_count}.\nx_0 = {x_0}, df_x_0 = {df_x_0}")
        if df_x_0 > sigma:
            b = x_0
            logging.info(f"df_x_0 > {sigma}, a = {a}, b = {b}")
        elif df_x_0 < -sigma:
            a = x_0
            logging.info(f"df_x_0 < {-sigma}, a = {a}, b = {b}")
        elif abs(df_x_0) <= sigma:
            break
    result = (a + b) / 2
    logging.info(f"Результат работы алгоритма: x = {result}, f(x) = {f(result)}\n")
    return result


x = mid_point(0.0, 4.0, 0.01, 0.01)
