class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        new = set()

        for x in nums1:
            if x in nums2 or x in nums3:
                new.add(x)
        
        for y in nums2:
            if y in nums1 or y in nums3:
                new.add(y)
        
        return new