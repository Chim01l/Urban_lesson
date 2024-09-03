# крестики - нолики консольная
# для  двух игроков:
# Инициализация карты
maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# Инициализация победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


# Вывод карты на экран
def print_maps():

    print(maps[0], end=" ")
    print(maps[1], end=" ")
    print(maps[2])

    print(maps[3], end=" ")
    print(maps[4], end=" ")
    print(maps[5])

    print(maps[6], end=" ")
    print(maps[7], end=" ")
    print(maps[8])

def check(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

# Сделать ход в ячейку
def step_maps(step, symbol):
    if not check(step) : #если совсем не тудаk
        print("Ход неверный - вы пропускаете ход ")
        return
    else :
       step =  int(step)
    if step> 9 :
        print("Ход неверный - вы пропускаете ход ")
        return
    ind = step-1
    if maps[ind] == step:        #проверяем возможен ли ход
        maps[ind] = symbol

    else :
       print ("Место занято - вы пропускаете ход ")


# Получить текущий результат игры
def get_result():
    win = ""
   # print(maps)
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"

    return win


# Основная программа
game_over = False
player1 = True

while game_over == False:

    # 1. Показываем карту
    print_maps()

    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
    else:
        symbol = "O"
    step = input(f"{symbol}, ваш ход: ")
    if len(step) > 0 :
        step_maps(step, symbol)  # делаем ход в указанную ячейку
    else :
        print(f'{symbol}  - пропускает ход')

    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
print_maps()
print("Победил", win)