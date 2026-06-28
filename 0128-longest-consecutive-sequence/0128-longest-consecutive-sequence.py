class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left = 0
        right = 1
        max_count = 1
        counter = 1
        if len(nums) == 0:
            return 0
        while right < len(nums):
            if nums[right] - nums[left] == 1:
                counter += 1
                left += 1
                right += 1
                if counter > max_count:
                    max_count = counter

            elif nums[right] - nums[left] == 0:
                left = left + 1
                right = right + 1

            elif nums[right] - nums[left] > 1:
                if counter > max_count:
                    max_count = counter
                    counter = 1
                    left += 1
                    right += 1  
                else:
                    counter = 1
                    left += 1
                    right += 1   
        return max_count