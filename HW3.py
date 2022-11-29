import os
Task = 0
List1 = ['1. Сумма нечетных позиций списка.','2. Произведение пар чисел списка.','3. Разница между min и max дробной частью.','4. Десятичное число в двоичное.','5. Фибоначчи.','6. Выход']
os.system('cls')

def enter_key_to_continue():
    input("\033[0m{}".format('=================================================\nДля продолжения нажмите клавишу [ENTER]'))
    main()
def error(x):
    os.system('cls')
    print("\033[37m\033[41m{}".format('\n                                       '
                              '\n              ОШИБКА!!!                '
                              '\n  Вы ввели не существующую команду...  '
                              '\n      Выберите команду из списка.      '
                              '\n                                       '))
    enter_key_to_continue()
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
    print("\033[36m{}".format('Task 4 text'))
    print("\033[32m{}".format('=================================================\nresult\n=================================================\n'))
def Task05():
    print("\033[36m{}".format('Task 5 text'))
    print("\033[32m{}".format('=================================================\nresult\n=================================================\n'))

# ======================================================================

def choice(x):
    os.system('cls')
    if x <= len(List1):
        print("\033[33m{}".format(f'=================================================\n{List1[x-1]}\n================================================='))
    if x == 1:
        Task01()
        enter_key_to_continue()
    elif x == 2:
        Task02()
        enter_key_to_continue()
    elif x == 3:
        Task03()
        enter_key_to_continue()
    elif x == 4:
        Task04()
        enter_key_to_continue()
    elif x == 5:
        Task05()
        enter_key_to_continue()
    elif x == 6:
        os.system('cls')
        print("\033[0m{}".format('Выход из программы...'))
        import sys
        sys.exit()
    else:
        error(Task)
def main():
    os.system('cls')
    print("\033[32m{}".format('================================================\n============ Г Л А В Н О Е  М Е Н Ю ============\n================================================'))
    print("\033[33m{}".format('Выберите действие...'))
    print(*List1, sep='\n')
    print("\033[32m{}".format('================================================'))
    try:
        Task = int(input("\033[0m{}".format('Введите номер операции ->  ')))
    except:
        Task = 0
    choice(Task)

main()