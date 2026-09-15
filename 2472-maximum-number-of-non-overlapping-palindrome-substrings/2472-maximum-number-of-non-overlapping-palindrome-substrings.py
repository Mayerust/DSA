class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        count = 0
        start = 0
        n = len(s)
        for i in range(k - 1, n):
            left_k = i - k + 1
            if left_k >= start:
                sub = s[left_k : i + 1]
                if sub == sub[::-1]:
                    count += 1
                    start = i + 1
                    continue 
            left_k_plus_1 = i - k
            if left_k_plus_1 >= start:
                sub = s[left_k_plus_1 : i + 1]
                if sub == sub[::-1]:
                    count += 1
                    start = i + 1
                    
        return count