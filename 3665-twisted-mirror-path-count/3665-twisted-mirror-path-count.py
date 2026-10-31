class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        go = [[[None, None] for _ in range(n)] for _ in range(m)]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                for direction in (0, 1):
                    nr = r + (1 if direction == 1 else 0)
                    nc = c + (1 if direction == 0 else 0)
                    if nr >= m or nc >= n:
                        go[r][c][direction] = None
                    elif grid[nr][nc] == 0:
                        go[r][c][direction] = (nr, nc)
                    else:
                        next_dir = 1 if direction == 0 else 0
                        go[r][c][direction] = go[nr][nc][next_dir]
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 or dp[r][c] == 0:
                    continue
                paths = dp[r][c]
                dest_r = go[r][c][0]
                if dest_r:
                    nr, nc = dest_r
                    dp[nr][nc] = (dp[nr][nc] + paths) % MOD
                dest_d = go[r][c][1]
                if dest_d:
                    nr, nc = dest_d
                    dp[nr][nc] = (dp[nr][nc] + paths) % MOD
        return dp[m - 1][n - 1]