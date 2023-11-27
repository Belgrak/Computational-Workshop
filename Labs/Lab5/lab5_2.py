import math

from Labs.Lab1 import lab1, approximation_methods
import scipy.integrate as spi


EPS = 10 ** - 12


def f_5(x):
    return x ** 5 + x ** 3 + 1


def f_7(x):
    return x ** 7 + x ** 5 + 1


def f_9(x):
    return x ** 9 + x ** 7 + 1


def f(x):
    return math.cos(x ** 2)


def p_n(x, n):
    match n:
        case 0:
            return 1
        case 1:
            return x
        case _:
            return (2 * n - 1) / n * p_n(x, n - 1) * x - (n - 1) / n * p_n(x, n - 2)


print("Вычисление интегралов при помощи КФ Гаусса. Вариант 8. [𝑎, 𝑏] = [0, pi/4], 𝑓(𝑥) = cos(𝑥^2), 𝑁 = 6,7,8")

def bisection_method(f, a, b):
    roots = []
    intervals = []
    h = (b - a) / 100
    x1 = a
    x2 = x1 + h
    y1 = f(x1)
    while x2 <= b:
        y2 = f(x2)
        if y1 * y2 <= 0:
            intervals.append((x1, x2))
        x1 = x2
        x2 += h
        y1 = y2

    for a, b in intervals:
        while b - a > 2 * 10 ** (-13):
            c = (a + b) / 2
            if f(a) * f(c) <= 0:
                b = c
            else:
                a = c
        roots.append((a + b) / 2)
    l = len(roots)
    if l % 2 != 0:
        roots[int(l / 2)] = 0
    return roots


gauss_n = {}
check_polys = {3: f_5, 4: f_7, 5: f_9}
for n in range(1, 9):
    print("\nN =", n)
    sections = lab1.localize_roots(-1, 1, lambda x: p_n(x, n), n)
    print("{:<20} {:<20}".format("Узел", "Коэффициент"))
    nodes_t = bisection_method(lambda x: p_n(x, n), -1, 1)
    c_k_list = []
    for t in nodes_t:
        c_k = 2 * (1 - t ** 2) / (n ** 2 * p_n(t, n - 1) ** 2)
        c_k_list.append(c_k)
        print("{:<20} {:<20}".format(t, c_k))
    kf_gauss_init = lambda func: sum(c_k_list[i - 1] * func(nodes_t[i - 1]) for i in range(n))
    if n in range(3, 6):
        print(f"\nПроверка для x ** {2 * n - 1} + x ** {2 * n - 3} + 1")
        real_val, _ = spi.quad(check_polys[n], -1, 1)
        res = kf_gauss_init(check_polys[n])
        print("Значение интеграла по отрезку [-1, 1] в библиотеке scipy:", real_val)
        print(f"Приближенное значение КФ Гаусса ({n} узлов): {res:.15f}")
        print("Абсолютная фактическая погрешность:", abs(res - real_val))
    gauss_n[n] = (nodes_t, c_k_list)

print("\n")
print("Вычисление интегралов при помощи КФ Гаусса. Вариант 8. [𝑎, 𝑏] = [0, pi/4], 𝑓(𝑥) = cos(𝑥^2), 𝑁 = 6,7,8")
a, b = 0, math.pi / 4
while True:
    n_s = map(int, input("Введите N1, N2, N3 через пробел: ").split())
    for n in n_s:
        if n not in gauss_n.keys():
            sections = lab1.localize_roots(-1, 1, lambda x: p_n(x, n), n)
            nodes_t = bisection_method(lambda x: p_n(x, n), -1, 1)
            c_k_list = [2 * (1 - t ** 2) / (n ** 2 * p_n(t, n - 1) ** 2) for t in nodes_t]
            gauss_n[n] = (nodes_t, c_k_list)
        t_list, c_k_list = gauss_n[n]
        a_k_list, x_list = [], []
        print("{:<20} {:<20}".format("Узел", "Коэффициент для [a, b]"))
        for i in range(n):
            a_k = (b - a) / 2 * c_k_list[i]
            x_k = (b - a) / 2 * t_list[i] + (b + a) / 2
            a_k_list.append(a_k)
            x_list.append(x_k)
            print("{:<20} {:<20}".format(x_k, a_k))
        kf_gauss = lambda f: sum(a_k_list[j] * f(x_list[j]) for j in range(n))

        real_val, _ = spi.quad(f, a, b)
        res = kf_gauss(f)
        print("Значение интеграла по отрезку [a, b] в библиотеке scipy:", real_val)
        print(f"Приближенное значение КФ Гаусса ({n} узлов): {res:.15f}")
        print("Абсолютная фактическая погрешность:", abs(res - real_val))
        print("\n")

    a, b = float(input("Введите границу интегрирования a: ")), float(input("Введите границу интегрирования b: "))

