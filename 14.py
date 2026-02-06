# Функции
# Функция - Блок кода, который можно выполнять многократно

a = 5
b = 3

c = a + b
print(c)  # 8

a = 18
b = 12

c = a + b
print(c)

# Это одинаковые блоки кода!, создадим функцию


def sum(a, b):
    c = a + b
    print(c)


a = 5
b = 3

sum(a, b)  # 8

a = 8
b = 12

sum(a, b)  # 20

# Функция - Это обьект
# Каждая функция - это экземпляр класса function


def sum(a, b):
    c = a + b
    print(c)


print(type(sum))  # <class 'function'>
# Функция возвращает None если нет ключевого слова Return
# Функцию нужно вызвать для выполнения кода внутри функции

# Вызов функции


def my_fn(a, b):
    a = a + 1
    c = a + b
    return c


res = my_fn(10, 3)
print(res)  # 14
