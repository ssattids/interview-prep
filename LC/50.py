class Solution:

    def myPow(self, x: float, n: int) -> float:
        """
            The trick is:
                - if you square the number
                - you can half the power
                - e.g. 2^8 == 4^4 == 16^2
                    = 2*2*2*2*2*2*2*2 = 256
                    = 4*4*4*4 = 256
                    = 16*16 = 256
        """

        abs_n = abs(n)
        if abs_n == 0:
            pow_res = 1
        elif abs_n == 1:
            pow_res = x
        elif abs_n % 2 == 1:
            pow_res = x * self.myPow(x * x, (abs_n - 1) // 2)
        else:
            pow_res = self.myPow(x * x, abs_n // 2)

        if n < 0:
            return 1 / pow_res
        else:
            return pow_res

    
    def myPow_dict(self, x: float, n: int) -> float:
        
        my_pow_res = {
            0 : 1,
            1 : x,
            2 : x*x
        }

        def my_pow(x, n):
            
            if n in my_pow_res:
                return my_pow_res[n]
            else:
                res = my_pow(x, n//2) * my_pow(x, n//2) * my_pow(x, n%2)
                my_pow_res[n] = res
                return res

        my_n = abs(n)
        pow_res = my_pow(x, my_n)

        if n < 0:
            return 1 / pow_res
        else:
            return pow_res

