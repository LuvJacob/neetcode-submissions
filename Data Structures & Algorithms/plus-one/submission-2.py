class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 0
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                if i == 0:
                    digits[i] = 1
                    digits.append(0)
                    return digits
                rem = 1
                digits[i] = 0
            else:
                if i == 0:
                    digits[i] +=1
                else:
                    digits[i] = digits[i] + 1
                return digits
            

        