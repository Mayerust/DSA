class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k - 1
        max_sum = sum(nums[left:right+1])
        curr_sum = max_sum
        while right < len(nums) - 1:
            curr_sum = curr_sum - nums[left] + nums[right + 1]
            left += 1
            right += 1
            if curr_sum > max_sum:
                max_sum = curr_sum     
        return max_sum / k

        

        