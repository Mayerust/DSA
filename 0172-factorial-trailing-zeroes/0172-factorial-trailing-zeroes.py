class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            count = 0
            while n > 0:
                n = n // 5
                count += n
            return count       
