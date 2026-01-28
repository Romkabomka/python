# Кортежи (Tuple)
# Кортеж - Упорядоченная последовательность элементов
# Кортеж изменять нельзя
# В кортеже могут быть обьекты разных типов
# Порядок в кортежах важен

my_fruits = ('apple', 'banana', 'lime')

other_fruits = ('lime', 'banana', 'apple')

print(my_fruits == other_fruits)  # False

print(len(my_fruits))  # 3

# Получения значений
posts_ids = (52, 152, 99, 0)

print(posts_ids[1])  # 152
print(posts_ids[0])  # 52

#
my_nums = (10, 5, 52, 0)

print(type(my_nums))  # <class 'tuple'>

my_nums[1] = 7  # TypeError: 'tuple' object does not support item assignment

# Кортежы Удалять элементы нельзя!

fruits = ('Apple', 'Banana', 'Mango', 'Kiwi')
print(len(fruits))  # 4

del fruits[1]  # TypeError: 'tuple' object doesn't support item deletion

# Кортеж словарей
users = ({
    'user_id': 52,
    'user_name': 'Alice'
},
    {
    'user_id': 831,
    'user_name': 'Bob'
}
)

print(users[0]['user_id'])  # 52

users[1]['user_id'] = 100

print(users[1]['user_id'])  # 100

# Кортежы использование переменных
my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'

all_fruit = (my_fruit, other_fruit, new_fruit)

print(all_fruit)  # ('apple', 'banana', 'lime')

# Кортежи несуществуюшие элементы
fruits = ['apple', 'kiwi', 'mango', 'pear']

print(fruits[10])  # IndexError: list index out of range


# Кортежи обьединение кортежей
internal_ids = (151, 235)
external_ids = (21, 23, 82)

all_ids = (internal_ids + external_ids)
print(all_ids)  # (151, 235, 21, 23, 82)

# Методы кортежей всего два метода:
# count, index
# Методы кортежей наследуються от класса Tuple

# Метод count
posts_ids = (152, 32, 65, 32)

print(posts_ids.count(32))  # 2

print(posts_ids.count(152))  # 1

# Метод index поиск индекса элемента
posts_ids = (152, 32, 65, 32)

print(posts_ids.index(152))  # 0
# Если элемент встречается несколько раз, то возвращается индекс первого элемента
print(posts_ids.index(32))  # 1

# Кортеж конвертация в список
posts_ids = (152, 22)

posts_ids_list = list(posts_ids)
posts_ids_list.append(34)

print(posts_ids_list)  # [152, 22, 34]

posts_ids_tuple = tuple(posts_ids_list)

print(posts_ids_tuple)  # (152, 22, 34)


# Практика - Кортежи
my_nums = (10, 5, 100, 0, 5, 5)

my_list = list(my_nums)

my_list.append(7)

print(my_list)  # [10, 5, 100, 0, 5, 5, 7]
print(my_nums)  # (10, 5, 100, 0, 5, 5)

#
my_tuple = tuple('abcd')
print(my_tuple)  # ('a', 'b', 'c', 'd')

#
my_tuple = tuple({'first': 1, 'second': True})
print(my_tuple)  # ('first', 'second')
