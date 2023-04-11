# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя

# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3


def sum(First_number, Second_number, result):
    
    if result < First_number + Second_number:
        result += 1
        return sum (First_number, Second_number, result)
    else:
        print (f'Сумма указанных чисел равна: {result}')
    



First_number = int(input())
Second_number = int(input())
result = 0
sum(First_number, Second_number, result)