import math
from Labs.Lab2 import lab2
from Labs.Lab1 import approximation_methods


VARIANT = 8


def f(x):
    return math.exp(1.5 * ((VARIANT % 5) + 1) * x)


def creating_table(f, a, h, m1):
    d = {}
    for i in range(m1):
        x_i = a + h * i
        d[x_i] = f(x_i)

    print("{:<30} {:<30}".format("Узел", "Значение функции f"))
    for k, v in sorted(d.items(), key=lambda x: x[0]):
        print("{:<30} {:<30}".format(k, v))
    return d


def first_method(f, n, F, initial_table):
    modified_table = sorted([(i[1], i[0]) for i in initial_table.items()], key=lambda z: abs(F - z[0]))[:n + 1]
    print("\nОтраженная таблица")
    print("{:<30} {:<30}".format("Значение функции f", "Аргумент"))
    for k, v in modified_table:
        print("{:<30} {:<30}".format(k, v))
    x = lab2.get_p_l(F, modified_table)
    print("\nЗначение аргумента, найденного при помощи представления в форме Лагранжа: {}".format(x))
    r_n = abs(f(x) - F)
    print("Абсолютная величина невязки: " + str(r_n))


def second_method(f, a, b, n, F, eps, initial_table):
    modified_table = sorted(initial_table.items(), key=lambda z: abs(F - z[1]))[:n + 1]
    print("\nОбновленная таблица")
    print("{:<30} {:<30}".format("Узел", "Значение функции f"))
    for k, v in modified_table:
        print("{:<30} {:<30}".format(k, v))
    p_n = lambda x: lab2.get_p_l(x, modified_table) - F
    steps, approximated_x, diff, first_approximation = approximation_methods.secant_method(a, b, p_n, eps)
    print("Начальное приближение: " + str(first_approximation))
    if steps < 0:
        print("За " + str(abs(steps)) + " решение с заданной точностью не было найдено")
        return
    print("Количество шагов: " + str(steps))
    print("Приближенное решение: " + str(approximated_x))
    print("Расстояние до предыдущего приближения: " + str(abs(diff)))
    r_n = abs(f(approximated_x) - F)
    print("Абсолютная величина невязки: " + str(r_n))


def run_task(com=""):
    print("Нахождение производных таблично-заданной функции по формулам численного дифференцирования\nВариант 8")
    m1 = int(input("Введите число значений в таблице (в наших обозначениях это m+1): "))
    a, h = float(input("Введите левую границу a: ")), \
        float(input("Введите размер шага h: "))
    print("\n")
    initial_table = creating_table(f, a, h, m1)
    while True:
        if com == "exit":
            return
        n = int(input("Введите степень интерполяционного многочлена n ≤ {}: ".format(m1 - 1)))
        while n >= m1:
            print("Ошибка. Указано неверное значение n")
            n = int(input("Введите степень интерполяционного многочлена n ≤ {}: ".format(m1 - 1)))
        F = float(input("Введите значение функции для обратного интерполирования: "))
        epsilon = 10 ** ((-1) * int(input("Введите x, степень точности 10 ** (-x): ")))
        print("\n Метод первый:")
        first_method(f, n, F, initial_table)
        print("\n Метод второй:")
        second_method(f, a, b, n, F, epsilon, initial_table)
        com = input("Введите новое значение x или введите exit, чтобы завершить программу: ")


if __name__ == '__main__':
    run_task()