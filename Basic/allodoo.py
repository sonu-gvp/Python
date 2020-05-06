num = int(input("Enter a number to print all odd number."))
for i in range(1, num):
    if(i%2 == 0):
        print("Even Numbers are:", i)
    else:
        print("Odd Numbers are:", i)
