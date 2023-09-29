class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = decrease = False
        n = len(nums)

        for _ in range(n - 1):
            if nums[_] < nums[_ + 1]:
                decrease = True
            
            if nums[_] > nums[_ + 1]:
                increase = True
            
            if increase and decrease:
                return False

        return True