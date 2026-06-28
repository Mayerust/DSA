class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                right += 1
            else:
                return True    
        return False        