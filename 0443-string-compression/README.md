<h2><a href="https://leetcode.com/problems/string-compression">443. String Compression</a></h2><h3>Medium</h3><hr><p>Given an array of characters <code>chars</code>, compress it using the following algorithm:</p>

<p>Begin with an empty string <code>s</code>. For each group of <strong>consecutive repeating characters</strong> in <code>chars</code>:</p>

<ul>
	<li>If the group&#39;s length is <code>1</code>, append the character to <code>s</code>.</li>
	<li>Otherwise, append the character followed by the group&#39;s length.</li>
</ul>

<p>The compressed string <code>s</code> <strong>should not be returned separately</strong>, but instead, be stored <strong>in the input character array <code>chars</code></strong>. Note that group lengths that are <code>10</code> or longer will be split into multiple characters in <code>chars</code>.</p>

<p>After you are done <strong>modifying the input array,</strong> return <em>the new length of the array</em>.</p>

<p>You must write an algorithm that uses only constant extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> chars = [&quot;a&quot;,&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;c&quot;,&quot;c&quot;,&quot;c&quot;]
<strong>Output:</strong> Return 6, and the first 6 characters of the input array should be: [&quot;a&quot;,&quot;2&quot;,&quot;b&quot;,&quot;2&quot;,&quot;c&quot;,&quot;3&quot;]
<strong>Explanation:</strong> The groups are &quot;aa&quot;, &quot;bb&quot;, and &quot;ccc&quot;. This compresses to &quot;a2b2c3&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> chars = [&quot;a&quot;]
<strong>Output:</strong> Return 1, and the first character of the input array should be: [&quot;a&quot;]
<strong>Explanation:</strong> The only group is &quot;a&quot;, which remains uncompressed since it&#39;s a single character.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> chars = [&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;]
<strong>Output:</strong> Return 4, and the first 4 characters of the input array should be: [&quot;a&quot;,&quot;b&quot;,&quot;1&quot;,&quot;2&quot;].
<strong>Explanation:</strong> The groups are &quot;a&quot; and &quot;bbbbbbbbbbbb&quot;. This compresses to &quot;ab12&quot;.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= chars.length &lt;= 2000</code></li>
	<li><code>chars[i]</code> is a lowercase English letter, uppercase English letter, digit, or symbol.</li>
</ul>
# String Compression

## Problem Description

The goal is to compress a list of characters in place by following these rules:
- For each group of consecutive repeating characters:
  - Replace the group with the character followed by the count of repetitions.
  - If a character appears only once, it is not followed by a count.
- The function modifies the input list in place and returns the new length of the compressed list.

---

## Algorithm Explanation

1. **Initialization**:
   - Use two pointers: 
     - `r` (read pointer) to traverse the input list.
     - `w` (write pointer) to overwrite the list with the compressed version.
   - Start both pointers at the beginning of the list.

2. **Traverse the List**:
   - For each group of consecutive repeating characters:
     - Use a nested loop to count the repetitions and increment the `r` pointer.
     - Write the current character at the position pointed by `w` and increment `w`.

3. **Handle Counts**:
   - If the count is greater than 1, write each digit of the count to the list at subsequent positions pointed by `w`, incrementing `w` for each digit.

4. **Return the Result**:
   - The value of `w` represents the length of the compressed list.

---

## Examples and Traces

### Example 1: Input `['a', 'a', 'b', 'b', 'c', 'c', 'c']`

| Step | Read Pointer (`r`) | Write Pointer (`w`) | Current Character | Count | Updated List           |
|------|---------------------|---------------------|-------------------|-------|------------------------|
| 1    | 0                  | 0                   | `'a'`             | 2     | `['a', '2', 'b', 'b', 'c', 'c', 'c']` |
| 2    | 2                  | 2                   | `'b'`             | 2     | `['a', '2', 'b', '2', 'c', 'c', 'c']` |
| 3    | 4                  | 4                   | `'c'`             | 3     | `['a', '2', 'b', '2', 'c', '3', 'c']` |

**Output**: `6`  
**Compressed List**: `['a', '2', 'b', '2', 'c', '3']`

---

### Example 2: Input `['a']`

| Step | Read Pointer (`r`) | Write Pointer (`w`) | Current Character | Count | Updated List |
|------|---------------------|---------------------|-------------------|-------|--------------|
| 1    | 0                  | 0                   | `'a'`             | 1     | `['a']`      |

**Output**: `1`  
**Compressed List**: `['a']`

---

### Example 3: Input `['a', 'a', 'a', 'b', 'b', 'a', 'a']`

| Step | Read Pointer (`r`) | Write Pointer (`w`) | Current Character | Count | Updated List           |
|------|---------------------|---------------------|-------------------|-------|------------------------|
| 1    | 0                  | 0                   | `'a'`             | 3     | `['a', '3', 'a', 'b', 'b', 'a', 'a']` |
| 2    | 3                  | 2                   | `'b'`             | 2     | `['a', '3', 'b', '2', 'b', 'a', 'a']` |
| 3    | 5                  | 4                   | `'a'`             | 2     | `['a', '3', 'b', '2', 'a', '2', 'a']` |

**Output**: `6`  
**Compressed List**: `['a', '3', 'b', '2', 'a', '2']`

---

## Complexity Analysis

### Time Complexity
- The algorithm processes each character exactly once:
  - Counting repetitions: \( O(n) \), where \( n \) is the length of the list.
  - Writing the compressed characters and counts: \( O(n) \).
- **Overall Time Complexity**: \( O(n) \).

### Space Complexity
- The algorithm uses constant extra space:
  - Two pointers and temporary variables.
- **Space Complexity**: \( O(1) \).

---

## How to Use

### Example Usage
```python
solution = Solution()
chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
length = solution.compress(chars)
print(length)  # Output: 6
print(chars[:length])  # Output: ['a', '2', 'b', '2', 'c', '3']

