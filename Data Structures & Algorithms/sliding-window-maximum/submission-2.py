class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        sliding_heap = []
        
        result = []
        left = 0

        for left in range(len(nums)-k+1):
            for i in range(k):
                heapq.heappush(sliding_heap, -nums[left + i])
            result.append(-heapq.heappop(sliding_heap))
            sliding_heap = []
        return result