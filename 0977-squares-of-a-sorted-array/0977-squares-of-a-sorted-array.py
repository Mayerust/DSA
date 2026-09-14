class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        i = 0
        j = len(nums) - 1
        k = len(nums) - 1
        while 0 <= j < len(nums) and 0 <= k < len(nums) and i <= j:
            if abs(nums[i]) > abs(nums[j]):
                result[k] = nums[i] * nums[i]
                k -= 1
                i += 1
            else:
                result[k] = nums[j] * nums[j]   
                k -= 1
                j -= 1
        return result        