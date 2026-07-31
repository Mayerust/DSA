from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        sorted_freq = sorted(freq.values(), reverse=True)
        
        pushes = 0
        for i, count in enumerate(sorted_freq):
            cost_multiplier = (i // 8) + 1
            pushes += count * cost_multiplier
            
        return pushes