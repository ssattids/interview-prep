class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        time complexity: O(n)
        """
        p1 = 0
        p2 = 0

        alt_merged_str = ""
        # iterate over length of both strings
        for i in range(len(word1)+len(word2)):

            if p1 == len(word1):
                alt_merged_str += word2[p2]
                p2+=1
            elif p2 == len(word2):
                alt_merged_str += word1[p1]
                p1+=1
            else:
                if i % 2 == 0:
                    alt_merged_str += word1[p1]
                    p1+=1
                else:
                    alt_merged_str += word2[p2]
                    p2+=1
        
        return alt_merged_str
