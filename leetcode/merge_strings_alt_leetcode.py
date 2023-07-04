class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined = ""
        word1_len = len(word1)
        word2_len = len(word2)
 
        for x in range(word1_len):
            combined += word1[x]
            if x >= word2_len:
                combined += word2[x :: ]
            else:
                combined += word2[x]
        if word2_len > word1_len:
            diff = word2_len - word1_len
            combined += word2[word1_len::]
        return combined