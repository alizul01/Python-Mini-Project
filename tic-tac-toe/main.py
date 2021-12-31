# tic tac toe game
import random as rd

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)


def printPapan(theBoard):
    print(theBoard['7'] + '|' + theBoard['8'] + '|' + theBoard['9'])
    print('-+-+-')
    print(theBoard['4'] + '|' + theBoard['5'] + '|' + theBoard['6'])
    print('-+-+-')
    print(theBoard['1'] + '|' + theBoard['2'] + '|' + theBoard['3'])


def game():
    turn = 'X'
    count = 0
    confirm = True
    player = "0"

    for i in range(10):
        if count == 0:
            player = input(
                "Ingin bermain dengan bot atau 2 Player?\n1. Bot\n2. 2-Player\nMasukkan Pilihanmu : ")

        if confirm == True:
            printPapan(theBoard)
        else:
            pass

        if player == '1':
            if count == 0:
                print("Kamu bermain dengan bot")
            print(f"Ini adalah giliranmu, {turn}", end=" ")
            if turn == 'O':
                move = str(rd.randint(1, 9))
            else:
                move = input()
        else:
            if count == 0:
                print("Kamu bermain dengan 2 Player")
            print(f"Ini adalah giliranmu, {turn}", end=" ")
            move = input()

        # if turn == 'O':
        #     move = str(rd.randint(1, 9))

        # else:
        #     move = input()

        if move not in board_keys:
            print("Pilihan kamu tidak valid! Masukkan angka 1 - 9")
            confirm = False
            continue

        if theBoard[move] == ' ':
            theBoard[move] = turn
            confirm = True
            count += 1
        else:
            print('Tidak boleh ditempati')
            confirm = False
            continue

        if count >= 5:
            if checkWinner() == True:
                break
        elif count >= 9:
            print("It's a Tie!")
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


def checkWinner():
    if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
        printPapan(theBoard)
        print(f"Pemenangnya adalah {theBoard['1']}")
        return True
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
        printPapan(theBoard)
        print(f"Pemenangnya adalah {theBoard['4']}")
        return True
    elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
        printPapan(theBoard)
        print(f"Pemenangnya adalah {theBoard['7']}")
        return True
    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
        printPapan(theBoard)
        print(f"Pemenangnya adalah {theBoard['3']}")
        return True
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
        printPapan(theBoard)
        print(f"Pemenangnya adalah {theBoard['2']}")
        return True
    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
        printPapan(theBoard)
        print(f"Pemenangnya adalah {theBoard['1']}")
        return True
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
        printPapan(theBoard)
        print(f"Pemenangnya adalah {theBoard['1']}")
        return True
    elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':
        printPapan(theBoard)
        print(f"Pemenangnya adalah {theBoard['5']}")
        return True
    else:
        return False


game()
