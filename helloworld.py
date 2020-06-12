# getting started
print("Hello! World" )
# learning about the if statements
a= 12
b= 3
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")
# Creating a variable
x=5
y=-12
print(x/y)
# creating a defining function
x = "awesome"

def myfunc():
    print('Python is ' + x)

myfunc()
    
# normally, when u create a variable inside a function, that variable is
# local, and can only be used inside that fuction
# creating a global function
def coco():
    global x
    x = "fantastic"

coco()
print('python is ' + x)

#one more example of global function
x = "awesome"
def myfunc():
    global x
    x ='fantastic'

myfunc()
print("python is "+ x)

