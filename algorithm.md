# 3. Intuition of the algorithm's operation
Having formulated the problem, I now design the algorithm for the QEP with 3 different levels of complexity based on their level of difficulty.  I describe the  algorithm I implemented and I provide an intuition on how it works for the QEPs I formulated previously. 

## 3.1 Overview of Each Algorithm

### 3.1.1 Backtracking
The backtracking algorithm is a recursion-based approach which uses brute force to find the desired output.  It attempts to incrementally build a solution, removing any solutions that fail to meet the constraints of the problem.  Backtracking can also be considered as an improvement over using brute force. The retracing method simply involves searching through all of the choices to find a solution to an issue.  

I begin the algorithm by choosing one possible option.  If the problem is solved with that option, I return the solution.  Else, I backtrack the algorithm and choose another option.  If none of the options gives the solution, then the algorithm will not return any  solution to that particular problem.  Until termination is reached, the process of selecting the best option is repeated recursively. 
 This removes the options that cannot return a solution and moves on to the options that might.

#### 3.1.1.1 Pseudocode of Backtracking
The algorithmic design for the backtracking algorithm can be defined as follows:

<p align="center">
<img width="573" alt="Algorithmic Design" src="/assets/algorithmic-design-QEP1.png">
</p>

#### 3.1.1.2 Steps of Backtracking
1. To represent the quasigroup, create a $m x m$ grid (2D array), where $m$ is the order of the quasigroup.
2. Set placeholder values (-1 or any unused value) in each cell of the grid.
3. Create a function that accepts the board of the quasigroup and its order $m$ as inputs.
4. Iterate through each cell on the board and check that each condition is met.
5. Return False if any of these tests are unsuccessful for any cell.
6. Return True to show that the quasigroup is legitimate if all requirements are met for all cells.
7. Create a recursive function that takes the board and $m$ as parameters.
8. Using the first function created, find the first empty cell on the quasigroup board inside this recursive function.
9. If a viable solution has been identified and there are no empty cells, return true.
10. Else, give a value to the current empty cell by iterating through the range of potential values (0 to m-1).
11. Determine whether the quasigroup is still valid after assigning a value.
12. Recursively call backtrack on the next empty cell if the quasigroup is still valid.
13. If the recursive call returns False, go back and test the following value after changing the cell's value to -1.
14. Return False if all potential values have been tested and none have produced a workable solution.

### 3.1.2 Forward Checking
The branches of the search tree that will result in failure can be trimmed sooner using forward checking since it finds the discrepancy earlier than simple backtracking. This lessens the size of the search tree and, ideally, the total amount of labour.  According to Roman Barták (1998), forward checking is the easiest way to prevent future conflicts as it detects inconsistency earlier than backtracking.

I begin the algorithm by checking if all the conditions are met for the quasigroup.  I apply recursive Depth-First Search (hereafter: DFS) to explore potential solutions while verifying the constraints and backtracking if a solution is incorrect.  The algorithm then identifies the first empty cell in the quasigroup.  It checks the validity of placing a number in a specific cell by checking that the number is not in the same row or column.  I then initialize the quasigroup board to solve the quasigroup.

#### 3.1.2.1 Pseudocode of Forward Checking
The algorithmic design for the Forward Checking algorithm can be defined as follows:

<p align="center">
<img width="573" alt="Algorithmic Design" src="/assets/algorithmic-design-QEP1.png">
</p>

#### 3.1.2.2 Steps of Forward Checking
1. Initialize the quasigroup board.
2. Create a function to determine if the quasigroup's current state complies with the requirements specified. It checks the following conditions by iterating over all possible cell pairings (a, b, c, and d):
   * For all pairs where (a, b)!= (c, d), $a * b = c * d$ is satisfied.
   * For all pairs where (a, b)!= (d, c), $a * 312 b = c * 312 d$ is true.
3. Return false if any condition fails for any pair of cells.
4. Return true if all conditions are met for all pairs of cells.
5. Create a function that uses recursive DFS to find potential solutions while verifying conditions and if backtracking is necessary.
6. Find the first empty cell.
7. If there are no empty cells, return true to indicate a successful solution.
8. Else, iterate through possible values (0 to m-1) to check for a valid move.
9. If recursion returned false, backtrack by resetting the cell's value to -1 and continuing the loop to check the next potential value.
10. Else, return true.

### 3.1.3 Look Ahead Algorithm
The Look Ahead Algorithm is a backtracking search technique that can be used to locate a valid quasigroup that satisfies ann conditions for order $m$.  The algorithm explores potential values for every cell in the quasigroup matrix and determines whether they adhere to the constraints or not.  If a value is suitable for a cell, the algorithm moves to the next empty cell.  Else, it backtracks and attempts to assign a new value.

I begin the algorithm by searching for the first empty cell in the quasigroup board.  Cells are given values starting at 0 and increasing up to m-1.  Before moving on to the next vacant cell, the algorithm determines if the value that was assigned fulfils the criteria.  It goes back to the previous cell and attempts a different value if there isn't a valid value entered.  The procedure is repeated until a comprehensive answer is discovered, at which point the answer is added to the solution matrix.  Repeating steps 3 through 6 allows the programme to locate every potential outcome.

#### 3.1.3.1 Pseudocode of Look Ahead Algorithm
The algorithmic design for the Look Ahead Algorithm can be defined as follows:

<p align="center">
<img width="573" alt="Algorithmic Design" src="/assets/algorithmic-design-QEP1.png">
</p>

#### 3.1.3.2 Steps of Look Ahead Algorithm
1. Initialize the quasigroup board with empty cells as an $m x m$ matrix.
2. Choose an empty cell and iterate through all potential solutions from 0 to $m - 1$.
3. Assign a value to the cell and check for the next empty cell.
4. For each assigned value, check if the solution satisfies all conditions.
5. Apply recursion to move to the next empty cell while assigning values and verifying that they satisfy all conditions.
6. If no value can be assigned, backtrack and attempt to assign a new value.
7. If a solution is found, store it in the solution matrix.
8. Repeat until all potential solutions are found.
9. When the process terminates, print the solution if a solution is found, else indicate that no solution is found.

[Read about the Performance Comparison.](https://github.com/wafaajaunnoo/solving-a-CSP/blob/main/performance-%20comparison.md)


