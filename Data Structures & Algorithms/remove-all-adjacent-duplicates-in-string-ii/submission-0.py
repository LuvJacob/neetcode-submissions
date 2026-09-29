class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        U - input: s: str ,k: int
        '''
        stack = []
        new = ""
        for i in s:
            if stack and stack[-1][0] == i:
                stack[-1][1] +=1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([i,1])
            
        return "".join(ch * count for ch, count in stack)
        