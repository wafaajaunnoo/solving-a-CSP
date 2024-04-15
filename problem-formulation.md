# 2. Combinatorial Problem Formulation
<!--In Artificial Intelligence, the following steps are to be followed when solving problems:

1. Problem definition (specify inputs and acceptable solutions).
2. Problem analysis.
3. Knowledge representation (provide detailed information about the problem and define all possible techniques).
4. Problem-solving (selection of best technique(s)).
-->
I start this section by defining a Quasigroup Existence Problem [hereafter: QEP].  I follow with the simplification of the different levels of complexity, which I define as the *constraints* and *objectives*.  Later, I argue the rationale behind my choice to solve the Quasigroup Problem with:

1. The Backtracking Algorithm
2. The Forward Checking Algorithm
3. The Look Ahead Algorithm 

## 2.1 Quasigroup Existence Problem
A Latin square of dimension $m$ is an order $m$ quasigroup. This is a multiplication table using the notation $m \times m$ where each element appears exactly once in each row and column. A set and a binary multiplication operator $\times$ defined over this set can both be used to specify a quasigroup. The existence or non-existence of quasigroups with extra attributes and a specific size is determined by quasigroup existence issues. Given we have 2 relations, $\times 321$ and $\times 312$ by $a \times 321 b = c$ iff $c \times b=a$ and $a \times 312 b = c$ iff $b \times c=a$, we can formulate 3 QEPs with different levels of complexities:

### 2.1.1 QEP 1
At this stage, the problem is of order $m$ quasigroups for which if $a \times b = c$, $a \times b = c \times d$ and $a \times 321 b = c \times 321 d$ then $a=c$ and $b=d$.

#### 2.1.1.1 Constraints
1. Each element must appear precisely once in each row and column in order for the quasigroup to conform to the basic features of a Latin square (a quasigroup of order $m$).
2. $a \times b = c$ <!--The result of the multiplication operation between any two elements 'a' and 'b' should equal 'c'-->
3. $a \times b = c \times d$ <!--If 'a \times b' equals 'c', then 'a \times b' must also equal 'c \times d'.-->
4. $a \times 321 b = c \times 321 d$ <!--If 'a \times 321 b' equals 'c', then 'a \times 321 b' must also equal 'c \times 321 d'.-->
   
#### 2.1.1.1 Objectives
The main goal of the QG1 issue is to identify an order $m$ quasigroup that complies with the aforementioned restrictions. The general objective is to produce a quasigroup with components occurring precisely once in each row and column and a multiplication operation that meets the requirements.

### 2.1.2 QEP 2
At this stage, the problem is of order $m$ quasigroups for which if $a \times b = c \times d$ and $a \times 312 b = c \times 312 d$ then $a=c$ and $b=d$.

#### 2.1.2.1 Constraints
In addition to the characteristics of _QEP 1_, additional limitations are introduced:
1. $a \times b = c \times d$ <!--The result of the multiplication operation between any two elements 'a' and 'b' should equal the result of the multiplication operation between 'c' and 'd'.-->
2. $a \times 312 b = c \times 312 d$ <!--If 'a \times 312 b' equals 'c', then $a \times 312 b$ must also equal $c \times 312 d$.-->

#### 2.1.2.1 Objectives
Similar to _QEP 1_, finding an order $m$ quasigroup that meets all the restrictions is the main goal of _QEP 2_. The quasigroup should satisfy the newly proposed constraints as well as the fundamental Latin square features (each element occurs once in each row and column). The goal is to produce a Latin square in which the multiplication operation complies with these requirements.

### 2.1.3 QEP 3
At this stage, the problem becomes more complex as it consists of non-trivial algebraic operations.  The problem is of order $m$ quasigroups for which $(a \times b) \times (b \times a) = a$.

#### 2.1.3.1 Constraints
The main constraint is that for an order 'm' quasigroup, the result of the operation $(a \times b) \times (b \times a)$ must equal $a$.  To create a Latin square (quasigroup) that meets the algebraic constraint and the fundamental characteristics of a quasigroup is the fundamental challenge. 

#### 2.1.3.1 Objectives
1. The given algebraic constraint must be met by the quasigroup: $(a \times b) \times (b \times a) = a$.
2. Similar to _QEP 1_ and _QEP 2_, the quasigroup must abide by the basic characteristics of a Latin square (a quasigroup of order 'm'), which requires that each element appear precisely once in each row and column.
3. Reduce conflicts that result from multiplicative operations inside the quasigroup while still adhering to the main algebraic restriction.

## 2.2 Problem-solving
Using algorithms that reduce computation is necessary when solving any problem.  For this assignment, the QEPs are solved using algorithms that diversify on their levels of complexity, based on the levels of complexity of the QEPs.

In this assignment, I will solve _QEP 1_, _QEP2_, and _QEP 3_ with the following algorithms respectively:
1. The Backtracking Algorithm
2. The Forward Checking Algorithm
3. The Look Ahead Algorithm


### 2.2.1 Rationale of Algorithms
1. **_QEP 1_**: The level of complexity in this QEP only requires basic constraint fulfilment and not complicated algebraic operations.  By methodically investigating and filling in the quasigroup while making sure the given constraints are satisfied, the Backtracking algorithm, as proposed, seeks to discover a viable solution that satisfies these goals. The goal is to finish the full quasigroup and find out if there is a quasigroup with the specified order 'm' that satisfies the requirements.
2. **_QEP 2_**: This problem adds more limitations, but propagates them in a very simple way.  A more effective way to rule out possibilities is through forward checking.  This algorithm aids in effectively ruling out options while guaranteeing that the specified constraints are met.  It lowers the search space and propagates constraints forward to rapidly spot any inconsistencies.
3. **_QEP 3_**: _QEP 3_ is more complex than _QEP 1_ and _QEP 2_ because non-trivial algebraic procedures are involved. The Dancing Links method may be modified to effectively handle these algebraic limitations and is particularly helpful for addressing exact cover issues.

The varied levels of difficulty of the problem descriptions are matched with each algorithm proposal. Backtracking is appropriate for less complicated problems, Forward Checking adds some complexity but not too much, and Dancing Links with Algorithm X is appropriate for challenging problems with deep algebraic restrictions.


[Read about the algorithmic design for this QEP.](https://github.com/wafaajaunnoo/solving-a-CSP/blob/main/algorithm.md)


