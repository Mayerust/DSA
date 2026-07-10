class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # Sort node indices by value
        sorted_idx = sorted(range(n), key=lambda i: nums[i])
        sorted_vals = [nums[i] for i in sorted_idx]
        
        # pos[original_node] = its position in sorted order
        pos = [0] * n
        for i, idx in enumerate(sorted_idx):
            pos[idx] = i
        
        # R[i] = rightmost sorted position reachable from i in 1 step (two pointers)
        R = [0] * n
        r = 0
        for i in range(n):
            r = max(r, i)
            while r + 1 < n and sorted_vals[r + 1] - sorted_vals[i] <= maxDiff:
                r += 1
            R[i] = r
        
        # Binary lifting: jump[k][i] = furthest position reachable in 2^k steps
        LOG = 17
        jump = [R[:]]
        for k in range(1, LOG):
            prev = jump[k - 1]
            jump.append([prev[prev[i]] for i in range(n)])
        
        ans = []
        for u, v in queries:
            pu, pv = pos[u], pos[v]
            if pu > pv:
                pu, pv = pv, pu
            
            if pu == pv:
                ans.append(0)
                continue
            
            # Greedily jump as far right as possible without overshooting pv
            cur, steps = pu, 0
            for k in range(LOG - 1, -1, -1):
                if jump[k][cur] < pv:
                    cur = jump[k][cur]
                    steps += (1 << k)
            
            # One final jump needed to reach pv
            if jump[0][cur] >= pv:
                ans.append(steps + 1)
            else:
                ans.append(-1)
        
        return ans