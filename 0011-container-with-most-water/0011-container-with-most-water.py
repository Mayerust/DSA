class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        left =  0
        right = size - 1
        area_list = [0] * size
        pos = size - 1
        while left <  right and pos >= 0:
            if height[left] >= height[right]:
                length = height[right]
                breadth = right - left
                area = length * breadth
                area_list[pos] = area
                right = right - 1
                pos = pos - 1
            elif height[right] >= height[left]:
                length = height[left]
                breadth = right - left
                area = length * breadth
                area_list[pos] = area
                left = left + 1
                pos = pos - 1
        area_list.sort()
        return area_list[size - 1]         

