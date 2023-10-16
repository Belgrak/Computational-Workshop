import math

VARIANT = 1


def f(x):
    return math.exp(1.5 * ((VARIANT % 5) + 1) * x)


def f_der(x):
    return (1.5 * ((VARIANT % 5) + 1)) * math.exp(1.5 * ((VARIANT % 5) + 1) * x)


def f_sec_der(x):
    return ((1.5 * ((VARIANT % 5) + 1)) ** 2) * math.exp(1.5 * ((VARIANT % 5) + 1) * x)


def creating_table(f, a, h, m1):
    d = {}
    for i in range(m1):
        x_i = a + h * i
        d[x_i] = [f(x_i)]
    #
    # print("{:<30} {:<30}".format("Узел", "Значение функции f"))
    # for k, v in sorted(d.items(), key=lambda x: x[0]):
    #     print("{:<30} {:<30}".format(k, v[0]))
    return d


def get_derivative(table, ind, h, secDer=False):
    if secDer:
        if ind == 0 or ind == len(table) - 1:
            return -1
        return (table[ind - 1][1][0] + table[ind + 1][1][0] - 2 * table[ind][1][0]) / (h * h)
    t = len(table[ind][1]) - 1
    if ind == 0:
        return ((-3) * table[ind][1][t] + 4 * table[ind + 1][1][t] - table[ind + 2][1][t]) / (2 * h)
    if ind == len(table) - 1:
        return (3 * table[ind][1][t] - 4 * table[ind - 1][1][t] + table[ind - 2][1][t]) / (2 * h)
    return (table[ind + 1][1][t] - table[ind - 1][1][t]) / (2 * h)


def run_task(com=""):
    print("Нахождение производных таблично-заданной функции по формулам численного дифференцирования\nВариант 8")
    while True:
        if com == "exit":
            return
        m1 = int(input("Введите число значений в таблице (в наших обозначениях это m+1): "))
        a, h = float(input("Введите левую границу a: ")), \
            float(input("Введите размер шага h: "))
        print("\n")
        initial_table = creating_table(f, a, h, m1)
        for i in range(2):
            for k, v in initial_table.items():
                initial_table[k].append(get_derivative(list(initial_table.items()), round((k - a) / h), h, i == 1))
        print("{:<25} {:<25} {:<25} {:<25} {:<30} {:<25} {:<25} {:<25}".format("xi", "f(xi)", "f'*(xi)",
                                                                               "|f'(xi) - f'*(xi)|", "|f'(xi) - f'*(xi)| / f'*(xi)", "f''*(xi)", "|f''(xi) - f''*(xi)|", "|f''(xi) - f''*(xi)| / f''*(xi)"))
        for k, v in initial_table.items():

            print("{:<25} {:<25} {:<25} {:<25} {:<30} {:<25} {:<25}".format(k, v[0], v[1], abs(f_der(k) - v[1]), abs(f_der(k) - v[1]) / v[1],
                                                                     v[2], abs(f_sec_der(k) - v[2])))
        input()
        com = input("Нажмите Enter или введите exit, чтобы завершить программу: ")
        print("\n")


if __name__ == '__main__':
    run_task()
