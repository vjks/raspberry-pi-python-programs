class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index1 = index2 = 0
        for x in nums:
            for count, item in enumerate(nums):
                if x + item == target and nums.index(x) != count:
                    index1 = nums.index(x)
                    index2 = count
                    break
            else:
                continue
            break
        return [index1, index2]