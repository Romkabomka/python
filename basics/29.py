# Лямбда функция
# lambda parameters: expression
# lambda - ключевое слово
# parameters - может иметь несколько параметров
# expression - допускается только одно выражение
# Лямбда функции всегда анонимные

# Функция
# def mult(a, b):
#     return a * b

def mult(a, b): return a * b


print(mult(10, 5))
# Лямбда функция
# lambda a, b: a * b


# Пример Лямбда функция
def greeting(greet):
    return lambda name: f"{greet}, {name}!"

morning_greeting = greeting("Good Morning")

print(morning_greeting("Roman"))
# Good Morning, Roman!

evening_greeting = greeting("Good Evening")

print(evening_greeting('Roman'))