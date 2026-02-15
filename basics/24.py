#       Операторы в python
# = Оператор присвоения 
# a, 10 - операнды
a = 10


# Арифмитические операторы: + - * /
# Сранения операторы: == != < > 
# Логические операторы: not and or 
# Присвоения = 
# Текстовые операторы: not, and, or, is, is not, in, not in 

a = 10
b = 10

c = a + b

print(a is b) # True
print(c is a) # False 


# У операторов есть соответствующие магические методы классов 

a = [1, 2]
b = [1, 2]

print(a == b) # True

print(a.__eq__(b)) # True

print(a.__eq__)
# <method-wrapper '__eq__' of list object at 0x100e19680>