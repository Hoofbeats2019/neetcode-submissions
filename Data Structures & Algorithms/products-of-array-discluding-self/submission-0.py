class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create the first run from left to right
        result_left = []
        result = 1
        for num in nums:
            result_left.append(result)
            result = result * num
        
        print(result_left)
        
        result_right = []
        result = 1
        for num in reversed(nums):
            result_right.append(result)
            result = result * num
        result_right.reverse()
        print(result_right)

        products = []
        for i in range(len(nums)):
            products.append(result_left[i] * result_right[i])
        
        return products

        
            



        