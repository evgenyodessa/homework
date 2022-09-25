# Задание 3:
# Программа с помощью библиотеки random генерирует случайное число от 1 до 10, задача пользователя угадать
# это число за 3 попытки. В случае если пользователь указал больше загаданного числа, то нужно
# вывести "Бери меньше" и наоборот.
#
# На экране должно быть:
# Попытка #1: <ввод тут>
# Бери меньше
# Попытка #2: <ввод тут>
# Бери больше
# Попытка #3: <ввод тут>
# Ты угадал!

import random

a = random.randint(1, 10)
for c in range(3):
    user_digit = int(input("Попытка " + str(c + 1) + ": "))
    if user_digit > a:
        print("Бери меньше")
    elif user_digit < a:
        print("Бери больше")
    else:
        print("Ты угадал!")
        exit()
