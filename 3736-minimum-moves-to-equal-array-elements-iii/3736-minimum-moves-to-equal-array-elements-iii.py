class Solution:
    def minMoves(self, nums: List[int]) -> int:
        target = max(nums)
        count = 0
        for i in range (len(nums)):
            if nums[i] < target:
                count += target - nums[i]
        return count        
    