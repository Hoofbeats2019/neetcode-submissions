class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window algorithem
        # a window sliding through s2
        # if the chars in the sliding window same as the chars in s1, then
        # return Ture, otherwise return False

        left = 0
        set_s1 = sorted(list(s1))
        window_size = len(set_s1)

        for left in range(len(s2) - window_size + 1):
            set_s2 = sorted(list(s2[left:left+window_size]))
            if set_s1 == set_s2:
                return True
        return False
                