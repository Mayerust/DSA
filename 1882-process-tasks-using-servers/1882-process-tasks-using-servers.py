import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        m = len(tasks)
        free_servers = [(servers[i], i) for i in range(n)]
        heapq.heapify(free_servers)
        busy_servers = []
        ans = [0] * m
        current_time = 0
        for j in range(m):
            current_time = max(current_time, j)
            while busy_servers and busy_servers[0][0] <= current_time:
                free_time, weight, idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, idx))
            if not free_servers:
                current_time = busy_servers[0][0]
                while busy_servers and busy_servers[0][0] <= current_time:
                    free_time, weight, idx = heapq.heappop(busy_servers)
                    heapq.heappush(free_servers, (weight, idx))
            weight, idx = heapq.heappop(free_servers)
            ans[j] = idx
            release_time = current_time + tasks[j]
            heapq.heappush(busy_servers, (release_time, weight, idx))
        return ans