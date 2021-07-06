'''
Problem Statement
You are given a binary number, you just need to flip each and every bit of it ie. 1 turns to 0 and 0 turns to 1.

Input
Input contains a binary number.

Output
Print the flipped binary number.

Constraints
The binary number can be any binary number of 0 bit to 32 bit.

Sample Input
11100110101

Sample Output

00011001010

https://code.dcoder.tech/challenges/58164a8bba0d95f40dca6050/the-bit-flipper
'''

bin = input()
out = ''
for x in bin:
    if(x == '0'):
        out += '1'
    else:
        out += '0'
        
print(out)