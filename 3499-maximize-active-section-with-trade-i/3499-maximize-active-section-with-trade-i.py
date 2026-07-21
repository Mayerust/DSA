class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        base_ones = s.count('1')
        t = '1' + s + '1'
        blocks = []
        current_char = t[0]
        count = 1
        
        for char in t[1:]:
            if char == current_char:
                count += 1
            else:
                blocks.append((current_char, count))
                current_char = char
                count = 1
        blocks.append((current_char, count))
        max_gain = 0

        for i in range(2, len(blocks) - 1, 2):
            left_zeros_len = blocks[i - 1][1]
            right_zeros_len = blocks[i + 1][1]
            gain = left_zeros_len + right_zeros_len
            if gain > max_gain:
                max_gain = gain
    
        return base_ones + max_gain