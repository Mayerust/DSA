class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        tree_sum = [0] * (4 * n)
        sum_c = [0] * (4 * n)
        lazy = [0] * (4 * n)
        def push(node, l, r):
            if lazy[node] != 0:
                val = lazy[node]
                mid = (l + r) // 2
                left_len = mid - l + 1
                tree_sum[2 * node] = (tree_sum[2 * node] + 2 * val * sum_c[2 * node] + val * val * left_len) % MOD
                sum_c[2 * node] = (sum_c[2 * node] + val * left_len) % MOD
                lazy[2 * node] = (lazy[2 * node] + val) % MOD
                right_len = r - mid
                tree_sum[2 * node + 1] = (tree_sum[2 * node + 1] + 2 * val * sum_c[2 * node + 1] + val * val * right_len) % MOD
                sum_c[2 * node + 1] = (sum_c[2 * node + 1] + val * right_len) % MOD
                lazy[2 * node + 1] = (lazy[2 * node + 1] + val) % MOD
                lazy[node] = 0
        def update(node, l, r, ql, qr, val):
            if ql > r or qr < l:
                return
            if ql <= l and r <= qr:
                length = r - l + 1
                tree_sum[node] = (tree_sum[node] + 2 * val * sum_c[node] + val * val * length) % MOD
                sum_c[node] = (sum_c[node] + val * length) % MOD
                lazy[node] = (lazy[node] + val) % MOD
                return
            push(node, l, r)
            mid = (l + r) // 2
            update(2 * node, l, mid, ql, qr, val)
            update(2 * node + 1, mid + 1, r, ql, qr, val)
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            sum_c[node] = (sum_c[2 * node] + sum_c[2 * node + 1]) % MOD
        last_occurrence = {}
        total_ans = 0
        for i, num in enumerate(nums):
            prev = last_occurrence.get(num, -1)
            last_occurrence[num] = i
            update(1, 0, n - 1, prev + 1, i, 1)
            total_ans = (total_ans + tree_sum[1]) % MOD    
        return total_ans