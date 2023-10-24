

name = input("Привет! Как тебя зовут? ")

# Шаг 2: Вывод данных на экран
print(f"Привет, {name}!")

# **Часть 2: Проверка ввода**

# Шаг 1: Ввод и проверка числа
while True:
    try:
        age = int(input("Сколько тебе лет? "))
        break
    except ValueError:
        print("Пожалуйста, введите число.")

# Шаг 2: Вывод возраста
print(f"Тебе {age} лет.")

names = []
count = int(input("Сколько имен ты хочешь ввести? "))
for i in range(count):
    name = input(f"Введите имя {i + 1}: ")
    names.append(name)

# Шаг 2: Вывод введенных имён
print("Введенные имена:")
for name in names:
    print(name)


def greet_user():
    name = input("Как тебя зовут? ")
    print(f"Привет, {name}!")

# Шаг 2: Вызов функции
greet_user()

