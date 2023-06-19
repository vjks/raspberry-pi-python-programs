class Solution:
    def equivalent(self, symbol) -> int:
        value = 0
        match symbol:
            case 'I':
                value += 1
            case 'V':
                value += 5
            case 'X':
                value += 10
            case 'L':
                value += 50
            case 'C':
                value += 100
            case 'D':
                value += 500
            case 'M':
                value += 1000
            case _:
               value += 0
        return value
    
    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0
        while(i < len(s)):
            if i + 1 < len(s):
                current_element = self.equivalent(s[i])
                next_element = self.equivalent(s[i + 1])
                if(current_element < next_element):
                    sum += (next_element - current_element)
                    i += 2
                else:
                    sum += current_element
                    i += 1
            else:
                sum += self.equivalent(s[i])
                i += 1
        return sum

s = Solution()
s.romanToInt("MCMXCIV")