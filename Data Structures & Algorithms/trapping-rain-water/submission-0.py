class Solution:
    def trap(self, heights: List[int]) -> int:
        # find the prefix and suffix
        prefix = []
        suffix = []
        
        current = 0
        for height in heights:
            current = max(current, height)
            prefix.append(current)
        
        current = 0
        for height in reversed(heights):
            current = max(current, height)
            suffix.append(current)
        suffix.reverse()

        water = 0
        for i in range(len(heights)):
            water = water + min(prefix[i], suffix[i]) - heights[i]
        
        return water




            