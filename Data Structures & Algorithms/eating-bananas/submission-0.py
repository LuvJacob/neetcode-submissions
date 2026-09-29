class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(piles,h,k):
            total_hours = 0
            for p in piles:
                hours = (p+k-1)//k
                total_hours += hours
            if total_hours <= h:
                return True
            else:
                return False
        left = 1

        right = max(piles)
        answer = right
        while left <= right:
            mid = (left + right)//2
            if canEatAll(piles, h, mid):
                answer= mid
                right = mid -1
            else:
                left = mid +1
        return answer
                
        
        