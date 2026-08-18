class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        if k == 1:
            counts = {}
            for num in nums:
                counts[num] = counts.get(num, 0) + 1
            
            largest = -1
            for num, count in counts.items():
                if count == 1:
                    largest = max(largest, num)
            return largest
            
        elif k == n:
            return max(nums)
            
        else:
            counts = {}
            for num in nums:
                counts[num] = counts.get(num, 0) + 1
                
            first = nums[0]
            last = nums[-1]
            
            largest = -1
            
            if counts[first] == 1:
                largest = max(largest, first)
                
            if counts[last] == 1:
                largest = max(largest, last)
                
            return largest