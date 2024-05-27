# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr 3ohn Smit h 13
# Output: "Mr%203ohn%20Smith"
# Hints: #53,0118 


# %%
input_str = list("Mr John Smith    ")
output_str = "Mr%20John%20Smith"


flag_process = False
j = len(input_str)-1

for i in input_str[::-1]:
    if i != " ":
        flag_process = True
    if flag_process==True:
        if i == " ":
            input_str[j] = "0"
            input_str[j-1] = "2"
            input_str[j-2] = "%"
            j = j-3
        else:
            input_str[j] = i
            j = j-1

print("".join(input_str))
# %%
