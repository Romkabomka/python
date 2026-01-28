# Словарь - Набор Єлементов Ключ:Значение

my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2
}

print(my_motorbike)  # {'brand': 'Ducati', 'price': 25000, 'engine_vol': 1.2}
# Порядок элементов в словаре не имеет значения

other_motorbike = {
    'price': 25000,
    'engine_vol': 1.2,
    'brand': 'Ducati'
}
print(my_motorbike == other_motorbike)  # True

print(id(my_motorbike) == id(other_motorbike))  # False


# Словари Получение значений
print(my_motorbike['brand'])  # Ducati

print(my_motorbike['price'])  # 25000


# Словари Изменение значений
fruits = {
    '1': 'Apple',
    '2': 'Banana',
    '3': 'Kiwi',
    '4': 'Mango',
}
print(fruits)  # {'1': 'Apple', '2': 'Banana', '3': 'Kiwi', '4': 'Mango'}
fruits['2'] = 'Speramint'
print(fruits)  # {'1': 'Apple', '2': 'Speramint', '3': 'Kiwi', '4': 'Mango'}

# Словари Добавление новых элементоа
fruits['5'] = 'Passion Fruit'
# {'1': 'Apple', '2': 'Speramint', '3': 'Kiwi', '4': 'Mango', '5': 'Passion Fruit'}
print(fruits)


# Словари удаление элементов
del fruits['5']
print(fruits)  # {'1': 'Apple', '2': 'Speramint', '3': 'Kiwi', '4': 'Mango'}


# Словари Доступ к значению элемента с помощью переменной
key_name = '1'
fruits[key_name] = 'Pear'
print(fruits)  # {'1': 'Pear', '2': 'Speramint', '3': 'Kiwi', '4': 'Mango'}


# Словари вложенные словари
my_motorbike = {
    'brand': 'Ducati',
    'engine_vol': 1.2,
    'price_info': {
        'price': 25000,
        'is_available': True
    }
}

print(my_motorbike['price_info']['price'])  # 25000
print(my_motorbike['price_info']['is_available'])  # True


# Словари использование переменных
brand = 'Ducati'
bike_price = 25000
engine_volume = 1.2

my_motorbike = {
    'brand': brand,
    'price': bike_price,
    'engine_volume': engine_volume,
}

# {'brand': 'Ducati', 'price': 25000, 'engine_volume': 1.2}
print(my_motorbike)

# Длина словаря
print(len(my_motorbike))  # 3

del my_motorbike['price']

print(len(my_motorbike))  # 2


# Словари несуществующие ключи
# print(my_motorbike['model'])  # KeyError: 'model'

# Метод "get" для получения значений ключей
print(my_motorbike.get('model'))  # None

# Значение по умолчанию для метода "get"
print(my_motorbike.get('qty', 0))  # 0

# Метод "get" для получения значений ключей
print(my_motorbike.get('brand'))  # Ducati
print(my_motorbike.get('price'))  # 25000

# Метод __doc__
my_dict = {}
print(my_dict.__doc__)


# Практика Словари
my_disk = {}

# print(id(my_disk))  # 4296435968
# print(type(my_disk))  # <class 'dict'>

my_disk['brand'] = 'Samsung'
my_disk['price'] = 80
# print(my_disk)  # {'brand': 'Samsung', 'price': 80}

# print(my_disk)
# print(id(my_disk))  # 4296435968

print(my_disk.copy())
# print(type(my_disk.items()))  # <class 'dict_items'>
print(my_disk)

new_disk = my_disk.copy()
new_disk['type'] = 'ssd'

print(my_disk)
print(new_disk)


print(len(new_disk))


# Практика - Конвертация других значений в словарь
my_list = [['first', 0], ['second', True]]

my_dict = dict(my_list)

print(my_dict)
