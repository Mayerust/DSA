class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 30
        for num in nums:
            for b in range(30):
                if (num & (1 << b)):
                    bit_counts[b] += 1
        max_nums = [0] * k
        for b in range(29, -1, -1):
            for i in range(min(k, bit_counts[b])):
                max_nums[i] |= (1 << b)
        ans = 0
        for num in max_nums:
            ans = (ans + num * num) % MOD
        return ans