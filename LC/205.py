class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        # 01234
        # paper
        # 01234
        # title

        # p = [0,2]
        # a = [1]
        # e = [3]
        # r = [4]

        # t = [0,2]
        # i = [1]
        # l = [3]
        # e = [4]


        s_code = {}
        for i, c in enumerate(s):
            if c in s_code:
                s_code[c].append(i)
            else:
                s_code[c] = [i]

        t_code = {}
        for i, c in enumerate(t):
            if c in t_code:
                t_code[c].append(i)
            else:
                t_code[c] = [i]

        s_arr = []
        for k, v in s_code.items():
            s_arr.append(v)
        t_arr = []
        for k, v in t_code.items():
            t_arr.append(v)

        for x,y in zip(s_arr, t_arr):
            if x != y:
                return False
        return True