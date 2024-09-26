class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        numlen = len(nums)

        for i in range(numlen):
            for j in range(i):
                #print(nums[i], nums[j])
                if nums[i] + nums[j] == target:
                    output.append(j)
                    output.append(i)
                    break
            else:
                continue
            break
        return output
