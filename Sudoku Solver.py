def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def is_valid_move(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board):
    row, col = find_empty_location(board)
    if row is None:
        return True
    
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    
    return False

def get_user_input():
    board = []
    print("Enter the Sudoku puzzle row by row. Use 0 to represent empty cells.")
    for i in range(9):
        row = input(f"Enter row {i + 1} (9 numbers separated by spaces): ").split()
        row = [int(cell) for cell in row]
        board.append(row)
    return board

# Example usage:
user_board = get_user_input()

print("\nSudoku puzzle to solve:")
print_board(user_board)
print("\nSolving...\n")

if solve_sudoku(user_board):
    print("Sudoku solved:")
    print_board(user_board)
else:
    print("No solution exists.")
