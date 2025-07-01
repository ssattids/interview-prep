class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        time complexity: O(log_n), where n = number of digits in the integer
        space complexity: O(1)

        convert the integer to a string and then check if it is a palindrome
        """


        str_x = str(x)

        # even case
        if len(str_x) % 2 == 0:
            # "abcd" 4/2 = 2
            #  0123
            mid_minus = len(str_x) // 2 -1
            mid_plus = len(str_x) // 2

            while mid_minus >= 0:
                if str_x[mid_minus] != str_x[mid_plus]:
                    return False
                mid_minus -= 1
                mid_plus += 1
        # odd case
        else:
            mid = len(str_x) // 2
            mid_minus = mid - 1
            mid_plus = mid + 1
            while mid_minus >= 0:
                if str_x[mid_minus] != str_x[mid_plus]:
                    return False
                mid_minus -= 1
                mid_plus += 1
        return True



        