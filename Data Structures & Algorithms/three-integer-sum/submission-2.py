class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            # use two pointer algrithm
            left = 0 
            right = len(nums) - 1
            target = -nums[i]

            # check begining and ending of the loop, move pointer accordingly
            if i == left:
                left = left + 1
            if i == right:
                right = right - 1            
            
            # two pointer algrithm
            while left < right:
                if nums[left] + nums[right] > target:
                    right = right - 1
                    if right == i:
                        right = right - 1
                
                if nums[left] + nums[right] < target:
                    left = left + 1
                    if left == i:
                        left = left + 1
            
                if nums[left] + nums[right] == target and right != left:
                    if left != right and right != i:
                        triplet = [nums[i], nums[left], nums[right]]
                        triplet.sort()
                    if triplet not in result:
                        result.append(triplet)
                    right = right - 1
        return result
            