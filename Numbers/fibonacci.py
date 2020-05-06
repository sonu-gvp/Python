num = int(input("Enter a number to calculte fibonacci seris:"))
a = 0
b = 1
print(a,b)
for i in range(2, num):
    c = a + b
    a = b
    b = c
    print(c)
    
    
