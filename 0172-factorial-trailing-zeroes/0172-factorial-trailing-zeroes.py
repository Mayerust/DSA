class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            fact = 1
            count = 0
            for i in range (n, 0,-1):
                fact *= i
        while fact % 10 == 0:
            count += 1
            fact = fact // 10
        return count    
