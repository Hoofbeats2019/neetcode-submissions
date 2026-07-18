class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        sliding_heap = []
        
        result = []
        left = 0

        for left in range(len(nums)-k+1):
            result.append(max(nums[left:left+k]))
        return result