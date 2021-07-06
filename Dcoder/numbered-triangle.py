'''
Problem Statement
You need to print this pattern upto N. For N = 4, 1 1 2 1 2 3 1 2 3 4

Input
A single positive integer N.

Output
Numbered Triangle upto N. Do not leave trailing whitespaces at the end of each line.

Constraints
1 ≤ N ≤ 9

Sample Input
3

Sample Output

1
1 2
1 2 3

https://code.dcoder.tech/challenges/5b55730fab46cd2f99d3bf80/numbered-triangle
'''

n = int(input())
for i in range(1,n+1):
  aux = ''
  for j in range(1,i+1):
    aux += str(j) + ' '
  final_str=aux[:-1]
  print(final_str)