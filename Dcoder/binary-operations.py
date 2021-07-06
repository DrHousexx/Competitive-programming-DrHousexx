'''
Problem Statement
You will be given two numbers, a and b, in their binary form. You need to print their sum and their product in binary.

Input
Two strings separated by space representing the binary values of a and b.

Output
Print their sum(a+b) in the first line. Print their product(a*b) in the second line.

Constraints
1 ≤ string.length ≤ 16

Sample Input
101 10

Sample Output

111
1010

https://code.dcoder.tech/challenges/5b6581c14bc1dd1052db259d/binary-operations
'''

a,b = input().split()

def bintodec(bin):
  dec = 0
  con = len(bin)-1
  for x in range(0,len(bin)):
    aux = int(bin[con]) * (2**x)
    dec += aux
    con -= 1
  return dec

def dectobin(dec):
  bin = ''
  while dec!=0:
    bin = str(dec%2) + bin
    dec = dec // 2
  return bin
  
suma = bintodec(a)+bintodec(b)
mult = bintodec(a)*bintodec(b)
print(dectobin(suma))
print(dectobin(mult))