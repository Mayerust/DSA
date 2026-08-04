class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        result = []
        for i in range(min(seen), (max(seen) + 1)):
            if (i) not in seen:
                result.append(i)
        return result              