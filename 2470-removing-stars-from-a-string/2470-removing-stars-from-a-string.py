class Solution:  # Define a class named Solution
    def removeStars(self, s: str) -> str:  # Define a method that takes a string 's' as input and returns a string
        ans = []  # Initialize an empty list to store characters of the final result
        
        for i in s:  # Iterate over each character in the input string 's'
            if i == '*':  # If the current character is '*'
                ans.pop()  # Remove the last character from the list (simulating backspace behavior)
            else:  # If the character is not '*'
                ans.append(i)  # Add the character to the list
        
        return "".join(ans)  # Convert the list of characters back into a string and return it
