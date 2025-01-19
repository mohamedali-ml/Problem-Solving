class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev_cnt = cnt = 0
        max_length = 0
        
        if 0 not in nums: return len(nums)-1
        
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                
                if prev_cnt + cnt > max_length:
                    max_length = prev_cnt + cnt
                    
            else:
                prev_cnt = cnt
                cnt = 0
        
        return max_length