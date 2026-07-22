from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')
        blocks = []
        start = 0
        for i in range(1, n):
            if s[i] != s[start]:
                blocks.append((s[start], start, i - 1, i - start))
                start = i
        blocks.append((s[start], start, n - 1, n - start))
        
        M = len(blocks)
        block_idx = [0] * n
        for i, (b_type, b_start, b_end, b_len) in enumerate(blocks):
            block_idx[b_start : b_end + 1] = [i] * b_len
        G = [0] * M
        for i in range(1, M - 1):
            if blocks[i][0] == '1':
                G[i] = blocks[i - 1][3] + blocks[i + 1][3]
        st = [G]
        k = 1
        while (1 << k) <= M:
            step = 1 << (k - 1)
            prev = st[-1]
            next_col = [a if a > b else b for a, b in zip(prev[:-step], prev[step:])]
            st.append(next_col)
            k += 1
        ans = []
        for l, r in queries:
            idx_l = block_idx[l]
            idx_r = block_idx[r]
            if idx_l == idx_r or idx_l + 1 == idx_r:
                ans.append(total_ones)
                continue
            first_1 = idx_l + 1 if blocks[idx_l][0] == '0' else idx_l + 2
            last_1 = idx_r - 1 if blocks[idx_r][0] == '0' else idx_r - 2
            
            max_gain = 0
            
            if first_1 <= last_1:
                l_len = blocks[first_1 - 1][2] - l + 1 if (first_1 - 1) == idx_l else blocks[first_1 - 1][3]
                r_len = r - blocks[first_1 + 1][1] + 1 if (first_1 + 1) == idx_r else blocks[first_1 + 1][3]
                if l_len + r_len > max_gain:
                    max_gain = l_len + r_len
                    
                if first_1 < last_1:
                    l_len = blocks[last_1 - 1][2] - l + 1 if (last_1 - 1) == idx_l else blocks[last_1 - 1][3]
                    r_len = r - blocks[last_1 + 1][1] + 1 if (last_1 + 1) == idx_r else blocks[last_1 + 1][3]
                    if l_len + r_len > max_gain:
                        max_gain = l_len + r_len
                    if first_1 + 2 <= last_1 - 2:
                        L_q = first_1 + 2
                        R_q = last_1 - 2
                        length = R_q - L_q + 1
                        k_log = length.bit_length() - 1
                        
                        mx = max(st[k_log][L_q], st[k_log][R_q - (1 << k_log) + 1])
                        if mx > max_gain:
                            max_gain = mx
            ans.append(total_ones + max_gain)
            
        return ans