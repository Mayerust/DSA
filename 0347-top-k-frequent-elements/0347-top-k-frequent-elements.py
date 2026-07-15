class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        #highest_freq = 1
        #most_freq_element = None
        for i in range(0, len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
                #if freq[nums[i]] > highest_freq:
                    #highest_freq = freq[nums[i]]
                    #most_freq_element = nums[i]
        result_arr = [0] * k
        j = 0
                 
        sorted_freq = dict(sorted(freq.items(), key = lambda item: item[1], reverse = True))
        for key, values in sorted_freq.items():
            result_arr[j] = key
            j += 1
            if j == k:
                break 
        return result_arr    
