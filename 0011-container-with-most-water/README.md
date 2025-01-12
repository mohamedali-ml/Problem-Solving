# 11. Container With Most Water

**Difficulty**: Medium

## Problem Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `iᵗʰ` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the **maximum amount of water a container can store**.

**Notice**: The container may not slant.

---

## Examples

### Example 1

![Example 1 Image](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

**Input**: `height = [1,8,6,2,5,4,8,3,7]`  
**Output**: `49`  
**Explanation**: The lines at indices `1` and `8` form a container with an area of `49`.

---

### Example 2

**Input**: `height = [1,1]`  
**Output**: `1`  

---

### Example 3

**Input**: `height = [4,3,2,1,4]`  
**Output**: `16`

---

### Example 4

**Input**: `height = [1,2,1]`  
**Output**: `2`

---

## Constraints

- \( n == \text{height.length} \)
- \( 2 \leq n \leq 10^5 \)
- \( 0 \leq \text{height}[i] \leq 10^4 \)

---

## Algorithm Explanation

### Approach: Two Pointers

This algorithm uses the **two-pointer technique** to find the maximum area efficiently.

### Steps:

1. **Initialization**:
   - Start with two pointers:
     - `left` at the start (`index 0`).
     - `right` at the end (`index len(height) - 1`).
   - Initialize `max_area` to store the maximum area found so far.

2. **Calculate Area**:
   - For each step, compute the area:
     \[
     \text{Area} = (\text{right} - \text{left}) \times \min(\text{height[left]}, \text{height[right]})
     \]
   - Update `max_area` with the larger of the current area and `max_area`.

3. **Move Pointers**:
   - Move the pointer pointing to the shorter line inward:
     - If `height[left] < height[right]`, increment `left`.
     - Otherwise, decrement `right`.

4. **Termination**:
   - Repeat until the `left` and `right` pointers meet.

5. **Return Result**:
   - Return the `max_area`.

---

## Complexity Analysis

- **Time Complexity**: \(O(n)\), since each pointer is moved at most \(n\) steps.
- **Space Complexity**: \(O(1)\), as only a few variables are used for computation.

---

## Implementation

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Calculates the maximum area of water that can be contained between two vertical lines,
        represented by the `height` array.

        Args:
            height (List[int]): An array of non-negative integers where each element
                                represents the height of a vertical line.

        Returns:
            int: The maximum area of water that can be contained.

        Example:
        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate current area
            area = (right - left) * min(height[left], height[right])
            # Update max_area
            max_area = max(max_area, area)

            # Move the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


