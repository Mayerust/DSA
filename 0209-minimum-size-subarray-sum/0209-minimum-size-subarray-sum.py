class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        curr_count = None 
        curr_sum = 0
        min_count = len(nums) + 1
        while right < len(nums):
            curr_sum = curr_sum + nums[right]
            while curr_sum >= target:
                curr_count = (right + 1) - left
                min_count = min(curr_count, min_count)
                curr_sum -= nums[left]
                left += 1
            right += 1    
        if min_count == len(nums) + 1:
            return 0
        else:
            return min_count                

      


             

        