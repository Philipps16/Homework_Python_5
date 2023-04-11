# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения. Циклы использовать нельзя

# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16


def Pow(First_number, Second_number, result):
    
    if Second_number > 0:
        result *= First_number
        return Pow (First_number, Second_number - 1, result)
    else:
        print (result)
    



First_number = int(input())
Second_number = int(input())
result = 1
Pow(First_number, Second_number, result)
