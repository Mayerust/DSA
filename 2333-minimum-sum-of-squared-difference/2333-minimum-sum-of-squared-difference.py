class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        if sum(diff) <= k:
            return 0
        left = 0
        right = max(diff)
        target = right
        while left <= right:
            mid = (left + right) // 2
            needed = sum(max(0, d - mid) for d in diff)
            if needed <= k:
                target = mid
                right = mid - 1
            else:
                left = mid + 1
        remaining_k = k
        new_diff = []
        for d in diff:
            if d > target:
                remaining_k -= (d - target)
                new_diff.append(target)
            else:
                new_diff.append(d)
        for i in range(len(new_diff)):
            if remaining_k > 0 and new_diff[i] == target:
                new_diff[i] -= 1
                remaining_k -= 1     
        return sum(d * d for d in new_diff)