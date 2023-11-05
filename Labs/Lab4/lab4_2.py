import math

from quadrature_methods import complex_left_rectangle_method, complex_right_rectangle_method, \
    complex_middle_rectangle_method, complex_trapeze_method, complex_simpson_method


def p(x):
    return x + 1


def f_custom(x):
    return math.cos(x) - 2 * x


def integral_f_custom(a, b):
    return math.sin(b) - math.sin(a) + a * a - b * b


def f_0(x):
    return 1


def integral_f_0(a, b):
    return b - a


def f_1(x):
    return 2 * x


def integral_f_1(a, b):
    return b * b - a * a


def f_2(x):
    return 3 * (x ** 2)


def integral_f_2(a, b):
    return b ** 3 - a ** 3


def f_3(x):
    return 4 * (x ** 3)


def integral_f_3(a, b):
    return b ** 4 - a ** 4


print("Приближённое вычисление интеграла по составным квадратурным формулам")
a, b = float(input("Введите границу интегрирования a: ")), float(input("Введите границу интегрирования b: "))
m = int(input("Введите число промежутков деления [a, b]: "))
funcs = {f_custom: integral_f_custom, f_0: integral_f_0, f_1: integral_f_1, f_2: integral_f_2, f_3: integral_f_3}
funcs_str = {f_custom: "cos(x) - 2 * x", f_0: "1", f_1: "2 * x", f_2: "3 * (x ** 2)", f_3: "4 * (x ** 3)"}
for f in funcs.keys():
    print("\n", f"Функция f: {funcs_str[f]}")
    j = funcs[f](a, b)
    print("Значение интеграла по отрезку [a, b]:", j, "\n")
    methods = {"СКФ левых прямоугольников": complex_left_rectangle_method,
               "СКФ правых прямоугольников": complex_right_rectangle_method,
               "СКФ средних прямоугольников": complex_middle_rectangle_method,
               "СКФ трапеций": complex_trapeze_method, "СКФ Симпсона": complex_simpson_method}
    for i in methods.keys():
        print("======================================")
        print(i)
        j_h = methods[i](f, a, b, m)
        print("Значение интеграла по данной формуле:", j_h)
        print("Абсолютная фактическая погрешность:", abs(j_h - j))
        print("Относительная фактическая погрешность:", abs(j_h - j) / abs(j))
