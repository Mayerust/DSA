class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            s = str(x)
            arr = list(map(int, s))
            left = 0
            right = len(arr) - 1
            while left < right:
                if arr[left] == arr[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True        
