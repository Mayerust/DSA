class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 1 or sum > num * 9:
            return ""  
        res = []
        curr_sum = sum
        for i in range(num):
            rem_slots = num - 1 - i
            d = min(9, curr_sum)
            res.append(str(d))
            curr_sum -= d
        return "".join(res)