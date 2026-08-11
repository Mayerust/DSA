class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prev = nums[0]
        #max_sum = 0
        curr_sum = nums[0]
        #streak = 0
        #longest_streak = 0
        i = 1
        while i < len(nums):
            if nums[i] - prev == 1:
                curr_sum += nums[i]
                prev = nums[i]
                #streak += 1
                i += 1
            else:
                break

        result = curr_sum
        seen = set(nums)
        while True:
            if result in seen:
                result += 1
            else:
                return result      
                




                
            
