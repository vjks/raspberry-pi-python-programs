class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        sum_array = 0
        for x in nums:
            sum_array += x
            running_sum.append(sum_array)
        return running_sum
        