class Solution:
    def reverseWords(self, s: str) -> str:
        array = list(map(str, s.split()))
        reverse = list()
        for word in array:
            reverse.append(word[::-1])
        
        return ' '.join(reverse)