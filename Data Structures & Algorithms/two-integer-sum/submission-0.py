class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        for (i, num) in enumerate(nums):
            difference = target - num
            nums_remain = nums[i+1:]
            if difference in nums_remain:
                return [i, i + 1 + nums_remain.index(difference)]