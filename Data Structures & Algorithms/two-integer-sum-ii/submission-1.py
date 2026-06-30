class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1
        current_cum = numbers[left_pointer] + numbers[right_pointer]

        while current_cum != target:
            if current_cum > target:
                right_pointer = right_pointer - 1
                current_cum = numbers[left_pointer] + numbers[right_pointer]
            else:
                left_pointer = left_pointer + 1
                current_cum = numbers[left_pointer] + numbers[right_pointer]
        return [left_pointer + 1, right_pointer + 1]