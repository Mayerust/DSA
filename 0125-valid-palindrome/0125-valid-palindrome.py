class Solution(object):
    def isPalindrome(self, s):
        cleaned_string = "".join([char for char in s if char.isalnum()])
        small_cleaned_string = cleaned_string.lower()
        left = 0
        right = len(small_cleaned_string) - 1

        while left < right:
            if small_cleaned_string[left] == small_cleaned_string[right]:
                left = left + 1
                right = right - 1
            else:
                return False
        return True            