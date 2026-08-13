class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        left = 0
        right = k - 1
        curr_count = 0
        max_count = 0
        for i in range(k):
            if s[i] in vowels:
                curr_count += 1
                max_count = curr_count
        while right < len(s) - 1:
            if s[right + 1] in vowels:
                if s[left] in vowels:
                    left += 1
                    right += 1
                else:
                    curr_count += 1
                    left += 1
                    right += 1
                    if curr_count > max_count:
                        max_count = curr_count
            else:
                if s[left] in vowels:
                    curr_count -= 1
                    left += 1
                    right += 1
                    if curr_count > max_count:
                        max_count = curr_count
                else:
                    left += 1
                    right += 1     
        return max_count