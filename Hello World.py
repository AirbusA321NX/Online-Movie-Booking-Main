# 1.)  How to Print
print("Hi")
# How to give spaces in between codes
print("\n\n\n\n\n\n\n\n\n")
# if you want to print value of some variable do not use  ""
a = 96
print(a)
# addition/Subtraction in python

x = input("Enter 1st number")
a = int(x)  # It basically makes ur input as an integer value even if number is 1,2,3,4,5,6...
y = input("Enter 2nd number")
b = int(y)
z = a+b
print(z)
# for getting output as characters like A B C D we use char function
ch = input('enter a char')
print(ch)
# here user entered the character as pqr so char=pqr
# but what if we want 3rd or 4th element of character

print(ch[0])

# USUAL MISTAKE - if u want to write a word and number together we use string in front of number

# but what if we want to evaluate something as it will just tell 1st letter of what ever the position of letter

# for example 2+6-1 , it will print 2
# to evaluate it we use eval function

result = eval(input("enter an expression"))
print(result) # here eval evaluated the expression that user gave to the console rather than just printing it exactly as user have it

m = "boeing"
n = "747"

print(m + str(n))
# indexing in python

name = 'hi'
print(name[0])

# PYTHON
# 012345

print(name[1:4])       # it will  print till 3rd character
# we can directly add character in print of name
print('s' + name)
# len is function used in determining the length of the character
print(len(name))

# introduction to tuple :-

tuple = (1, 2, 3)
print(tuple)
# indexing is possible in tuple also tuple is faster than list
print(tuple[0])
# but tuple is immutable (cannot be changed)

s = {100, 7, 8, 98}  # it basically arranges all number in random order.
print(s)

num = 5
print(id(num)) # it basically tells  where the function is mapped inside your pc  for eg number 5 key  in this case we got 140733787726760
# id is used for identifying the address of the function

# not only for numbers we also have address for any name

name = 'airbus'
print(id(name))  # here we got as 1840525013872

a = '10'
b = '10'

print(id(a))
print(id(b))
# POSSIBLE INTERVIEW QUESTION Q1
# here a=b=10 and we are getting same address (ie 2096949033200) that's why python is more memory efficient than any other language.

# METHODS OF ADDING ELEMENTS IN LIST
# 1.USING APPEND
nums = [1, 2, 64, 26]
nums.append(75)   # append is a function to add another element in the list.

print(nums)

# here append added the value at the end of the list , in order to specifically add the element at a specific position.

# 2. USING INSERT

nums.insert(2, 100)  # here 2 means it will add at 3rd place and 100 is the element we wanted to add.
print(nums)

# Q2 INTERVIEW QUESTION POSSIBLE - WHAT'S DIFFERENCE BETWEEN APPEND AND INSERT ?

# 3. USING EXTEND

nums.extend([6542, 5762, 1762, 454])  # COMMON MISTAKE "USE SQUARE BRACKETS TO WRITE ELEMENTS".

print(nums)

# Basically extend is used to add multiple values at same time   and adds at last.

nums.pop(1)   # it will remove the 2nd element of the list.

print(nums)

# what happen if we do not give any input in pop()

nums.pop()
print(nums)  # it removed the last element  of the list.

# we have another function known as del it deletes the values in list , lets look at the example.

del nums[2:]  # COMMON MISTAKE , DO NOT USE "nums.del".
# here it deleted the values in list which are at position more than 3 , [2: ] means it will delete element from 3rd place  till end.

del nums[0:3]

print(nums)

# POSSIBLE INTERVIEW QUESTION - DIFFERENCE BETWEEN POP AND DEL

k = 10
print(type(k))  # type tells that what type of value constant have like 1 2 3  (integers) or 4.455 6.682 (float values)

M = 2.24
print(type(m))

# Conversion of int to float value and vice a versa :-
# 1.) Float To int
a = 5.6
b = int(a)  # Basically  GINT ( Greatest Integer ) of the number
print(b)
# 2.) Int to Float
L = 9
x = float(L)
print(x)

# COMPLEX NUMBER CAN BE REPRESENTED IN FORM OF LETTER "j" , SEE VIA EXAMPLE.

g = 6+8j
print(type(g))

c = complex(b, L) # it is a technique to create a complex number where b is real part of the complex number and L is imaginary part.
print(c)

# Introduction to Boolean system (True/False)
print(b < L)  # here b is less than L 'so' it printed true.

print(bool(b < L))  # Another way of using boolean systems.

print(int(True))  # value of true is 1
print(int(False))  # value of False is 0

# operators in python

x = 2
x = x+2

print(x)

x += 2  # here += means you are increasing the value of x by a value which is equal to 2
print(x)

print(x*3)

a, b, c, d = 1, 2, 3, 4  # here we can assign multiple value to multiple variables

print(a)
print(b)
print(c)
print(d)

print(a == b) # if we use single = , we are assigning a equal to b ,here double = means we are comaparing and demanding that whether a is equal to b

# just like in mathematics we have greater than and equal to  we denote it by x>= .

# we denote not equal to by !=

print(a != b)

# logical operators

# 1.) And
# 2.) Not
# 3.) Or let's see examples based on there usage

V = 7
C = 9

print(V < 8 and C < 10)  # if both are true then we get true , if both are false or even one of them is false then we get false.

print(V > 80 or C < 90)  # if one of them is true it gives  true , until and unless both are false.

# not is used in reversing the output

x = True
x = not x
print(x)

# introduction to number systems

# 1.) binary format :-

print(bin(25))

# let's see the logic behind how it calculated  the binary format of the number 25.

