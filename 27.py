# Приоритетность операторов 
a + b * c / d - e
a + ((b * c) / (d - e))
(((a + b) * c) / d) - e

# Задача 
# 1.Создайте две переменных и присвойте им одинаковые последовательности типа set,
# При этом не копируйте одну переменную в другую 
set_one = { 'apple', 'mango', 'banana'}
set_two = {'apple', 'mango', 'banana'}
print(set_one == set_two) # True

print(set_one.__eq__(set_two)) # True
print(set_one is set_two) # False
print('speramint' in set_one) # False