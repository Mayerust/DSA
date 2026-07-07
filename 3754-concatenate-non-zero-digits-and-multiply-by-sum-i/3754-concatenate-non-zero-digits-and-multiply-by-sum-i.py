class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [int(d) for d in str(n) if d != '0']
        x = int(''.join(map(str, digits))) if digits else 0
        return x * sum(digits)