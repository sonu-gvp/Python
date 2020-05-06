num = int(input("Enter a number to check palindrome or not:"))
rev = 0
dummy = num
while(num > 0):
    digit = num % 10
    rev = rev*10 + digit
    num = num//10
if(rev == dummy):
    print(dummy, "is palindrome number")
else:
    print(dummy, "is not palindrome number")
