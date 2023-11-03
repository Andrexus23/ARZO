import logging

logging.basicConfig(format='%(message)s', filename='../golden_section.log', encoding='utf-8', level=logging.INFO)


def f(x: float) -> float:
    return 3 * (x ** 4) + (x - 1) ** 2


def golden_section(a: float, b: float, epsilon: float) -> float:
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
        logging.info(f"Итерация №{iter_count}.\nx_1 = {x_1}, x_2 = {x_2}, f_x_1 = {f_x_1}, f_x_2 = {f_x_2}\n")
        if f_x_1 < f_x_2:
            b = x_2
            delta = abs(b - a)
            logging.info(f"f_x_1 < f_x_2\na = {a}, b = {b}, delta = {delta}\n")
            if delta <= 2 * epsilon:
                break
            x_2 = x_1
            f_x_2 = f_x_1
            x_1 = b - lambda_ * delta
            f_x_1 = f(x_1)
        if f_x_1 > f_x_2:
            a = x_1
            delta = abs(b - a)
            logging.info(f"f_x_1 > f_x_2\na = {a}, b = {b}, delta = {delta}\n")
            if delta <= 2 * epsilon:
                break
            x_1 = x_2
            f_x_1 = f_x_2
            x_2 = a + lambda_ * delta
            f_x_2 = f(x_2)
        iter_count += 1
    result = (a + b) / 2
    logging.info(f"Результат работы алгоритма: x = {result}, f(x) = {f(result)}\n")
    return result


x = golden_section(0.0, 4.0, 0.1)
