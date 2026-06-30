class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left = 0
        right = 1
        max_count = 1
        counter = 1
        if len(nums) == 0:
            return 0
        while right < len(nums):
            if nums[right] - nums[left] == 1:
                counter += 1
                left += 1
                right += 1
                if counter > max_count:
                    max_count = counter

            elif nums[right] - nums[left] == 0:
                left = left + 1
                right = right + 1

            elif nums[right] - nums[left] > 1:
                if counter > max_count:
                    max_count = counter
                    counter = 1
                    left += 1
                    right += 1  
                else:
                    counter = 1
                    left += 1
                    right += 1   
        return max_count

        #method 2

        #set_nums = set(nums)
        #longest_streak = 1
        #streak = 1
        #current = 0

        #if len(nums) == 0:
            #return 0
        #for num in set_nums:
            #if (num - 1) not in set_nums:
                #current = num
                #streak = 1

                #while (current + 1) in set_nums:
                    #current += 1
                    #streak += 1

                    #if streak > longest_streak:
                        #longest_streak = streak
        #return longest_streak


                


            
       