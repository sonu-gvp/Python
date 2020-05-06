year = int(input("Enter a year:"))
if(year%400 == 0 or year%4 == 0):
    print(year,"is leap year.")
else:
    print(year,"is not leap year.")
