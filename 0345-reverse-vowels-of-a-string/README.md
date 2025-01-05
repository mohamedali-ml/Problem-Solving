<h2><a href="https://leetcode.com/problems/reverse-vowels-of-a-string">345. Reverse Vowels of a String</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code>, reverse only all the vowels in the string and return it.</p>

<p>The vowels are <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, and <code>&#39;u&#39;</code>, and they can appear in both lower and upper cases, more than once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;IceCreAm&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;AceCreIm&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>The vowels in <code>s</code> are <code>[&#39;I&#39;, &#39;e&#39;, &#39;e&#39;, &#39;A&#39;]</code>. On reversing the vowels, s becomes <code>&quot;AceCreIm&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;leetcode&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;leotcede&quot;</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> consist of <strong>printable ASCII</strong> characters.</li>
</ul>
# Reverse Vowels of a String

## Problem Description

Given a string `s`, reverse only the vowels of the string while keeping all other characters in their original positions.

### Definitions:
- Vowels are defined as `a, e, i, o, u` (both uppercase and lowercase).

---

## Algorithm Explanation

1. Convert the input string into a list of characters for easy swapping.
2. Use two pointers (`start` and `end`) initialized at the beginning and end of the list.
3. Iterate through the list until the `start` pointer is no longer less than the `end` pointer:
   - Move the `start` pointer forward until it points to a vowel.
   - Move the `end` pointer backward until it points to a vowel.
   - Swap the vowels at the `start` and `end` pointers.
   - Move both pointers inward and repeat.
4. Convert the modified list back into a string and return it.

---

## Examples and Traces

### Example 1: `s = "hello"`

| Step | Character Array       | Start Pointer | End Pointer | Swap Performed | Resultant Array       |
|------|------------------------|---------------|-------------|----------------|-----------------------|
| 1    | `['h', 'e', 'l', 'l', 'o']` | 0             | 4           | No             | `['h', 'e', 'l', 'l', 'o']` |
| 2    | `['h', 'e', 'l', 'l', 'o']` | 1             | 4           | Yes            | `['h', 'o', 'l', 'l', 'e']` |
| 3    | `['h', 'o', 'l', 'l', 'e']` | 2             | 3           | No             | `['h', 'o', 'l', 'l', 'e']` |

**Output**: `"holle"`

---

### Example 2: `s = "leetcode"`

| Step | Character Array         | Start Pointer | End Pointer | Swap Performed | Resultant Array        |
|------|--------------------------|---------------|-------------|----------------|------------------------|
| 1    | `['l', 'e', 'e', 't', 'c', 'o', 'd', 'e']` | 0             | 7           | No             | `['l', 'e', 'e', 't', 'c', 'o', 'd', 'e']` |
| 2    | `['l', 'e', 'e', 't', 'c', 'o', 'd', 'e']` | 1             | 7           | Yes            | `['l', 'e', 'e', 't', 'c', 'e', 'd', 'o']` |
| 3    | `['l', 'e', 'e', 't', 'c', 'e', 'd', 'o']` | 2             | 5           | Yes            | `['l', 'e', 'o', 't', 'c', 'e', 'd', 'e']` |
| 4    | `['l', 'e', 'o', 't', 'c', 'e', 'd', 'e']` | 3             | 4           | No             | `['l', 'e', 'o', 't', 'c', 'e', 'd', 'e']` |

**Output**: `"leotcede"`

---

### Example 3: `s = "aA"`

| Step | Character Array | Start Pointer | End Pointer | Swap Performed | Resultant Array |
|------|------------------|---------------|-------------|----------------|-----------------|
| 1    | `['a', 'A']`    | 0             | 1           | Yes            | `['A', 'a']`    |

**Output**: `"Aa"`

---

## Complexity Analysis

### Time Complexity
1. **Traversal**: The `start` and `end` pointers traverse the string, ensuring every character is visited at most once.  
   **Time Complexity**: \( O(n) \), where \( n \) is the length of the string.

### Space Complexity
1. **Conversion**: The string is converted into a character array for in-place modification.  
   **Space Complexity**: \( O(n) \), where \( n \) is the length of the string.

---

## How to Use

### Example Usage
```python
sol = Solution()
print(sol.reverseVowels("hello"))      # Output: "holle"
print(sol.reverseVowels("leetcode"))  # Output: "leotcede"
print(sol.reverseVowels("aA"))        # Output: "Aa"
