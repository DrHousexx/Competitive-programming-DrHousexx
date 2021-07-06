'''
Problem Statement
Bob has a floating point number N. 
He wants to set the precision for 2 digits after the decimal point for the number. 
He is not good at coding, hence looking for your help.

Input
The first line contains T, the number of test cases. Next T line contains floating point number N.

Output
Print N in a separate line after setting precision for 2 digits after the decimal point:

Constraints
1 <= T <= 1000 1 <= N <= 10000

Sample Input
1
713.166

Sample Output

713.17

https://code.dcoder.tech/challenges/5e1086efa1312802b296d39f/floating-number
'''

n = int(input())
for i in range(0,n):
  a = float(input())
  a = round(a,2)
  print( "{0:.2f}".format(a))