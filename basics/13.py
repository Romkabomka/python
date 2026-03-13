# Изменение обьектов в Python
# Переменная содержит ссылку на обьект
# Переменные могут ссылаться на один и тотже обьект в памьяти

# Адреса неизменяемых обьектов


from copy import deepcopy
my_number = 10
print(id(my_number))  # 4382975032

other_number = 10
print(id(other_number))  # 4382975032

print(id(10))  # 4382975032

# Копирование неизменяемых обьектов
first_num = 10
second_num = first_num

print(id(first_num))  # 4388938808
print(id(second_num))  # 4388938808

second_num += 5
print(second_num)  # 15
print(first_num)  # 10

print(id(second_num))  # 4392871128
print(id(first_num))  # 4392870968

# Адреса изменяемых обьектов
# Пример 1:
my_list = [1, 2, 3]  # Список list
print(id(my_list))  # 4310800000

other_list = [1, 2, 3]
print(id(other_list))  # 4310993152

print(id([1, 2, 3]))  # 4311224512

my_list = [1, 2, 3]
other_list = [1, 2, 3]
other_list.append(4)

print(my_list)  # [1, 2, 3]

print(other_list)  # [1, 2, 3, 4]

# Пример 2:
info = {
    'name': 'Roman',
    'is_instructor': True
}

info_copy = info
info['reviews_qty'] = 5

print(info)  # {'name': 'Roman', 'is_instructor': True, 'reviews_qty': 5}

# Пример 3:
my_info = {
    'name': 'Roman',
    'is_instructor': True
}

print(id(my_info))  # 4376176960

other_info = {
    'name': 'Roman',
    'is_instructor': True
}

other_info['rating'] = 5.0
print(other_info)
print(id(other_info))  # 4376587520
# После копирования изменяемых обьектов изменения отражаются на всех копиях


# Как избежать изменения копий

# Вариант 1 метод copy():
info = {
    'name': 'Roman',
    'is_instructor': True
}

info_copy = info.copy()

info_copy['reviews_qty'] = 5

print(info_copy)  # {'name': 'Roman', 'is_instructor': True, 'reviews_qty': 5}

print(info)  # {'name': 'Roman', 'is_instructor': True}

# Вариант 2:
info = {
    'name': 'Roman',
    'is_instructor': True,
    'reviews': []
}

info_copy = info.copy()

info_copy['reviews'].append('Great course!')

print(info)
# {'name': 'Roman', 'is_instructor': True, 'reviews': ['Great course!']}

print(info_copy)
# {'name': 'Roman', 'is_instructor': True, 'reviews': ['Great course!']}


# Создание глубокой копии обьекта deep copy
info = {
    'name': 'Roman',
    'is_instructor': True,
    'reviews': []
}

info_deepcopy = deepcopy(info)

info_deepcopy['reviews'].append('Great course!')

print(hello)
#	new file:   9.py
print(info)

print(info_deepcopy)
