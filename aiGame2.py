import random

def display(board):
  print("\nCurrent board")
  for row in board:
    print("|".join(row))
    print("-" *9)

def check_winner(board, player):

    for row in board:
      if all(s==player for s in row):
        return True
    for col in range(3):
      if all(board[row][col] == player for row in range(3)):
        return True

    if all(board[i][i] == player for i in range(3) or all(board[i][2-i] == player for i in range(3))):
        return True
    return False

def is_full(board):

    return all(board[row][col] != " " for row in range(3) for col in range(3))

def random_agent_move(board):
  empty_cells = [(row,col) for row in range(3) for col in range(3) if board[row][col] == " "]
  return random.choice(empty_cells)

# Main game loop
def play_game():
    # Initialize the empty board
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe! You are 'X' and the Random Agent is 'O'.")
    display(board)

    while True:
        # Player move (X)
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column, separated by space, e.g., '0 1'): ").split())
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column numbers between 0 and 2.")

        display(board)

        # Check if the player wins
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break

        # Check for a draw
        if is_full(board):
            print("It's a draw!")
            break

        # Random Agent move (O)
        row, col = random_agent_move(board)
        board[row][col] = "O"
        print(f"Random Agent placed 'O' at ({row}, {col}).")
        display(board)

        # Check if the Random Agent wins
        if check_winner(board, "O"):
            print("Random Agent wins! Better luck next time.")
            break

        # Check for a draw
        if is_full(board):
            print("It's a draw!")
            break

# Run the game
play_game()
