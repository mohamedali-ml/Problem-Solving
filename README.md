# Problem-Solving
Problem Solving Repo

<!---LeetCode Topics Start-->
# LeetCode Topics
## Two Pointers
|  |
| ------- |
| [1894-merge-strings-alternately](https://github.com/mohamedali-ml/Problem-Solving/tree/master/1894-merge-strings-alternately) |
## String
|  |
| ------- |
| [1894-merge-strings-alternately](https://github.com/mohamedali-ml/Problem-Solving/tree/master/1894-merge-strings-alternately) |

```markdown
# Merge Alternately - Python Function

This Python function merges two strings alternately, character by character. If one string is longer, the remaining characters of the longer string are appended to the merged result.

---

## **Function Signature**
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merge two strings alternately, character by character.

        Args:
        word1 (str): The first input string.
        word2 (str): The second input string.

        Returns:
        str: A merged string formed by taking characters alternately from `word1` and `word2`.
             If one string is longer, the remaining characters from the longer string are appended.

        Example:
        >>> solution = Solution()
        >>> solution.mergeAlternately("abc", "pqr")
        'apbqcr'

        >>> solution.mergeAlternately("ab", "pqrs")
        'apbqrs'

        >>> solution.mergeAlternately("abcd", "pq")
        'apbqcd'
        """
        merged = []  # Initialize an empty list to store the merged characters.
        max_len = max(len(word1), len(word2))  # Find the length of the longer string.

        # Iterate up to the length of the longer string.
        for i in range(max_len):
            if i < len(word1):  # Add a character from `word1` if within bounds.
                merged += word1[i]
            if i < len(word2):  # Add a character from `word2` if within bounds.
                merged += word2[i]

        # Join the list of characters into a single string and return.
        return "".join(merged)

```

---

## **How It Works**
The function takes two input strings, `word1` and `word2`. Using a loop, it alternates characters from both strings to build the merged result. If one string is shorter, the remaining characters from the longer string are appended at the end.

---

## **Algorithm**
1. Calculate the length of the longer string.
2. Iterate through the indices up to the length of the longer string.
3. Add the character from `word1` at the current index if it exists.
4. Add the character from `word2` at the current index if it exists.
5. Combine the merged characters into a final string and return it.

---

## **Time and Space Complexity**
- **Time Complexity**: \(O(n + m)\), where \(n\) is the length of `word1` and \(m\) is the length of `word2`. The function processes each character of both strings once.
- **Space Complexity**: \(O(n + m)\), as the function stores the merged result in a list before converting it to a string.

---

## **Traced Examples**

### **Example 1**
**Input:**
```python
word1 = "abc"
word2 = "pqr"
```

**Execution Steps:**
| Step | `i` | `merged`         | Explanation                 |
|------|-----|------------------|-----------------------------|
| 1    | 0   | `['a']`          | Add `word1[0]` ('a')        |
| 2    | 0   | `['a', 'p']`     | Add `word2[0]` ('p')        |
| 3    | 1   | `['a', 'p', 'b']`| Add `word1[1]` ('b')        |
| 4    | 1   | `['a', 'p', 'b', 'q']` | Add `word2[1]` ('q') |
| 5    | 2   | `['a', 'p', 'b', 'q', 'c']` | Add `word1[2]` ('c') |
| 6    | 2   | `['a', 'p', 'b', 'q', 'c', 'r']` | Add `word2[2]` ('r') |

**Output:** `"apbqcr"`

---

### **Example 2**
**Input:**
```python
word1 = "ab"
word2 = "pqrs"
```

**Execution Steps:**
| Step | `i` | `merged`         | Explanation                 |
|------|-----|------------------|-----------------------------|
| 1    | 0   | `['a']`          | Add `word1[0]` ('a')        |
| 2    | 0   | `['a', 'p']`     | Add `word2[0]` ('p')        |
| 3    | 1   | `['a', 'p', 'b']`| Add `word1[1]` ('b')        |
| 4    | 1   | `['a', 'p', 'b', 'q']` | Add `word2[1]` ('q') |
| 5    | 2   | `['a', 'p', 'b', 'q', 'r']` | Add `word2[2]` ('r') |
| 6    | 3   | `['a', 'p', 'b', 'q', 'r', 's']` | Add `word2[3]` ('s') |

**Output:** `"apbqrs"`

---

### **Example 3**
**Input:**
```python
word1 = "abcd"
word2 = "pq"
```

**Execution Steps:**
| Step | `i` | `merged`         | Explanation                 |
|------|-----|------------------|-----------------------------|
| 1    | 0   | `['a']`          | Add `word1[0]` ('a')        |
| 2    | 0   | `['a', 'p']`     | Add `word2[0]` ('p')        |
| 3    | 1   | `['a', 'p', 'b']`| Add `word1[1]` ('b')        |
| 4    | 1   | `['a', 'p', 'b', 'q']` | Add `word2[1]` ('q') |
| 5    | 2   | `['a', 'p', 'b', 'q', 'c']` | Add `word1[2]` ('c') |
| 6    | 3   | `['a', 'p', 'b', 'q', 'c', 'd']` | Add `word1[3]` ('d') |

**Output:** `"apbqcd"`

---

## **Summary**
The `mergeAlternately` function provides an efficient and intuitive solution to merge two strings alternately. Its complexity ensures scalability, while the logic is easy to follow, making it suitable for real-world applications requiring string manipulation.
```
<!---LeetCode Topics End-->
