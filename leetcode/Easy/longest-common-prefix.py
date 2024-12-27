class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        first = strs[0]

        smallest_len = len(first)    
        for string in strs:
            if len(string) == 0:
                return ""
            else:
                if len(string) < smallest_len:
                    smallest_len = len(string)
                    
        if len(strs) == 1:
            return strs[0]
        i = 0
        while i < smallest_len:
            character = strs[0][i]
            print(character)
            exists = True
            for string in strs:
                if string[i] != character:
                    print(string[i], character)
                    exists = False
                    break
            if exists:
                longest_prefix += character
            else:
                break
            i += 1
        return longest_prefix
