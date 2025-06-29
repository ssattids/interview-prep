class Solution:

    def longestPalindrome(self, s:str)-> str:
        """
        time complexity: O(n^2), where n = number of characters in a string
        space complexity: O(1)

        take a character and expand around it (both towards the left and right), keep checking to see if it is a palindrome, then update the longest palindrome
        """

        if len(s) <= 1:
            return s


        longest_palindrome = ""

        for i, c in enumerate(s):

            # treat i as the middle 
            i_minus = i-1
            i_plus = i+1

            if len(s[i]) > len(longest_palindrome):
                longest_palindrome = s[i]

            while(i_minus >= 0 and i_plus < len(s) and s[i_minus] == s[i_plus] ):
                if len(s[i_minus:i_plus+1]) > len(longest_palindrome):
                    longest_palindrome = s[i_minus:i_plus+1]
                i_minus = i_minus - 1
                i_plus = i_plus + 1

            # treat i and i+1 as the middle letters
            if i > 0:
                i_minus = i-1
                i_plus = i

                while(i_minus >= 0 and i_plus < len(s) and s[i_minus] == s[i_plus] ):
                    if len(s[i_minus:i_plus+1]) > len(longest_palindrome):
                        longest_palindrome = s[i_minus:i_plus+1]
                    i_minus = i_minus - 1
                    i_plus = i_plus + 1

        return longest_palindrome


    def longestPalindrome_v1(self, s:str)-> str:

        # edge case
        if len(s) == 0:
            return s
        if len(s) == 1:
            return s

        # declare the matrix
        N_N = [[None]*len(s) for i in range(len(s))]
        
        # all substr of length 1 are palindromes
        max_substr = s[0]
        for i in range(len(N_N)):
            N_N[i][0] = True

        for len_substr in range(3,len(s)+1,2):
            
            for index in range(len(s)):

                index_left = index-(int((len_substr)/2))
                index_right = index+(int((len_substr)/2))
                # overflow from left or right - is it a valid index
                if index_left < 0 or index_right >= len(s):
                    continue


                # only true, if the previous smaller substr is true
                if N_N[index][len_substr-2-1] == True:

                    # if the smaller substr is true, then check if the next is true too
                    if s[index_left] == s[index_right]:
                        N_N[index][len_substr-1] = True
                        if len(s[index_left:index_right+1]) > len(max_substr):
                            max_substr = s[index_left:index_right+1]
                    else:
                        N_N[index][len_substr-1] = False
                else:
                    N_N[index][len_substr-1] = False

        for i in range(len(N_N)):
            if i == 0:
                N_N[i][1] = False
            else:
                if s[i]==s[i-1]:
                    N_N[i][1] = True
                    if len(s[i-1:i+1]) > len(max_substr):
                            max_substr = s[i-1:i+1]
                else:
                    N_N[i][1] = False

        for len_substr in range(4,len(s)+1,2):
            for index in range(len(s)):
                                                    
                index_left = index-(len_substr-1) #      
                index_right = index 

                if index_left < 0 or index_right >= len(s):
                    continue

                # check if the previous one is true
                if N_N[index-1][len_substr-1-2] == True:
                    if s[index_left] == s[index_right]:
                        N_N[index][len_substr-1] = True
                        if len(s[index_left:index_right+1]) > len(max_substr):
                            max_substr = s[index_left:index_right+1]
                else:
                    N_N[index][len_substr-1] = False


        return max_substr