<h2><a href="https://leetcode.com/problems/is-subsequence">392. Is Subsequence</a></h2><h3>Easy</h3><hr><p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code><em> if </em><code>s</code><em> is a <strong>subsequence</strong> of </em><code>t</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>A <strong>subsequence</strong> of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;<u>a</u>b<u>c</u>d<u>e</u>&quot;</code> while <code>&quot;aec&quot;</code> is not).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "abc", t = "ahbgdc"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "axc", t = "ahbgdc"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 100</code></li>
	<li><code>0 &lt;= t.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist only of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Suppose there are lots of incoming <code>s</code>, say <code>s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub></code> where <code>k &gt;= 10<sup>9</sup></code>, and you want to check one by one to see if <code>t</code> has its subsequence. In this scenario, how would you change your code?

# `isSubsequence` Method

## Function Description

### **Docstring**
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Determines if the string `s` is a subsequence of the string `t`.

        A subsequence is a sequence derived from another string by deleting 
        some or no elements without changing the order of the remaining elements.

        Args:
            s (str): The string to check as a subsequence.
            t (str): The string to check against.

        Returns:
            bool: True if `s` is a subsequence of `t`, False otherwise.

        Algorithm:
        - Use two pointers:
            - `sp` for traversing `s`.
            - `tp` for traversing `t`.
        - Move the `tp` pointer through `t`. If characters at `s[sp]` and `t[tp]`
          match, increment the `sp` pointer.
        - If the `sp` pointer reaches the end of `s`, return True, indicating
          all characters in `s` have been matched in `t`.
        - Otherwise, return False.
        """
# Tracing Examples for `isSubsequence`

## Example 1: `s = "abc"`, `t = "ahbgdc"`

### Trace Table

| Step | `sp` (Index of `s`) | `tp` (Index of `t`) | `s[sp]` | `t[tp]` | Match? | Action                       |
|------|----------------------|---------------------|---------|---------|--------|------------------------------|
| 1    | 0                    | 0                   | `'a'`   | `'a'`   | Yes    | Increment `sp` and `tp`      |
| 2    | 1                    | 1                   | `'b'`   | `'h'`   | No     | Increment `tp`               |
| 3    | 1                    | 2                   | `'b'`   | `'b'`   | Yes    | Increment `sp` and `tp`      |
| 4    | 2                    | 3                   | `'c'`   | `'g'`   | No     | Increment `tp`               |
| 5    | 2                    | 4                   | `'c'`   | `'d'`   | No     | Increment `tp`               |
| 6    | 2                    | 5                   | `'c'`   | `'c'`   | Yes    | Increment `sp` and `tp`      |

### Final Result
- `sp = 3`, which is the length of `s`.
- **Output**: `True`

---

## Example 2: `s = "axc"`, `t = "ahbgdc"`

### Trace Table

| Step | `sp` (Index of `s`) | `tp` (Index of `t`) | `s[sp]` | `t[tp]` | Match? | Action                       |
|------|----------------------|---------------------|---------|---------|--------|------------------------------|
| 1    | 0                    | 0                   | `'a'`   | `'a'`   | Yes    | Increment `sp` and `tp`      |
| 2    | 1                    | 1                   | `'x'`   | `'h'`   | No     | Increment `tp`               |
| 3    | 1                    | 2                   | `'x'`   | `'b'`   | No     | Increment `tp`               |
| 4    | 1                    | 3                   | `'x'`   | `'g'`   | No     | Increment `tp`               |
| 5    | 1                    | 4                   | `'x'`   | `'d'`   | No     | Increment `tp`               |
| 6    | 1                    | 5                   | `'x'`   | `'c'`   | No     | Increment `tp`               |
| 7    | 1                    | 6                   | -       | End     | -      | Exit loop                    |

### Final Result
- `sp = 1`, which is less than the length of `s`.
- **Output**: `False`

---

## Example 3: `s = ""`, `t = "ahbgdc"`

### Trace Table

| Step | `sp` (Index of `s`) | `tp` (Index of `t`) | `s[sp]` | `t[tp]` | Match? | Action                       |
|------|----------------------|---------------------|---------|---------|--------|------------------------------|
| 1    | 0                    | -                   | -       | -       | -      | No characters to process     |

### Final Result
- `sp = 0`, which is the length of `s`.
- **Output**: `True`

---

## Example 4: `s = "abc"`, `t = ""`

### Trace Table

| Step | `sp` (Index of `s`) | `tp` (Index of `t`) | `s[sp]` | `t[tp]` | Match? | Action                       |
|------|----------------------|---------------------|---------|---------|--------|------------------------------|
| 1    | 0                    | -                   | -       | -       | -      | No characters in `t`         |

### Final Result
- `sp = 0`, which is less than the length of `s`.
- **Output**: `False`
