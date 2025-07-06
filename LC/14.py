# %%
from typing import List

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Iterate over each position of the character for each string, see if there is a match, then move to the next character
        time complexity = O(n*m), n = len(strs), m = avg size of the string
        space complexity = O(1)

        best case:
        time complexity = O(n*minLen), n = len(strs), minLen = the minimum length of a str in strs
        """

        longest_common_prefix = ""
        
        for i in range(len(strs[0])):
            for str_ in strs:
                if i == len(str_) or str_[i] != strs[0][i]:
                    return longest_common_prefix
            longest_common_prefix += strs[0][i]

        return longest_common_prefix


    def longestCommonPrefix_v1(self, strs: List[str]) -> str:

        i = 0
        prefix = ''
        flag_broke = False
        while (True):
            if i > len(strs[0]):
                break
            sub_prefix = strs[0][:i]
            for str_ in strs:
                if i > len(str_):
                    flag_broke = True
                    break
                if str_[:i] != sub_prefix:
                    flag_broke = True
                    break
                else:
                    continue
            
            if flag_broke == True:
                break
            prefix = sub_prefix
            i+=1
        
        return prefix