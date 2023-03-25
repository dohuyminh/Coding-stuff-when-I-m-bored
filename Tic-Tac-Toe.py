# Code for playing Tic-Tac-Toe (3x3 or 5x5) on Terminal 

# Updated again: Added number denotation for the board for ease of tracking
# Added 1-player mode (vs computer)
# This should be the final update
# Code by Huy Minh Do. LinkedIn: https://www.linkedin.com/in/huy-minh-%C4%91%E1%BB%97-11096526a/
# Email: minhdohuy2111@gmail.com

import random

def print_grid(lst):
    numRow = 1
    rowSize = len(lst)
    colSize = len(lst[0])
    add_row = "     "
    for a in range(rowSize):
        add_row += "+{}  ".format(a)
    print(add_row)
    for i in range(rowSize):
        print('    -' + '----' * (rowSize))
        row = f'{numRow:<2}  |'
        for j in range(colSize):
            if lst[i][j] == 0:
                row += '   |'
            else:
                row += ' {} |'.format(lst[i][j])
        print(row)
        numRow += rowSize;
        row = f'{numRow:<2}  |'
    print('    -' + '----' * (rowSize))

def test_input(remain, grid, comp):
    if comp == "COMP":
        player = random.choice(remain)
        return player
    try:
        player = int(input("Enter a number from 1 to {} to make a move on the grid: ".format(len(grid) ** 2)))
    except:
        player = int(input("Invalid input, do it again: "))
    while (player not in remain):
        player = int(input("Invalid input, do it again: "))
    confirm1 = input("Are you sure? Remember: If you say no, the next time there won't be any oopsie poopsie (Y/N): ")
    while confirm1 != 'Y' and confirm1 != 'N':
        confirm1 = input("Invalid answer, try again (Y/N): ")
    if confirm1 == 'N':
        player = int(input("Last chance, enter a number from 1 to 9 to make a move: "))
        while (player not in remain):
            player = int(input("Invalid input, do it again: "))
    return player

def result(grid, remain, P1, P2):
    for i in range(len(grid)):
        check_row = grid[i]
        if len(list(set(check_row))) == 1:
            win = list(set(check_row))[0]
            if win != 0:
                return "P1 wins the game!!!" if win == P1 else "P2 wins the game!!!"
        check_col = [grid[j][i] for j in range(len(grid))]
        if len(list(set(check_col))) == 1:
            win = list(set(check_col))[0]
            if win != 0:
                return "P1 wins the game!!!" if win == P1 else "P2 wins the game!!!"
    check_diag1 = [grid[k][k] for k in range(len(grid))]
    check_diag2 = [grid[len(grid) - 1 - k][k] for k in range(len(grid))]
    if len(list(set(check_diag1))) == 1:
        win = list(set(check_diag1))[0]
        if win != 0:
            return "P1 wins the game!!!" if win == P1 else "P2 wins the game!!!"
    if len(list(set(check_diag2))) == 1:
        win = list(set(check_diag2))[0]
        if win != 0: 
            return "P1 wins the game!!!" if win == P1 else "P2 wins the game!!!"
    return "Tie" if remain == [] else 0

def check(grid, remain, P1, P2):
    if result(grid, remain, P1, P2) != 0:
        print(result(grid, remain, P1, P2))
        print("The game is as followed: ")
        print_grid(grid)
        more = input("Another match? (Y/N): ")
        while (more != 'Y' and more != 'N'):
            more = input("Invalid answer, try again (Y/N): ")
        if more == 'Y':
            letsplay()
        else:
            print("\n*************************")
            print("Thank you for playing!!!")
            print("*************************\n")
            return 0
    return 1

def generate_board():
    try:
        size = int(input("Enter the Tic-Tac-Toe size (3 or 5): "))
    except:
        size = int(input("Invalid, try again: "))
    while size != 3 and size != 5:
        size = int(input("Invalid, try again: "))
    grid = []
    for i in range(size):
        grid.append([0] * size)
    return grid

def letsplay():
    try:
        comp = int(input("1-player or 2 players? (1/2): "))
    except:
        comp = int(input("Invalid, try again: "))
    while (comp != 1 and comp != 2):
        comp = int(input("Invalid, try again: "))
    player_dict = {}
    if comp == 1:
        try:
            choice = int(input("What player do you want to play as? (1/2): "))
        except:
            choice = int(input("Invalid, try again: "))
        while (choice != 1 and choice != 2):
            choice = int(input("Invalid, try again: "))
        player_dict[choice] = "PLAYER"
        if choice != 1: player_dict[1] = "COMP"
        elif choice != 2: player_dict[2] = "COMP"
    elif comp == 2:
        player_dict = {1: "PLAYER", 2: "PLAYER"}
    grid = generate_board()
    P1 = input("Choose a digit to play as player one: ")
    while (len(P1) != 1):
        P1 = input("Invalid name, try again: ")
    print("Player 1: {}".format(P1))
    P2 = input("Choose a digit to play as player two: ")
    while (len(P2) != 1 or P2 == P1):
        P2 = input("Invalid name, try again: ")
    print("Player 2: {}".format(P2))
    print('\n******************')
    print("Great, let's play!")
    print('******************\n')
    remain = [i for i in range(1, len(grid) ** 2 + 1)]
    print("Choose a number from 1 to 9 with respect to the following\nboard format:")
    print_grid(grid)
    colInd = [i for i in range(len(grid))] * len(grid)
    rowInd = []
    for i in range(len(grid)):
        rowInd += [i] * len(grid)
    while True:
        
        print("\nIt's player 1's turn: ")
        turn1 = test_input(remain, grid, player_dict[1])
        remain.remove(turn1)
        grid[rowInd[turn1 - 1]][colInd[turn1 - 1]] = P1;
        print("The grid currently looks like this: ")
        print_grid(grid)
        if check(grid, remain, P1, P2) == 0: break
        
        print("\nIt's player 2's turn: ")
        turn2 = test_input(remain, grid, player_dict[2])
        remain.remove(turn2)
        grid[rowInd[turn2 - 1]][colInd[turn2 - 1]] = P2;
        print("The grid currently looks like this: ")
        print_grid(grid)
        if check(grid, remain, P1, P2) == 0: break


letsplay()
