import copy

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to evaluate the board
def evaluate(board):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    else:
        return 0

# Minimax algorithm
def minimax(board, depth, maximizing_player):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    elif board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move for AI
def find_best_move(board):
    best_move = None
    best_eval = float('-inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                eval = minimax(board, 0, False)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Main function to play the game
def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        # Player's move
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue
        board[row][col] = 'O'

        # Check if player wins
        if check_winner(board, 'O'):
            print("You win!")
            break

        # Check for a tie
        if board_full(board):
            print("It's a tie!")
            break

        # AI's move
        print("AI's move:")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = 'X'

        # Check if AI wins
        if check_winner(board, 'X'):
            print_board(board)
            print("AI wins!")
            break

        # Check for a tie
        if board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
