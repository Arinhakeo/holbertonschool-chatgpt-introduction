#!/usr/bin/python3

def print_board(board):
    """
    Affiche le plateau de jeu.
    
    Args:
        board (list of list of str): Le plateau de jeu, une liste de listes contenant les symboles des joueurs ("X", "O", ou " ").
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Vérifie si un joueur a gagné.
    
    Args:
        board (list of list of str): Le plateau de jeu.
    
    Returns:
        bool: True si un joueur a gagné, False sinon.
    """
    # Vérifie les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifie les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifie les diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    """
    Vérifie si la partie est un match nul (draw).
    
    Args:
        board (list of list of str): Le plateau de jeu.
    
    Returns:
        bool: True si le plateau est plein et aucun joueur n'a gagné, False sinon.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Fonction principale pour exécuter le jeu de Tic Tac Toe.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Row and column must be between 0 and 2. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
        
        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("The game is a draw!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()