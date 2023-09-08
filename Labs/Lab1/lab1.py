import math

def localize_roots(a, b, f, n):
    sections = []
    h = (b - a) / n

    beg, end = a, a + h
    while end <= b:
        y1, y2 = f(beg), f(end)
        if y1 * y2 <= 0:
            sections.append((beg, end))
        beg, end = end, end + h
    print("Количество отрезков перемены знака функции: " + str(len(sections)))
    print("Отрезки перемена знака функции:\n" + ",".join(str(i) for i in sections))
    return sections            


F = lambda x: 4 * math.cos(x) + 0.3 * x
A, B = int(input("Введите параметр A, левую границу отрезка: ")), int(input("Введите параметр B, правую границу отрезка: "))
eps = 10 ** ((-1) * int(input("Введите x, степень точности 10 ** (-x): ")))
N = 1 / eps

localize_roots(A, B, F, N)