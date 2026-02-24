# Обработка ошибок
print(10 / 0)
# Traceback - ZeroDivisionError: division by zero
# Выполнение кода остонавливаетьсч после появления ошибки

print('Continue...')

# Try/Except
try:
    # Выполнение блока кода
    pass
except ErrorType:
    # Этот блок выполняется в случае возникновения ошибок в блоке try
    pass

# Except с определенным типом ошибки 
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error - Division by zero!")
    
print('Continue...')