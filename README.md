# Tic Tac Toe

A command line Tic Tac Toe game written in Python for the Rockborne Python Game Development project.

![Flowchart](flowchart.png)

## Features

* **Two game modes:** play against a friend on the same keyboard, or against the computer.
* **Computer opponent:** takes a winning move if it has one, blocks you if you are about to win, then prefers the centre and corners.
* **Input checking:** the game handles text, numbers outside 1 to 9 and squares that are already taken, so it never crashes.
* **Session statistics:** games played, wins for X and O, draws, average moves per game, win rates and the number of invalid inputs.
* **Quit any time:** type `q` during a move to abandon a game. Abandoned games are not counted in the statistics.

## Requirements

Python 3.8 or later. No extra packages are needed.

## How to run

Clone the repository and run the script:

```bash
git clone https://github.com/cimraan03/tic-tac-toe.git
cd tic-tac-toe
python tic_tac_toe.py
```

Or open `Python_GameProject.ipynb` in Jupyter and run the cells in order.

## How to play

1. Choose a mode: type `1` for two players or `2` to play the computer.
2. Enter player names, or press Enter to use the defaults.
3. X always goes first. On your turn, type the number of the square you want:

   ```
    1 | 2 | 3
   ---+---+---
    4 | 5 | 6
   ---+---+---
    7 | 8 | 9
   ```

4. Get three of your marks in a row, column or diagonal to win. If all nine squares fill with no winner, it is a draw.
5. After each game the statistics are shown. Type `y` to play again or `n` to exit.

## Code structure

| Function | Purpose |
| --- | --- |
| `show_instructions()` | Prints the rules and the square numbering |
| `create_board()` | Returns a new empty board |
| `display_board(board)` | Prints the board, with numbers in empty squares |
| `get_menu_choice(prompt, options)` | Repeats a question until a valid answer is given |
| `get_player_name(label)` | Asks for a name with a sensible default |
| `get_player_move(board, name, mark)` | Gets and validates a square from a human player |
| `find_winning_move(board, mark)` | Finds a square that completes three in a row |
| `get_computer_move(board, ...)` | Chooses the computer's move |
| `check_winner(board, mark)` | Checks all eight winning lines |
| `is_board_full(board)` | Checks for a draw |
| `update_statistics(result)` | Updates the global counters |
| `show_statistics()` | Prints the session summary |
| `play_game(names, computer_mark)` | Runs one full game |
| `main()` | Menu loop that ties everything together |

The statistics are stored in global counters (`games_played`, `x_wins`, `o_wins`, `draws`, `total_moves`, `invalid_inputs`) so they persist between games in a session.

## Files

* `tic_tac_toe.py`: the game
* `Python_GameProject.ipynb`: the project notebook with flowchart and code
* `flowchart.png`: flowchart of the game logic
* `flowchart.dot`: source for the flowchart (Graphviz)
