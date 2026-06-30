class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer algrithem
        left = 0
        right = len(heights) - 1
        area = 0

        while left < right:
            if area < min(heights[left], heights[right]) * (right - left):
                area = min(heights[left], heights[right]) * (right - left)
            
            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right - 1
        
        return area
