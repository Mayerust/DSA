class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        max_val_left = [[0] * n for _ in range(n)]
        max_val_right = [[0] * n for _ in range(n)]

        for i in range(n):
            max_val_left[i][i] = stoneValue[i]
            max_val_right[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                mid = i
                while mid < j and (pref[mid + 1] - pref[i]) * 2 < pref[j + 1] - pref[i]:
                    mid += 1

                if mid > i:
                    dp[i][j] = max(dp[i][j], max_val_left[i][mid - 1])
                if mid < j and (pref[mid + 1] - pref[i]) * 2 == pref[j + 1] - pref[i]:
                    dp[i][j] = max(dp[i][j], max_val_left[i][mid])
                    dp[i][j] = max(dp[i][j], max_val_right[mid + 1][j])
                if mid < j:
                    if (pref[mid + 1] - pref[i]) * 2 == pref[j + 1] - pref[i]:
                        if mid + 2 <= j:
                            dp[i][j] = max(dp[i][j], max_val_right[mid + 2][j])
                    else:
                        dp[i][j] = max(dp[i][j], max_val_right[mid + 1][j])

                max_val_left[i][j] = max(
                    max_val_left[i][j - 1], dp[i][j] + pref[j + 1] - pref[i]
                )
                max_val_right[i][j] = max(
                    max_val_right[i + 1][j], dp[i][j] + pref[j + 1] - pref[i]
                )

        return dp[0][n - 1]
