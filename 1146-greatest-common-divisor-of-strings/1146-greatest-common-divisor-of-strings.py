class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Finds the greatest common divisor (GCD) of two strings. The GCD of two strings
        is defined as the largest string that can divide both strings (i.e., the largest
        string `S` such that both `str1` and `str2` are concatenations of `S`).

        Parameters:
        ----------
        str1 : str
            The first input string.
        str2 : str
            The second input string.

        Returns:
        -------
        str
            The GCD string if it exists; otherwise, an empty string.

        Explanation:
        -----------
        1. The method first checks if `str1 + str2` equals `str2 + str1`. If not, there is no valid GCD,
           and the method returns an empty string. This ensures both strings can be repeatedly
           concatenated from a common divisor.
        
        2. A helper function, `greatest_common_divisor`, calculates the GCD of the lengths of the two 
           strings using the Euclidean algorithm.
        
        3. The method then slices the first string up to the length of the calculated GCD. This substring
           represents the largest common divisor string that can divide both input strings.

        Notes:
        -----
        - If `str1` and `str2` are not valid for a GCD (e.g., their concatenation orders don't match), 
          the result is an empty string.
        - The use of the Euclidean algorithm ensures efficient computation of the GCD for lengths.

        Example:
        -------
        Input: str1 = "ABCABC", str2 = "ABC"
        Output: "ABC"

        Input: str1 = "LEET", str2 = "CODE"
        Output: ""

        """
        def greatest_common_divisor(a, b):
            """Calculates the GCD of two integers using the Euclidean algorithm."""
            while b:
                a, b = b, a % b
            return a
        
        # Check if concatenated strings are compatible for GCD
        if str1 + str2 != str2 + str1:
            return ""
        
        # Calculate GCD of the lengths of the strings
        gcd_length = greatest_common_divisor(len(str1), len(str2))
        
        # Return the substring up to the GCD length
        return str1[:gcd_length]
