# A nice simple implementation of the minimax algorithm for a Tic Tac Toe game

# The minimax algorithm is used to generate the best possible move for the computer player by
# recursively playing out all the possible moves and choosing the one that maximises the computer's
# chances of winning and minimises the player's chances of winning

# This is only possible to do because there are a very limited number of moves within a game of tic tac toe

# At most, the engine has to look at a total of 9! = 362,880 possible board states per move
# (drops to 8! = 40,320 if goes second), and this is only for the first move

# The number of possible board states decreases exponentially as the game progresses


def printBoard(bo: list[list[str]]):
    """Prints out the current state of the board in a presentable format"""

    for c, row in enumerate(bo):
        print(f"{row[0]} | {row[1]} | {row[2]}")
        if c != 2:
            print("---------")
    print("")


def makeMove(bo: list[list[str]], row: int, col: int, player: str) -> bool:
    """
    Makes a move on the board if the cell is empty,
    otherwise prints an error message and returns False
    """

    if bo[row][col] == " ":
        bo[row][col] = player
    else:
        print("Invalid move. Try again.")
        return False
    return True


def checkGameState(bo: list[list[str]]) -> tuple[bool, str]:
    """
    Checks the state of the game, returns True if
    the game is over and the winner if there is one
    """

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


def checkDraw(bo: list[list[str]]) -> bool:
    """Checks for a draw"""

    for row in bo:
        for cell in row:
            if cell == " ":
                return False
    return True


def getAvailableMoves(bo: list[list[str]]) -> list[tuple[int, int]]:
    """Returns a list of available moves on the board"""

    available_moves = []
    for row in range(3):
        for col in range(3):
            if bo[row][col] == " ":
                available_moves.append((row, col))
    return available_moves


def minimax(bo: list[list[str]], is_maximizing: bool) -> int:
    """The minimax algorithm for the AI to generate the best possible move"""

    # Checks if the game is over, and if so, who won
    _, winner = checkGameState(bo)

    # Because the AI is trying to maximise its score, it will return 1 if it wins,
    # to indicate that it is a good move, and -1 if it loses, to indicate that it is a bad move
    # And if the game is a draw, it will return 0
    if winner == "X":
        return -1
    if winner == "O":
        return 1
    if checkDraw(bo):
        return 0

    # If the AI is maximising, then it will try to maximise its score by recursively playing out
    # all the possible moves and choosing the one that maximises its score
    if is_maximizing:

        # Sets the score to negative infinity to ensure that the first move is always better,
        # regardless of whether its score is good or bad
        best_score = float("-inf")

        # Loops through all the available moves and plays them out
        for move in getAvailableMoves(bo):
            row, col = move
            bo[row][col] = "O"

            # Recursively plays out the move and gets the score
            score = minimax(bo, False)

            # Undoes the move to try out the next move, so that it doesn't affect the board state
            bo[row][col] = " "

            best_score = max(score, best_score)
        return best_score

    # Otherwise, the AI will try to minimise the score, as if it is playing as the player. It will
    # still play the best possible move for the player, but it will still try to minimise the score
    else:
        # Repeats the same process as above, but tries to minimise the score
        best_score = float("inf")
        for move in getAvailableMoves(bo):
            row, col = move
            bo[row][col] = "X"
            score = minimax(bo, True)
            bo[row][col] = " "
            best_score = min(score, best_score)
        return best_score


def generateEngineMove(bo: list[list[str]], player: str) -> tuple[int, int]:
    """Generates the best possible move for the AI using the minimax algorithm"""

    best_score = float("-inf")
    # Initialises the best row and column variables
    best_row = None
    best_col = None

    for move in getAvailableMoves(bo):

        # Like the function above, it plays out all the possible moves and chooses the one that
        # maximises the AI's score, whilstt minimising the player's score
        row, col = move
        bo[row][col] = player
        score = minimax(bo, False)
        bo[row][col] = " "

        # If the score is better than the best score, then it updates the best score and the
        # best row and column
        if score > best_score:
            best_score = score
            best_row = row
            best_col = col

    return best_row, best_col


def playGame() -> None:
    """The main function to play the game of Tic Tac Toe"""

    # Initialises the board and the current player
    board = [[" " for _ in range(3)] for _ in range(3)]
    curr_player = "X"

    # Loops through the game until it is over
    while True:
        printBoard(board)

        # Checks whose turn it is and makes the move
        if curr_player == "X":
            # User inputs the row and column of the move
            while True:
                row = int(input("Enter row: ")) - 1
                col = int(input("Enter col: ")) - 1
                if makeMove(board, row, col, "X"):
                    break
        else:
            # Generates the best possible move for the AI
            print("Computer's turn")
            row, col = generateEngineMove(board, "O")
            makeMove(board, row, col, "O")

        # Checks the state of the game and responds accordingly
        game_over, winner = checkGameState(board)
        if game_over:
            printBoard(board)
            print(f"Player {winner} wins!")
            break
        if checkDraw(board):
            printBoard(board)
            print("Draw!")
            break

        # Switches the player
        curr_player = "O" if curr_player == "X" else "X"


if __name__ == "__main__":
    playGame()
