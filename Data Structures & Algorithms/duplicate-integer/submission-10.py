class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i, n in enumerate(nums):
            if i < len(nums)-1:
                if n == nums[i+1]:
                    return True
        return False