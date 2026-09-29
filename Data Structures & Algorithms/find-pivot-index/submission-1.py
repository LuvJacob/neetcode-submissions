class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = sum(nums[:i]) if i > 0 else 0
            y = sum(nums[i+1:]) if i < len(nums) else 0
            if x == y:
                return i
        return -1
        