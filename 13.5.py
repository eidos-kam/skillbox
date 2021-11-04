print('Задача 5. Недоделка 2')


# Вы всё так же работаете в конторе по разработке игр
# и смотрите различные программы прошлого горе-программиста.
# В одной из игр для детей, связанной с мультяшной работой с числами,
# вам нужно было написать код по следующим условиям:
# программа получает на вход два числа.
#
# В первом числе должно быть не меньше трёх цифр,
# во втором числе — не меньше четырёх,
# иначе программа выдаёт ошибку.
# Если всё нормально, то в каждом числе первая и последняя цифра меняются местами,
# а затем выводится их сумма.
#
#
# И тут вы натыкаетесь на программу,
# которая была написана прошлым программистом и которая как раз решает такую задачу!
# Однако старший программист сказал вам немного переписать этот код,
# чтобы он не выглядел так ужасно.
# Да и вам самим становится, мягко говоря, не по себе от него.
#
# Разбейте приведённую ниже программу на функции.
# Повторений кода должно быть как можно меньше.
# Также сделайте,
# чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.

def calculate_digits(number):
    first_num_count = 0
    temp = number
    while temp > 0:
        first_num_count += 1
        temp = temp // 10
    return first_num_count


def change_numbers(number):
    number = str(number)
    return int(number[-1:] + number[1:-1] + number[0:1])


first_n = int(input("Введите первое число: "))
if calculate_digits(first_n) < 3:
    print("В первом числе меньше трёх цифр.")
    exit()
second_n = int(input("\nВведите второе число: "))
if calculate_digits(second_n) < 4:
    print("Во втором числе меньше четырёх цифр.")
    exit()

first_n = change_numbers(first_n)
second_n = change_numbers(second_n)
print("Измененное первое число", first_n)
print("Измененное второе число", second_n)
print('\nСумма чисел:', first_n + second_n)

"""
last_digit = first_n % 10
first_digit = first_n // 10 ** (first_num_count - 1)
between_digits = first_n % 10 ** (first_num_count - 1) // 10
first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
print('Изменённое первое число:', first_n)
second_num_count = 0
temp = second_n

while temp > 0:
    second_num_count += 1
    temp = temp // 10
if second_num_count < 4:
    print("Во втором числе меньше четырёх цифр.")
else:
    last_digit = second_n % 10
    first_digit = second_n // 10 ** (second_num_count - 1)
    between_digits = second_n % 10 ** (second_num_count - 1) // 10
    second_n = last_digit * 10 ** (second_num_count - 1) + between_digits * 10 + first_digit
    print('Изменённое второе число:', second_n)
    print('\nСумма чисел:', first_n + second_n)
"""