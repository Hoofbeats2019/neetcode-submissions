class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer algrithem
        left = 0
        right = len(heights) - 1
        result = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            result = max(area, result)
            
            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right - 1
        
        return result
