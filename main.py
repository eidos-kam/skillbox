import random
from collections import Counter
print('Задача 9. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.


def rock_paper_scissors():
    #Здесь будет игра "Камень, ножницы, бумага"
    is_win = False
    items = {1: "камень", 2: "ножницы", 3: "бумага"}
    wins = Counter() # 1 - игрок, 2 - компьютер, 3 - ничья
    print("Камень, ножницы, бумага")
    while True:
        current_choice = random.randint(1, 3)
        player_choice = int(input("Ваш ход: 1 - камень, 2 - ножницы, 3 - бумага, 0 - выход: "))
        if player_choice == 0:
            break
        elif player_choice == current_choice:
            print("Ничья! Я загадал то же самое!")
            wins[3] += 1
        elif current_choice - player_choice in (-1, 2):
            print(f"Мой выбор {items[current_choice]}, Ваш выбор {items[player_choice]}. Победитель Я!")
            wins[2] += 1
        else:
            print(f"Мой выбор {items[current_choice]}, Ваш выбор {items[player_choice]}. Победитель Вы!")
            wins[1] += 1
    print("Игра окончена!")
    print(f"Вы выиграли {wins[1]}, я выиграл {wins[2]}, ничья {wins[3]}")
    mainMenu()


def guess_the_number():
    #Здесь будет игра "Угадай число"
    print("Угадай число\n", "=" * 20)
    print("Загадываю число от 1 до 100")
    print("Если Ваше число больше загаданного, я отвечу 'горячо', если меньше - 'холодно'")
    magic_number = random.randint(1, 100)
    rounds = 0
    while True:
        player_choice = int(input("Введите число: "))
        if player_choice == 0:
            break
        elif player_choice == magic_number:
            print("Поздравляю! Вы угадали. Число попыток: ", rounds)
            break
        elif player_choice > magic_number:
            print("Горячо!")
        elif player_choice < magic_number:
            print("Холодно!")
        rounds += 1
    print("Игра окончена!\n")
    mainMenu()

def mainMenu():
    print("Главное меню")
    print("="*20)
    print("Выберите игру")
    print("1 - Камень, ножницы, бумага")
    print("2 - Угадай число")
    print("0 - Выход")
    game_number = int(input())
    if game_number == 1:
        rock_paper_scissors()
    elif game_number == 2:
        guess_the_number()
    elif game_number == 0:
        return
    else:
        print("Команда не распознана")
        mainMenu()

mainMenu()