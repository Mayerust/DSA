class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        sorted_pairs = sorted([(nums[i], i) for i in range(n)])
        
        components = []
        current_comp = [sorted_pairs[0]]
        
        for i in range(1, n):
            if sorted_pairs[i][0] - sorted_pairs[i-1][0] <= limit:
                current_comp.append(sorted_pairs[i])
            else:
                components.append(current_comp)
                current_comp = [sorted_pairs[i]]
                
        components.append(current_comp)
        
        res = [0] * n
        for comp in components:
            indices = sorted([p[1] for p in comp])
            vals = [p[0] for p in comp]
            
            for i in range(len(comp)):
                res[indices[i]] = vals[i]
                
        return res