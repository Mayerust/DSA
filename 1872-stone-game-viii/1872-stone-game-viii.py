class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        pref = [0] * n
        pref[0] = stones[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + stones[i]
            
        dp = pref[-1]
        
        for i in range(n - 2, 0, -1):
            dp = max(dp, pref[i] - dp)
            
        return dp