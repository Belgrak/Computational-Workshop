import math

from quadrature_methods import complex_left_rectangle_method, complex_right_rectangle_method, \
    complex_middle_rectangle_method, complex_trapeze_method, complex_simpson_method


def p(x):
    return x + 1


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


def der_2_f_3(x):
    return 24 * x


def der_3_f_3(x):
    return 24


def der_4_f_3(x):
    return 0


def integral_f_3(a, b):
    return b ** 4 - a ** 4


print("Приближённое вычисление интеграла по составным квадратурным формулам")
a, b = float(input("Введите границу интегрирования a: ")), float(input("Введите границу интегрирования b: "))
m = int(input("Введите параметр m: "))
l = int(input("Введите параметр l: "))
funcs = {f_custom: integral_f_custom, f_0: integral_f_0, f_1: integral_f_1, f_2: integral_f_2, f_3: integral_f_3}
ders = {0: der_f_3, 1: der_2_f_3, 3: der_4_f_3}
funcs_str = {f_custom: "cos(x) - 2 * x", f_0: "1", f_1: "2 * x", f_2: "3 * (x ** 2)", f_3: "4 * (x ** 3)"}
for f in funcs.keys():
    print("\n", f"Функция f: {funcs_str[f]}")
    j = funcs[f](a, b)
    methods = {"СКФ левых прямоугольников": complex_left_rectangle_method,
               "СКФ правых прямоугольников": complex_right_rectangle_method,
               "СКФ средних прямоугольников": complex_middle_rectangle_method,
               "СКФ трапеций": complex_trapeze_method, "СКФ Симпсона": complex_simpson_method}
    consts = {complex_left_rectangle_method: 1 / 2,
               complex_right_rectangle_method: 1 / 2,
               complex_middle_rectangle_method: 1 / 24,
               complex_trapeze_method: 1 / 12, complex_simpson_method: 1 / 2880}
    ast = {complex_left_rectangle_method: 0,
              complex_right_rectangle_method: 0,
              complex_middle_rectangle_method: 1,
              complex_trapeze_method: 1, complex_simpson_method: 3}
    for i in methods.keys():
        h = (b - a) / m
        print("======================================")
        print(i)
        j_h = methods[i](f, a, b, m)
        j_h_l = methods[i](f, a, b, m * l)
        print("Значение интеграла по данной формуле для m*l делений:", j_h_l)
        print("Абсолютная фактическая погрешность для m*l делений:", abs(j_h_l - j))
        ast_cur = ast[methods[i]]
        _j = ((l ** (ast_cur + 1)) * j_h_l - j_h) / (l ** (ast_cur + 1) - 1)
        print("Уточненное значение по принципу Рунге:", _j)
        print("Абсолютная фактическая погрешность для уточненного значения:", abs(_j - j))
