class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
            
        first_half = []
        middle = ""
        for i in range(26):
            if freq[i] > 0:
                char = chr(i + ord('a'))
                if freq[i] % 2 == 1:
                    middle = char
                first_half.append(char * (freq[i] // 2))
        left_side = "".join(first_half)
        return left_side + middle + left_side[::-1]