# Algorithm design workbook

> Fill each design after implementation. The expected technique is fixed by the assignment. No solved algorithms are claimed in this workbook.

## Task 01 - Coin Removal

**Mandatory technique:** Greedy

**Problem:** A row of H/T coins: remove an H and flip original immediate neighbors, never close gaps.

**Interface:** `removeCoins(...)`

**Assumptions:** Original adjacency is fixed after a removal; no shifting

**Algorithm idea / pseudocode:** [REPLACE AFTER DESIGN]

**Why it is Greedy:** [REPLACE]

**Correctness argument:** [REPLACE]

**Time:** `O([derive from code])` - [explain]

**Auxiliary space:** `O([derive from code])` - [explain]

**3+ executable test inputs:** `examples/inputs/task_01.json` (draft cases)

**Actual screenshots:** `report/assets/screenshots/task_01/`


## Task 02 - Domino Tiling

**Mandatory technique:** Brute Force

**Problem:** n x n board with two missing squares of opposite chessboard colors.

**Interface:** `tileDominoes(...)`

**Assumptions:** Return each domino as a pair of adjacent cells; input PDF notation is under-specified

**Algorithm idea / pseudocode:** [REPLACE AFTER DESIGN]

**Why it is Brute Force:** [REPLACE]

**Correctness argument:** [REPLACE]

**Time:** `O([derive from code])` - [explain]

**Auxiliary space:** `O([derive from code])` - [explain]

**3+ executable test inputs:** `examples/inputs/task_02.json` (draft cases)

**Actual screenshots:** `report/assets/screenshots/task_02/`


## Task 03 - Security Switches

**Mandatory technique:** Decrease and Conquer

**Problem:** All switches initially on; toggle rightmost or legal earlier switch to make all off in minimum moves.

**Interface:** `turnOffSwitches(...)`

**Assumptions:** Toggle indices are zero-based, rightmost=n-1

**Algorithm idea / pseudocode:** [REPLACE AFTER DESIGN]

**Why it is Decrease and Conquer:** [REPLACE]

**Correctness argument:** [REPLACE]

**Time:** `O([derive from code])` - [explain]

**Auxiliary space:** `O([derive from code])` - [explain]

**3+ executable test inputs:** `examples/inputs/task_03.json` (draft cases)

**Actual screenshots:** `report/assets/screenshots/task_03/`


## Task 04 - Point Coloring

**Mandatory technique:** Iterative Improvement

**Problem:** Color unique (x,y) points black/white, balancing every occupied x- and y-line.

**Interface:** `colorPoints(...)`

**Assumptions:** Equal x means vertical line; equal y means horizontal line

**Algorithm idea / pseudocode:** [REPLACE AFTER DESIGN]

**Why it is Iterative Improvement:** [REPLACE]

**Correctness argument:** [REPLACE]

**Time:** `O([derive from code])` - [explain]

**Auxiliary space:** `O([derive from code])` - [explain]

**3+ executable test inputs:** `examples/inputs/task_04.json` (draft cases)

**Actual screenshots:** `report/assets/screenshots/task_04/`


## Task 05 - King Arthur's Round Table

**Mandatory technique:** Dynamic Programming

**Problem:** Find a circular order so every adjacent pair are friends.

**Interface:** `seatKnights(...)`

**Assumptions:** Clarify whether friendship counts include self; self-entries ignored for adjacency

**Algorithm idea / pseudocode:** [REPLACE AFTER DESIGN]

**Why it is Dynamic Programming:** [REPLACE]

**Correctness argument:** [REPLACE]

**Time:** `O([derive from code])` - [explain]

**Auxiliary space:** `O([derive from code])` - [explain]

**3+ executable test inputs:** `examples/inputs/task_05.json` (draft cases)

**Actual screenshots:** `report/assets/screenshots/task_05/`


## Task 06 - Killing Squares

**Mandatory technique:** Dynamic Programming

**Problem:** Remove a minimum set of board toothpicks breaking every square of any size.

**Interface:** `breakAllSquares(...)`

**Assumptions:** A toothpick needs H/V orientation in addition to row and column; PDF signature is ambiguous

**Algorithm idea / pseudocode:** [REPLACE AFTER DESIGN]

**Why it is Dynamic Programming:** [REPLACE]

**Correctness argument:** [REPLACE]

**Time:** `O([derive from code])` - [explain]

**Auxiliary space:** `O([derive from code])` - [explain]

**3+ executable test inputs:** `examples/inputs/task_06.json` (draft cases)

**Actual screenshots:** `report/assets/screenshots/task_06/`


## Task 07 - Poisoned Wine

**Mandatory technique:** Divide and Conquer

**Problem:** Identify one poisoned barrel out of 1000 before the five-week feast with 10 and 8 testers.

**Interface:** `designWineTests(...)`

**Assumptions:** Because death is exactly 30 days after tasting, timed tasting days may add outcomes; document time assumptions

**Algorithm idea / pseudocode:** [REPLACE AFTER DESIGN]

**Why it is Divide and Conquer:** [REPLACE]

**Correctness argument:** [REPLACE]

**Time:** `O([derive from code])` - [explain]

**Auxiliary space:** `O([derive from code])` - [explain]

**3+ executable test inputs:** `examples/inputs/task_07.json` (draft cases)

**Actual screenshots:** `report/assets/screenshots/task_07/`


## Task 08 - Colored Tromino Tiling

**Mandatory technique:** Divide and Conquer

**Problem:** Tile a 2^n board with one missing square using non-overlapping L-trominoes and three colors.

**Interface:** `tileTromino(...)`

**Assumptions:** Tiles sharing a unit-length edge cannot have the same color

**Algorithm idea / pseudocode:** [REPLACE AFTER DESIGN]

**Why it is Divide and Conquer:** [REPLACE]

**Correctness argument:** [REPLACE]

**Time:** `O([derive from code])` - [explain]

**Auxiliary space:** `O([derive from code])` - [explain]

**3+ executable test inputs:** `examples/inputs/task_08.json` (draft cases)

**Actual screenshots:** `report/assets/screenshots/task_08/`
