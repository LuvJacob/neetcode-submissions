class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        list[range(x)]
        while low <= high:
            mid = (low + high)//2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
                best = mid
            else:
                high = mid -1
        return best
        