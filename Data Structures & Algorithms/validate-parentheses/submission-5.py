class Solution:
    def isValid(self, s: str) -> bool:
        m = {")":"(", "]":"[", "}":"{"}

        stack = []
        for i in s:
            if i in m:
                if not stack:
                    return False
                elif stack.pop() != m[i]:
                    return False
            else:
                stack.append(i)
        return stack == []