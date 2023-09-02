
# 5. Tests

To find the smallest runtime value, the following program was executed:

```python
list1 = [1.0029006004333496, 1.0026416778564453, 1.0026721954345703]
list1.sort()

print("Smallest runtime is:", list1[0])
```

When $m = 4 $, the runtime for each algorithm was as follows:
1. **Backtracking:** 1.0029006004333496 (no solution found)
2. **Forward Checking:** 1.0026416778564453
3. **Look Ahead:** 1.0026721954345703

**Conclusion:** When $m = 4 $, the forward checking algorithm was the fastest.

When $m = 10 $, the runtime for each algorithm was as follows:
1. **Backtracking:** 1.0072627067565918 (no solution found) 
2. **Forward Checking:** 1.0190763473510742 (solution found)
3. **Look Ahead:** 1.0045676231384277 (solution found)

**Conclusion:** When $m = 10 $, the Look Ahead algorithm was the fastest.

When $m = 15 $, the runtime for each algorithm was as follows:
1. **Backtracking:** 1.003654956817627 (no solution found) 
2. **Forward Checking:** 215.335275888443 (solution found)
3. **Look Ahead:**  1.0095722675323486 (solution found)

**Conclusion:** When $m = 15 $, the backtracking algorithm was the fastest.  However, it did not provide any solution.

When $m = 40 $, the runtime for each algorithm was as follows:
1. **Backtracking:** 8 minutes, the program returned `error: maximum recursion depth exceeded in comparison`
2. **Forward Checking:** 
3. **Look Ahead:** 1, the program returned `RecursionError: maximum recursion depth exceeded in comparison`

**Conclusion:** When $m = 40 $, the Look Ahead algorithm was the fastest, but did not provide a solution and returned an error.


