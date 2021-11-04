def bedroom():
    print("Вы в спальне. Куда идем?")
    print("1 - В коридор")
    print("2 - В ванную")
    player_choice = int(input())
    if player_choice == 1:
        corridor()
    elif player_choice == 2:
        bathroom()
    else:
        print("Команда не распознана")
        bedroom()


def bathroom():
    print("Вы в ванной. Куда идем?")
    print("1 - В коридор")
    print("2 - В спальню")
    player_choice = int(input())
    if player_choice == 1:
        corridor()
    elif player_choice == 2:
        bedroom()
    else:
        print("Команда не распознана")
        bathroom()


def kitchen():
    print("Вы в кухне. Куда идем?")
    print("1 - В коридор")
    print("2 - В окно")
    player_choice = int(input())
    if player_choice == 1:
        corridor()
    elif player_choice == 2:
        print("Вы выпрыгнули из окна и разбились. Проигрыш!")
        end_game()
    else:
        print("Команда не распознана")
        kitchen()


def end_game():
    print("Игра окончена!")


def corridor():
    print("Вы в коридоре. Куда идем?")
    print("1 - В спальню")
    print("2 - В ванную")
    print("3 - На кухню")
    print("4 - В дверь")
    player_choice = int(input())
    if player_choice == 1:
        bedroom()
    elif player_choice == 2:
        bathroom()
    elif player_choice == 3:
        kitchen()
    elif player_choice == 4:
        print("Вам удалось выйти из квартиры! Победа!")
        end_game()
    else:
        print("Команда не распознана")
        corridor()


corridor()
