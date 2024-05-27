# %%
"""
leap years rules
if the year is a multiple of 4
if year is a multiple of 100 then it is not a leap year
  except if it is 400
"""

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if(year % 400 == 0):
                return True
            else:
                return False
        return True
    else:
        return False

start_year = 1582


for year in range(1585, 2023+1):
    if is_leap_year(year):
        print(year)
        
        
        

