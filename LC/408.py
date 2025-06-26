class Solution:

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i, j = 0, 0
        number_str = ""
        while (i < len(abbr)):
            # build up the nums
            if abbr[i].isnumeric():
                number_str += abbr[i]
                i+=1
            else:
                # we are not using the number str
                if number_str != "":
                    if number_str[0] == '0':
                        return False
                    number = int(number_str)
                    number_str = ""
                    j+=number
                # we are using the number string
                else:
                    # edge case: if the abbreviation number has pushed us beyond the size of the word
                    if j >= len(word):
                        return False
                    if abbr[i] != word[j]:
                        return False
                    i+=1
                    j+=1
        # fenceposting 
        if number_str != "":
            if number_str[0] == '0':
                    return False
            number = int(number_str)
            number_str = ""
            j+=number

        # edge case: if the abbreviation doesn't exactly match the word
        if j != len(word):
            return False
                
        return True


    def validWordAbbreviation_v2(self, word: str, abbr: str) -> bool:
        num_str = ""
        i,j = 0, 0
        while(i<len(abbr)):
            if j > len(word)-1:
                return False
            if abbr[i].isdigit():
                num_str += abbr[i]
                i+=1
            elif abbr[i].isalpha():
                # skip the num
                if num_str != "":
                    if num_str[0]=="0":
                        return False
                    num_int = int(num_str)
                    j += num_int
                    num_str=""
                else:
                    if abbr[i] != word[j]:
                        return False
                    i+=1
                    j+=1
        if num_str != "":
            if num_str[0]=="0":
                return False
            num_int = int(num_str)
            j += num_int
            num_str=""
        print(i)
        print(j)
        print(len(word))
        if j != len(word):
            return False

        return True


    def validWordAbbreviation_v1(self, word: str, abbr: str) -> bool:
        
        l_p = 0
        r_p = 0

        new_word = ""
        number = ""
        i=0
        while(i<len(abbr)):
            char = abbr[i]
            if char.isnumeric():
                if number=="":
                    l_p = len(new_word)
                number += char
            if char.isalpha():
                # no leading zeros allowed
                if number != "":
                    # no leading zeros allowed
                    if number[0]=="0":
                        return False
                    # pernicious python feature - if end index is larger than word it will still return the word
                    if l_p > len(word) or l_p + int(number) > len(word):
                        return False
                    new_word += word[l_p: l_p + int(number)]
                    number=""
                new_word += char
            i+=1
        # fence posting
        if number != "":
            if number[0]=="0":
                return False
            if l_p > len(word) or l_p + int(number) > len(word):
                return False
            new_word += word[l_p: l_p + int(number)]

        if new_word == word:
            return True
        else:
            return False

         

            
# %%
solution = Solution()
# %%
print(solution.validWordAbbreviation(
    "hi",
    "2i"
))

# %%
print(solution.validWordAbbreviation(
    "internationalization",
    "i12iz4n"
))
# %%
print(solution.validWordAbbreviation(
    "internationalization",
    "i5a11o1"
))
# %%
print(solution.validWordAbbreviation(
    "a",
    "01"
))
# %%
print(solution.validWordAbbreviation(
    "apple",
    "a2e"
))
# %%

# %%
print(solution.validWordAbbreviation(
    "internationalization",
    "i12iz4n"
))
# %%




# %%