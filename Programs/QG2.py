#initialize quasigroup board
def is_valid_quasigroup(board, m):
    for a in range(m):
        for b in range(m):
            for c in range(m):
                for d in range(m):
                    # add condition 1: a * b = c * d
                    if board[a][b] == board[c][d] and (a, b) != (c, d):
                        return False

                    # add condition 2: a * 312 b = c * 312 d
                    if board[a][b] == board[d][c] and (a, b) != (d, c):
                        return False
    return True

def forward_checking(board, m):
    empty_cell = find_empty_cell(board, m)
    if not empty_cell:
        return True  # return true if a solution is found
    
    row, col = empty_cell
    
    for num in range(m):
        if is_valid_move(board, m, row, col, num):
            board[row][col] = num
            if forward_checking(board, m):
                return True  # move to the next empty cell
            board[row][col] = -1  # if no solution is found, backtrack
    
    return False

def find_empty_cell(board, m):
    for row in range(m):
        for col in range(m):
            if board[row][col] == -1:
                return row, col
    return None

def is_valid_move(board, m, row, col, num):
    if num in board[row]:
        return False  # check row
    if num in [board[i][col] for i in range(m)]:
        return False  # check column
    return True

def solve_quasigroup(m):
    board = [[-1 for _ in range(m)] for _ in range(m)]
    if forward_checking(board, m):
        print("Solution Found:")
        for row in board:
            print(row)
    else:
        print("No solution found.")

m = 4 
solve_quasigroup(m)

