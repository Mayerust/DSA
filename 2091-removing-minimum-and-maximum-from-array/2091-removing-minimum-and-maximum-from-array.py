class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_idx = max_idx = 0
        
        for k in range(1, n):
            if nums[k] < nums[min_idx]:
                min_idx = k
            if nums[k] > nums[max_idx]:
                max_idx = k
                
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)
        
        return min(j + 1, n - i, i + 1 + n - j)