def chek_even(num):
	return num % 2 == 0
nums = [0,1,2,3,4,5,6,7,8,9,10]
filter(chek_even,nums)
list(filter(chek_even,nums))