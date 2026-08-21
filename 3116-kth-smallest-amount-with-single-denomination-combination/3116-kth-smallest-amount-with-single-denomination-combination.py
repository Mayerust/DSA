import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        filtered_coins = []
        for c in coins:
            if not any(c % fc == 0 for fc in filtered_coins):
                filtered_coins.append(c)
                
        n = len(filtered_coins)
        limit = filtered_coins[0] * k
        
        pos_lcms = []
        neg_lcms = []
        
        def dfs(idx, current_lcm, bits):
            if idx == n:
                if bits > 0:
                    if bits % 2 == 1:
                        pos_lcms.append(current_lcm)
                    else:
                        neg_lcms.append(current_lcm)
                return
            
            dfs(idx + 1, current_lcm, bits)
            
            next_lcm = math.lcm(current_lcm, filtered_coins[idx])
            if next_lcm <= limit:
                dfs(idx + 1, next_lcm, bits + 1)
                
        dfs(0, 1, 0)
        
        left, right = 1, limit
        while left < right:
            mid = (left + right) // 2
            cnt = 0
            for l in pos_lcms:
                cnt += mid // l
            for l in neg_lcms:
                cnt -= mid // l
                
            if cnt >= k:
                right = mid
            else:
                left = mid + 1
                
        return left