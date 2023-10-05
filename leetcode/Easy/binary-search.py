def binarySearch(nums, x):
        n = len(nums)
        low = 0
        mid = 0
        high = n - 1
        pos = -1

        while low <= high:
            mid = (low + high) // 2
            #print("mid is:", mid)
            if nums[mid] < x:
                low = mid + 1
                #print("low is:", low, high)
            elif nums[mid] > x:
                high = mid - 1
                #print("high is:", high, high)
            elif nums[mid] == x:
                pos = mid
                #print("pos is: ", mid, low, high)
                break
        return pos
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        x = binarySearch(nums, target)
        return x