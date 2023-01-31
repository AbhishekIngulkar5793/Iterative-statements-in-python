"""
2. Iterative statements
-for loop
Examples:
=========================================

s = 'Python is simple'
for i in s:
     print(i)
output is:
P
y
t
h
o
n

i
s

s
i
m
p
l
e

Process finished with exit code 0
==============================
s = 'python is simple'
for i in s.split():
    print(i)
output is:
python
is
simple

Process finished with exit code 0
=================================

s = 'python is simple to use code:4567'
# fetch only code from string:4567
output = s.split(':')
print(output[-1])
output is:
4567

Process finished with exit code 0
=============================

s = 'python is simple to use code:4567'
for i in s:
    if i.isnumeric():
        print(i)
output is:
4
5
6
7

Process finished with exit code 0

ht = [5, 5.6, 5.7, 6, 6.2, 4.5, 4.2, 4, 4.8]
#select candidates with ht less than 6
for num in ht:
    #print(num)
    if num < 6:
        print(num)
output is:
5
5.6
5.7
4.5
4.2
4
4.8

Process finished with exit code 0
===============================================

g = [12, 44, 67, 21, 5, 10, 45, 23, 28]
# select num divisible by 5
for num in g:
    if num % 5 == 0:
        print(num)
output is:
5
10
45

Process finished with exit code 0
================================

g = [12, 44, 67, 21, 5, 10, 45, 23, 28, 35]
# select num divisible by 5 and 7
for num in g:
    if (num % 5 == 0) or (num % 7 == 0):
        print(num)
output is:
21
5
10
45
28
35

Process finished with exit code 0
g = [12, 44, 67, 21, 5, 10, 45, 23, 28, 35]
# select num divisible by 5 and 7 & also
# give me the list as an output
k = []
for num in g:
    if(num % 5 == 0) or (num % 7 == 0):
        #print (num)
        k.append(num)
        print('Final list is:', k)
output is:
Final list is: [21]
Final list is: [21, 5]
Final list is: [21, 5, 10]
Final list is: [21, 5, 10, 45]
Final list is: [21, 5, 10, 45, 28]
Final list is: [21, 5, 10, 45, 28, 35]

Process finished with exit code 0
================================

g = [12, 44, 67, 21, 5, 10, 45, 23, 28, 35]
k = []
for num in g:
    if(num % 5 == 0) or (num % 7 == 0):
        #print (num)
        k.append(num)
print('final list is:',k)
output is:
final list is: [21, 5, 10, 45, 28, 35]

Process finished with exit code 0
# we need this output is None:
+++++++++
=========================================
nmes = ['abhishek', 'pooja', 'anisa', 'ganesh', 'ashwini']
# fetch names staring with a
for i in nmes:
    #print(i)
    if i.startswith('a'):
        print(i)
output is:
abhishek
anisa
ashwini

Process finished with exit code 0
=============================================

d = {'name':'python', 'age':32, 'dev':'python.org'}
for i in d:#default it will give keys of dict
    print(i)
==========================================

d = {'name':'python', 'age':32, 'dev':'python.org'}
for i in d:
    print(i, d[i]) # (key,value)
output is :
name python
age 32
dev python.org

Process finished with exit code 0

d = {'name':'python', 'age':32, 'dev':'python.org'}
for i in d.values():
    print(i)
output is:
python
32
python.org

Process finished with exit code 0
==============================================

d = {'name':'python', 'age':32, 'dev':'python.org'}
for i in d.items():
    print(i)
output is:
  ('name', 'python')
('age', 32)
('dev', 'python.org')

Process finished with exit code 0
================================================

# set
s = {1, 2, 3, 1, 2, 3}
for i in s:
    print(i)
output is:
1
2
3

Process finished with exit code 0

s ={1, 3, 1, 'A', 'B', 99, 99}
for i in s:
    print(i)
output is :
1
3
99
A
B

Process finished with exit code 0
===================================
msg = 'chintu got marks 21 24 25'
# display the addition of marks and %
print(msg.split())
data = msg.split()
add = 0
for i in data:
    if i.isnumeric():
        add += int(i)
print('ADDTION IS:', add)
print('AVERAGE IS:', add/3)
output is:
['chintu', 'got', 'marks', '21', '24', '25']
ADDTION IS: 70
AVERAGE IS: 23.333333333333332

Process finished with exit code 0
================================
"""


