class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        rank_map = {val: rank for rank, val in enumerate(sorted(set(arr)), 1)}
        
  
        return [rank_map[num] for num in arr]