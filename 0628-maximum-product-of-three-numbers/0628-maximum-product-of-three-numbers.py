class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        elif len(nums) > 3:
            nums.sort()
            #max_product = None
            positive_product = 0
            negative_product = 0
            positive_product = nums[len(nums) - 1] * nums[len(nums) - 2] * nums[len(nums) - 3]
            if nums[0] and nums[1] < 0:
                negative_product = nums[0] * nums[1] * nums[len(nums) - 1]
            return max(positive_product, negative_product)    



