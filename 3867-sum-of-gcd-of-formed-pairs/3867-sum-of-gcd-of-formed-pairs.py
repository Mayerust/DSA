from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_gcd = []
        mx = 0
        for x in nums:
            mx = max(mx, x)
            prefix_gcd.append(gcd(x, mx))
        
        prefix_gcd.sort()
        
        total = 0
        i, j = 0, n - 1
        while i < j:
            total += gcd(prefix_gcd[i], prefix_gcd[j])
            i += 1
            j -= 1
        
        return total