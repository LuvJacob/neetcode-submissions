class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        count = 0
        for i in matrix:
            high = len(i) -1
            low = 0

            while high >= low:
                count += 1
                mid = (high+low)//2
                if i[mid] == target:
                    return True
                elif target > i[high]:
                    break
                elif i[mid] > target:
                    high = mid -1
                else:
                    low = mid +1
        return False
                
                


        