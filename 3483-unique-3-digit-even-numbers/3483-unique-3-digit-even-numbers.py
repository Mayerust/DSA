from itertools import permutations
from typing import List
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique_evens = set()
        for p in permutations(digits, 3):
            if p[0] != 0 and p[2] % 2 == 0:
                unique_evens.add(p)
                
        return len(unique_evens)