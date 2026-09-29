class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # found = set()
        # for i in range(len(nums)):
        #     if nums[i] in found:
        #         return nums[i]
        #     found.add(nums[i])
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        s = 0
        while True:
            s = nums[s]
            slow = nums[slow]
            if s == slow:
                return s
               
        