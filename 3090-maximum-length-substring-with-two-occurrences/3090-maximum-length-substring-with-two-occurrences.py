class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        right = 0
        count = 0
        max_count = 0
        freq = {} 
        while right < len(s):
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] += 1
            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1
            count = (right + 1) - left
            max_count = max(count, max_count)
            right += 1    
        return max_count    

