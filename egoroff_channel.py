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



