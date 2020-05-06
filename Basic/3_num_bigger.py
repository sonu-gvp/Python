num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
num3 = int(input("Enter Third Number:"))
if(num1 > num2 and num1 > num3):
    print(num1,"is Biggest among three.")
elif(num2 > num3):
    print(num2,"is Biggest among three.")
else:
    print(num3,"is Biggest among three.")
