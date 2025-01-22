class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Convert arrays to sets
        h1 = set(nums1)
        h2 = set(nums2)

        # Remove common elements
        for num in nums2:
            if num in h1:
                h1.remove(num)
                h2.discard(num)

        # Return the remaining unique elements
        return [list(h1), list(h2)]