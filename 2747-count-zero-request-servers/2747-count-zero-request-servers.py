class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda l: l[1])
        sorted_queries = sorted((q, idx) for idx, q in enumerate(queries))
        ans = [0] * len(queries)
        server_counts = [0] * (n + 1)
        active_servers = 0
        log_idx_left = 0
        log_idx_right = 0
        num_logs = len(logs)
        for q, idx in sorted_queries:
            window_start = q - x
            window_end = q
            while log_idx_right < num_logs and logs[log_idx_right][1] <= window_end:
                s_id, t = logs[log_idx_right]
                if server_counts[s_id] == 0:
                    active_servers += 1
                server_counts[s_id] += 1
                log_idx_right += 1
            while log_idx_left < num_logs and logs[log_idx_left][1] < window_start:
                s_id, t = logs[log_idx_left]
                server_counts[s_id] -= 1
                if server_counts[s_id] == 0:
                    active_servers -= 1
                log_idx_left += 1
            ans[idx] = n - active_servers     
        return ans