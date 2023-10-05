class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = dict()

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        elements = list()
        n = len(nums)
        for key, value in d.items():
            if value > n // 3:
                elements.append(key) 
        return elements