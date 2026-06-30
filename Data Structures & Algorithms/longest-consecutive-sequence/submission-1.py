class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a hash table
        nums_map = {}
        for num in nums:
            nums_map[num] = True
        
        max = 0
        for num in nums:
            result = 0
            while nums_map.get(num, None) != None:
                result = result + 1
                num = num + 1
            if result > max:
                max = result
        return max

