x=25
def printer():
     x=50
     return x

print(x)
25
print(printer())
50



>>> f = lambda x : x**2
>>> f
<function <lambda> at 0x02DD5108>
>>> f(x)
625
>>> x
25


name="this is a global name"
>>> def greet():
...     name="Sammy"
...     def hello():
...             print("hello"+name)
...     hello()
...
>>> greet()
helloSammy

>>> print(name)
This is a global name


x = 50
>>> def func():
...     global x
...     print("This function is nuw using the global x!")
...     print("Because of global x is:",x)
...     x = 2
...     print("Run func(), changed global x to",x)
print("Before calling func(),x is:",x)
func()
print("Value of x(outside of func())is",x)
...
>>> func()
This function is nuw using the global x!
Because of global x is: 50
Run func(), changed global x to 2
Before calling func(),x is: 2



>>> def myfun(*argv):
...     for arg in argv:
...             print(arg)
...
>>> myfun("Hello","welcome","to","gvp")
Hello
welcome
to
gvp


>>> def myfun(**kwargs):
...     for key,value in kwargs.items():
...             print("%s==%s"%(key,value))
...
>>> myfun(first="geeks",mid='for',last='geeks')
first==geeks
mid==for
last==geeks

>>> def myfun(arg1,**kwargs):
...     print(arg1)
...     for key,value in kwargs.items():
...             print("%s==%s"%(key,value))
...
>>> myfun("Hi",first="geeks",mid='for',last='geeks')
Hi
first==geeks
mid==for
last==geeks


>>> def myfunc(**kwargs):
...     if 'fruit' in kwargs:
...             print("My favorite fruit is {kwargs['fruit']}")
...     else:
...             print("I dont like fruit")
...
>>> myfunc(fruit="Apple")
My favorite fruit is {kwargs['fruit']}
>>> myfunc(sweet="Apple")
I dont like fruit


>>> def myfunc(*arg,**kwargs):
...     if 'fruit' and 'juice' in kwargs:
...              print(f"my favorite fruit is {kwargs['fruit']}")
...              print(f"may i have some {kwargs['juice']}juice?")
...     else:
...             pass
...
>>> myfunc('eggs','spam',fruit='apple',juice='orange')
my favorite fruit is apple
may i have some orangejuice?


>>> def func(radius):
...     return 4/3*3.14*radius**3
...
>>> func(3)
113.03999999999999



>>> def ran_check(x,y,z):
...     if x in range(y,z):
...             print(x)
...
>>> ran_check(5,2,7)
5
>>> ran_check(10,2,7)
>>>


>>> def ran_check(x,y,z):
...     return x in range(y,z)
...
>>> ran_check(5,2,7)
True
>>> ran_check(10,2,7)
False




>>> def fun(s):
	d={"low":0,"upr":0}
	for i in s:
		if i.islower():
			d["low"]+=1
		elif i.isupper():
			d["upr"] =+1
		else:
			pass
	print(d["low"])
	print(d["upr"])

	
>>> fun(s)
5
0
>>> s
'hello'
>>> 