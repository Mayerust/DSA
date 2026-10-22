from collections import deque

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        init_t, init_s = -1, -1
        if all(nums[i] == (i + nums[0]) % n for i in range(n)):
            init_t, init_s = 0, nums[0]
        else:
            shift = (n - 1 - nums[0]) % n
            if all(nums[i] == n - 1 - ((i + shift) % n) for i in range(n)):
                init_t, init_s = 1, shift
        if init_t == -1:
            return -1
        target = (0, 0)
        if (init_t, init_s) == target:
            return 0
        visited = [[False] * n for _ in range(2)]
        queue = deque([(init_t, init_s, 0)])
        visited[init_t][init_s] = True
        while queue:
            t, s, d = queue.popleft()
            if (t, s) == target:
                return d
            nt, ns = t, (s + 1) % n
            if not visited[nt][ns]:
                visited[nt][ns] = True
                queue.append((nt, ns, d + 1))
            nt, ns = 1 - t, (n - s) % n
            if not visited[nt][ns]:
                visited[nt][ns] = True
                queue.append((nt, ns, d + 1))
                
        return -1