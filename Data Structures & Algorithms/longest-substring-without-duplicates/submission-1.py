class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        temp = []
        for i in s:
            if i in temp:
                if len(temp) > longest:
                    longest = len(temp)
                while i in temp:
                    temp.pop(0)
                temp.append(i)
            else:
                temp.append(i)
        return max(longest, len(temp))
        