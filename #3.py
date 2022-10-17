"""
Напишите функцию sum_range(start, end),
которая суммирует все целые числа от значения
"start" до величины "end" включительно. Если
пользователь задаст первое число больше второго,
просто поменяйте их местами.
"""


def sum_range(start, end):
    if start > end:
        start, end = end, start
    s = 0
    for i in range(start, end + 1):
        s += i
    return s


a, b = map(int, input("Enter two numbers(start, end):").split(','))
print(sum_range(a, b))
