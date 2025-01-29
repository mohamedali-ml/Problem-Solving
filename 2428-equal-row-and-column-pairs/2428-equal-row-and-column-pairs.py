from typing import List
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Dictionary to store the frequency of each row (converted to string)
        m = defaultdict(int)
        # Counter to keep track of equal row-column pairs
        cnt = 0

        # Iterate through each row in the grid
        for row in grid:
            # Convert row to a string and store its count in the dictionary
            m[str(row)] += 1

        # Iterate through each column in the grid
        for i in range(len(grid[0])):  # Number of columns
            col = []  # List to store column elements
            for j in range(len(grid)):  # Number of rows
                col.append(grid[j][i])  # Extract the i-th column element
            
            # Convert column to string and check if it exists in the dictionary
            # If it does, add its count to cnt
            cnt += m[str(col)]

        return cnt  # Return the total count of equal row-column pairs
