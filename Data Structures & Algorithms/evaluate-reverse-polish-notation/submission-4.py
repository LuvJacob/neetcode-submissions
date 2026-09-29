class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp = []
        total = 0
        for i in tokens:
            if i in ("+","-","*", "/"):
                val2 = int(temp.pop())
                val1 = int(temp.pop())
                if i == "+":
                    total = val1 + val2
                    temp.append(total)
                elif i == "-":
                    total = val1 - val2
                    temp.append(total)
                elif i == "*":
                    total = val1 * val2
                    temp.append(total)
                else:
                    total = int(val1 / val2)
                    temp.append(total)
            else:
                temp.append(int(i))
        return temp[0]            
            
                    

                
                
        