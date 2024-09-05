#!/usr/bin/python3

def print_board(board):
    border = "-" * (len(board[0]) * 4 + 1)
    print(border)
    for row in board:
        print("| " + " | ".join(row) + " |")
        print(border)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        while True:
            try:
                row = int(input(f"Enter row (1, 2, or 3) for player {player}: ")) - 1
                col = int(input(f"Enter column (1, 2, or 3) for player {player}: ")) - 1
                if row in [0, 1, 2] and col in [0, 1, 2]:
                    if board[row][col] == " ":
                        board[row][col] = player
                        break
                    else:
                        print("That spot is already taken! Try again.")
                else:
                    print("Invalid input! Enter row and column as 1, 2, or 3.")
            except ValueError:
                print("Invalid input! Enter numbers only.")
        # Switch player
        player = "O" if player == "X" else "X"

    print_board(board)
    winner = "O" if player == "X" else "X"
    print(f"Player {winner} wins!")

tic_tac_toe()
