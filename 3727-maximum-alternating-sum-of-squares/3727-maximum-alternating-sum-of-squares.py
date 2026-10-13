class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        squares = [x * x for x in nums]
        squares.sort()
        n = len(squares)
        mid = n // 2
        return sum(squares[mid:]) - sum(squares[:mid])