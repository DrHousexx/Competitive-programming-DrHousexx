'''
Problem Statement
You will be given a positive integer in its decimal form. You need to convert it to its binary form, 
reverse the bits, and then convert the number back to its decimal form. For example, N = 6. Binary form = 110. 
Reversed binary form = 011 Decimal form = 3(answer)

Input
First line contains T, the no. of test cases. Each test case contains N, a positive integer, in a new line.

Output
For each test case, print the resultant decimal form in a new line.

Constraints
1 ≤ T ≤ 100 1 ≤ N ≤ 2^16

Sample Input
2
11
18

Sample Output

13
9

https://code.dcoder.tech/challenges/5b220bfa1831d87e6d179e50/reverse-bits
'''

n = int(input())

for i in range(0,n):
  b=""
  c=0
  y=0
  a = int(input())
  while(a != 0):
    b = str(a % 2) + b
    a = a//2
  for n in b:
    c = c + (int(n) * (2**y))
    y+=1
  print(c)