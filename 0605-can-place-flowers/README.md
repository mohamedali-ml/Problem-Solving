# Can Place Flowers

## Problem Description

You are given a flowerbed represented as a list of integers, where:
- `1` indicates a plot already planted with a flower.
- `0` indicates an empty plot.

You are also given an integer `n`, which represents the number of flowers you want to plant. Flowers cannot be planted in adjacent plots.

The task is to determine if it is possible to plant `n` flowers in the flowerbed without violating the no-adjacent-flowers rule.

---

## Approach

1. **Iterate Through the Flowerbed**: Traverse each plot in the flowerbed.
2. **Check Current Plot**: If the current plot is empty (`0`):
   - Check if the left plot is empty or if the current plot is at the beginning of the flowerbed.
   - Check if the right plot is empty or if the current plot is at the end of the flowerbed.
3. **Plant the Flower**: If both conditions are satisfied, plant a flower in the current plot (`set the value to 1`) and increment the count.
4. **Early Termination**: If the count of planted flowers equals or exceeds `n`, return `True`.
5. **Final Check**: If the loop completes and the count is less than `n`, return `False`.

---

## Complexity Analysis

### Time Complexity
- **Iteration**: The solution involves a single pass through the flowerbed.
- Complexity: \( O(\text{len}(flowerbed)) \).

### Space Complexity
- **Extra Storage**: No additional data structures are used, only variables for tracking count and conditions.
- Complexity: \( O(1) \).

---

## Examples and Traces

### Example 1: `flowerbed = [1, 0, 0, 0, 1], n = 1`

| Index | Current Plot | Left Plot | Right Plot | Can Plant | Action      | Updated Flowerbed | Count |
|-------|--------------|-----------|------------|-----------|-------------|-------------------|-------|
| 0     | 1            | N/A       | 0          | No        | Skip        | [1, 0, 0, 0, 1]   | 0     |
| 1     | 0            | 1         | 0          | No        | Skip        | [1, 0, 0, 0, 1]   | 0     |
| 2     | 0            | 0         | 0          | Yes       | Plant Flower | [1, 0, 1, 0, 1]   | 1     |
| 3     | 0            | 1         | 1          | No        | Skip        | [1, 0, 1, 0, 1]   | 1     |
| 4     | 1            | 0         | N/A        | No        | Skip        | [1, 0, 1, 0, 1]   | 1     |

**Output**: `True`

---

### Example 2: `flowerbed = [1, 0, 0, 0, 1], n = 2`

| Index | Current Plot | Left Plot | Right Plot | Can Plant | Action      | Updated Flowerbed | Count |
|-------|--------------|-----------|------------|-----------|-------------|-------------------|-------|
| 0     | 1            | N/A       | 0          | No        | Skip        | [1, 0, 0, 0, 1]   | 0     |
| 1     | 0            | 1         | 0          | No        | Skip        | [1, 0, 0, 0, 1]   | 0     |
| 2     | 0            | 0         | 0          | Yes       | Plant Flower | [1, 0, 1, 0, 1]   | 1     |
| 3     | 0            | 1         | 1          | No        | Skip        | [1, 0, 1, 0, 1]   | 1     |
| 4     | 1            | 0         | N/A        | No        | Skip        | [1, 0, 1, 0, 1]   | 1     |

**Output**: `False`

---

### Example 3: `flowerbed = [0, 0, 1, 0, 0, 1, 0], n = 2`

| Index | Current Plot | Left Plot | Right Plot | Can Plant | Action      | Updated Flowerbed | Count |
|-------|--------------|-----------|------------|-----------|-------------|-------------------|-------|
| 0     | 0            | N/A       | 0          | Yes       | Plant Flower | [1, 0, 1, 0, 0, 1, 0] | 1     |
| 1     | 0            | 1         | 1          | No        | Skip        | [1, 0, 1, 0, 0, 1, 0] | 1     |
| 2     | 1            | 0         | 0          | No        | Skip        | [1, 0, 1, 0, 0, 1, 0] | 1     |
| 3     | 0            | 1         | 0          | No        | Skip        | [1, 0, 1, 0, 0, 1, 0] | 1     |
| 4     | 0            | 0         | 1          | Yes       | Plant Flower | [1, 0, 1, 0, 1, 1, 0] | 2     |
| 5     | 1            | 0         | 0          | No        | Skip        | [1, 0, 1, 0, 1, 1, 0] | 2     |
| 6     | 0            | 1         | N/A        | No        | Skip        | [1, 0, 1, 0, 1, 1, 0] | 2     |

**Output**: `True`

---

## How to Use

### Code:
```python
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
        return count >= n
