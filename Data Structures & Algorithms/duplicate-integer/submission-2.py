class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test = set()
        for i in nums:
            if i not in test:
                test.add(i)
            else:
                return True
        return False
        