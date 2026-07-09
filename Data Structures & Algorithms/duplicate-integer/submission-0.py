class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = set(nums)
        if len(nums2) == len(nums):
            return False
        else:
            return True
        