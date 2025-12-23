import time

# place X or O at chosen space and return edited grid if x or o could be placed. else it returns 0 along with appropriate message
def place_XO(grid, choice, xo):
  
  positions = { 1: (0,0), 2: (0,1), 3: (0,2),
                4: (1,0), 5: (1,1), 6: (1,2),
                7: (2,0), 8: (2,1), 9: (2,2)  }

  if choice in positions.keys():
    i, j = positions[choice]  # unpacking the tuples that are stored as values corresponding to the choice of key of the positions dictionary 
    
    if grid[i][j] != 'X' and grid[i][j] != 'O':
      grid[i][j] = xo
    else:
      print("Position is occupied, try again!")
      return 0
  
  else:
      print("Invalid Choice, try again!")
      return 0
  
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
def winner(grid):
  for x in range(3):
    if (grid[0][x] == grid[1][x] == grid[2][x]):
      return grid[0][x]
    elif (grid[x][0] == grid[x][1] == grid[x][2]):
      return grid[x][0]
    elif (grid[0][0] == grid[1][1] == grid[2][2]):
      return grid[0][0]
    else:
      return 0

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

  while True:
    xo = input("So who plays first? X or O\n").upper()
    if xo == 'X' or xo == 'O':
      break

  # Place X or O at chosen space and print new grid
  count = 0
  while (count < 9):
    while True:
      try:
        choice = int(input("Place X at position: "))
      except ValueError:
        print("Invalid Input! Enter a number between 1 and 9")
        continue

      test_grid = place_XO(game_grid, choice, xo)   # Test grid used to test if place_XO returns a grid or 0

      if test_grid != 0:        # if returned value is a grid then we later store it in game_grid else we dont
        game_grid = test_grid
        print_grid(game_grid)
        break

    if winner(game_grid) != 0:
      print("The winner is:", winner(game_grid))
      break

    if xo == 'X':
      xo = 'O'
    else:
      xo = 'X'

    count += 1      # Increment count by 1 after each iteration of while loop

  if winner(game_grid) == 0:
    print("It's a DRAW!")
  print("Thank you for playing!")

if __name__ == "__main__":
  main()