class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def backtrack(open_count: int, close_count: int, current: str):
            if len(current) == 2 * n:
                res.append(current)
                return
            if open_count < n:
                backtrack(open_count + 1, close_count, current + "(")
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current + ")")
        backtrack(0, 0, "")
        return res