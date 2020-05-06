num = int(input("Enter a number"))
years = num//365
weeks = (num%365)//7
days = (num%365)%7
print("Year:",years,"\nWeeks:",weeks,"\nDays:",days)
