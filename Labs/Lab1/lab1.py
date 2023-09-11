import math
from approximation_methods import bisection_method, newton_method, modified_newton_method, secant_method


def localize_roots(a, b, f, n):
    roots_sections = []
    h = (b - a) / n

    beg, end = a, a + h
    while end <= b:
        y1, y2 = f(beg), f(end)
        if y1 * y2 <= 0:
            roots_sections.append((beg, end))
        beg, end = end, end + h
    return roots_sections


if __name__ == '__main__':
    print("ЧИСЛЕННЫЕ МЕТОДЫ РЕШЕНИЯ НЕЛИНЕЙНЫХ УРАВНЕНИЙ")
    print("Данные в условии: f(x)= 4∙cos(x) + 0,3∙x [A, B] = [-15; 5] ε = 10-5")

    F = lambda x: 4 * math.cos(x) + 0.3 * x
    Derivative = lambda x: (-4) * math.sin(x) + 0.3
    SecondDerivative = lambda x: (-4) * math.cos(x)
    A, B = int(input("Введите параметр A, левую границу отрезка: ")), int(
        input("Введите параметр B, правую границу отрезка: "))
    epsilon = 10 ** ((-1) * int(input("Введите x, степень точности 10 ** (-x): ")))
    N = 1 / epsilon

    funcs = {"Метод бисекции": bisection_method, "Метод Ньютона": newton_method,
             "Модифицированный метод Ньютона": modified_newton_method, "Метод секущих": secant_method}
    sections = localize_roots(A, B, F, N)

    print("\nКоличество отрезков перемены знака функции: " + str(len(sections)))
    print("Отрезки перемена знака функции:\n" + ",".join(str(i) for i in sections))

    for i, j in sections:
        for title, g in funcs.items():
            steps, approximated_x, diff, first_approximation = g(i, j, F, epsilon, Derivative, SecondDerivative)
            print("\n=============================================================\n")
            print(title)
            print("Начальное приближение: " + str(first_approximation))
            if steps < 0:
                print("За " + str(abs(steps)) + " решение с заданной точностью не было найдено")
                continue
            print("Количество шагов: " + str(steps))
            print("Приближенное решение: " + str(approximated_x))
            print("Расстояние до предыдущего приближения: " + str(diff))
            print("Абсолютная величина невязки: " + str(F(approximated_x)))
