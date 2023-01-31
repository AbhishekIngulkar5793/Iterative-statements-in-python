"""
interview question: After for loop can we use else?
ans= Yes, we can. It is allowed in python
# only a single else is allowed or accepted
# it is rarely used i.e. else after for loop

for i in range(4):
    print(i)
else:
    print('End of loop')
output is:
0
1
2
3
End of loop

Process finished with exit code 0
========================================
# while loop :
- It is a infinite loop
for example,
ex.1:
while 1 == 1:
    print('Python')
    1 != 1
print()
output is :
you will get  printed 'Python' for infinite times
- If we want to make this loop as a finite one,
 then we need an extra variable which will be useful
  to make this condition False
----------------------------------
num = 1
while num == 1:
    print('Python')
    num = 2
ouput is :
Python

Process finished with exit code 0
# which means that as we give an false
argument as in our example we give
num == 1 condition, and as this condition is
True, it will print python in while loop,
but here after print statement we have supplied
num = 2 which is False in front of our condition
i.e. num == 1. Hence we able to finite the while loop.
============================================
- while loop is condition based
- it executes untill the condition is True
- if it becomes False, then it will stop execution of itself.
====================================
#Q.print 1 to 10 numbers using while loop:
num = 1
while  num < 11:
    print('Number is :', num)
    num += 1 #num= num + 1
print()
output is:
Number is : 1
Number is : 2
Number is : 3
Number is : 4
Number is : 5
Number is : 6
Number is : 7
Number is : 8
Number is : 9
Number is : 10


Process finished with exit code 0
==================================================
#Q. do the addition of 1 to 10 numbers using while loop
num = 1
result = 0
while num < 11:
    print(num)
    result += num
    num += 1
print('Addition of 1-10 is :', result)
output is :
1
2
3
4
5
6
7
8
9
10
Addition of 1-10 is : 55

Process finished with exit code 0
=================================================
#Q. 10 - 1 in reverse order using while loop
like, 10 9 8 7 ....... 1
-----------
num = 10
while num > 0:
    print(num)
    num -= 1
output is:
10
9
8
7
6
5
4
3
2
1

Process finished with exit code 0
==================================
#Q. 10 - 1 even numbers in reverse order using while loop
---------
num = 10
while num > 0:
    if num %2 == 0:
        print('EVEN:', num)
    else:
        print('ODD:', num)
    num -= 1
output is :
EVEN: 10
ODD: 9
EVEN: 8
ODD: 7
EVEN: 6
ODD: 5
EVEN: 4
ODD: 3
EVEN: 2
ODD: 1

Process finished with exit code 0
====================================
#Q. Create two separate lists
 FOR odd numbers and even numbers
 with the same problem statement
10 - 1 in reverse order
------
Odd = []
Even = []
num = 10
while num > 0:
    if num %2 == 0:
        Even.append(num)
    else:
        Odd.append(num)
    num -= 1
print('Odd List :', Odd[::-1])
print('Even List :', Even[::-1])


output is :
Odd List : [1, 3, 5, 7, 9]
Even List : [2, 4, 6, 8, 10]

Process finished with exit code 0
========================================
#Q. Do the addition of elements from a list
solution:
Odd = []
Even = []
num = 10
while num > 0:
    if num %2 == 0:
        Even.append(num)
    else:
        Odd.append(num)
    num -= 1
print('Addition of Odd List :', sum(Odd))
print('Addition of Even List :', sum(Even))

Output is:
Addition of Odd List : 25
Addition of Even List : 30

Process finished with exit code 0
======================================
s = input('Enter your name:')
#EX: Abhi5793
# A is a character
# 5 is a number
for i in s:
    if i.isalpha():
        print(i, 'is a character')
    elif i.isdigit():
        print(i, 'Is a number')
    else:
        print(i, 'is a special character')

Output is:
Enter your name:Abhi5793
A is a character
b is a character
h is a character
i is a character
5 Is a number
7 Is a number
9 Is a number
3 Is a number

Process finished with exit code 0
=================================================
#Q.Add a special character also
s = input('Enter your name:')
# ex.- Abhishek5793$@
# A is a character
# 5 is a number
c = 0
le = len(s)
while c < len(s):
    #print(c)
    #print(s[c])
    if s[c].isalpha():
        print(s[c], 'Is a character')
    elif s[c].isdigit():
        print(s[c], 'Is a number')
    else:
        print(s[c], 'Is a special character')
    c += 1
output is:
Enter your name:Abhishek5793$@
A Is a character
b Is a character
h Is a character
i Is a character
s Is a character
h Is a character
e Is a character
k Is a character
5 Is a number
7 Is a number
9 Is a number
3 Is a number
$ Is a special character
@ Is a special character

Process finished with exit code 0
=====================================
index= 0
k = ['se','fm12','#$']
while index < len(k):
    #print(c)
    #print(k[index])
    for i in k[index]:
        if i.isalpha():
            print(i, 'is char')
        elif i.isdigit():
            print(i, 'is a number')
        else:
            print(i, 'is special character')
    index+=1
output is:
s Is character
e Is character
# Is a special character
$ Is a special character

Process finished with exit code 0
=====================================



"""







