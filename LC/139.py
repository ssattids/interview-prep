class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        n = len(s), m=len(word_dict), k=average length of the words in wordDict
        time complexity: O(n^3 + m*k) 
        space complexity: (O(n) + m*k)
        """

        queue = [""]
        seen = set()
        
        while(queue!=[]):

            item_str = queue.pop()

            if item_str == s:
                return True

            part_str = ""
            # at each node, we iterate over the nodes in front of the current node, so for each node, we have O(n^2) time complexity
            for i in range(len(item_str), len(s)):
                part_str += s[i]
                if part_str in wordDict:
                    # adding 2 strings is a O(n) behaviour where n = x + y, where x = lenght of first string, and y = length of second string
                    if item_str+part_str not in seen:
                        queue.append(item_str+part_str)
                        seen.add(item_str+part_str)

        return False
