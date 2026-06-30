class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s) - 1

        while (right_pointer - left_pointer) > 0:
            
            while not s[left_pointer].isalnum() and left_pointer < len(s) - 1:
                left_pointer = left_pointer + 1

            while not s[right_pointer].isalnum() and right_pointer > 0:
                right_pointer = right_pointer - 1

            if s[left_pointer].isalnum() and s[right_pointer].isalnum() and s[left_pointer].lower() != s[right_pointer].lower():
                return False
            else:
                left_pointer = left_pointer + 1
                right_pointer = right_pointer - 1
        
        return True
                
        
