num1 = int(input("Enter first number for starting add:"))
num2 = int(input("Enter second number to add till:"))
add = 0
for i in range(num1, num2+1):
    if i % 2 == 0:
       add = add + i
print(add)
    
