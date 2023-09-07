def isLeapYear(year):
 if (year % 4 == 0 and year % 100 == 0)or year % 400 == 0:
   return True
 else:
   return False

Year = int(input("enter a year:"))
if isLeapYear:
  print(Year,"is a leap year.")
else:
  print(Year,"is not a leap year")
  

  