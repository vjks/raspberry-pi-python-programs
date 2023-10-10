class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = list(text.split())

        count = 0
        for word in words:
            found = False
            for char in brokenLetters:
                if char in word:
                    found = True
                    break
            if found:
                count += 1
        
        return len(words) - count