# Наборы Set
# Набор - Неупорядоченная последовательность элементов
# Набор содержит только уникальные элементы
# Изменять наборы можно
# В наборах обычно сохраняют однотипные данные например набор строк
# В наборе могут быть обьекты разных типов

# Набор структура и синтаксис
my_fruits = {'apple', 'banana', 'mango'}
print(my_fruits)  # {'mango', 'banana', 'apple'}

posts_ids = {152, 42, 32, 22}

user_inputs = {True, 'Roma', 10.2}
print(type(user_inputs))

# Набор уникальные элементы
my_fruits = {'apple', 'apple', 'mango', 'kiwi', 'mango'}

print(my_fruits)  # {'mango', 'apple', 'kiwi'}

print(type(my_fruits))


# Порядок в наборе не важен
my_fruits = {'apple', 'banana', 'lime'}

other_fruits = {'banana', 'apple', 'lime'}

print(my_fruits == other_fruits)  # True

print(len(my_fruits))  # 3

# Наборы у элементов нет индексов!
my_fruits = {'apple', 'banana', 'lime'}
print(my_fruits[0])  # TypeError: 'set' object is not subscriptable


#
posts_ids = [10, 25, 15, 12]
print(posts_ids.__getitem__(0))

# Изменяемые обьекты в наборах
lists_set = {[1, 2], [20, 5]}
# TypeError: cannot use 'list' as a set element (unhashable type: 'list')
# в наборах нельзя добавлять изменяемые обьекты, такие как list, dict, set

# Для наборов нельзя удалять єлементы с помощьб del нельзя
my_set = {10, 5, 15, 15}
print(my_set)

# Создание пустого набора с помощью set()

my_set = set()

print(my_set)  # set()
print(type(my_set))  # <class 'set'>


# Методы наборов
# add, union, remove, difference, intersection, discard,
# clear, copy, update, issubset, issuperset, pop
# Методы наборов наследуются от класса Set

# Наборы add

fruits = {'apple', 'mango'}

fruits.add('kiwi')

print(fruits)  # {'mango', 'apple', 'kiwi'}

# Union обьединение наборов
my_fruits = {'apple', 'mango', 'pear'}
other_fruits = {'pear', 'speramint'}

all_fruits = my_fruits.union(other_fruits)

print(all_fruits)  # {'pear', 'mango', 'speramint', 'apple'}

# Intersection Пересечение наборов
my_fruits = {'apple', 'mango', 'pear'}
other_fruits = {'pear', 'speramint'}

all_fruits = my_fruits.intersection(other_fruits)
print(all_fruits)

# Issubset Один набор включен в другой
nums = {10, 5, 25}
other_nums = {20, 5, 12, 10, 25}

res = nums.issubset(other_nums)

print(res)  # True

# Практика методы наборов
my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

print(my_set.intersection(other_set))  # {'f', 'd'}
print(other_set.intersection(my_set))  # {'f', 'd'}
print(my_set.intersection('abcd'))  # {'d'}

# Симетричная разница
my_set = {'abc', 'd', 'f', 'y'}

copied_set = my_set.copy()

my_set.add('t')
copied_set.add('l')

print(my_set.symmetric_difference(copied_set))  # {'t', 'l'}

# Задача Наборы
my_set = {0, 5, 10, 15, 20}
other_set = {0, 5, 1, 4}


my_set.add(25)
print(my_set)

print(my_set.intersection(other_set))  # {0, 5}

my_set = list(my_set)
print(my_set)  # [0, 20, 5, 25, 10, 15]
