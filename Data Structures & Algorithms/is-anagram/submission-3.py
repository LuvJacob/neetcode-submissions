class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def hashTable(p):
            table = {}
            for char in p:
                if char in table:
                    table[char] += 1
                else:
                    table[char] = 1
            return table
        tab1 = hashTable(s)
        tab2 = hashTable(t)
        return tab1 == tab2

        