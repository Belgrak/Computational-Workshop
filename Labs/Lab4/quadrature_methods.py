import random


def rectangle_method(f, a, b):
    return (b - a) * f(random.uniform(a, b))


def left_rectangle_method(f, a, b):
    return (b - a) * f(a)


def right_rectangle_method(f, a, b):
    return (b - a) * f(b)


def middle_rectangle_method(f, a, b):
    return (b - a) * f((a + b) / 2)


def trapeze_method(f, a, b):
    return (b - a) / 2 * (f(a) + f(b))


def trapeze_method(f, a, b):
    return (b - a) / 2 * (f(a) + f(b))


def simpson_method(f, a, b):
    return (b - a) / 6 * (f(a) + 4 * f((a + b) / 2) + f(b))


def three_eighth_method(f, a, b):
    h = (b - a) / 3
    return (b - a) * (f(a) / 8 + 3 * f(a + h) / 8 + 3 * f(a + 2 * h) / 8 + f(b) / 8)
