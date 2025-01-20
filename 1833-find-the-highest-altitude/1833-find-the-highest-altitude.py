class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        Calculates the highest altitude reached during a journey based on altitude gains.

        This function takes a list of integers `gain`, where each element represents the net gain 
        or loss in altitude between consecutive points in a journey. It starts at an altitude of 0 
        and iteratively calculates the altitude at each point. The highest altitude encountered 
        during the journey is returned.

        Parameters:
        - gain (List[int]): A list of integers representing the net altitude changes 
          between consecutive points.

        Returns:
        - int: The maximum altitude reached during the journey.

        Approach:
        1. Initialize `maxAltitude` to 0, representing the highest altitude observed so far.
        2. Initialize `currentAltitude` to 0, representing the current altitude at any point in the journey.
        3. Iterate through the `gain` list:
           - Update `currentAltitude` by adding the current gain or loss (`g`).
           - Update `maxAltitude` to be the maximum of `maxAltitude` and `currentAltitude`.
        4. Return `maxAltitude` as the highest altitude reached during the journey.

        Example:
        Input: gain = [-5, 1, 5, 0, -7]
        - Starting altitude: 0
        - After 1st gain (-5): Altitude = -5
        - After 2nd gain (+1): Altitude = -4
        - After 3rd gain (+5): Altitude = 1 (highest so far)
        - After 4th gain (0): Altitude = 1
        - After 5th gain (-7): Altitude = -6
        Output: 1 (maximum altitude reached)

        Time Complexity: O(n) where `n` is the length of the `gain` list, as we process each element once.
        Space Complexity: O(1) as we use only a constant amount of additional space.
        """
        maxAltitude = 0
        currentAltitude = 0
        
        for g in gain:
            currentAltitude += g
            maxAltitude = max(maxAltitude, currentAltitude)
        
        return maxAltitude
