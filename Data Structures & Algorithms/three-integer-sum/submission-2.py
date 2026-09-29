class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)-2):
            a = nums[i]
            if i > 0 and a == nums[i-1]:
                continue
            if a > 0:
                break
            left = i+1
            right = len(nums) - 1
            while left < right:
                if a + nums[left] + nums[right] == 0:
                    res.append([a,nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif a + nums[left] + nums[right] < 0:
                    left +=1
                else:
                    right-=1
        return res

        