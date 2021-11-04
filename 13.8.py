print('Задача 8. Сумма ряда')


# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709
def get_input_float_data(input_string: str):
    """
    проверка вводимого значения на предмет возможности приведения
    к полоижетльному действительному числу (тип float без знака)
    :param input_string:
    :return:
    """
    while True:
        result_item = input(input_string)
        if result_item.replace('.', '', 1).isdigit() and float(result_item) > 0:
            return float(result_item)
        else:
            print("Вы ошиблись при вводе")


def get_input_int_data(input_string: str):
    """
    проверка вводимого значения на предмет возможности приведения к полоижетльному целому числу (тип int без знака)
    :param input_string:
    :return:
    """
    while True:
        result_item = input(input_string)
        if result_item.isdigit() and int(result_item) > 0:
            return int(result_item)
        else:
            print("Вы ошиблись при вводе")


def math_power(number, degree):
    """
    интерпретация функции возведения числа в степень
    :param number:
    :param degree:
    :return:
    """
    result_number = number
    if degree == 0:
        return 1
    elif degree == 1:
        return number
    for _ in range(degree - 1):
        result_number *= number
    return result_number


def math_factorial(number):
    """
    интерпретация функции нахождения факториала числа
    :param number:
    :return:
    """
    result_number = 1
    for step in range(1, number + 1):
        result_number *= step
    return result_number


x = get_input_int_data("Введите х: ")
precision = get_input_float_data("Введите точность: ")
summ = 1
step = 1
while True:
    power_i = math_power(x, 2 * step)
    factorial_i = math_factorial(2 * step)
    step_result = math_power(-1, step) * power_i / factorial_i
    summ += step_result
    if abs(step_result) < precision:
        break
    step += 1
print("Сумма ряда:", summ)
