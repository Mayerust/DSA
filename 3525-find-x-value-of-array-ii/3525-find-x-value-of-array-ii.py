class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        M = 1
        while M < n:
            M <<= 1

        tree_prod = [1] * (2 * M)
        tree_cnt = [0] * (2 * M * k)

        for i in range(n):
            v = nums[i] % k
            pos = M + i
            tree_prod[pos] = v
            tree_cnt[pos * k + v] = 1

        for pos in range(M - 1, 0, -1):
            left = pos << 1
            right = left | 1

            l_prod = tree_prod[left]
            r_prod = tree_prod[right]
            tree_prod[pos] = (l_prod * r_prod) % k

            p_base = pos * k
            l_base = left * k
            r_base = right * k

            for r in range(k):
                tree_cnt[p_base + r] = tree_cnt[l_base + r]

            for r in range(k):
                c = tree_cnt[r_base + r]
                if c:
                    rem = (l_prod * r) % k
                    tree_cnt[p_base + rem] += c

        def update(idx: int, val: int) -> None:
            v = val % k
            pos = M + idx
            tree_prod[pos] = v
            base = pos * k
            for r in range(k):
                tree_cnt[base + r] = 0
            tree_cnt[base + v] = 1

            pos >>= 1
            while pos > 0:
                left = pos << 1
                right = left | 1

                l_prod = tree_prod[left]
                r_prod = tree_prod[right]
                tree_prod[pos] = (l_prod * r_prod) % k

                p_base = pos * k
                l_base = left * k
                r_base = right * k

                for r in range(k):
                    tree_cnt[p_base + r] = tree_cnt[l_base + r]

                for r in range(k):
                    c = tree_cnt[r_base + r]
                    if c:
                        rem = (l_prod * r) % k
                        tree_cnt[p_base + rem] += c

                pos >>= 1

        def query(start: int, target_x: int) -> int:
            l = M + start
            r = M + n - 1

            left_nodes = []
            right_nodes = []

            while l <= r:
                if l % 2 == 1:
                    left_nodes.append(l)
                    l += 1
                if r % 2 == 0:
                    right_nodes.append(r)
                    r -= 1
                l >>= 1
                r >>= 1

            curr_prod = 1
            curr_cnt = [0] * k

            for node in left_nodes + list(reversed(right_nodes)):
                node_base = node * k
                node_prod = tree_prod[node]
                next_cnt = list(curr_cnt)

                for r_rem in range(k):
                    c = tree_cnt[node_base + r_rem]
                    if c:
                        rem = (curr_prod * r_rem) % k
                        next_cnt[rem] += c

                curr_prod = (curr_prod * node_prod) % k
                curr_cnt = next_cnt

            return curr_cnt[target_x]

        ans = []
        for idx, val, start, x in queries:
            update(idx, val)
            ans.append(query(start, x))

        return ans