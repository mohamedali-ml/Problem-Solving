class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Determine if `n` flowers can be planted in a flowerbed without violating the rule
        that no two flowers can be planted in adjacent plots.

        The flowerbed is represented as a list of integers:
        - `0` indicates an empty plot.
        - `1` indicates a plot with a flower.

        Rules for planting:
        - A flower can only be planted in a plot if both the left and right plots are empty
          (or if the plot is at the boundary of the flowerbed, only one adjacent plot needs to be empty).

        Args:
            flowerbed (List[int]): A list representing the flowerbed.
            n (int): The number of flowers to be planted.

        Returns:
            bool: `True` if it is possible to plant `n` flowers without violating the rules,
                  `False` otherwise.

        Approach:
        1. Iterate through each plot in the flowerbed.
        2. For each empty plot (`0`), check if the left and right plots are also empty:
           - If the plot is at the beginning or end of the flowerbed, only check the adjacent plot.
        3. If both conditions are satisfied, plant a flower (`set the plot to 1`) and increment the flower count.
        4. If the count of flowers planted meets or exceeds `n`, return `True`.
        5. If the loop completes and the count is less than `n`, return `False`.

        Time Complexity:
        - O(len(flowerbed)): We iterate through the flowerbed once.

        Space Complexity:
        - O(1): No extra data structures are used, only a constant amount of space.

        Example:
            flowerbed = [1, 0, 0, 0, 1], n = 1
            Output: True
            Explanation: A flower can be planted at index 2.

            flowerbed = [1, 0, 0, 0, 1], n = 2
            Output: False
            Explanation: Only one flower can be planted at index 2, so `n=2` is not possible.
        """
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    
        return count >= n
