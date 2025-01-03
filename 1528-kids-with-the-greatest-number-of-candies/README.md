# Kids With Candies

## Problem Description

Given a list of integers representing the number of candies each kid has, and an integer representing extra candies, determine which kids could have the greatest number of candies after receiving the extra candies. Return a boolean list where `True` means the kid can have the most candies and `False` means they cannot.

---

## Examples and Traces

### Example 1: `candies = [2, 3, 5, 1, 3], extraCandies = 3`

| Kid | Candies Before | Candies After Adding Extra | Max Candies | Result |
|-----|----------------|----------------------------|-------------|--------|
| 1   | 2              | 2 + 3 = 5                 | 5           | True   |
| 2   | 3              | 3 + 3 = 6                 | 5           | True   |
| 3   | 5              | 5 + 3 = 8                 | 5           | True   |
| 4   | 1              | 1 + 3 = 4                 | 5           | False  |
| 5   | 3              | 3 + 3 = 6                 | 5           | True   |

**Output**: `[True, True, True, False, True]`

---

### Example 2: `candies = [4, 2, 1, 1, 2], extraCandies = 1`

| Kid | Candies Before | Candies After Adding Extra | Max Candies | Result |
|-----|----------------|----------------------------|-------------|--------|
| 1   | 4              | 4 + 1 = 5                 | 4           | True   |
| 2   | 2              | 2 + 1 = 3                 | 4           | False  |
| 3   | 1              | 1 + 1 = 2                 | 4           | False  |
| 4   | 1              | 1 + 1 = 2                 | 4           | False  |
| 5   | 2              | 2 + 1 = 3                 | 4           | False  |

**Output**: `[True, False, False, False, False]`

---

### Example 3: `candies = [12, 1, 12], extraCandies = 10`

| Kid | Candies Before | Candies After Adding Extra | Max Candies | Result |
|-----|----------------|----------------------------|-------------|--------|
| 1   | 12             | 12 + 10 = 22              | 12          | True   |
| 2   | 1              | 1 + 10 = 11               | 12          | False  |
| 3   | 12             | 12 + 10 = 22              | 12          | True   |

**Output**: `[True, False, True]`

---

## Complexity Analysis

### Time Complexity
1. **Finding Max Candies**: `O(n)` where `n` is the length of the `candies` list.
2. **Iterating Through the List**: `O(n)` to calculate the results for each kid.

**Total Time Complexity**: `O(n)`

### Space Complexity
- The algorithm uses a list `result` to store boolean values for each kid, which takes `O(n)` space.
- Additional space for temporary variables is constant: `O(1)`.

**Total Space Complexity**: `O(n)`

---

## How to Use

1. Clone the repository.
2. Include the `Solution` class in your project.
3. Call the `kidsWithCandies` method with a list of candies and the extra candies value.

### Example Usage:
```python
sol = Solution()
candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(sol.kidsWithCandies(candies, extraCandies))
# Output: [True, True, True, False, True]
