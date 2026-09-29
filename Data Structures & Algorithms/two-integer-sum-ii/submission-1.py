class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers)-1

        while True:
            total = numbers[high] + numbers[low]
            if target == total:
                return[low+1,high+1]
            if target < total:
                high = high -1
            elif target > total:
                low = low + 1
        