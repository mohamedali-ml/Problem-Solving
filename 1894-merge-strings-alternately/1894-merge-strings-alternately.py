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
