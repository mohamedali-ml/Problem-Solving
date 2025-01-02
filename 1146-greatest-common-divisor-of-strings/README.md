# GCD of Strings

## Problem Description

The **Greatest Common Divisor (GCD) of Strings** is a problem where, given two strings `str1` and `str2`, the goal is to determine the largest string `S` such that:

1. Both `str1` and `str2` can be formed by repeating `S` multiple times.
2. `S` is the longest possible string satisfying the above condition.

---

## Algorithm Explanation

### Key Steps:
1. **Concatenation Check**: If `str1 + str2 != str2 + str1`, it is impossible for the strings to share a common divisor. In this case, return an empty string.
2. **GCD of Lengths**: Compute the GCD of the lengths of `str1` and `str2` using the Euclidean algorithm. The GCD length determines the size of the largest possible common divisor string.
3. **Substring Extraction**: The first `GCD length` characters of `str1` represent the largest common divisor string.

---

## Example Traces

### Example 1: `str1 = "ABCABC", str2 = "ABC"`

| Step                | Operation                                     | Result          |
|---------------------|-----------------------------------------------|-----------------|
| Concatenation Check | `"ABCABC" + "ABC" == "ABC" + "ABCABC"`        | True            |
| GCD of Lengths      | GCD of `len("ABCABC") = 6` and `len("ABC") = 3` | GCD = 3         |
| Substring Extraction| First 3 characters of `"ABCABC"`              | `"ABC"`         |

**Output**: `"ABC"`

---

### Example 2: `str1 = "ABABAB", str2 = "AB"`

| Step                | Operation                                     | Result          |
|---------------------|-----------------------------------------------|-----------------|
| Concatenation Check | `"ABABAB" + "AB" == "AB" + "ABABAB"`          | True            |
| GCD of Lengths      | GCD of `len("ABABAB") = 6` and `len("AB") = 2` | GCD = 2         |
| Substring Extraction| First 2 characters of `"ABABAB"`              | `"AB"`          |

**Output**: `"AB"`

---

### Example 3: `str1 = "LEET", str2 = "CODE"`

| Step                | Operation                                     | Result          |
|---------------------|-----------------------------------------------|-----------------|
| Concatenation Check | `"LEET" + "CODE" != "CODE" + "LEET"`          | False           |
| GCD of Lengths      | Not applicable                                | -               |
| Substring Extraction| Not applicable                                | -               |

**Output**: `""`

---

## Complexity Analysis

## Complexity Analysis

### Time Complexity
1. **Concatenation Check**: `O(len(str1) + len(str2))`
2. **GCD Calculation**: `O(log(min(len(str1), len(str2))))`
3. **Substring Extraction**: `O(len(str1))`

**Total Time Complexity**:  
`O(len(str1) + len(str2) + log(min(len(str1), len(str2))))`

### Space Complexity
- The algorithm uses constant extra space, i.e., `O(1)`.


---

## Code Implementation

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Finds the greatest common divisor (GCD) of two strings.
        
        Parameters:
        - str1 (str): The first input string.
        - str2 (str): The second input string.
        
        Returns:
        - str: The largest common divisor string, or an empty string if none exists.
        """
        def greatest_common_divisor(a, b):
            while b:
                a, b = b, a % b
            return a
        
        if str1 + str2 != str2 + str1:
            return ""
        
        gcd_length = greatest_common_divisor(len(str1), len(str2))
        return str1[:gcd_length]
