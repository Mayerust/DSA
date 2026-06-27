class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left = 0
        right = 1
        counter = 1
        if len(nums) == 1:
            return nums[0]

        else:
            while right < len(nums) and left < len(nums):
                if nums[right] == nums[left]:
                    counter += 1
                    if counter > len(nums) / 2:
                        return nums[left]
                    else:
                        right = right + 1
                elif nums[right] != nums[left]:
                    if counter > len(nums) / 2:
                       return nums[left]
                    else:
                        left = right
                        right = right + 1
                        counter = 1



