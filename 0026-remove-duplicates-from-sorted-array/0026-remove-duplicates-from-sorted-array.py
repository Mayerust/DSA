class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        
        while right < len(nums):
            if nums[right] == nums[left]:
                nums.pop(right)
                
            elif nums[right] > nums[left]:
                left = right
                right += 1
        return len(nums)            
