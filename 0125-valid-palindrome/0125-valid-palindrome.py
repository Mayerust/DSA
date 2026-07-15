class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_clean = "".join(char for char in s if char.isalnum())
        str_lower = str_clean.lower()
        left = 0
        right = (len(str_lower)) - 1
        while left < right:
            if str_lower[left] == str_lower[right]:
                left += 1
                right -= 1
            else:
                return False    
        return True        