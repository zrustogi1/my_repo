print("hello world!")

# this is a comment

'''
this is for a lot of comments
used often to describe function
'''

# this is a comment
# describing a functio
# here is the input

x = 100
print(x)
x=5.5
print(x)
x="hello"
x=[1,2,3]
print(x)

x=100
y=10
z=x/y
print(z)
z=int(z)
print(z)

result=x//y
print(result)

min_val=min(10,2)
print(min_val)
raised=pow(2,4)
print(raised)
raised=2**4
print(raised)

if x<0:
    print("x is less than 0")
    print("another line of code")

if x<0 and y<0:
    print("both less than 0")

if x<0 or y<0:
    print("at least one less than 0")


if x<0:
    print("less than 0")
elif x<0:
    print("greater than 0")
else:
    print(0)

counter=0
while counter < 10:
    print(counter)
    counter += 1

for i in range(5):
    print(i)

for i in range(2,5):
    print(i)

lst=[1,2,3,4,5]
for i in range(1,len(lst)):
    print(i, lst[i])

for i in range(len(lst)-1, -1, -1):
    print(i, lst[i])

for i, val in enumerate(lst):
    print(i, val)

for val in lst:
    print(val)

def hello(name="Bob"):
    print("hello",name)
hello("Jamie")

full_name="Kathleen Marie Malone"
first_name=full_name[:8]
middle_name=full_name[9:14]
last_name=full_name[15:]
first_initial=full_name[0]
last_char=full_name[-1]