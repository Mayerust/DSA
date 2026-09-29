from functools import cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        max_open = (m + n - 1) // 2
        @cache
        def dfs(r: int, c: int, open_count: int) -> bool:
            open_count += 1 if grid[r][c] == '(' else -1
            if open_count < 0 or open_count > max_open:
                return False
            if r == m - 1 and c == n - 1:
                return open_count == 0
            if r + 1 < m and dfs(r + 1, c, open_count):
                return True
            if c + 1 < n and dfs(r, c + 1, open_count):
                return True  
            return False
        return dfs(0, 0, 0)