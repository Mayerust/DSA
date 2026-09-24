class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        """
        i = 0
        while i < len(nums):
            if nums[i] == 1000:
                total = 1
                if i == total:
                    return i
                i += 1    
            elif 99 < nums[i] <= 999:
                number1 = nums[i] // 100
                number2 = (nums[i] % 100) // 10
                number3 = (nums[i] % 100) % 10 
                total = number1 + number2 + number3
                if i == total:
                    return i
                i += 1    
            elif 9 < nums[i] < 100:
                number1 = nums[i] // 10
                number2 = nums[i] % 10
                total = number1 + number2
                if i == total:
                    return i
                i += 1    
            elif 0 <= nums[i] <= 9:
                if i == nums[i]:
                    return i
                i += 1
        return -1            
        """
        for i, num in enumerate(nums):
            if i == sum(int(d) for d in str(num)):
                return i
        return -1    