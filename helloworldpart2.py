x=12
y=13
z=14

a=complex(x)

print(a)
# python string
b ="""lorem50 sdfhfh hosfo shf fh sf fsoo fs s s fs ofs gshdd gd  sfgsjfsg fa
h fiifhdsfhghsdfihgi"""

print(b)
# string are array
c='hello, world'
print(c[1])
d='  hello, world  '
print(d[-5:-2])
print(len(d))
# string method
print(d.strip())# thsi method removes the white spaces from the beginning and the end
print(d)# whitespaces are the bank or the spaces


print(d.lower())# to turn hte string into the lower case
#similarly
print(d.upper())
print(d.replace('h', 'co'))# to replace something in the string

# now to Check if the phrase "ain" is present in the following text
txt = 'the rain in spain stays mainly in the plain'
x = 'ain' in txt
print(x)
# now to Check if the phrase "ain" is NOT present in the following text
y = "abcd" not in txt
print(y)

# String Format
##age = 36    # way of printing string format is not possible because, it doesn't work in this way
##txt ="My name is john, I am" + age   #printing int and str at the the same time is not possible
##pirnt(txt)

# for the above thing to work, we will have to use format()
age = 36
txt ="My name is john, I am {}"
print(txt.format(age))

# one more example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#one more example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# escape character
pxp ="we are the so-called \"Viking\"from the north."
print(pxp)#did u see that \\ symbol, it is used to insert the "" in the statement



