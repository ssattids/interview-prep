class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        i = len(num1)-1
        j = len(num2)-1
        carryover = 0
        new_num = ""
        while (i >= 0 or j >= 0):
            if i < 0:
                single_sum = ord(num2[j])-ord('0')
            elif j < 0:
                single_sum = ord(num1[i])-ord('0')
            else:       
                single_sum = ord(num1[i])-ord('0') + ord(num2[j])-ord('0')

            single_sum += carryover
            carryover = single_sum // 10
            current_digit = str(single_sum % 10)
            new_num = str(current_digit) + new_num
            i-=1
            j-=1

        if carryover != 0:
            new_num = str(carryover) + new_num

        return new_num

