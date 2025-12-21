import time

# place X or O at chosen space and return edited grid
def place_XO(grid, choice, xo):
  for i in range(3):
    for j in range(3):
      if choice == grid[i][j]:
        if grid[i][j] != 'X' and grid[i][j] != 'O':
          grid[i][j] == xo
          break
        else:
          print("Position is occupied, try again!")
          break
      if choice > 9 or choice < 1:
          print("Invalid Choice, try again!")
  return grid

# print the grid
def print_grid(grid):
  print("-------------")
  for i in range(3):
    for j in range(3):
      print("|", grid[i][j], end=" ")
    print("|")
    print("-------------")

# prints the winner if any
def print_winner(grid):
  for i in range(3):
    for j in range(3):
      if (grid[0][j] == grid[1][j] == grid[2][j]):
        print(grid[0][j], "is the winner!")
        break
      elif (grid[i][0] == grid[i][1] == grid[i][2]):
        print(grid[i][0], "is the winner!")
        break
      elif (grid[0][0] == grid[1][1] == grid[2][2]):
        print(grid[0][0], "is the winner!")
      else:
        print("It's a DRAW!")

def main():

  game_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

  print("TIC-TAC-TOE")
  print("Loading", end="")
  for i in range(3):
    time.sleep(0.7)
    print(".", end="")
  time.sleep(0.7)
  print("\n\nBEGIN!")
  time.sleep(0.7)

  # Print the original grid
  print_grid(game_grid)

  # Place X or O at chosen space and print new grid
  count = 0
  xo = 'X'
  while (count < 9):
    if xo == 'X':
      choice = int(input("Place X at position: "))
      game_grid = place_XO(game_grid, choice, xo)
      if game_grid:
        print_grid(game_grid)
      else:
        print("Position is occupied, try again!")
      count += 1
      xo = 'O'

    elif xo == 'O':
      choice = int(input("Place O at position: "))
      game_grid = place_XO(game_grid, choice, xo)
      if game_grid:
        print_grid(game_grid)
      else:
        print("Position is occupied, try again!")
      count += 1
      xo = 'X'

  print_winner(game_grid)

if __name__ == "__main__":
  main()