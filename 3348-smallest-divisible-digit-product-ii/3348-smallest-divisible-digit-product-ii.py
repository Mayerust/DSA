class Solution:
    _dp = None

    def smallestNumber(self, num: str, t: int) -> str:
        req2 = req3 = req5 = req7 = 0
        temp = t
        for p in (2, 3, 5, 7):
            cnt = 0
            while temp % p == 0:
                cnt += 1
                temp //= p
            if p == 2: req2 = cnt
            elif p == 3: req3 = cnt
            elif p == 5: req5 = cnt
            elif p == 7: req7 = cnt
            
        if temp > 1:
            return "-1"
            
        if Solution._dp is None:
            Solution._dp = [[None] * 30 for _ in range(47)]
            Solution._dp[0][0] = ""
            factors_dp = {
                2: (1, 0), 3: (0, 1), 4: (2, 0), 
                6: (1, 1), 8: (3, 0), 9: (0, 2)
            }
            
            for r2 in range(47):
                for r3 in range(30):
                    if r2 == 0 and r3 == 0:
                        continue
                    best = None
                    for d, (v2, v3) in factors_dp.items():
                        pr2 = max(0, r2 - v2)
                        pr3 = max(0, r3 - v3)
                        
                        if pr2 == r2 and pr3 == r3:
                            continue
                            
                        if Solution._dp[pr2][pr3] is not None:
                            cand = Solution._dp[pr2][pr3] + str(d)
                            cand = "".join(sorted(cand))
                            if best is None or len(cand) < len(best) or (len(cand) == len(best) and cand < best):
                                best = cand
                    Solution._dp[r2][r3] = best
                    
        dp = Solution._dp
        
        factors = {
            1: (0, 0, 0, 0), 2: (1, 0, 0, 0), 3: (0, 1, 0, 0),
            4: (2, 0, 0, 0), 5: (0, 0, 1, 0), 6: (1, 1, 0, 0),
            7: (0, 0, 0, 1), 8: (3, 0, 0, 0), 9: (0, 2, 0, 0)
        }
        
        N = len(num)
        pref2 = [0] * (N + 1)
        pref3 = [0] * (N + 1)
        pref5 = [0] * (N + 1)
        pref7 = [0] * (N + 1)
        
        z = N
        for i in range(N):
            if num[i] == '0':
                if z == N:
                    z = i
                pref2[i+1] = pref2[i]
                pref3[i+1] = pref3[i]
                pref5[i+1] = pref5[i]
                pref7[i+1] = pref7[i]
            else:
                c = int(num[i])
                v2, v3, v5, v7 = factors[c]
                pref2[i+1] = pref2[i] + v2
                pref3[i+1] = pref3[i] + v3
                pref5[i+1] = pref5[i] + v5
                pref7[i+1] = pref7[i] + v7
                
        if z == N:
            if pref2[N] >= req2 and pref3[N] >= req3 and pref5[N] >= req5 and pref7[N] >= req7:
                return num
                
        for i in range(min(N - 1, z), -1, -1):
            start_d = int(num[i]) + 1
            for d in range(start_d, 10):
                v2, v3, v5, v7 = factors[d]
                rem2 = max(0, req2 - pref2[i] - v2)
                rem3 = max(0, req3 - pref3[i] - v3)
                rem5 = max(0, req5 - pref5[i] - v5)
                rem7 = max(0, req7 - pref7[i] - v7)
                
                s23 = dp[rem2][rem3]
                L_min = len(s23) + rem5 + rem7
                max_len = N - 1 - i
                
                if L_min <= max_len:
                    pad = "1" * (max_len - L_min)
                    suffix = pad + s23 + "5" * rem5 + "7" * rem7
                    suffix = "".join(sorted(suffix))
                    return num[:i] + str(d) + suffix
                    
        L = N + 1
        while True:
            for d in range(1, 10):
                v2, v3, v5, v7 = factors[d]
                rem2 = max(0, req2 - v2)
                rem3 = max(0, req3 - v3)
                rem5 = max(0, req5 - v5)
                rem7 = max(0, req7 - v7)
                
                s23 = dp[rem2][rem3]
                L_min = len(s23) + rem5 + rem7
                max_len = L - 1
                
                if L_min <= max_len:
                    pad = "1" * (max_len - L_min)
                    suffix = pad + s23 + "5" * rem5 + "7" * rem7
                    suffix = "".join(sorted(suffix))
                    return str(d) + suffix
            L += 1