import logging
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
from scipy.misc import derivative

logging.basicConfig(format='%(message)s', filename='../newton_raphson.log', encoding='utf-8', level=logging.INFO)


def f(x: float) -> float:
    return 3 * (x ** 4) + (x - 1) ** 2


def newton_raphson(a: float, b: float, sigma: float) -> float:
    k = 0
    x_k = b
    logging.info(f"Начало работы алгоритма.\nx_k = {b}")
    while True:
        df_x_k = derivative(f, x_k, dx=1e-6)
        ddf_x_k = derivative(f, x_k, dx=1e-6, n=2)
        logging.info(f"Итерация №{k}.\nx_k = {x_k}, df_x_k = {df_x_k}, ddf_x_k = {ddf_x_k}")
        if abs(df_x_k) <= sigma:
            break
        x_k = x_k - df_x_k / ddf_x_k
        k += 1
    logging.info(f"Результат работы алгоритма: x = {x_k}, f(x) = {f(x_k)}")
    return x_k


x = newton_raphson(0.0, 4.0, 0.01)
