import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def get_empty_cells(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty_cells.append((row, col))
    return empty_cells

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    total_moves = 0

    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn.")

        if players[current_player] == "X":
            row = int(input("Enter row (0-2) or -1 to quit: "))
            if row == -1:
                print("Quitting the game.")
                break
            col = int(input("Enter column (0-2): "))
        else:
            empty_cells = get_empty_cells(board)
            row, col = random.choice(empty_cells)

        if board[row][col] == " ":
            board[row][col] = players[current_player]
            total_moves += 1

            if check_win(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break

            if total_moves == 9:
                print_board(board)
                print("It's a draw!")
                break

            current_player = 1 - current_player
        else:
            print("That cell is already occupied. Try again.")

if __name__ == "__main__":
    main()
