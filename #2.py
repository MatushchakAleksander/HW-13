"""
Напишите функцию to_dict(lst),
которая принимает аргумент в виде списка и возвращает словарь,
в котором каждый элемент списка является ключом и значением.
Предполагается,что элементы списка
будут соответствовать правилам задания ключей в словарях.
"""


def to_dict(lst):
    return {element: element for element in lst}


# Тесты
print(to_dict([1, 2, 3, 4]))
print(to_dict(['Python', (1, 120), 85.17, -34]))