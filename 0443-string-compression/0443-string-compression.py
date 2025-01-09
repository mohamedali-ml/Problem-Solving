class Solution:
    def compress(self, c: list[str]) -> int:
        """
        Compresses the given list of characters `c` in place, using the following rules:
        - For each group of consecutive repeating characters in `c`:
            - Replace the group with the character followed by the count of repetitions.
            - If a character appears only once, it is not followed by a count.
        - The list is modified in place to contain the compressed version.
        - The function returns the length of the compressed list.

        Args:
            c (list[str]): The input list of characters to compress.

        Returns:
            int: The length of the compressed list.

        Example:
        Input: ['a', 'a', 'b', 'b', 'c', 'c', 'c']
        Output: 6 (list becomes ['a', '2', 'b', '2', 'c', '3'])

        Explanation of the algorithm:
        - Use two pointers: `r` (read pointer) to traverse the input list and `w` (write pointer)
          to overwrite the list in place with the compressed version.
        - For each group of consecutive repeating characters:
            - Count the number of repetitions using a nested loop.
            - Write the character to the position pointed by `w`.
            - If the count is greater than 1, write each digit of the count to subsequent positions
              in `w`.
        - Increment `r` and continue until all characters are processed.
        - Return `w`, which indicates the length of the compressed list.
        """
        n = len(c)
        if n == 0:
            return 0  # Edge case: empty input list
        w = 0  # Write pointer
        r = 0  # Read pointer
        
        while r < n:
            x = c[r]  # Current character
            cnt = 0  # Count of consecutive occurrences
            
            # Count how many times the current character repeats
            while r < n and c[r] == x:
                r += 1
                cnt += 1
            
            # Write the character to the compressed list
            c[w] = x
            w += 1
            
            # If the count is greater than 1, write the count as well
            if cnt > 1:
                for d in str(cnt):  # Convert the count to string to handle multi-digit counts
                    c[w] = d
                    w += 1
        
        return w  # The length of the compressed list