# 25 is divided by 2  giving remainder 1 and quotient 12                                     1                     ^
# now the  quotient 12 is further divided by 2 giving remainder 0 and quotient 6             0                     |
# now the quotient 6 is divided  by 2 giving remainder 0 and quotient 3                      0                     |
# again doing same process with 3 where we divide 2 with 3 giving remainder 1 and quotient 1 1                     |
# here we ended left with 1 divided by 1 giving remainder 0                                  1  DO NOT  TAKE IT 0  |

# we get 11001 (GO IN REVERSE ORDER)

# how to get binary to integer.

# understanding via example :-

# for Example, we have 1    1   0   0   1
#                    2^4 2^3 2^2 2^1 2^0  (Write powers of 2 in reverse order)
#                    16   8   4   2   1 (IGNORE 4 2 AS THEY ARE MULTIPLYING BY 0)
#     add 16 , 8 ,  1 :- 16+8+1 = 25.

print(0b01010001)  # just simply write it in binary format it will give us integer.

# 2.) Octal Format

print(oct(25))

# 3.) Hexadecimal format

print(hex(99))

print(hex(10))


# "Swapping values of 2 variables" .

d = 5
z = 6
# Method 1

temp = d
d = z
z = temp
print(d)
print(z)

# HIGHLY EXPECTED INTERVIEW QUESTION , Q3 :- How do you swap 2 variables without using a third variable
# Method 2
# we have a direct formula for it

z = z+d
d = z-d
z = z-d

print(z)

# Method 3
# In order to save using extra bit (here bit means we are using is + - but in xor we use only one thing which is ^) we use xor function.

z = z ^ d
d = z ^ d
z = z ^ d

print(z)

# Method 4

z, d = d, z

print(z)
print(d)

# -------------------------------------------------------------------------------------------------------------------------------------
print(-0b11110011)

print(~12)

# compliment of 0 is 1 and compliment of 1 is 0

print(12 & 13)  # & means and (the logical operator)

# 12 is 0b1100 13 is 0b1101

#  001100
#  001101
#  001100 --> 1 and 0 gives 0 , 1 and 1 gives 1

print(12 | 13)  # |  means or (logical operator)

# in case of xor    ^ = xor

# 1^1 =0
# 1^0 =1   #if same then 0 if different 1
# 0^1 =1
# 1^1 =0

# left/right shift operation :-
print(10 << 4) # it is a left shift operation in which the extra 0 is transferred towards the left side of binary form of 10
# 10 is 0b1010.00 after doing 10<<2 it looks like 0b101000
# if it would be 10<<4 then 4 0 will be transferred towards left and looks like 0b10100000
# same works for right shift

# introduction of maths in python :-

import math
x = math.sqrt(25)
print(x)

# -------------    ceiling  (3)


# ---------------  flooring  (2)

print(math.floor(2.9)) # it bascially rounds value of 2.9 to an integer (here floor means that it will round off to a lower integer just like floor is at bottom/low level
print(math.ceil(2.1))  # it basically rounds value of 2.1 to an integer which +1 higher than its  gint ( gint of 2.1 is 2 and ceil of 2.1 = [2.1]+1 =3

x = 7
r = x % 2  # here % tells remainder for example x%2 means what will be remainder if x(i.e 8) is divided by 2

if r == 0:  # common mistake  (DO NOT USE SINGLE "=")
    print("even")
# to  check odd number we have 2 ways
# M-1
if r != 0:
    print("odd")
# M-2 #it is preferred as it increases performance of the code
else:  # else means if number is even print "even" otherwise or else print odd
    print("odd")

y = 19  # Warning-starting the code involving "if" should start from line without using any space
r = y % 2
if r == 0:  # Warning 2 -print must be  written under : symbol
        print("even")
        if y > 1:  # Warning 3 -in case of using another if function/nested if if should be written directly under where there is written print
                print("great")

else:
                      print("odd")

# How  to repeat the function (for n times)

i = 1 # from this value  we start

while i <= 5:
      print("hi")
      i = i +1

# Printing the values 1 2 3 4 5 along hi in order wise via "while loop".
while i <= 5:  # it means it will print hi for 5 times
      print("hi", i)
      i = i + 1

# using while loop in a day to day to life example

# Q- We want to make a wending machine .



# introduction to for loop

P = ['yo', 9, 0]

for i in P:  # it will print the element of list one by one
    print(i)


K = 'hello' # you can print  the letter in  alphabet wise

for i in K:
    print(i)

for i in range(0,10):
    print(i) # it will write counting from 0~9 "WARNING - IT  WILL TYPE FROM 0 TO 9 NOT FROM 0 TO 10"

    # we can also  print an AP (Arithmetic progression) using for loop

    for i in range(0,100,5):
        print(i)

        # for loop is ascending , but we can also type it in descending order

        for i in range(20,11,-1): # technically it will start  printing ap
            print(i)

for i in range(1,21):
    if i%5==0 : # "WARNING -DONOT USE = , USE =="
        print(i)

for i in range(1,21):
    if i%5!=0 :
        print(i)

# using concept of candy machine in while loop

x = int(input("how many candy do you want"))

i=1
while i<=x:
    print("candy")
    i=i+1

# what if user wants  more candy than the machine have

av = 10

# if we want to remove multiple of 3 from the set of number

for i in range (1,101) :

    if i%3==0: # it will skip all the values divisible by 3
        continue # it is a function telling that keep continue if the number gives remainder 0 with 3 and 5

        print(i)

        print("bye")

for i in range(1, 101):

    if i % 2 == 0:  # it will skip all the values divisible by 3
        continue  # it is a function telling that keep continue if the number gives remainder 0 with 3 and 5

    print(i)