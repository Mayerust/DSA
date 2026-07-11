class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        for a, b in edges:
            union(a, b)
        
        node_count = Counter(find(i) for i in range(n))
        edge_count = Counter(find(a) for a, b in edges)
        
        return sum(
            1 for root, m in node_count.items()
            if edge_count[root] == m * (m - 1) // 2
        )