# https://stepik.org/lesson/296967/step/3?unit=278695 
# Dictionaries
# A program that prints an alphabet dictionary, where the keys are lowercase English characters and the values are the sequence numbers of the letters in the alphabet.
# The beginning of the dictionary is {"a": 1, "b": 2 }. The answer prints the keys and values of this dictionary alphabetically, each pair on a new line.

alphabet = {}
count = 1
from string import ascii_lowercase

for i in ascii_lowercase:
    alphabet[i] = count
    print(i, alphabet[i])
    count += 1


# https://stepik.org/lesson/296964/step/5?unit=278692
# Nested lists
# An integer matrix with N rows and M columns is given. You need to bypass the elements of this matrix from top to left and output the elements in that order in the form of a table. 
# The program takes as input two natural numbers N and M - the number of matrix rows and columns. Each of the following N rows contains M integers - the matrix elements.


n, m = map(int,input(). split())
# c = list(map(int,input().split()))
b = []
for i in range (n):
    b.append(list(map(int,input().split()))) 
    for j in range(1, m+1):
        print(b[i][-j], end = ' ')
    print()
    


# https://stepik.org/lesson/296964/step/6?unit=278692
# Nested lists
# An integer matrix with N rows and M columns is given. You need to bypass the elements of this matrix from left to right from bottom to top and output the elements in that order in the form of a table. 
# The program takes as input two natural numbers N and M - the number of matrix rows and columns. Each of the following N rows contains M integers - the matrix elements.     
    
 
n, m = map(int,input(). split())
b = []
s = []
for i in range (n):
    b.append(list(map(int,input().split()))) 
    for j in range(1, m+1):
        s.append(b[i][-j])

for j in range (n):
    for i in range(1,m+1):

        print(s[-i],end=' ')
    print()     
 
    for i in range(m):
        s.pop()  


# For cycle
# https://stepik.org/lesson/296961/step/5?unit=278689
# Finds the record number of occurrences (not necessarily consecutive) of a character in a string.

st = input().lower()
letters = []
for l in st:
    letters.append(st.count(l))
print(max(letters))


# https://stepik.org/lesson/296961/step/4?unit=278689
# Find the smallest positive value in this list. If there are no positive values, print the line "Empty".

t = list(map(int, input().split()))
while  len(t) > 0 and min(t) <= 0:
    t.remove(min(t))
#    print(t)
if len(t) == 0 or min(t) == 0:
    print('Empty')
elif min(t) > 0:
    print(min(t))


# https://stepik.org/lesson/296961/step/6?unit=278689
# Check the divisibility of a given number by 11.

n = input()
b = []
c = []
for i in range(len(n)):
    if i % 2 == 0:
        b.append(n[i])
    else:
        c.append(n[i])
bs = ''.join(b)
cs = ''.join(c)
q = [int(digit) for digit in bs]
w = [int(digit) for digit in cs]
if abs(sum(q) - sum(w))%11 == 0:
    print('YES')
else:
    print('NO')


    
# https://stepik.org/lesson/296962/step/3?unit=278690
# The program receives as input the number n - the number of elements in the list, then the elements of the list themselves.
# You need to output a sorted list (without using the sorted function).    

n = int(input())
s = list(map(int,input().split()))

a=[]
while len(s)!=0:
    a.append(min(s))
    s.remove(min(s))
print(*a)


# https://stepik.org/lesson/296963/step/8?unit=278691
# The task is to sort the list in ascending order by sorting with inserts, in case the adjacent elements coincide, there is no need to change them. The answer is to output the sorted list.

b=int(input())
a= list(map(int,input().split()))
count=0
for j in range(1,b):
    i=j-1
    while i>=0:
        if a[j]<a[i]:
            a[j],a[i]=a[i],a[j]
            j=j-1
        i = i - 1
print(*a)


# while cycle
# https://stepik.org/lesson/296615/step/8?unit=278349       
# The program takes one natural number as an input and displays the product of digits of that number.


from functools import reduce
from operator import mul
a = list(map(int, input()))
print(reduce(mul,a))



