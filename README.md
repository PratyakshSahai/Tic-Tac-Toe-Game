# Tic-Tac-Toe (C Console Game)

A simple 2-player Tic-Tac-Toe game written in C, played in the terminal.  
Players take turns entering positions 1–9 to place `X` or `O` on a 3×3 grid.

## Features

- 2-player local game (X vs O)
- Numbered grid (1–9) for easy move selection
- Input validation for:
  - Invalid positions (not 1–9)
  - Occupied positions
- Detects winner and draw


## How to Play

- The grid positions are numbered 1 to 9:

  1 | 2 | 3  
  4 | 5 | 6  
  7 | 8 | 9  

- Player **X** starts first.
- On your turn, type the number of the position where you want to place your mark.
- The game ends when:
  - X or O gets three in a row (horizontally, vertically, or diagonally), or
  - All 9 positions are filled (draw).

## Requirements

- C compiler (e.g., GCC, clang, or MSVC)
- Windows console (if using `Sleep` from `windows.h`), or adjust/remove those calls for other platforms.
