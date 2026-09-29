class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean =""
        for char in s:
            if char.isalnum():
                clean += char
        s_list = list(clean)
        
        test = []
        test_string = ''
        for i in range((len(s_list)-1),-1,-1):
            test.append(s_list[i])
        for i in test:
            test_string +=i
        return test_string.lower() == clean.lower()
             
        