import logging

file = '../golden_section.log'
logging.basicConfig(format='%(message)s', filename=file, encoding='utf-8', level=logging.INFO)

ROUND_NUMBER = 3


def f(x: float) -> float:
    return 3 * (x ** 4) + (x - 1) ** 2


def golden_section(a: float, b: float, epsilon: float) -> tuple[float, float]:
    """Метод золотого сечения"""
    lambda_ = 0.618
    delta = abs(b - a)
    sigma = lambda_ * delta
    x_1 = b - sigma
    x_2 = a + sigma
    f_x_1 = f(x_1)
    f_x_2 = f(x_2)
    iter_count = 0
    while delta > 2 * epsilon:
        logging.info(f"Итерация №{iter_count}.\nx_1 = {round(x_1, ROUND_NUMBER)}, x_2 = {round(x_2, ROUND_NUMBER)}, "
                     f"f_x_1 = {round(f_x_1, ROUND_NUMBER)}, f_x_2 = {round(f_x_2, ROUND_NUMBER)}")
        if f_x_1 < f_x_2:
            b = x_2
            delta = abs(b - a)
            logging.info(f"f_x_1 < f_x_2\nInterval = [{round(a, ROUND_NUMBER)}, {round(b, ROUND_NUMBER)}] delta = {round(delta, ROUND_NUMBER)}")
            if delta <= 2 * epsilon:
                break
            x_2 = x_1
            f_x_2 = f_x_1
            x_1 = b - lambda_ * delta
            f_x_1 = f(x_1)
        elif f_x_1 > f_x_2:
            a = x_1
            delta = abs(b - a)
            logging.info(f"f_x_1 > f_x_2\nInterval = [{round(a, ROUND_NUMBER)}, {round(b, ROUND_NUMBER)}], delta = {round(delta, ROUND_NUMBER)}")
            if delta <= 2 * epsilon:
                break
            x_1 = x_2
            f_x_1 = f_x_2
            x_2 = a + lambda_ * delta
            f_x_2 = f(x_2)
        iter_count += 1
    result = (a + b) / 2
    f_x = f(result)
    logging.info(f"Результат работы алгоритма: x = {round(result, ROUND_NUMBER)}, f(x) = {round(f_x, ROUND_NUMBER)}")
    return result, f_x


x, y = golden_section(0.0, 4.0, 0.1)
