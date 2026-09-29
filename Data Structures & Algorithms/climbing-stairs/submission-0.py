class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            temp = one # temp = 1. next run, temp = 2, temp = 3
            one = one + two # one = 1 + 1 one = 2 + 1=3, one = 3 + 2 = 5
            two = temp #two = 1. , two = 2, two = 3
        return one
        
        