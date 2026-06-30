class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # build the hash map
        nums_map = {}
        for (i, num) in enumerate(nums):
            difference = target - num
            if difference in nums_map:
                return [nums_map[difference], i]
            nums_map[num] = i
        
    
    
    