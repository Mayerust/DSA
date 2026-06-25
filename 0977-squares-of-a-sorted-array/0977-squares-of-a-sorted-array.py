class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        pos = (len(result) - 1)
        #n = len(nums) - 1
        while left <= right and pos >= 0:
            if abs(nums[left]) >= abs(nums[right]):
                #result.append(nums[left] * nums[left])
                result[pos] = nums[left] * nums[left]
                left = left + 1
                pos = pos - 1
            elif abs(nums[right]) >= abs(nums[left]):
                #result.append(nums[right] * nums[right])
                result[pos] = nums[right] * nums[right]
                right = right - 1
                pos = pos - 1
        #result.reverse()
        return result            