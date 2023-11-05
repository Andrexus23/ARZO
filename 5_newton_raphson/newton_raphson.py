import logging
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
from scipy.misc import derivative

file = '../newton_raphson.log'
logging.basicConfig(format='%(message)s', filename=file, encoding='utf-8', level=logging.INFO)

DX = 1e-6
ROUND_NUMBER = 3


def f(x: float) -> float:
    return 3 * (x ** 4) + (x - 1) ** 2


def newton_raphson(b: float, sigma: float) -> tuple[float, float]:
    k = 0
    x_k = b
    logging.info(f"Начало работы алгоритма.\nx_k = {b}, sigma = {sigma}")
    while True:
        df_x_k = derivative(f, x_k, dx=DX)
        ddf_x_k = derivative(f, x_k, dx=DX, n=2)
        logging.info(f"Итерация №{k}.\nx_k = {round(x_k, ROUND_NUMBER)}, df_x_k = {round(df_x_k, ROUND_NUMBER)}, "
                     f"ddf_x_k = {round(ddf_x_k, ROUND_NUMBER)}")
        if abs(df_x_k) <= sigma:
            break
        x_k = x_k - df_x_k / ddf_x_k
        k += 1
    f_x = f(x_k)
    logging.info(f"Результат работы алгоритма: x = {round(x_k, ROUND_NUMBER)}, f(x) = {round(f_x, ROUND_NUMBER)}")
    return x_k, f_x


x, y = newton_raphson(4.0, 0.01)
