class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0
        best = 0
        for num in s:
            if num - 1 in s:
                continue
            else:
                count = 1
                while num + count in s:
                    count+=1
                best = max(count,best)
        return best

                

        