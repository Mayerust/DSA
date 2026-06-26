class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        curr_sum = 0.00000
        max_sum = None
        for i in range(k):
            curr_sum += nums[i]
            max_sum = curr_sum
            #return curr_sum -> got error so debuggibg :(
        if len(nums) == k:
            return curr_sum / k    
 
        else:        
            for i in range(k, len(nums)):
                curr_sum = curr_sum - nums[i - k] + nums[i]
                if curr_sum > max_sum:
                    max_sum = curr_sum
            return (max_sum / k)        