class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        string_x = str(x)
        reversed_string_x = string_x[::-1]
        if string_x == reversed_string_x:
            return True
        else:
            return False
