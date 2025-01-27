class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Initialize two frequency arrays of size 26 (for each letter in the alphabet)
        # to store the frequency of each character in word1 and word2.
        freq1 = [0] * 26
        freq2 = [0] * 26

        # Calculate the frequency of each character in word1.
        # ord(ch) - ord('a') maps 'a' to 0, 'b' to 1, ..., 'z' to 25.
        for ch in word1:
            freq1[ord(ch) - ord('a')] += 1

        # Calculate the frequency of each character in word2.
        for ch in word2:
            freq2[ord(ch) - ord('a')] += 1

        # Check if the two words contain the same set of characters.
        # If one word has a character that the other doesn't, they cannot be "close."
        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False

        # Sort the frequency arrays to compare the frequency distributions.
        # This allows us to check if the frequencies of characters can be swapped.
        freq1.sort()
        freq2.sort()

        # Compare the sorted frequency arrays.
        # If they are not identical, the words cannot be "close."
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False

        # If all checks pass, the words are "close."
        return True