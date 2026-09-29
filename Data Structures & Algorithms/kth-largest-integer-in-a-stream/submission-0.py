class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        sort_nums = sorted(self.nums, reverse = True)
        return sort_nums[self.k-1]
        
