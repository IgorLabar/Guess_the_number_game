import random


MAX_GUESS = 10 # Количество попыток
NUM_DIGIT = 2 # Количество попыток


# Получить секртеное число
def get_secret_num():
    numbers = list('0123456789')
    random.shuffle(numbers)

    secret_num = ''

    for i in range(NUM_DIGIT):
        secret_num += str(numbers[i])

    return secret_num


# Основная логика игры
def start_game():
    print('Игра началась!')
    print('Число загадано!')

    guess = 1
    secret_num = get_secret_num() # Загаданное число

    while guess <= MAX_GUESS:
        print(f'попытка номер {guess}')
        guess += 1
        users_guesses = input()
        if users_guesses < secret_num:
            print('Больше')
            users_guesses
        elif users_guesses > secret_num:
            print('Меньше')
            users_guesses
        else:
            print("Поздравляю, Вы его нашли!")
            return main()


# Главное меню игры
def main():
    print(f'''
        Правила игры: Игрок должен отгадать число, загаданное  компьютером, всего у Вас будет {MAX_GUESS} попыток,
        а диапозон чисел составляет 1-50.
        Также в игре есть подсказки:
        1 - Больше - если вы ввели число меньше загадонного
        2 - Меньше - если вы ввели число больше загадонного

        Это все, удачи!!\n
    ''')
    print('Хотите начать игру? 1-Да 0-Нет')

    user_command = int(input())

    while True:
        if user_command == 1:
            return start_game()
        else:
            print("До скорой встречи!")
            break


if __name__ == '__main__':
    main()