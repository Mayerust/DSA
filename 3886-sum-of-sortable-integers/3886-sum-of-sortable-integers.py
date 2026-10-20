class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)         
        total_sum = 0
        for k in divisors:
            possible = True
            prev_max = -float('inf')
            for i in range(0, n, k):
                descents = 0
                block_min = float('inf')
                block_max = -float('inf')
                for j in range(k):
                    curr = nums[i + j]
                    nxt = nums[i + ((j + 1) % k)]
                    if curr > nxt:
                        descents += 1
                    if curr < block_min:
                        block_min = curr
                    if curr > block_max:
                        block_max = curr
                if descents > 1:
                    possible = False
                    break
                if block_min < prev_max:
                    possible = False
                    break   
                prev_max = block_max
            if possible:
                total_sum += k
        return total_sum