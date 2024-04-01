def printBoard(bo):
    for c, row in enumerate(bo):
        print(f"{row[0]} | {row[1]} | {row[2]}")
        if c != 2:
            print("---------")
    print("")

def makeMove(bo, row, col, player) -> bool:
    if bo[row][col] == " ":
        bo[row][col] = player
    else:
        print("Invalid move. Try again.")
        return False
    return True


def checkGameState(bo) -> tuple[bool, str]:
    for player in ["X", "O"]:
        for row in bo:
            if row[0] == row[1] == row[2] == player:
                return True, player

        for col in range(3):
            if bo[0][col] == bo[1][col] == bo[2][col] == player:
                return True, player

        if bo[0][0] == bo[1][1] == bo[2][2] == player:
            return True, player
        if bo[0][2] == bo[1][1] == bo[2][0] == player:
            return True, player

    return False, None


def checkDraw(bo) -> bool:
    for row in bo:
        for cell in row:
            if cell == " ":
                return False
    return True


def playGame():
    board = [[" " for _ in range(3)] for _ in range(3)]

    curr_player = "X"
    while True:
        printBoard(board)
        if curr_player == "X":
            while True:
                row = int(input("Enter row: ")) - 1
                col = int(input("Enter col: ")) - 1
                if makeMove(board, row, col, "X"):
                    break
        else:
            print("Computer's turn")
            # TODO: Implement computer's move
            row = int(input("Computer enter row: ")) - 1
            col = int(input("Computer enter col: ")) - 1
            makeMove(board, row, col, "O")

        game_over, winner = checkGameState(board)
        if game_over:
            printBoard(board)
            print(f"Player {winner} wins!")
            break
        if checkDraw(board):
            printBoard(board)
            print("Draw!")
            break
        curr_player = "O" if curr_player == "X" else "X"

if __name__ == "__main__":
    playGame()
