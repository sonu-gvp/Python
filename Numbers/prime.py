num = int(input("Enter a number to check prime or not:"))
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count = count + 1
if count == 2:
    print(num, "is prime number.")
else:
    print(num, "is not prime number.")
    
