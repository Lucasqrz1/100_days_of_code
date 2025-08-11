# Tic Tac Toe - Text Version

A simple command-line tic-tac-toe game built in Python. Two players take turns placing X and O on a 3x3 grid.

## What This Is

Think of this as the classic pencil-and-paper game, but on your computer. Players take turns trying to get three symbols in a row - just like the original!

## How to Play

1. The game shows a 3x3 grid with position numbers (1-9)
2. Player X goes first
3. Choose a position by typing a number (1-9)
4. Players alternate turns
5. First to get 3 in a row (horizontal, vertical, or diagonal) wins!
6. If all 9 spaces are filled with no winner, it's a tie

## Game Board Layout

```
Position numbers:    Example game:
   |   |              |   |   
 1 | 2 | 3          X | O | X 
___|___|___         ___|___|___
   |   |              |   |   
 4 | 5 | 6          O | X | O 
___|___|___         ___|___|___
   |   |              |   |   
 7 | 8 | 9          X | O | X 
   |   |              |   |   
```

## Requirements

- Python 3.x
- No external libraries needed!

## How to Run

### Option 1: Download and Run
```bash
# Save the code as tic_tac_toe.py
python tic_tac_toe.py
```

### Option 2: Copy and Paste
1. Copy the Python code
2. Paste it into a new file called `tic_tac_toe.py`
3. Open terminal/command prompt
4. Navigate to the file location
5. Run: `python tic_tac_toe.py`

## Game Features

- **Visual Board Display** - Shows current game state clearly
- **Position Helper** - Numbers show where you can place symbols
- **Input Validation** - Won't let you pick invalid or taken spots
- **Win Detection** - Automatically finds winners
- **Tie Detection** - Knows when the board is full
- **Play Again** - Keep playing without restarting the program
- **Error Handling** - Friendly messages for invalid inputs

## Example Game Flow

```
Welcome to Tic Tac Toe!
Players take turns placing X and O
First to get 3 in a row wins!

Current Board:
   |   |   
   |   |   
___|___|___
   |   |   
   |   |   
___|___|___
   |   |   
   |   |   
   |   |   

Player X's turn
Choose position (1-9): 5

Current Board:
   |   |   
   |   |   
___|___|___
   |   |   
   | X |   
___|___|___
   |   |   
   |   |   
   |   |   

Player O's turn
Choose position (1-9): 1
```

## Code Structure

The game is organized into simple parts:
- **TicTacToe Class** - Contains all game logic
- **display_board()** - Shows the current board
- **make_move()** - Places symbols on the board
- **check_winner()** - Finds if someone won
- **play_game()** - Main game loop

## Customization Ideas

Want to make it your own? Try adding:
- Player names instead of X and O
- Score tracking across multiple games
- Different board sizes (4x4, 5x5)
- Computer opponent with AI
- Colorful text output

## Troubleshooting

**"Invalid move" message?**
- Make sure you enter a number between 1-9
- Check that the position isn't already taken

**Game won't start?**
- Make sure you have Python installed
- Check that the file is saved as `.py`

---

**Ready to play?** Just run the file and start your first game!