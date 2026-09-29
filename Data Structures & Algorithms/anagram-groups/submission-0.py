class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        test = {}
        for i in strs:
            sig = "".join(sorted(i))
            if sig not in test:
                test[sig] = []
            test[sig].append(i)
        return list(test.values())

            
        