import heapq

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        left = []          
        right = []         
        left_sum = 0
        right_sum = 0
        left_cnt = 0
        right_cnt = 0
        del_left = {}
        del_right = {}
        target_left_size = (x + 1) // 2
        def prune(heap, del_map):
            while heap and del_map.get(heap[0], 0) > 0:
                val = heapq.heappop(heap)
                del_map[val] -= 1
        def add_num(val):
            nonlocal left_sum, right_sum, left_cnt, right_cnt
            if not left or val <= -left[0]:
                heapq.heappush(left, -val)
                left_sum += val
                left_cnt += 1
            else:
                heapq.heappush(right, val)
                right_sum += val
                right_cnt += 1
            rebalance()
        def remove_num(val):
            nonlocal left_sum, right_sum, left_cnt, right_cnt
            if left and val <= -left[0]:
                del_left[-val] = del_left.get(-val, 0) + 1
                left_sum -= val
                left_cnt -= 1
                prune(left, del_left)
            else:
                del_right[val] = del_right.get(val, 0) + 1
                right_sum -= val
                right_cnt -= 1
                prune(right, del_right)
            rebalance()
        def rebalance():
            nonlocal left_sum, right_sum, left_cnt, right_cnt
            while left_cnt > target_left_size:
                prune(left, del_left)
                val = -heapq.heappop(left)
                left_sum -= val
                left_cnt -= 1
                heapq.heappush(right, val)
                right_sum += val
                right_cnt += 1
            while left_cnt < target_left_size and right_cnt > 0:
                prune(right, del_right)
                val = heapq.heappop(right)
                right_sum -= val
                right_cnt -= 1
                heapq.heappush(left, -val)
                left_sum += val
                left_cnt += 1
            prune(left, del_left)
            prune(right, del_right)
        cost = [0] * n
        for i in range(n):
            add_num(nums[i])
            if i >= x:
                remove_num(nums[i - x])
            if i >= x - 1:
                median = -left[0]
                c = (left_cnt * median - left_sum) + (right_sum - right_cnt * median)
                cost[i] = c
        INF = float('inf')
        dp = [[INF] * n for _ in range(k + 1)]
        dp[0] = [0] * n
        for j in range(1, k + 1):
            min_prev = INF
            for i in range(n):
                if i - x >= 0:
                    min_prev = min(min_prev, dp[j - 1][i - x])
                elif j == 1 and i == x - 1:
                    min_prev = 0
                if i > 0:
                    dp[j][i] = dp[j][i - 1]
                if min_prev != INF and i >= x - 1:
                    dp[j][i] = min(dp[j][i], min_prev + cost[i])
        return dp[k][n - 1]