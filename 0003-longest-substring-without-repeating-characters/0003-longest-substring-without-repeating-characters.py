class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = set()
        current_count = 0
        max_count = 0
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            right += 1
            current_count = right - left
            if current_count > max_count:
                max_count = current_count
        return max_count                 



   