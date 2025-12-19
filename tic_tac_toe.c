#include <stdio.h>
#include <windows.h>
#include <stdbool.h>

int place_XO(char xo, int choice, int array[][3], char new_array[][3]); // place X or O at the chosen place in the tic-tac-toe grid
void print_ttt(char array[][3]);  // print the edited tic-tac-toe grid after entering X or O
char winner(char array[][3]);     // check whether X or O is the winner 

void main() {
  printf("TIC-TAC-TOE\n");

  int arr[][3] =  {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};    // array (array 1) for chosing the block number
  char new_arr[][3] = {{'1', '2', '3'}, {'4', '5', '6'}, {'7', '8', '9'}}; // array in which X and O are updated according to the number of block chosen from array 1

  // Loading the game 
  printf("Loading");
  for (int i=3; i>0; i--) {
    Sleep(500);
    printf("%c", '.');
  }
  Sleep(500);
  printf("\n\nBEGIN!\n");
  Sleep(500);

  // Print initial grid
  printf("-------------\n");
  for (int i=0; i<3; i++) {
    for (int j=0; j<3; j++) {
      printf("| %d ", arr[i][j]);
    }
    printf("|");
    printf("\n-------------\n");
  }

  char xo = 'X';    // Either X or O (xo is a variable that stores the symbol X or O)
  int choice = 0;   // Choice of the position(block) in grid
  int count = 0;    // number of blocks replaced by X and O combined 
  while (count<9) {

    if (xo == 'X') { 
      Repeat_x:
      printf("Place X at position: ");
      scanf("%d", &choice);

      if (choice < 1 || choice > 9) {
        printf("Invalid Choice, try again!\n");
        goto Repeat_x;
      }

      if (place_XO(xo, choice, arr, new_arr) == 1) {
        printf("Position is occupied, try again!\n");
        goto Repeat_x;
      }

      print_ttt(new_arr);

      if (winner(new_arr)) {    // Checking if we have a winner already
        printf("The WINNER is %c!", winner(new_arr));
        break;
      }

      xo = 'O';   // switch xo from 'X' to 'O'

    }
    else if (xo == 'O') {
      Repeat_o:
      printf("Place O at position: ");
      scanf("%d", &choice);

      if (choice < 1 || choice > 9) {
        printf("Invalid Choice, try again!\n");
        goto Repeat_o;
      }

      if (place_XO(xo, choice, arr, new_arr) == 1) {
        printf("Position is occupied, try again!\n");
        goto Repeat_o;
      }
      print_ttt(new_arr);

      if (winner(new_arr)) {    // Checking if we have a winner already
        printf("The WINNER is %c!", winner(new_arr));
        break;
      }

      xo = 'X';   // switch xo from 'O' to 'X'
    }
    count++;
  }

  if (count == 9 && winner(new_arr) == '\0') {
    printf("It's a DRAW!");
  }

  printf("\nThank You for Playing!\n");
}

int place_XO(char xo, int choice, int array[][3], char new_array[][3]) {
  for (int i=0; i<3; i++) {
    for (int j=0; j<3; j++) {
      if (choice == array[i][j]) {
        if (new_array[i][j] != 'X' && new_array[i][j] != 'O') {
          new_array[i][j] = xo;
          return 0; // X or O is placed in position  
        }
        else {
          return 1; // position is not empty 
        }
      }
    }
  }
  return 1; // if error received
}
// Returns new_array

void print_ttt(char array[][3]) {
  printf("-------------\n");
  for (int i=0; i<3; i++) {
    for (int j=0; j<3; j++) {
      printf("| %c ", array[i][j]);
    }
    printf("|");
    printf("\n-------------\n");
  }
}
// Prints the elements of new_array in tic-tac-toe format

char winner(char array[][3]) {

  for (int i=0; i<3; i++) {
    if (array[i][0] == array[i][1] && array[i][1] == array[i][2]) {
      return array[i][0];
    }

    if (array[0][i] == array[1][i] && array[1][i] == array[2][i]) {
      return array[0][i];
    }
  }

  if (array[0][0] == array[1][1] && array[1][1] == array[2][2]) {
    return array[0][0];
  }
  return '\0';
}
// returns the whinning character 'X' or 'O' 