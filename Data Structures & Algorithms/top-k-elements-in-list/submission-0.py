class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build a dict / map, (key, value) is (num, count)
        count_map = {}

        for num in nums:
            if num in count_map:
                count_map[num] = count_map[num] + 1
            else:
                count_map[num] = 1
        
        # Build a new list which is sorted based on count
        sorted_map = sorted(count_map.items(), key=lambda x: x[1], reverse=True)
        
        keys = [key for key, value in sorted_map[:k]]
        return keys