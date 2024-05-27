# %%
def longestPalindrome(s: str) -> str:
    
    # edge case
    if len(s) == 0:
        return s
    if len(s) == 1:
        return s

    max_substr = ""
    for i in range(0, len(s)):
        # check the case where the middle is one char 
        j=0
        while(i+j != len(s)):
            if i-j < 0:
                break
            if s[i-j] == s[i+j]:
                if len(s[i-j:i+1+j]) > len(max_substr):
                    max_substr = s[i-j:i+1+j]
                j+=1
            else:
                break

        # check the case where the middle is two chars
        j=0
        if i == len(s)-1:
            break
        if s[i] == s[i+1]:
            i_l = i
            i_r = i+1
            while(i_r+j != len(s)):
                if i-j < 0:
                    break
                if s[i_l-j] == s[i_r+j]:
                    if len(s[i_l-j:i_r+1+j]) > len(max_substr):
                        max_substr = s[i_l-j:i_r+1+j]
                    j+=1
                else:
                    break

        
    return max_substr

def longestPalindromeDP(s:str)-> str:

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
    
    print(N_N)


    return max_substr


# %%
# s = "babad"
# s_true = "bab"
# s_pred = longestPalindromeDP(s)
# print(s_pred)
# assert s_true == s_pred

s = "cbbd"
s_true = "bb"
s_pred = longestPalindromeDP(s)
print(s_pred)
assert s_true == s_pred
# %%
s = "dddddddd"
s_true = "dddddddd"
s_pred = longestPalindromeDP(s)
print(s_pred)
assert s_true == s_pred
# %%
