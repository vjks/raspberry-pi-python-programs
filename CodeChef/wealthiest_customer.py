class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for x in accounts:
            sum = 0
            for y in x:
                sum += y
            if sum > richest:
                richest = sum
        return richest