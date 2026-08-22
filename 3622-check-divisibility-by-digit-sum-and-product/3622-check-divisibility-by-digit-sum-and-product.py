class Solution:
    def checkDivisibility(self, n: int) -> bool:
        #s = str(n)
        arr = list(map(int, str(n)))
        total = 0
        product = 1
        for i in arr:
            total += + i
            product *= i
        total_sum = total + product
        if n % total_sum == 0:
            return True
        else:
            return False         

        