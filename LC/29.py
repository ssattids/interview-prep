# %%
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        flag_negative = False
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
            flag_negative = False
        elif dividend < 0 and divisor > 0:
            dividend = -dividend
            flag_negative = True
        elif dividend > 0 and divisor < 0:
            divisor = -divisor
            flag_negative = True
        else:
            flag_negative = False

        divisor_arr = []
        sum_ = 0
        for i in range(9):
            sum_ += divisor
            divisor_arr.append(sum_)
        print(divisor_arr)
        
        accumalted_answer = 0
        
        while(dividend >= divisor):

            print("current dividend=", dividend)

            dividend_str = str(dividend)

            i = 1
            while(int(dividend_str[0:i]) < divisor):
                i+=1

            partial_dividend_str = dividend_str[0:i]
            partial_dividend_int = int(partial_dividend_str)
            print("partial_dividend_int=",partial_dividend_int)

            # get the best divisor_value
            for j, da in enumerate(divisor_arr):
                if da > partial_dividend_int:
                    break
            j = j-1
            best_divisor_val = divisor_arr[j]
            print("best_divisor_val=",best_divisor_val)


            ten_difference = len(dividend_str) - len(partial_dividend_str)
            print("ten_difference=",ten_difference)
            

            partial_answer = int(str(j+1) + '0'*ten_difference)
            print("partial_answer=",partial_answer)

            accumalted_answer += partial_answer

            dividend_remove = int(str(best_divisor_val) + '0'*ten_difference)
            print("dividend_remove=",dividend_remove)
            dividend -= dividend_remove

            print("")

        if flag_negative:
            return -accumalted_answer
        else:
            return accumalted_answer


# %%
s = Solution()

# %%
print("Expected solution=", 617)
print("Returned solution=", s.divide(1234, 2))

# %%
print("Expected solution=", s.divide(7, 3))
print("Returned solution=", 2)

# %%
print("Expected solution=", s.divide(1, 1))
print("Returned solution=", 1)

# %%