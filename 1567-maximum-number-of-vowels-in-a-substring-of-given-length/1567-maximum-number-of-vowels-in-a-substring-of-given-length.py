class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Finds the maximum number of vowels in any substring of length `k` in the input string `s`.

        The algorithm uses a sliding window approach to efficiently calculate the number of vowels
        in each substring of length `k` without recomputing the entire count for overlapping substrings.

        Parameters:
        - s (str): The input string consisting of lowercase English letters.
        - k (int): The length of the substring to analyze.

        Returns:
        - int: The maximum number of vowels found in any substring of length `k`.

        Explanation:
        1. Initialize a set of vowels (`vowels = {'a', 'e', 'i', 'o', 'u'}`) for quick lookup.
        2. Use two pointers (`left` and `right`) to define the bounds of the sliding window.
        3. Calculate the initial number of vowels in the first `k` characters and store it in `maxVow`.
        4. Set `curr` to the initial vowel count. This variable tracks the current number of vowels in the sliding window.
        5. Start sliding the window one character at a time:
            - Remove the contribution of the character going out of the window (`s[left]`).
            - Add the contribution of the character entering the window (`s[right]`).
            - Update `maxVow` if the current vowel count (`curr`) is greater than the previous maximum.
        6. Continue moving the window until the end of the string is reached.
        7. Return the maximum number of vowels found (`maxVow`).

        Example:
        Input: s = "abciiidef", k = 3
        - Initial substring ("abc") has 1 vowel.
        - Sliding window: ("bci" -> "cii" -> "iid" -> "ide") finds a maximum of 3 vowels.
        Output: 3

        Time Complexity: O(n) where `n` is the length of the string `s`, as each character is processed once.
        Space Complexity: O(1) as the space used is constant regardless of input size.
        """
        vowels = set("aeiou") 
        maxVow = 0
        left, right = 0, k 

        for i in range(0, k):
            if s[i] in vowels:
                maxVow += 1

        curr = maxVow  
        while right < len(s):
            if s[left] in vowels:
                curr -= 1
            if s[right] in vowels:
                curr += 1
            maxVow = max(maxVow, curr)
            
            left += 1
            right += 1

        return maxVow
