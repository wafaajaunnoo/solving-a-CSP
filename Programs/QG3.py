class QuasigroupSolver:
    def __init__(self, m):
        self.m = m
        self.board = [[-1 for _ in range(m)] for _ in range(m)]
        self.solution = []

    def is_valid_quasigroup(self, a, b, c, d):
        # Check if a * b = c
        if self.board[a][b] != self.board[c][0]:
            return False
        
        # Check if a * b = c * d
        if self.board[a][b] != self.board[c][d]:
            return False
        
        # Check if a * 321 b = c * 321 d
        if self.board[a][b] != self.board[c][d] or self.board[b][a] != self.board[d][c]:
            return False
        
        return True

    def solve_quasigroup(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            self.solution = [row.copy() for row in self.board]
            return True
        
        row, col = empty_cell
        for num in range(self.m):
            self.board[row][col] = num
            if self.is_valid_quasigroup(row, col, row, col) and self.solve_quasigroup():
                return True
            self.board[row][col] = -1
        
        return False

    def find_empty_cell(self):
        for row in range(self.m):
            for col in range(self.m):
                if self.board[row][col] == -1:
                    return row, col
        return None

    def print_solution(self):
        if not self.solution:
            print("No solution found.")
        else:
            print("Solution Found:")
            for row in self.solution:
                print(row)


# Example usage:
m = 4  # Replace with the desired order of quasigroup
solver = QuasigroupSolver(m)
if solver.solve_quasigroup():
    solver.print_solution()
else:
    print("No solution found.")

