
# %%
import sys
sys.set_int_max_str_digits(6000)

class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        """
        Exponential search

        n = the number in the dividend

        time complexity: worst case O(log(n)) * O(log(n)) = O((log(n))^2)

        space complexity: O(1)

        """

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

        answer = 0
        while (dividend >= divisor): # takes O(log(n))

            divisor_exp_val = divisor
            divisor_exp = 1
            while (True): # worst case takes O(log(n))

                if dividend >= divisor_exp_val:
                    break
                else:
                    divisor_exp_val = divisor_exp_val * 2
                    divisor_exp = divisor_exp * 2

            dividend -= divisor_exp_val

            answer += divisor_exp

        if flag_negative:
            return max(-answer, -2**31)
        else:
            return min(answer, 2**31-1)

        return answer



    def divide_v2(self, dividend: int, divisor: int) -> int:

        """
        This solution use the high school method of long division

        n = n = the number of digits in the dividend
        
        time complexity worst case (dividend is large, and divisor is 1): O(n^2), the first loop causes O(n) and then converting the int to a string causes O(n) as well

        space complexity worst case: O(n), since accumalted_answer could requre as many digits as dividend

        NOTE: it might not be feasible 

        """

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
        
        accumalted_answer = 0
        
        while(dividend >= divisor):
            dividend_str = str(dividend) # O(n)

            i = 1
            while(int(dividend_str[0:i]) < divisor): # O(n)
                i+=1

            partial_dividend_str = dividend_str[0:i]
            partial_dividend_int = int(partial_dividend_str) # O(n)

            # get the best divisor_value
            for j, da in enumerate(divisor_arr): # O(9) = O(1)
                if da > partial_dividend_int:
                    break
            j = j-1
            best_divisor_val = divisor_arr[j]

            ten_difference = len(dividend_str) - len(partial_dividend_str) # O(1)          

            partial_answer = int(str(j+1) + '0'*ten_difference)

            accumalted_answer += partial_answer

            dividend_remove = int(str(best_divisor_val) + '0'*ten_difference)
            dividend -= dividend_remove

        if flag_negative:
            return max(-accumalted_answer, -2**31)
        else:
            return min(accumalted_answer, 2**31-1)

    def divide_v1(self, dividend: int, divisor: int) -> int:
        
        dividend_flag_neg = False
        if dividend < 0:
            dividend = int(str(dividend)[1:])
            dividend_flag_neg = True
        divisor_flag_neg = False
        if divisor < 0:
            divisor = int(str(divisor)[1:])
            divisor_flag_neg = True

        divisor_arr_less_10 = [i*divisor for i in range(1,10) if i < 10]
        divisor_arr_more_than_10 = [i*divisor for i in range(1,10) if i < 10]

        if dividend_flag_neg == True and divisor_flag_neg == True:
            return count
        if dividend_flag_neg == True or divisor_flag_neg == True:
            return int("-"+str(count))

        return count




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