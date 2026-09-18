class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
            
        valid_intervals = []
        for char in set(s):
            l = first[char]
            r = last[char]
            
            valid = True
            i = l
            while i <= r:
                if first[s[i]] < l:
                    valid = False
                    break
                r = max(r, last[s[i]])
                i += 1
                
            if valid:
                valid_intervals.append((l, r))
        valid_intervals.sort(key=lambda x: x[1])
        
        res = []
        last_r = -1
        
        for l, r in valid_intervals:
            if l > last_r:
                res.append(s[l : r + 1])
                last_r = r
                
        return res