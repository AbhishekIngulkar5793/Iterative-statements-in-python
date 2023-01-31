"""
Transfer statements:
-If we want to suspend a current execute for a while
or permanent then use transfer statements or a block.
It has 3 types:
-break: when condition is mate, it will stop
further execution
-control will come out of the loop
- There are three types of transfer statements :
1. break
2. continue
3. pass
===========================================
-examples on break:
ex.1
fruits = ['mango', 'orange', 'banana', 'apple', 'orange']
for i in fruits:
    #if we get banana then stop iterations
    #print(i)
    if i == 'banana':
        break
        #it won/t proceed further
        #it is not going to continue the loop
    else:
        print(i)
output is:
mango
orange

Process finished with exit code 0
==================================
This is not only way to come out of loop
we can use exit() function
----------------------------------
ex.2
for i in range(11):
    if i == 7:
        exit()
    else:
        print(i)
print('Out of loop')
print(1123123)
output is:
0
1
2
3
4
5
6

Process finished with exit code 0
==========================================
# break will just come out of current loop
# but it will continue next instruction outside the loop
#-----------------
#exit(): will exit from whole program, termination of
current program
-----------------------------
2. continue:
examples on continue;
ex.1
fruits = ['mango', 'orange', 'banana', 'apple', 'banana', 'orange']
for i in fruits:
    if i == 'banana':
        continue
    #it won/t proceed for a current condition
    #but it is going to continue the loop
    else:
        print(i)
output is:
mango
orange
apple
orange

Process finished with exit code 0
==================================
# Q. What is the difference between break and continue??
-
- similarity between break and continue: both skips a element
  at a condition

ex.
for i in range(5):
    if i == 3:
        break
    else:
        print(i)
print('------------------')
output is:
0
1
2
------------------

Process finished with exit code 0
=======================================
ex.4
for i in range(5):
    if i == 3:
        continue
    else:
        print(i)
output is:
0
1
2
4

Process finished with exit code 0
=====================================
# flipkart examples:
problem statement 1: select the prices greater than 500 ie. >500
cart = [1999, 1190, 599, 455, 256, 788, 999, 1000, 178]

for i in cart:
    if i < 500:
        continue
    else:
        print('You have selected an item '
              'with price Rs.', i)
output is:
You have selected an item with price Rs. 1999
You have selected an item with price Rs. 1190
You have selected an item with price Rs. 599
You have selected an item with price Rs. 788
You have selected an item with price Rs. 999
You have selected an item with price Rs. 1000

Process finished with exit code 0
====================================
problem statement 2: select items with price less than
                     500 ie. <500

cart = [1999, 1190, 599, 455, 256, 788, 999, 1000, 178]
for i in cart:
    if i > 500:
        continue
    else:
        print('You have selected the items '
              'with price Rs.', i)
output is:
You have selected the items with price Rs. 455
You have selected the items with price Rs. 256
You have selected the items with price Rs. 178

Process finished with exit code 0
===============================
problem statement 2:
cart = [1999, 1190, 599, 455, 256, 788, 999, 1000, 178]

for i in cart:
    if i < 500:
        print(i, 'delivery charges applied')
        continue
    else:
        print('you have selected an item '
              'with price Rs.', i, 'Free Delivery')
output is:
you have selected an item with price Rs. 1999 Free Delivery
you have selected an item with price Rs. 1190 Free Delivery
you have selected an item with price Rs. 599 Free Delivery
455 delivery charges applied
256 delivery charges applied
you have selected an item with price Rs. 788 Free Delivery
you have selected an item with price Rs. 999 Free Delivery
you have selected an item with price Rs. 1000 Free Delivery
178 delivery charges applied

Process finished with exit code 0
==========================================
3. pass
- pass: it is used as a null statement, empty stub
 when we want to keep/write an empty block then
 use pass.
for example:
if 5 > 2:
    pass # line 179 is a null stub as we can keep it using pass
for i in range(12):
    pass



"""
fruits = ['mango', 'orange', 'banana', 'apple', 'orange', 'banana', 'grapes']

for frt in fruits:
    if frt == 'banana':
       continue
    else:
        print(frt)


print(fruits.count('banana'))





