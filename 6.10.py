print('Задача 10. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.

# Напишите программу,
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.

# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.
print("Загадай число от 1 до 100")
looking_number = 0
tries_counter = 0
higher_border = 100
lower_border = 1
while True:
    looking_number = (higher_border - lower_border) // 2 + lower_border
    # print(f"!DEBUG! looking_number:{looking_number}, borders: {lower_border} - {higher_border}" )
    some_number = int(input(f"Твое число равно (1), больше (2) или меньше(3) чем число {looking_number}? "))
    if some_number not in (1, 2, 3):
        print("Команда не распознана")
        continue
    tries_counter += 1
    if some_number == 1:
        break
    elif some_number == 2:
        lower_border = looking_number + 1
    else:
        higher_border = looking_number - 1
print(f"Я угадал! Число попыток: {tries_counter}")
