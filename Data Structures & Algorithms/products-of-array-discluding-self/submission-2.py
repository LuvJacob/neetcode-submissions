class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = nums[0]
        no_zero = nums[0]
        for i in range(1,len(nums),1):
            if nums[i] != 0:
                no_zero = nums[i] * no_zero
            product = nums[i] * product
        new_nums = []
        for i in range(len(nums)):
            if nums[i] == 0 and nums.count(0) <=1:
                new_nums.append(no_zero)
            elif nums.count(0) > 1:
                new_nums.append(0)
            else:
                new_nums.append(int(product/ nums[i])) 
        return new_nums
        