class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #nums.sort()
        #left = 0
        #right = 1
        #while right < len(nums):
            #if nums[left] != nums[right]:
                #left += 1
                #right += 1
            #else:
                #return True    
        #return False
        freq  = {}
        i = 0
        while i < len(nums):
            if nums[i] in freq:
                return True
            else:
                freq[nums[i]] = 1
                i = i + 1
        return False            
