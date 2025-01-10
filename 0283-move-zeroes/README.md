<h2><a href="https://leetcode.com/problems/move-zeroes">283. Move Zeroes</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code>, move all <code>0</code>&#39;s to the end of it while maintaining the relative order of the non-zero elements.</p>

<p><strong>Note</strong> that you must do this in-place without making a copy of the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [0,1,0,3,12]
<strong>Output:</strong> [1,3,12,0,0]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you minimize the total number of operations done?

# Move Zeroes to the End of Array

## Problem Description
Given an integer array `nums`, the task is to move all zeroes to the end of the array while maintaining the relative order of the non-zero elements. The operation must be performed **in-place** without making a copy of the array.

---

## Code Explanation

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all zeroes in the list `nums` to the end while maintaining the relative
        order of non-zero elements. This is done in-place.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            None: The function modifies the list in place and does not return anything.

        Algorithm:
        1. Use two pointers:
            - `left`: Tracks the position to place the next non-zero element.
            - `right`: Traverses the array to find non-zero elements.
        2. Traverse the array with the `right` pointer:
            - If `nums[right]` is not zero:
                - Swap `nums[right]` with `nums[left]`.
                - Increment the `left` pointer.
        3. At the end of the traversal, all zeroes will be at the end of the list.

        Time Complexity: O(n), where n is the length of `nums`.
        Space Complexity: O(1), as the operation is done in-place.

        Example:
        Input: [0, 1, 0, 3, 12]
        Output: [1, 3, 12, 0, 0]
        """
        left = 0  # Pointer to the next position for a non-zero element.

        # Traverse the list using the `right` pointer.
        for right in range(len(nums)):
            if nums[right] != 0:
                # Swap the non-zero element at `right` with the element at `left`.
                nums[right], nums[left] = nums[left], nums[right]
                left += 1

        return nums
# Move Zeroes to the End of Array: Examples and Traces



---

## Example 1: Input `[0, 1, 0, 3, 12]`

### Initial State
- Input Array: `[0, 1, 0, 3, 12]`
- `left` pointer: 0
- `right` pointer: 0

### Step-by-Step Execution

| Step | `right` Pointer | `left` Pointer | Current Element | Action         | Array State         |
|------|------------------|----------------|-----------------|----------------|---------------------|
| 1    | 0                | 0              | 0               | No swap        | `[0, 1, 0, 3, 12]` |
| 2    | 1                | 0              | 1               | Swap           | `[1, 0, 0, 3, 12]` |
| 3    | 2                | 1              | 0               | No swap        | `[1, 0, 0, 3, 12]` |
| 4    | 3                | 1              | 3               | Swap           | `[1, 3, 0, 0, 12]` |
| 5    | 4                | 2              | 12              | Swap           | `[1, 3, 12, 0, 0]` |

### Final Output
- Array: `[1, 3, 12, 0, 0]`

---

## Example 2: Input `[0]`

### Initial State
- Input Array: `[0]`
- `left` pointer: 0
- `right` pointer: 0

### Step-by-Step Execution

| Step | `right` Pointer | `left` Pointer | Current Element | Action | Array State |
|------|------------------|----------------|-----------------|--------|-------------|
| 1    | 0                | 0              | 0               | No swap | `[0]`       |

### Final Output
- Array: `[0]`

---

## Example 3: Input `[4, 0, 5, 0, 6]`

### Initial State
- Input Array: `[4, 0, 5, 0, 6]`
- `left` pointer: 0
- `right` pointer: 0

### Step-by-Step Execution

| Step | `right` Pointer | `left` Pointer | Current Element | Action         | Array State         |
|------|------------------|----------------|-----------------|----------------|---------------------|
| 1    | 0                | 0              | 4               | Swap           | `[4, 0, 5, 0, 6]`  |
| 2    | 1                | 1              | 0               | No swap        | `[4, 0, 5, 0, 6]`  |
| 3    | 2                | 1              | 5               | Swap           | `[4, 5, 0, 0, 6]`  |
| 4    | 3                | 2              | 0               | No swap        | `[4, 5, 0, 0, 6]`  |
| 5    | 4                | 2              | 6               | Swap           | `[4, 5, 6, 0, 0]`  |

### Final Output
- Array: `[4, 5, 6, 0, 0]`

---

## Example 4: Input `[1, 2, 3, 0, 0]`

### Initial State
- Input Array: `[1, 2, 3, 0, 0]`
- `left` pointer: 0
- `right` pointer: 0

### Step-by-Step Execution

| Step | `right` Pointer | `left` Pointer | Current Element | Action         | Array State         |
|------|------------------|----------------|-----------------|----------------|---------------------|
| 1    | 0                | 0              | 1               | Swap           | `[1, 2, 3, 0, 0]`  |
| 2    | 1                | 1              | 2               | Swap           | `[1, 2, 3, 0, 0]`  |
| 3    | 2                | 2              | 3               | Swap           | `[1, 2, 3, 0, 0]`  |
| 4    | 3                | 3              | 0               | No swap        | `[1, 2, 3, 0, 0]`  |
| 5    | 4                | 3              | 0               | No swap        | `[1, 2, 3, 0, 0]`  |

### Final Output
- Array: `[1, 2, 3, 0, 0]`

---

## Complexity Analysis

### Time Complexity
- The algorithm processes each element in the array exactly once.
- **Time Complexity**: \( O(n) \), where \( n \) is the length of the array.

### Space Complexity
- The operation is performed in-place, with no additional memory used.
- **Space Complexity**: \( O(1) \).
