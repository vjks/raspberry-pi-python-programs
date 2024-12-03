class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_s = ''
        sub_s = []
        start = 0
        for x in spaces:
            new_s = s[start : x]
            sub_s.append(new_s)
            start = x
        new_s = s[start : ]
        sub_s.append(new_s)

        x = ' '.join(map(str, sub_s))
        return x
