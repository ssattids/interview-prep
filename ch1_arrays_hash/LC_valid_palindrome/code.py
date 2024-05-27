class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if s == '':
            return False
        
        import re
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()

        if len(s) % 2 == 0:
            # "abba"
            # len = 4
            # len(s)/2 = 4
            # 2,3
            left_add = 1
            middle = int(len(s)/2)
            for right in range(middle,len(s)):
                left = middle-left_add
                left_add+=1
                if s[left] == s[right]:
                    continue
                else:
                    return False
        else:
            #abbba
            # len = 5
            # len(s/2) = 2.5, int(2.5)3
            middle = int((len(s)-1)/2)
            left_add = 1
            for right in range(middle+1, len(s)):
                left = middle-left_add
                left_add+=1
                if s[right]==s[left]:
                    continue
                else:
                    return False
                
        return True