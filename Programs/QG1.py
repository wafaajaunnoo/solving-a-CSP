# initialize quasigroup board
def is_valid_quasigroup(board, m):
    for a in range(m):
        for b in range(m):
            for c in range(m):
                for d in range(m):
                    if (board[a][b] == board[c][d] and 
                        board[a][b] != board[a][c] and 
                        board[a][b] != board[b][d] and 
                        board[a][b] != board[c][a] and 
                        board[a][b] != board[d][c]):
                        return False
    return True

def solve_quasigroup(m):
    board = [[-1 for _ in range(m)] for _ in range(m)]
    if backtrack(board, m, 0, 0):
        print("Solution Found:")
        for row in board:
            print(row)
    else:
        print("No solution found.")

def backtrack(board, m, row, col):
    if row == m:
        return True  # return true if a solution is found
    
    next_row, next_col = row, col + 1
    if next_col == m:
        next_row, next_col = row + 1, 0

    for num in range(m):
        board[row][col] = num
        if is_valid_quasigroup(board, m) and backtrack(board, m, next_row, next_col):
            return True  # move to next empty cell
    
    board[row][col] = -1  # if no solution is found, backtrack
    return False


m = 4  
solve_quasigroup(m)

