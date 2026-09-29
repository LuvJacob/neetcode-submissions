class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amount = {}
        for i in nums:
            if i in amount:
                amount[i] += 1 
            else:
                amount[i] = 1
        counts = []
        for key, value in amount.items():
            counts.append([key,value])
        counts.sort(key = lambda pair:pair[1], reverse = True)
        top = []
        for pair in counts[:k]:
            top.append(pair[0])
        return top


        