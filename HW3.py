import os
Task = 0
menu_list = ['1. Сумма нечетных позиций списка.','2. Произведение пар чисел списка.','3. Разница между min и max дробной частью.','4. Десятичное число в двоичное.','5. Фибоначчи.','6. Выход']
os.system('cls')

def error():# процедура вызывается при ошибке
    os.system('cls')
    print("\033[37m\033[41m{}".format('\n                                        '
                              '\n               ОШИБКА!!!                '
                              '\n    Ошибка ввода данных или не верный   '
                              '\n        формат введенных данных.        '
                              '\n                                        '))
    enter_key_to_continue()
def enter_key_to_continue():# ожидание нажатия ENTER
    input("\033[0m{}".format('=================================================\nДля продолжения нажмите клавишу [ENTER]'))
    main()
# def exit():# Выход из программы
#     print("\033[0m{}".format('Выход из программы...'))
#     import sys
#     sys.exit()

# Функции для заданий
def list_min(list):
    min = 0
    for i in range(len(list)):
        if list[i] < list[min]:
            min = i
    return min
def list_max(list):
    max = 0
    for i in range(len(list)):
        if list[i] > list[max]:
            max = i
    return max
def dec_bin(n, p = 1):
    return (n % 2) * p + dec_bin( n // 2, p * 10) if n > 0 else 0
def fib(x):
    if x in (1, 2):
        return 1
    return fib(x - 1) + fib(x - 2)
def fibneg(x):
    if x == -1:
        return 1
    elif x == -2:
        return -1
    return fibneg(x + 2) - fibneg(x + 1)

# ========================= ДОМАШНЕЕ ЗАДАНИЕ ===========================

def Task01():
    print("\033[36m{}".format('Задайте список из нескольких чисел. Напишите программу,\n'
                              'которая найдёт сумму элементов списка, стоящих на нечётной позиции.\n'
                              '*Пример:*\n'
                              '- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'))
    num = int(input("\033[0m{}".format('Укажите размер списка ->  ')))
    List01 = []
    result = 0
    for i in range(num):
        List01.insert(i, i+1)
        if i%2 !=0:
            result = result + List01[i]
    print("\033[32m{}".format(f'=================================================\n'
                              f'Сгенерирован список: {List01}\n'
                              f'Сумма нечетных позиций равна: {result}\n'
                              f'=================================================\n'))
def Task02():
    print("\033[36m{}".format('Напишите программу, которая найдёт произведение пар чисел списка.\n'
                              'Парой считаем первый и последний элемент, второй и предпоследний и т.д.\n'
                              '*Пример:*\n'
                              '- [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);\n'
                              '- [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) '))
    num = int(input("\033[0m{}".format('Задайте размер списка ->  ')))
    List02 = []
    for i in range(num):
        List02.insert(i, i+1)
    x = 0
    y = num - 1
    Result = []
    while x <= y:
        Result.append(List02[x] * List02[y])
        x = x + 1
        y = y - 1
    print("\033[32m{}".format(f'=================================================\n'
                              f'Сгенерирован список: {List02}\n'
                              f'Произведения пар списка: {Result}\n'
                              f'=================================================\n'))
def Task03():
    print("\033[36m{}".format('Задайте список из вещественных чисел. Напишите программу, которая найдёт\n'
                              'разницу между максимальным и минимальным значением дробной части элементов.\n'
                              '*Пример:*\n'
                              '- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'))
    num = int(input("\033[0m{}".format('Задайте размер списка ->  ')))
    List03 = []
    import random
    for i in range(num):
        List03.append(round(random.uniform(1.0, 10.0), 2))
    tempList = []
    for j in range(num):
        tempList.insert(i, round(List03[j]%1, 2))
    print("\033[32m{}".format(f'=================================================\n'
                              f'Сгенерирован список: {List03}\n'
                              f'Разница между минимальным и максимальными дробями равна:\n'
                              f'{round(tempList[list_max(tempList)] - tempList[list_min(tempList)], 2)}\n'
                              f'=================================================\n'))
def Task04():
    print("\033[36m{}".format('Напишите программу, которая будет преобразовывать десятичное число в двоичное.\n'
                              '*Пример:*\n'
                              '- 45 -> 101101\n'
                              '- 3 -> 11\n'
                              '- 2 -> 10'))
    num = int(input("\033[0m{}".format('Введите целое число ->  ')))
    x = num
    result = dec_bin(x)
    print("\033[32m{}".format(f'=================================================\n'
                              f'Число: {num} преобразованно в двоичный код и равно: {result}\n'
                              f'=================================================\n'))
def Task05():
    print("\033[36m{}".format('Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)\n'
                              '*Пример:*\n'
                              '- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]'))
    num = int(input("\033[0m{}".format('Введите целое число ->  ')))
    result = []
    for i in range(-num, num+1):
        if i < 0:
            result.append(fibneg(i))
        elif i == 0:
            result.append(0)
        elif i > 0:
            result.append(fib(i))
    
    print("\033[32m{}".format(f'=================================================\n'
                              f'фибоначчи ряда чисел от -{num} до {num}:\n'
                              f'{result}\n'
                              f'=================================================\n'))

# ======================================================================

def choice(x):
    os.system('cls')
    if x <= len(menu_list):
        print("\033[33m{}".format(f'=================================================\n{menu_list[x-1]}\n================================================='))
    if x == 1:
        try:
            Task01()
        except:
            error()
        enter_key_to_continue()
    elif x == 2:
        try:
            Task02()
        except:
            error()
        enter_key_to_continue()
    elif x == 3:
        try:
            Task03()
        except:
            error()
        enter_key_to_continue()
    elif x == 4:
        try:
            Task04()
        except:
            error()
        enter_key_to_continue()
    elif x == 5:
        try:
            Task05()
        except:
            error()
        enter_key_to_continue()
    elif x == 6:
        quit()
    else:
        error()
def main():
    os.system('cls')
    print("\033[32m{}".format('================================================\n============ Г Л А В Н О Е  М Е Н Ю ============\n================================================'))
    print("\033[33m{}".format('Выберите действие...'))
    print(*menu_list, sep='\n')
    print("\033[32m{}".format('================================================'))
    try:
        Task = int(input("\033[0m{}".format('Введите номер операции ->  ')))
    except:
        Task = 0
    if 0 < Task <= len(menu_list):
        choice(Task)
    else: error()

main()