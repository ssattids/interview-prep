class Solution:

    def myAtoi(self, s: str) -> int:
        """
        time complexity: O(n), where n is the number of characters in s
        space complexity: O(1)
        """

        negative_flag = False
        i=0

        if s == "":
            return 0

        while s[i] == ' ':
            i += 1
            if i == len(s):
                return 0

        if s[i] == '-':
            negative_flag = True
            i+=1
        elif s[i] == '+':
            i+=1

        min_range, max_range = 2147483648, 2147483647
        
        final_int = 0
        for i in range(i, len(s)):
            # if it is non=numeric, it is the end of the string
            if not s[i].isnumeric():
                break
            else:
                final_int = final_int*10 + int(s[i])
                # if it is a neagtive number, check the min range
                if negative_flag == True and final_int > min_range:
                    return min_range * -1
                # if it is a positive number, check the max range
                if negative_flag == False and final_int > max_range:
                    return max_range
                
        if negative_flag:
            return final_int * -1
        else:
            return final_int


    def myAtoi_v1(self, s: str) -> int:
        
        s = s.strip()

        if s == '':
            return 0

        sign = "plus"
        if s[0] == "+":
            s = s[1:]
            sign = "plus"
        elif s[0] == "-":
            s = s[1:]
            sign = "neg"
        else:
            pass


        integers = list("0123456789")
        num_str = ""
        # start = None
        # first_flag = False
        # # gets the first num value
        # for i, c in enumerate(s):
        #     if c in integers:
        #         num_str += c
        #         if first_flag==False and start == None:
        #             first_flag = True
        #             start = i

        #     else:
        #         if first_flag ==True:
        #             break
        # s = s[start:i+1]

        # integer = int(s)

        for i, c in enumerate(s):
            if c not in integers:
                break
            else:
                num_str += c

        if num_str == '':
            return 0

        integer = int(num_str)

        if sign == "neg":
            integer = integer*-1
            return max(integer, -2147483648)
        else:
            
            return min(integer, 2147483648-1)

