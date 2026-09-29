class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = {}
        m2 = {}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = 1
            else:
                m[s[i]] +=1
            if t[i] not in m2:
                m2[t[i]] = 1
            else:
                m2[t[i]]+=1
        
        return m == m2