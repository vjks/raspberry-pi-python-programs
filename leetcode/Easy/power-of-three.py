import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 or n == 2:
            return False
        else:
            x = math.log(n, 3)

            if math.ceil(x) - x < .1:
                x = math.ceil(x)
            else:
                x = int(x)
            if 3**x == n:
                return(True)
            else:
                return(False)