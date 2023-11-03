import logging

file = '../half_divide.log'
logging.basicConfig(format='%(message)s', filemode="w", filename='../half_divide.log', encoding='utf-8',
                    level=logging.INFO)

a = 1
b = 5
interval = [a, b]
sigma = 0.001
epsilon = 0.01
ROUND_NUMBER = 3


def f(x) -> float:
    """Целевая функция."""
    return 3 * x ** 4 + (x - 1) ** 2


def half_divide(a: float, b: float, sigma: float, epsilon: float, round_number=3) -> float:
    """Метод половинного деления."""
    logging.info('Запущен метод половинного сечения. '
                 'Интервал: [{}, {}]; sigma = {}; epsilon = {}'.format(a, b, sigma, epsilon))
    delta = b - a
    iter_count = 1

    while abs(delta) > 2 * epsilon:
        c = float((a + b) / 2)
        x_1 = float(c - (sigma / 2))
        x_2 = float(c + (sigma / 2))
        f_x_1 = f(x_1)
        f_x_2 = f(x_2)
        if f_x_1 < f_x_2:
            b = x_2
        elif f_x_1 > f_x_2:
            a = x_1

        logging.info('Итерация {}; Интервал: [{}, {}]; '
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
    logging.info('Результат метода половинного сечения: {}'.format(round(result, round_number)))
    return result


half_divide(a, b, sigma, epsilon)
