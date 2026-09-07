class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 + 7
        dp = [0] * 26
        total = 0
        
        for char in s:
            idx = ord(char) - ord('a')
            new_val = (total + 1) % mod
            total = (total + new_val - dp[idx]) % mod
            dp[idx] = new_val
            
        return total