num = int(input("Enter a number to print all armstrong number:"))
for i in range(1, num+1):
    add = 0
    temp1 = i
    temp2 = i
    while(temp1 > 0):
        digit = temp1 % 10
        add = add + (digit*digit*digit)
        temp1 = temp1 // 10
    if(temp2 == add):
        print(add)
