"""
#Patteren Programs
example:
*
* *
* * *
* * * *
* * * * *
=======================================
logic is:

for i in range(1, 6):
    print(i * '*')
output is:
*
**
***
****
*****

Process finished with exit code 0
==========================================
By using for loop we can do such patterns called as pattern programs.

#for reverse pattern

for i in range(5, 0, -1):
    print(i * '*')
output is:
*****
****
***
**
*

Process finished with exit code 0
=========================================
A
AB
ABC
ABCD
ABCDE

chr(): gives a unicode/character using a number
ord(): gives a number behind single character
A
BB
CCC
DDDD
EEEEE
--------------------------------------

for i in range(1,6):
    print(chr(64 + i) * i)
output is:
A
BB
CCC
DDDD
EEEEE

Process finished with exit code 0

for i in range(3): # outer rows
    for j in range(6): # inner columns
        print(i, j, end=' ')
    print()
output is:
0 0 0 1 0 2 0 3 0 4 0 5
1 0 1 1 1 2 1 3 1 4 1 5
2 0 2 1 2 2 2 3 2 4 2 5

Process finished with exit code 0
===========================================

# 3 rows and 6 columns
for i in range(3):#outer ROWS
    for j in range(i + 1):#inner COLUMNS
        print(i,j,end=' ')
    print()
output is:
 0 0
1 0 1 1
2 0 2 1 2 2

Process finished with exit code 0

for i in range(10):
    for j in range(1, 6):
        print(j * 10 + i + 1, "\t", end= "" )
    print()
output is:
11 	21 	31 	41 	51
12 	22 	32 	42 	52
13 	23 	33 	43 	53
14 	24 	34 	44 	54
15 	25 	35 	45 	55
16 	26 	36 	46 	56
17 	27 	37 	47 	57
18 	28 	38 	48 	58
19 	29 	39 	49 	59
20 	30 	40 	50 	60

Process finished with exit code 0
============================================
for i in range(1, 11):
    for j in range(10, 51, 10):
        print(i + j, "\t", end="")
    print()
output is:
11 	21 	31 	41 	51
12 	22 	32 	42 	52
13 	23 	33 	43 	53
14 	24 	34 	44 	54
15 	25 	35 	45 	55
16 	26 	36 	46 	56
17 	27 	37 	47 	57
18 	28 	38 	48 	58
19 	29 	39 	49 	59
20 	30 	40 	50 	60

Process finished with exit code 0
=================================
"""

