class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for string in strs:
            str_length = str(len(string)).zfill(3)
            result = result + str_length + string
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        while len(s) > 0:
            # split the string, s
            first_part = s[:3]
            length = int(first_part)
            string = s[3:(3+length)]
            result.append(string)
            s = s[(3+length):]
        return result

            



