class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        left = 0
        count = 1
        max_count = 1
        right = 1
        while right < len(nums):
            if nums[right] == nums[left] + 1:
                count += 1
                left += 1
                right += 1
                if count > max_count:
                    max_count = count
            elif nums[left] == nums[right]:
                left = left + 1
                right = right + 1

            else:
                if count > max_count:
                    max_count = count
                count = 1
                left += 1
                right += 1
        return max_count        
                        