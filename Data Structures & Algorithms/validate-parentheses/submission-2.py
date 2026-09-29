class Solution:
    def isValid(self, s: str) -> bool:
        m = {")":"(", "]":"[", "}":"{"}

        stack = []
        for i in s:
            if i in m:
                if not stack:
                    return False
                if stack.pop() != m[i]:
                    return False
            if i not in m:
                stack.append(i)
        return stack == []
        