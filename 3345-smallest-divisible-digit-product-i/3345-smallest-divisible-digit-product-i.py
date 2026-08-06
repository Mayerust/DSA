class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            digits = list(map(int, str(n)))
            product = None
            if len(digits) == 1:
                product = digits[0]
            elif len(digits) == 2:
                product = digits[0] * digits[1]
            elif len(digits) == 3:
                product = digits[0] * digits[1] * digits[2]           

            if product % t == 0:
                return n
            else:
                n += 1        
