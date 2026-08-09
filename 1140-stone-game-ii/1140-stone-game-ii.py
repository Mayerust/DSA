class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        suffix_sums = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]
            
        memo = {}
        
        def solve(i, M):
            if i >= n:
                return 0
                
            if i + 2 * M >= n:
                return suffix_sums[i]
                
            if (i, M) in memo:
                return memo[(i, M)]
                
            min_bob_score = float('inf')
            
            for X in range(1, 2 * M + 1):
                min_bob_score = min(min_bob_score, solve(i + X, max(M, X)))
                
            memo[(i, M)] = suffix_sums[i] - min_bob_score
            return memo[(i, M)]
            
        return solve(0, 1)