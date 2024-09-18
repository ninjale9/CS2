<<<<<<< HEAD
# year= int(input("Please enter the year for testing: "))

# def leapyr(year) : 
#     if year % 400 == 0 :
#         return True 
#     if year % 100 == 0 : 
#         return False 
#     if year % 4 == 0 :
#         return True 
#     return False 

# if leapyr(year) is True :
#     print (f'{year} is a leap year')
# else :
#     print (f'{year}- is not a leap year')

year = int(input("Please enter the year for testing: "))

def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

if is_leap_year(year):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
=======
# year= int(input("Please enter the year for testing: "))

# def leapyr(year) : 
#     if year % 400 == 0 :
#         return True 
#     if year % 100 == 0 : 
#         return False 
#     if year % 4 == 0 :
#         return True 
#     return False 

# if leapyr(year) is True :
#     print (f'{year} is a leap year')
# else :
#     print (f'{year}- is not a leap year')

year = int(input("Please enter the year for testing: "))

def is_leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

if is_leap_year(year):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
>>>>>>> 6f20c37f0abb291a4dfac2a71629878bda92c71c
