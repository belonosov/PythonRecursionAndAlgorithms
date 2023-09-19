# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.

# a = 3
# b = 5
# print(f(a, b))

# 1 вариант
# def recApowB(a, b):
#     if b == 0:
#         return 1
#     return a * recApowB(a, b - 1)

# a = int(input('Введите число: '))
# b = int(input('Введите степень: '))
# print(recApowB(a, b))


# 2 вариант
def f(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return 1 / f(a, - b)
    else:
        return a * f(a, b - 1)