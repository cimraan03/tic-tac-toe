"""
Tic Tac Toe
===========

A command line Tic Tac Toe game written in Python.

Features
--------
* Two player mode (player vs player on the same keyboard).
* Single player mode against a computer opponent.
* Input validation so the game never crashes on bad input.
* Session statistics tracked with global counters.

Run with:  python tic_tac_toe.py
"""

import random

# ---------------------------------------------------------------------------
# Global statistics counters
# These live outside every function so they persist across games in a session.
# Functions that change them declare them with the `global` keyword.
# ---------------------------------------------------------------------------
games_played = 0
x_wins = 0
o_wins = 0
draws = 0
total_moves = 0
invalid_inputs = 0

# Every combination of board positions that counts as three in a row.
# The board is a list of 9 cells, indexed 0 to 8:
#   0 | 1 | 2
#   3 | 4 | 5
#   6 | 7 | 8
WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def show_instructions():
    """Print the rules and explain how to choose a square."""
    print("\n" + "=" * 40)
    print("          WELCOME TO TIC TAC TOE")
    print("=" * 40)
    print("Two players take turns placing X and O on a 3x3 grid.")
    print("Get three of your marks in a row, column or diagonal to win.")
    print("If all nine squares fill up with no winner, the game is a draw.")
    print("\nChoose a square by typing its number:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("\nType 'q' at any time during a move to quit the current game.")


def create_board():
    """Return a new empty board as a list of 9 spaces."""
    return [" "] * 9


def display_board(board):
    """Print the board, showing square numbers in empty cells as a guide."""
    print()
    for row in range(3):
        cells = []
        for col in range(3):
            index = row * 3 + col
            # Show the square number if empty so players know what to type.
            cells.append(board[index] if board[index] != " " else str(index + 1))
        print(" " + " | ".join(cells))
        if row < 2:
            print("---+---+---")
    print()


def get_menu_choice(prompt, valid_options):
    """
    Keep asking until the user types one of the valid options.

    Args:
        prompt (str): The question shown to the user.
        valid_options (list[str]): Accepted answers, in lower case.

    Returns:
        str: The chosen option in lower case.
    """
    global invalid_inputs
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_options:
            return choice
        invalid_inputs += 1
        print(f"Please enter one of: {', '.join(valid_options)}")


def get_player_name(label):
    """Ask for a player's name, falling back to a default if left blank."""
    name = input(f"Enter a name for {label} (press Enter for '{label}'): ").strip()
    return name if name else label


def get_player_move(board, player_name, mark):
    """
    Ask a human player for a square and validate it.

    Rejects text that is not a number, numbers outside 1 to 9,
    and squares that are already taken.

    Args:
        board (list[str]): The current board.
        player_name (str): Name shown in the prompt.
        mark (str): 'X' or 'O'.

    Returns:
        int | None: Board index 0 to 8, or None if the player quits.
    """
    global invalid_inputs
    while True:
        answer = input(f"{player_name} ({mark}), choose a square 1 to 9: ").strip().lower()

        if answer == "q":
            return None

        # Catch anything that cannot be turned into a whole number.
        try:
            square = int(answer)
        except ValueError:
            invalid_inputs += 1
            print("That is not a number. Please type a number from 1 to 9.")
            continue

        if square < 1 or square > 9:
            invalid_inputs += 1
            print("That square does not exist. Please choose 1 to 9.")
            continue

        index = square - 1  # convert from 1 to 9 for players to 0 to 8 for the list
        if board[index] != " ":
            invalid_inputs += 1
            print("That square is already taken. Try another one.")
            continue

        return index


def find_winning_move(board, mark):
    """Return an index that would complete three in a row for `mark`, or None."""
    for a, b, c in WINNING_LINES:
        line = [board[a], board[b], board[c]]
        # Two of our marks plus one empty square means we can finish the line.
        if line.count(mark) == 2 and line.count(" ") == 1:
            return (a, b, c)[line.index(" ")]
    return None


def get_computer_move(board, computer_mark, player_mark):
    """
    Choose a move for the computer using simple rules, in order:
    1. Win if possible.
    2. Block the player if they are about to win.
    3. Take the centre.
    4. Take a random corner.
    5. Take any remaining square.
    """
    move = find_winning_move(board, computer_mark)
    if move is not None:
        return move

    move = find_winning_move(board, player_mark)
    if move is not None:
        return move

    if board[4] == " ":
        return 4

    corners = [i for i in (0, 2, 6, 8) if board[i] == " "]
    if corners:
        return random.choice(corners)

    return random.choice([i for i in range(9) if board[i] == " "])


def check_winner(board, mark):
    """Return True if `mark` has three in a row anywhere on the board."""
    return any(board[a] == board[b] == board[c] == mark for a, b, c in WINNING_LINES)


def is_board_full(board):
    """Return True if there are no empty squares left."""
    return " " not in board


def update_statistics(result):
    """
    Update the global counters after a finished game.

    Args:
        result (str): 'X', 'O' or 'draw'.
    """
    global games_played, x_wins, o_wins, draws
    games_played += 1
    if result == "X":
        x_wins += 1
    elif result == "O":
        o_wins += 1
    else:
        draws += 1


def show_statistics():
    """Print a summary of every game played in this session."""
    print("\n" + "=" * 40)
    print("           SESSION STATISTICS")
    print("=" * 40)
    print(f"Games played:      {games_played}")
    print(f"X wins:            {x_wins}")
    print(f"O wins:            {o_wins}")
    print(f"Draws:             {draws}")
    if games_played > 0:
        average = total_moves / games_played
        print(f"Average moves:     {average:.1f} per game")
        print(f"X win rate:        {x_wins / games_played:.0%}")
        print(f"O win rate:        {o_wins / games_played:.0%}")
    print(f"Invalid inputs:    {invalid_inputs}")
    print("=" * 40)


def play_game(player_names, computer_mark=None):
    """
    Play one full game and return the result.

    Args:
        player_names (dict): Maps 'X' and 'O' to display names.
        computer_mark (str | None): 'O' if the computer plays O, otherwise None.

    Returns:
        str | None: 'X', 'O', 'draw', or None if a player quit.
    """
    global total_moves
    board = create_board()
    current_mark = "X"  # X always goes first
    moves_this_game = 0  # only added to the global total if the game finishes

    while True:
        display_board(board)

        if current_mark == computer_mark:
            player_mark = "X" if computer_mark == "O" else "O"
            move = get_computer_move(board, computer_mark, player_mark)
            print(f"{player_names[current_mark]} chooses square {move + 1}.")
        else:
            move = get_player_move(board, player_names[current_mark], current_mark)
            if move is None:
                print("Game abandoned. It will not count towards the statistics.")
                return None

        board[move] = current_mark
        moves_this_game += 1

        # Check for a result straight after each move.
        if check_winner(board, current_mark):
            display_board(board)
            print(f"*** {player_names[current_mark]} ({current_mark}) wins! ***")
            total_moves += moves_this_game
            return current_mark

        if is_board_full(board):
            display_board(board)
            print("*** It's a draw! ***")
            total_moves += moves_this_game
            return "draw"

        # Hand the turn to the other player.
        current_mark = "O" if current_mark == "X" else "X"


def main():
    """Run the menu loop: set up players, play games and show statistics."""
    show_instructions()

    mode = get_menu_choice("\nPlay against (1) another player or (2) the computer? ", ["1", "2"])
    if mode == "1":
        player_names = {"X": get_player_name("Player X"), "O": get_player_name("Player O")}
        computer_mark = None
    else:
        player_names = {"X": get_player_name("Player X"), "O": "Computer"}
        computer_mark = "O"

    while True:
        result = play_game(player_names, computer_mark)
        if result is not None:
            update_statistics(result)
        show_statistics()

        again = get_menu_choice("\nPlay again? (y/n): ", ["y", "n", "yes", "no"])
        if again in ("n", "no"):
            break

    print("\nThanks for playing Tic Tac Toe. Goodbye!")


# Only start the game when the file is run directly, not when it is imported.
if __name__ == "__main__":
    main()
