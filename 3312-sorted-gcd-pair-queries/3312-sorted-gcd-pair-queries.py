from typing import List
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        maxVal = max(nums)
        
        
        cnt = [0] * (maxVal + 1)
        for x in nums:
            cnt[x] += 1
        
        
        countDivisible = [0] * (maxVal + 1)
        for d in range(1, maxVal + 1):
            s = 0
            for multiple in range(d, maxVal + 1, d):
                s += cnt[multiple]
            countDivisible[d] = s
        
        
        g = [0] * (maxVal + 1)
        for d in range(maxVal, 0, -1):
            c = countDivisible[d]
            total = c * (c - 1) // 2
            k = 2 * d
            while k <= maxVal:
                total -= g[k]
                k += d
            g[d] = total
        
        
        vals = []
        cum = []
        running = 0
        for d in range(1, maxVal + 1):
            if g[d] > 0:
                running += g[d]
                vals.append(d)
                cum.append(running)
        
        
        answer = []
        for q in queries:
            idx = bisect.bisect_right(cum, q)
            answer.append(vals[idx])
        
        return answer