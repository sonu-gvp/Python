num = int(input("Enter number to add all digits in the number:"))
add = 0
while(num > 0):
    digit = num%10
    add = add + digit
    num = num//10
print(add)
