# Ложные значения - Значение, которые при приведении к 
# логическому типу дает False, являетя ложным

# Ложные значения 
print(bool(0)) # False
print(bool(0.0)) # False
print(bool(0j)) # False
print(bool(None)) # False 
print(bool({})) # False
print(bool([])) # False
print(bool(set ())) # False

print(not not {}) # False



# Ложные значения в условных инструкциях if 
my_list = [1, 2]

if len(my_list) > 0:
    print("List has elements")

# Условия идентичные 
my_list = [1, 2]

if my_list:
    print("List has elements")