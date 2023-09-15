import random
import numpy as np
import pymongo

client = pymongo.MongoClient("mongodb://mongodb:27017/")
db = client["tic_tac_toe"]
record_collection = db["record"]

player_record = record_collection.find_one({"player": "player"})
pc_record = record_collection.find_one({"player": "pc"})

if not player_record:
    player_record = {"player": "player", "victorias": 0}
    record_collection.insert_one(player_record)

if not pc_record:
    pc_record = {"player": "pc", "victorias": 0}
    record_collection.insert_one(pc_record)

print(f"Record de player: {player_record['victorias']} victorias")
print(f"Record de PC: {pc_record['victorias']} victorias")

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

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    total_moves = 0
    win = "Tables"

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
            empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
            row, col = random.choice(empty_cells)

        if board[row][col] == " ":
            board[row][col] = players[current_player]
            total_moves += 1

            if check_win(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                win = f"Player {players[current_player]} wins!"
                if players[current_player] == "X":
                    player_record["victorias"] += 1
                    record_collection.update_one({"player": "player"}, {"$set": {"victorias": player_record["victorias"]}})
                else:
                    pc_record["victorias"] += 1
                    record_collection.update_one({"player": "pc"}, {"$set": {"victorias": pc_record["victorias"]}})
                break

            if total_moves == 9:
                print_board(board)
                print("It's a draw!")
                break

            current_player = 1 - current_player
        else:
            print("That cell is already occupied. Try again.")

    print(f"Final Game Board - {win}")
    np_board = np.array(board)
    print(np_board)

if __name__ == "__main__":
    main()
