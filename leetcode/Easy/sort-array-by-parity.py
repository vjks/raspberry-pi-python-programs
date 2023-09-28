class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        odds = list()
        
        for num in nums:
            if num % 2 == 1:
                odds.append(num)
                
        for odd in odds:
            nums.remove(odd)
            nums.append(odd)

        return nums