import math

from quadrature_methods import left_rectangle_method, right_rectangle_method, middle_rectangle_method, \
    trapeze_method, simpson_method, three_eighth_method


def f_custom(x):
    return math.cos(x) - 2 * x


def der_f_custom(x):
    return (-1) * math.sin(x) - 2


def integral_f_custom(a, b):
    return math.sin(b) - math.sin(a) + a * a - b * b


def f_0(x):
    return 1


def der_f_0(x):
    return 0


def integral_f_0(a, b):
    return b - a


def f_1(x):
    return 2 * x


def der_f_1(x):
    return 2


def integral_f_1(a, b):
    return b * b - a * a


def f_2(x):
    return 3 * (x ** 2)


def der_f_2(x):
    return 6 * x


def integral_f_2(a, b):
    return b ** 3 - a ** 3


def f_3(x):
    return 4 * (x ** 3)


def der_f_3(x):
    return 12 * (x ** 2)


def integral_f_3(a, b):
    return b ** 4 - a ** 4


print("Приближённое вычисление интеграла по квадратурным формулам")
a, b = float(input("Введите границу интегрирования a: ")), float(input("Введите границу интегрирования b: "))
funcs = {f_custom: integral_f_custom, f_0: integral_f_0, f_1: integral_f_1, f_2: integral_f_2, f_3: integral_f_3}
funcs_str = {f_custom: "cos(x) - 2 * x", f_0: "1", f_1: "2 * x", f_2: "3 * (x ** 2)", f_3: "4 * (x ** 3)"}
for f in funcs.keys():
    print("\n", f"Функция f: {funcs_str[f]}")
    j = funcs[f](a, b)
    print("Значение интеграла по отрезку [a, b]:", j, "\n")
    methods = {"КФ левого прямоугольника": left_rectangle_method,
               "КФ правого прямоугольника": right_rectangle_method,
               "КФ среднего прямоугольника": middle_rectangle_method,
               "КФ трапеции": trapeze_method, "КФ Симпсона (параболы)": simpson_method,
               "Формула 3/8": three_eighth_method}
    for i in methods.keys():
        print("======================================")
        print(i)
        value = methods[i](f, a, b)
        print("Значение интеграла по данной формуле:", value)
        print("Абсолютная фактическая погрешность:", abs(value - j))
        print("Относительная фактическая погрешность:", abs(value - j) / abs(j))
