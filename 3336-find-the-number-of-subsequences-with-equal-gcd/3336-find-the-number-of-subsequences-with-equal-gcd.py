class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        M = max(nums) + 1
        
        # dp[g1][g2] = # of ways to pick disjoint (seq1, seq2) from elements
        # seen so far where gcd(seq1)=g1, gcd(seq2)=g2
        # g=0 means the subsequence is currently empty
        dp = [[0] * M for _ in range(M)]
        dp[0][0] = 1
        
        for x in nums:
            new_dp = [[0] * M for _ in range(M)]
            for g1 in range(M):
                for g2 in range(M):
                    val = dp[g1][g2]
                    if val == 0:
                        continue
                    # Skip x
                    new_dp[g1][g2] = (new_dp[g1][g2] + val) % MOD
                    # Add x to seq1
                    ng1 = math.gcd(g1, x)
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + val) % MOD
                    # Add x to seq2
                    ng2 = math.gcd(g2, x)
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + val) % MOD
            dp = new_dp
        
        return sum(dp[g][g] for g in range(1, M)) % MOD