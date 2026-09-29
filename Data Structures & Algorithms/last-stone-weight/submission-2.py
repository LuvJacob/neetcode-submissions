class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sorted_stones = sorted(stones, reverse=True)
        while len(sorted_stones)!= 1:
            sorted_stones = sorted(sorted_stones, reverse=True)
            x = sorted_stones[0]
            y = sorted_stones[1]
            if x == y:
                sorted_stones.pop(0)
                sorted_stones.pop(0)
                sorted_stones.append(0)
            else:
                x= x-y
                sorted_stones[0] = x
                sorted_stones.pop(1)
        return sorted_stones[0]
                


        