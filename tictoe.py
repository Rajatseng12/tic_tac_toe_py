# Define the Tic Tac Toe board
board = [" " for _ in range(9)]

def print_board(board):
    # Print the Tic Tac Toe board
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
        if row != board[6:]:
            print("---------")

def check_winner(board, player):
    # Check for a win on the board
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    # Check for a draw
    return " " not in board

def make_move(board, position, player):
    # Make a move on the board
    if board[position] == " ":
        board[position] = player
        return True
    return False

def reset_board():
    # Reset the board for a new game
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
                move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
                if move < 0 or move >= 9:
                    print("Invalid move. Please enter a number between 1 and 9.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            if not make_move(board, move, current_player):
                print("This position is already taken. Try again.")
                continue
            
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if check_draw(board):
                print_board(board)
                print("It's a draw!")````````````````````````````````````````````````````````````
                break
            
            current_player = "O" if current_player == "X" else "X"
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Start the game
tic_tac_toe()
