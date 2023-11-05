def left_rectangle_method(f, a, b):
    return (b - a) * f(a)


def complex_left_rectangle_method(f, a, b, m):
    h = (b - a) / m
    return h * sum(f(a + i * h) for i in range(0, m))


def right_rectangle_method(f, a, b):
    return (b - a) * f(b)


def complex_right_rectangle_method(f, a, b, m):
    h = (b - a) / m
    return h * sum(f(a + i * h) for i in range(1, m + 1))


def middle_rectangle_method(f, a, b):
    return (b - a) * f((a + b) / 2)


def complex_middle_rectangle_method(f, a, b, m):
    h = (b - a) / m
    return h * sum(f(a + i * h + h / 2) for i in range(0, m))


def trapeze_method(f, a, b):
    return (b - a) / 2 * (f(a) + f(b))


def complex_trapeze_method(f, a, b, m):
    return (complex_left_rectangle_method(f, a, b, m) + complex_right_rectangle_method(f, a, b, m)) / 2


def simpson_method(f, a, b):
    return (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))


def complex_simpson_method(f, a, b, m):
    return (complex_left_rectangle_method(f, a, b, m) + complex_right_rectangle_method(f, a, b, m) +
            4 * complex_middle_rectangle_method(f, a, b, m)) / 6


def three_eighth_method(f, a, b):
    h = (b - a) / 3
    return (b - a) * (f(a) / 8 + 3 * f(a + h) / 8 + 3 * f(a + 2 * h) / 8 + f(b) / 8)
