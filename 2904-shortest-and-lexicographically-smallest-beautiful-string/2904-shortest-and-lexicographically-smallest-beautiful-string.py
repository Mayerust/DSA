class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        best_str = ""
        l = 0
        ones = 0
        
        for r in range(len(s)):
            if s[r] == '1':
                ones += 1
                
            # When we have exactly k ones, shrink the window from the left
            while ones == k:
                curr = s[l:r+1]
                
                # Update best_str if we found a shorter valid substring,
                # or a same-length substring that is lexicographically smaller.
                if not best_str:
                    best_str = curr
                elif len(curr) < len(best_str):
                    best_str = curr
                elif len(curr) == len(best_str) and curr < best_str:
                    best_str = curr
                    
                if s[l] == '1':
                    ones -= 1
                l += 1
                
        return best_str