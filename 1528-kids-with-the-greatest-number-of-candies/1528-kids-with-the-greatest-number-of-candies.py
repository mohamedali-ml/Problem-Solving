class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        Determines which kids will have the greatest number of candies
        after receiving extra candies.

        Parameters:
        - candies (List[int]): A list where each element represents the number 
          of candies each kid has.
        - extraCandies (int): The number of extra candies that can be given 
          to each kid.

        Returns:
        - List[bool]: A list of boolean values where each element indicates 
          whether the corresponding kid can have the greatest number of candies 
          among all kids if they are given the extra candies.

        Approach:
        1. Identify the maximum number of candies any kid currently has (`maxCandies`).
        2. For each kid, check if adding `extraCandies` to their current number of candies 
           results in a count that is greater than or equal to `maxCandies`.
        3. Append the result (True or False) to the `result` list.
        4. Return the `result` list.

        Example:
        >>> sol = Solution()
        >>> candies = [2, 3, 5, 1, 3]
        >>> extraCandies = 3
        >>> sol.kidsWithCandies(candies, extraCandies)
        [True, True, True, False, True]

        Explanation:
        - maxCandies = 5
        - After adding `extraCandies`:
          Kid 1: 2 + 3 = 5 (>= 5) -> True
          Kid 2: 3 + 3 = 6 (>= 5) -> True
          Kid 3: 5 + 3 = 8 (>= 5) -> True
          Kid 4: 1 + 3 = 4 (< 5)  -> False
          Kid 5: 3 + 3 = 6 (>= 5) -> True
        """
        # Find out the greatest number of candies among all the kids.
        maxCandies = max(candies)
        # For each kid, check if they will have greatest number of candies
        # among all the kids.
        result = []
        for i in range(len(candies)):            
            result.append(candies[i] + extraCandies >= maxCandies)
        return result
