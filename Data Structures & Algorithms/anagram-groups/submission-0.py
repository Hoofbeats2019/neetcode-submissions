class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = {}

        # Assume all strings in strs are different and unique
        for string in strs:
            string_sorted = ''.join(sorted(string))
            if string_sorted in strs_map:
                strs_map[string_sorted].append(string)
            else:
                strs_map[string_sorted] = [string]
        
        result = []
        for value in strs_map.values():
            result.append(value)
        
        return result