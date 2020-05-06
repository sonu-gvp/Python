def oddeven(min1,max1):
    if min1%2==0 and max1%2==0:
       return min(min1,max1)
        
    else:
        return max(min1,max1)
        
print(oddeven(15,11))
