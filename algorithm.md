# 3. Intuition of the algorithm's operation
Having formulated the problem, I now design the algorithm for the QEP with 3 different levels of complexity based on their level of difficulty.  I describe the  algorithm I implemented and I provide an intuition on how it works for the QEPs I formulated previously. 

## 3.1 Overview of Each Algorithm

### 3.1.1 Backtracking
The backtracking algorithm is a recursion-based approach which uses brute force to find the desired output.  It attempts to incrementally build a solution, removing any solutions that fail to meet the constraints of the problem.  Backtracking can also be considered as an improvement over using brute force. The retracing method simply involves searching through all of the choices to find a solution to an issue.  

I begin the algorithm by choosing one possible option.  If the problem is solved with that option, I return the solution.  Else, I backtrack the algorithm and choose another option.  If none of the options gives the solution, then the algorithm will not return any  solution to that particular problem.  Until termination is reached, the process of selecting the best option is repeated recursively. 
 This removes the options that cannot return a solution and moves on to the options that might.

#### 3.1.1.1 Pseudocode of Backtracking
The algorithmic design can be defined as follows:

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
The branches of the search tree that will result in failure can be trimmed sooner using forward checking since it finds the discrepancy earlier than simple backtracking. This lessens the size of the search tree and, ideally, the total amount of labour.  According to Fahiem Bacchus et al., forward checking is a popular and successful alternative to backtracking.

#### 3.1.2.1 Pseudocode of Forward Checking
#### 3.1.2.2 Steps of Forward Checking

### 3.1.3 Donald Knuth's Dancing Links (DKDL) with Algorithm X
#### 3.1.3.1 Pseudocode of DKDL with Algorithm X
#### 3.1.3.2 Steps of DKDL with Algorithm X

[Read about the Performance Comparison.](https://github.com/wafaajaunnoo/solving-a-CSP/blob/main/performance-%20comparison.md)


