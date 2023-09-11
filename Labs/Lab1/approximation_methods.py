import random


def bisection_method(a, b, f, eps, *args):
    steps = 0
    first_approximation = (a + b) / 2
    while b - a > 2 * eps:
        steps += 1
        c = (a + b) / 2
        y1, y2 = f(a), f(c)
        if y1 * y2 <= 0:
            b = c
        else:
            a = c
    return steps, (a + b) / 2, b - a, first_approximation


def find_first_approximation(a, b, f, second_derivative):
    x0 = random.uniform(a, b)
    while f(x0) * second_derivative(x0) <= 0:
        x0 = random.uniform(a, b)
    return x0


def newton_method(a, b, f, eps, derivative, second_derivative):
    steps = 0
    x0 = find_first_approximation(a, b, f, second_derivative)
    prev, cur = x0 - 100, x0
    while abs(cur - prev) >= eps:
        if steps > 100:
            return -100, -1, -1
        steps += 1
        prev, cur = cur, cur - (f(cur) / derivative(cur))
    return steps, cur, abs(cur - prev), x0


def modified_newton_method(a, b, f, eps, derivative, second_derivative):
    steps = 0
    x0 = find_first_approximation(a, b, f, second_derivative)
    prev, cur = x0 - 100, x0
    while abs(cur - prev) >= eps:
        if steps > 100:
            return -100, -1, -1
        steps += 1
        prev, cur = cur, cur - (f(cur) / derivative(x0))
    return steps, cur, abs(cur - prev), x0


def secant_method(a, b, f, eps, *args):
    steps = 0
    prev, cur = a, b
    while abs(cur - prev) >= eps:
        if steps > 100:
            return -100, -1, -1
        steps += 1
        prev, cur = cur, cur - (f(cur) / (f(cur) - f(prev))) * (cur - prev)
    return steps, cur, abs(cur - prev), (a, b)
