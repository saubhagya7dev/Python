def print_board(board):
    """Prints the current state of the board."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    """Returns True if the given player has won."""
    win_combinations = [
        (0, 1, 2),  # rows
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),  # columns
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),  # diagonals
        (2, 4, 6)
    ]
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def is_draw(board):
    """Returns True if the board is full and there is no winner."""
    return all(cell != " " for cell in board)


def get_valid_move(board):
    """Asks the current player for a valid move (1-9)."""
    while True:
        move_str = input("Choose a position (1-9): ")
        if not move_str.isdigit():
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        move = int(move_str)
        if move < 1 or move > 9:
            print("Invalid position. Please choose a number from 1 to 9.")
            continue

        index = move - 1
        if board[index] != " ":
            print("That position is already taken. Choose another one.")
            continue

        return index


def play_game():

    board = [" "] * 9


    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 is X, Player 2 is O.")
    print("Positions are numbered as follows:")
    print()
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        move_index = get_valid_move(board)
        board[move_index] = current_player


        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! 🎉")
            break


        if is_draw(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

        
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    while True:
        play_game()
        again = input("Do you want to play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
