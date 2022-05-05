



def greet():
    print("-------------------------------------------")
    print("        -------Привет-------")
    print("-------------------------------------------")
    print("        Давай сыграем с тобой в игру       ")
    print("-------------------------------------------")
    print("   ----------Вводи Х и У------------    ")
    print("__________Горизонталь это Х_______________")
    print("-----------Вертикаль это Y---------")

def show():
    print()
    print("         | 0 | 1 | 2 | ")
    print("   -------------------")
    for i, row in enumerate(field):
        row_str = f"    {i}   |  {' | '.join(row)} |"
        print(row_str)
        print("  ---------------------")
    print()


def ask():
    while True:
        cords = input("           Сделай Ход").split()

        if len(cords) != 3:
            print("  Введи координаты! ")
            continue

        x, y = cords

        if not(x.isdigit()) or not (y.isdigit()):
            print(" Вводи числа! ")

        x, y = int(x), int(y)
        if 1 > x or x > 3 or 1 > y or y > 3 :
            print(" Неправильный ввод! ")
            continue

        if field[x][y] != "":
            print(" Занято. Ходи в другое место! ")
            continue

        return x, y

def check_win():
    win_cord =(((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))

    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
            if symbols == ["X", "X", "X"]:
                print("Выиграл X!!!")
                return True
            if symbols == ["0", "0", "0"]:
                print("Выиграл 0!!!")
                return True
            return False
greet()
field = [[" "] * 3 for i in range(3)]
count = 0

while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break



