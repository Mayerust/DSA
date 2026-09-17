class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 3:
            if sum(nums) != 0:
                return []
            else:
                return [nums]    
        elif len(nums) < 3:
            return []
        else:
            nums.sort()
            result = [] 
            for i in range (len(nums) - 2):
                left = i + 1
                right = len(nums) - 1
                if i > 0 and nums[i] == nums[i - 1]: 
                        continue
                while left < right:     
                    total = nums[i] + nums[left] + nums[right]
                    if total > 0:
                        right -= 1
                    elif total < 0:
                        left += 1
                    else:
                        result.append([nums[i], nums[left], nums[right]]) 
                        left += 1
                        right -= 1               
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right = right - 1
        return result               
                  