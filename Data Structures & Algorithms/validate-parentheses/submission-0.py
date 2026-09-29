class Solution:
    def isValid(self, s: str) -> bool:
        test = {
         ")":"(",
         "]":"[",
         "}":"{"
        } 
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            if char in test:
                if not stack:
                    return False
                elif test[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack

        