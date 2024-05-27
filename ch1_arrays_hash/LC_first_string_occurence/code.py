# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if haystack==needle:
            return 0

        if len(needle) > len(haystack):
            return -1

        # if i + len(needle) > len(haystack)-1
        i=0
        needle_len = len(needle)
        while (i+needle_len-1) != len(haystack):
            if haystack[i:i+needle_len] == needle:
                return i
            else:
                i+=1

        return -1