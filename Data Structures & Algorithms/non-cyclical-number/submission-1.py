class Solution:
    def isHappy(self,n: int) -> bool:
        seen = []
        total = 0
        while True:
            if not seen:
                for i in str(n):
                    total += int(i) **2
            else:
                for i in str(seen[-1]):
                    total += int(i) **2
            if total == 1:
                return True
            if total in seen:
                return False
            seen.append(total)
            total = 0
            