# %%
# brute force
def lengthOfLongestSubstring(s: str) -> int:
    # edge case
    if s == '':
        return 0

    max_len = 0
    for i in range(len(s)):
        str_dict = {}
        for j in range(i,len(s)):
            if s[j] not in str_dict:
                str_dict[s[j]] = True
                if len(str_dict) > max_len:
                    max_len = len(str_dict)
            else:
                break

    return max_len

lengthOfLongestSubstring(" ")
# %%
# sliding window
