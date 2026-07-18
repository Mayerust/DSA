import math
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # Find the smallest and largest numbers in the array
        smallest = min(nums)
        largest = max(nums)
        
        # Return their Greatest Common Divisor
        return math.gcd(smallest, largest)