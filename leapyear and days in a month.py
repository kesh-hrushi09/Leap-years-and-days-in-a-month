year = int(input("Enter a year: "))
month = int(input("enter a month: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("its a leap year")
elif year % 100 == 0:
    print("its not a leap year")

    
if month < 1 or month > 12:
    print("invalid month enter in range 1 - 12: ")
    month = int(input("enter a month"))
    
elif month == 2:
    print("february has 29 in leap year and 28 in not leap years")
elif month / 2 != 0:
    print(f"month {month} has 31 days")
else:
    print(f"month {month} has 30 days")