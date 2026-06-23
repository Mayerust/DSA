#optimised_soln
class Solution(object):
    def twoSum(self, numbers, target):
    
        left =  0
        right = len(numbers) - 1
        #sum = numbers[left] + numbers[right]
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right = right - 1      
            elif sum < target:
                left = left + 1
            else:
                return [(left + 1), (right + 1)]
    #return [(i+1), (j+1)]        

