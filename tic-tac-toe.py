# Define the Tic Tac Toe board as a list of 9 empty spaces
board = [" " for _ in range(9)]

def print_board(board):
    # Print the Tic Tac Toe board in a 3x3 grid format
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
        if row != board[6:]:
            print("---------")

def check_winner(board, player):
    # Check for a win on the board by verifying if the player has three in a row, column, or diagonal
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    # Check for a draw by verifying if all spaces on the board are filled
    return " " not in board

def make_move(board, position, player):
    # Make a move on the board by placing the player's mark at the specified position
    if board[position] == " ":
        board[position] = player
        return True
    return False

def reset_board():
    # Reset the board for a new game by reinitializing it with empty spaces
    global board
    board = [" " for _ in range(9)]

def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    while True:
        current_player = "X"
        reset_board()
        while True:
            print_board(board)
            try:
                # Prompt the current player to enter their move (1-9)
                move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
                if move < 0 or move >= 9:
                    print("Invalid move. Please enter a number between 1 and 9.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            # Check if the move is valid (i.e., the space is not already occupied)
            if not make_move(board, move, current_player):
                print("This position is already taken. Try again.")
                continue
            
            # Check for a win or draw after the move
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            
            # Switch the current player
            current_player = "O" if current_player == "X" else "X"
        
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Start the game
tic_tac_toe()