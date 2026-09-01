from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        K = 0
        litter_grid = [-1] * (m * n)
        grid = ""
        sx = sy = -1
        for i in range(m):
            grid += classroom[i]
            for j in range(n):
                c = classroom[i][j]
                if c == 'L':
                    litter_grid[i * n + j] = K
                    K += 1
                elif c == 'S':
                    sx, sy = i, j
        if K == 0:
            return 0
        target_mask = (1 << K) - 1
        MAX_MASK = 1 << K
        bestEnergy = [-1] * (m * n * MAX_MASK)
        start_pos = sx * n + sy
        bestEnergy[start_pos * MAX_MASK] = energy       
        queue = deque([(start_pos, 0, energy)])
        steps = 0
    
        adj = [[] for _ in range(m * n)]
        for i in range(m):
            for j in range(n):
                pos = i * n + j
                if grid[pos] == 'X':
                    continue
                if i > 0 and grid[pos - n] != 'X':
                    adj[pos].append(pos - n)
                if i < m - 1 and grid[pos + n] != 'X':
                    adj[pos].append(pos + n)
                if j > 0 and grid[pos - 1] != 'X':
                    adj[pos].append(pos - 1)
                if j < n - 1 and grid[pos + 1] != 'X':
                    adj[pos].append(pos + 1)
        while queue:
            steps += 1
            for _ in range(len(queue)):
                pos, mask, e = queue.popleft()
                if e < bestEnergy[pos * MAX_MASK + mask]:
                    continue
                for n_pos in adj[pos]:
                    n_mask = mask
                    l_idx = litter_grid[n_pos]
                    if l_idx != -1:
                        n_mask |= (1 << l_idx)
                    if n_mask == target_mask:
                        return steps
                    n_e = energy if grid[n_pos] == 'R' else e - 1
                    if n_e > 0:
                        n_idx = n_pos * MAX_MASK + n_mask
                        if n_e > bestEnergy[n_idx]:
                            bestEnergy[n_idx] = n_e
                            queue.append((n_pos, n_mask, n_e))
                                
        return -1