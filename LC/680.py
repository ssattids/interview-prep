class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def check_valid_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        l = 0
        r = len(s)-1
        while (l < r):
            if s[l] != s[r]:
                # check skip both
                return check_valid_palindrome(s, l+1, r) or check_valid_palindrome(s, l, r-1)
            l += 1
            r -= 1
            

        return True