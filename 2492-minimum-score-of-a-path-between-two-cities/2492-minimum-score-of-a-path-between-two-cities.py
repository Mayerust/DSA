from typing import List
from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        self.ans = float("inf")
        visited = set()

        def dfs(u):
            visited.add(u)
            for v, w in graph[u]:
                self.ans = min(self.ans, w)
                if v not in visited:
                    dfs(v)

        dfs(1)
        return self.ans