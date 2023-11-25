import math

import numpy
import scipy.integrate as spi
import numpy as np
from scipy import integrate, optimize
from Labs.Lab1 import lab1, approximation_methods
from scipy.optimize import root

N = 6
EPS = 10 ** -10


def poly(x):
    return sum(x ** j for j in range(N))


def poly_2n(x):
    return x ** (2 * N - 1)


def f(x):
    return math.sin(x)


def p(x):
    return math.exp(x)


def ikf(func, a, b, n):
    h = (b - a) / n
    nodes = [a + i * h for i in range(n)]
    moments = [integrate.quad(lambda x: p(x) * x ** k, a, b)[0] for k in range(n)]
    coefficients = np.linalg.solve(np.rot90(np.vander(nodes)), moments)
    print("Моменты весовой функции:", moments)
    print("Найденные узлы:", nodes)
    print("Коэффициенты построенной ИКФ:", coefficients)
    approx_integral = sum(coeff * func(node) for node, coeff in zip(nodes, coefficients))
    return approx_integral



def kfnast(func, a, b, n):
    nodes = []
    moments = [integrate.quad(lambda x: p(x) * x ** k, a, b)[0] for k in range(2 * n)]
    matr_left = np.array([[moments[j] for j in range(i, i + n)] for i in range(n)])
    a_list = np.linalg.solve(matr_left, [(-1) * moments[i] for i in range(n, 2 * n)])
    w_n = lambda x: x ** n + sum(a_list[i] * x ** i for i in range(n))
    sections = lab1.localize_roots(a, b, w_n, n)
    for i, j in sections:
        steps, approximated_x, diff, first_approximation = approximation_methods.bisection_method(i, j, w_n, EPS)
        nodes.append(approximated_x)

    print("Найденный ортогональный многочлен:", "x ** n + " + " + ".join(f"{a_list[i]} * x ** {i}" for i in range(n)))

    print([i.real for i in numpy.roots([1] + a_list[::-1])])
    coefficients = np.linalg.solve(np.rot90(np.vander(nodes)), moments[:n])
    print("Моменты весовой функции:", moments)
    print("Найденный ортогональный многочлен:", "x ** n + " + " + ".join(f"{a_list[i]} * x ** {i}" for i in range(n)))
    print("Найденные узлы:", nodes)
    print("Коэффициенты построенной КФНАСТ:", coefficients)
    approx_integral = sum(coeff * func(node) for node, coeff in zip(nodes, coefficients))
    return approx_integral


print("Приближённое вычисление интегралов при помощи КФ НАСТ. Вариант 8. [𝑎, 𝑏] = [0, 1], 𝑓(𝑥) = sin(𝑥), 𝜌(𝑥) = 𝑒^x")
a, b = float(input("Введите границу интегрирования a: ")), float(input("Введите границу интегрирования b: "))

d = {f: "sin(x)", poly: "1 + " + " + ".join(f"x^{h}" for h in range(1, N)), poly_2n: f"x ** {2 * N - 1}"}
for i in [poly, f]:
    print("\n===================================")
    print("Функция:", d[i])
    real_val, _ = spi.quad(lambda x: i(x) * p(x), a, b)
    print("Значение интеграла по отрезку [a, b] в библиотеке sympy:", real_val)
    ikf_result = ikf(i, a, b, N)
    print(f"Приближенное значение ИКФ ({N} узлов): {ikf_result:.15f}")
    print("Абсолютная фактическая погрешность:", abs(ikf_result - real_val))
    print("\n")
# for j in [f, poly_2n]:
#     print("Функция:", d[j])
#     real_val, _ = spi.quad(lambda x: j(x) * p(x), a, b)
#     kfnast_result = kfnast(j, a, b, N)
#     print(f"Приближенное значение КФНАСТ ({N} узлов): {kfnast_result:.15f}")
#     print("Абсолютная фактическая погрешность:", abs(kfnast_result - real_val))
#     print("\n===================================")