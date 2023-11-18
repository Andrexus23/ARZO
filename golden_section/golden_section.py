import logging

from PyQt5.QtWidgets import QPlainTextEdit

# file = '../golden_section.log'
# logging.basicConfig(format='%(message)s', filename=file, encoding='utf-8', level=logging.INFO)

ROUND_NUMBER = 3


# def f(x: float) -> float:
#     """Целевая функция: 3 * x ^ 4 + (x - 1) ^ 2"""
#     return 3 * (x ** 4) + (x - 1) ** 2


def golden_section(lineEdit: QPlainTextEdit, func, a: float, b: float, epsilon: float) -> tuple[float, float, float]:
    """Метод золотого сечения"""
    lineEdit.appendPlainText('Запущен метод золотого сечения. '
                             'Интервал: [{}, {}]; epsilon = {}'.format(a, b, epsilon))
    lambda_ = 0.618
    delta = abs(b - a)
    sigma = lambda_ * delta
    x_1 = b - sigma
    x_2 = a + sigma
    f_x_1 = func(x_1)
    f_x_2 = func(x_2)
    iter_count = 0
    while delta > 2 * epsilon:
        lineEdit.appendPlainText(
            "Итерация №{}.\nx_1 = {}, x_2 = {}, f_x_1 = {}, f_x_2 = {}".format(
                iter_count,
                round(x_1, ROUND_NUMBER),
                round(x_2, ROUND_NUMBER),
                round(f_x_1, ROUND_NUMBER),
                round(f_x_2, ROUND_NUMBER)
            )
        )
        if f_x_1 < f_x_2:
            b = x_2
            delta = abs(b - a)
            lineEdit.appendPlainText("f_x_1 < f_x_2\nInterval = [{}, {}]"
                                     " delta = {}".format(
                round(a, ROUND_NUMBER),
                round(b, ROUND_NUMBER),
                round(delta, ROUND_NUMBER)
            ))
            if delta <= 2 * epsilon:
                break
            x_2 = x_1
            f_x_2 = f_x_1
            x_1 = b - lambda_ * delta
            f_x_1 = func(x_1)
        elif f_x_1 > f_x_2:
            a = x_1
            delta = abs(b - a)
            lineEdit.appendPlainText("f_x_1 > f_x_2\nInterval = [{}, {}], delta = {}".format(
                round(a, ROUND_NUMBER),
                round(b, ROUND_NUMBER),
                round(delta, ROUND_NUMBER)
            ))
            if delta <= 2 * epsilon:
                break
            x_1 = x_2
            f_x_1 = f_x_2
            x_2 = a + lambda_ * delta
            f_x_2 = func(x_2)
        iter_count += 1
    result = (a + b) / 2
    f_x = func(result)
    lineEdit.appendPlainText("Результат работы алгоритма: x = {}, f(x) = {}\n".format(
        round(result, ROUND_NUMBER),
        round(f_x, ROUND_NUMBER)
    ))
    return result, f_x, sigma

# x, y = golden_section(0.0, 4.0, 0.1)
