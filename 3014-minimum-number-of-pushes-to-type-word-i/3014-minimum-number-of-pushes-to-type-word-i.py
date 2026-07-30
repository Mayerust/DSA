class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        
        if n <= 8:
            return n
            
        full_cycles = n // 8
        remainder = n % 8
        
        pushes = 0
        for i in range(1, full_cycles + 1):
            pushes += 8 * i
            
        pushes += remainder * (full_cycles + 1)
        
        return pushes