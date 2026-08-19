from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        masks = defaultdict(int)
        
        for row, seat in reservedSeats:
            if seat == 2 or seat == 3:
                masks[row] |= 1
            elif seat == 4 or seat == 5:
                masks[row] |= 3
            elif seat == 6 or seat == 7:
                masks[row] |= 6
            elif seat == 8 or seat == 9:
                masks[row] |= 4
                
        ans = 2 * n
        for mask in masks.values():
            if mask == 0:
                continue
            elif (mask & 1) == 0 or (mask & 2) == 0 or (mask & 4) == 0:
                ans -= 1
            else:
                ans -= 2
                
        return ans