import collections
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # Extract coordinates of all 1s in both images
        A = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        B = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Count the frequency of each translation vector
        translation_counts = collections.Counter()
        
        for r1, c1 in A:
            for r2, c2 in B:
                # Vector to translate (r1, c1) to (r2, c2)
                vec = (r2 - r1, c2 - c1)
                translation_counts[vec] += 1
                
        # Return the maximum overlap, or 0 if no 1s exist to overlap
        return max(translation_counts.values()) if translation_counts else 0