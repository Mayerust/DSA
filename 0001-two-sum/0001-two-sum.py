class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set(nums)
        i = 0
        while i < len(nums):
            if (target - nums[i]) in seen and i != nums.index((target - nums[i])):
                return ([i, nums.index((target - nums[i]))])
                break
            #elif target <= nums[i] and (nums[i] - target) in seen and i != nums.index((nums[i] - target)):
                #return ([i, nums.index((nums[i] -  target))])
                #break
            else:
                i += 1
                