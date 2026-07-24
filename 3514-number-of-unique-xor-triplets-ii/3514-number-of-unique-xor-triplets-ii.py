from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        has_pair = bytearray(4096)
        seen_triplet = bytearray(4096)
        
        valid_pairs = []
        for i in range(n - 1, -1, -1):
            ni = nums[i]
            for k in range(i, n):
                px = ni ^ nums[k]
                if not has_pair[px]:
                    has_pair[px] = 1
                    valid_pairs.append(px)
            for px in valid_pairs:
                seen_triplet[ni ^ px] = 1
        return sum(seen_triplet)