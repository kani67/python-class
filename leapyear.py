#-----------------------------------------------------------------------
# leapyear.py
#-----------------------------------------------------------------------


import sys

# Accept an int year as a command-line argument. Write True to
# standard output if year is a leap year.  Otherwise write False.

#year = int(sys.argv[1])

value1 = input("Year? ")
year = int(value1)

isLeapYear = (year % 4 == 0)
isLeapYear = isLeapYear and (year % 100 != 0)
isLeapYear = isLeapYear or  (year % 400 == 0)

print(isLeapYear)

#-----------------------------------------------------------------------

# python leapyear.py 2016    
# True

# python leapyear.py 1900 
# False

# python leapyear.py 2000
# True


