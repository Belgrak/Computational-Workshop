import math
import random


def f(x):
    return 2 * math.sin(x) - x / 2


def f_sep_extr(key_values):
    if len(key_values) == 1:
        return key_values[0][1]
    return sum([(v / math.prod(k - j[0] for j in key_values if j[0] != k)) for k, v in key_values])


def creating_table(f, a, b, m1):
    d = {}
    for i in range(m1):
        z = random.uniform(a, b)
        while any(f(z) == j for j in d.values()):
            z = random.uniform(a, b)
        d[z] = f(z)

    print("{:<30} {:<30}".format("Узел", "Значение функции f"))
    for k, v in sorted(d.items(), key=lambda x: x[0]):
        print("{:<30} {:<30}".format(k, v))
    return d


def get_p_n(x, key_values, n):
    if n == 0:
        return key_values[0][1]
    return get_p_n(x, key_values, n - 1) + \
        (f_sep_extr(key_values[:n + 1])) * math.prod([x - i[0] for i in key_values[:n]])


def get_p_l(x, key_values):
    return sum(math.prod([x - j[0] for j in key_values if j[0] != i]) /
               math.prod([i - j[0] for j in key_values if j[0] != i]) * value for i, value in key_values)


def run_task(com=""):
    print("Задача алгебраического интерполирования\nВариант 8")
    print("Условия варианта 8: f(x)=2·sin(x) – x/2  a=0,2  b=0,7  m+1=11  n=8")
    m1 = int(input("Введите число значений в таблице (в наших обозначениях это m+1): "))
    a, b = float(input("Введите левую границу отрезка [a, b]: ")), \
        float(input("Введите правую границу отрезка [a, b]: "))
    print("\n")
    initial_table = creating_table(f, a, b, m1)
    x = float(input("\nВведите точку интерполирования x: "))
    while True:
        if com == "exit":
            return
        if com != "":
            x = float(com)
        n = int(input("Введите степень интерполяционного многочлена n ≤ {}: ".format(m1 - 1)))
        while n >= m1:
            print("Ошибка. Указано неверное значение n")
            n = int(input("Введите степень интерполяционного многочлена n ≤ {}: ".format(m1 - 1)))
        modified_table = sorted(initial_table.items(), key=lambda z: abs(x - z[0]))[:n + 1]
        print("\nОбновленная таблица")
        print("{:<30} {:<30}".format("Узел", "Значение функции f"))
        for k, v in modified_table:
            print("{:<30} {:<30}".format(k, v))

        p_l = get_p_l(x, modified_table)
        print(
            "\nЗначение интерполяционного многочлена, найденного при помощи представления в форме Лагранжа: {}".format(
                p_l))
        efn_l = abs(f(x) - p_l)
        print("Значение абсолютной фактической погрешности для формы Лагранжа: {}".format(efn_l))

        p_n = get_p_n(x, modified_table, n)
        print(
            "\nЗначение интерполяционного многочлена, найденного при помощи представления в форме Ньютона: {}".format(
                p_n))
        efn_p = abs(f(x) - p_n)
        print("Значение абсолютной фактической погрешности для формы Ньютона: {}".format(efn_p))
        com = input("Введите новое значение x или введите exit, чтобы завершить программу\n")


if __name__ == '__main__':
    run_task()
