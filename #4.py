"""
Напишите функцию read_last(lines, file),
которая будет открывать определенный файл и выводить на печать
построчно последние сроки в количестве
lines (на всякий случай проверим, что задано положительное целое число).
"""


def read_last(lines, file):
    if lines > 0:
        with open(file, encoding='utf-8') as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
        else:
            print('Должно быть задано только целое положительное число')


