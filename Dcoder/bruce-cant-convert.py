'''
Problem Statement
Bruce is having a hard time in his college trying to learn. 
He recently attended a lecture of "Number Theory" and was given an assignment on base conversion. 
He is given a decimal number and he needs to convert it to a number in a given base B. 
You need to help Bruce by writing a code that helps him to convert a decimal number to any base(2 ≤ B ≤ 16).

Input
First line of input contains T, the number of test cases. Next T lines contain two integers each, N and B, 
representing the decimal integer and the base it needs to be converted to.

Output
For each test case, print the converted number in a new line.

Constraints
1 ≤ T ≤ 100 1 ≤ N ≤ 10^5 2 ≤ B ≤ 16

Sample Input
3
154 16
24 8
21 11

Sample Output

9A
30
1A

https://code.dcoder.tech/challenges/5b1f6874dcb043933f06cbcf/bruce-cant-convert
'''

n = int(input())

def convertor(num,bas):
    conv = ''
    while num!=0:
        if str(num%bas) == '10':
            conv = 'A' + conv
        elif str(num%bas) == '11':
            conv = 'B' + conv
        elif str(num%bas) == '12':
            conv = 'C' + conv
        elif str(num%bas) == '13':
            conv = 'D' + conv
        elif str(num%bas) == '14':
            conv = 'E' + conv
        elif str(num%bas) == '15':
            conv = 'F' + conv
        else:            
            conv = str(num%bas) + conv
        num = num // bas
    return conv

for i in range(0,n):
    num,bas = input().split()
    print(convertor(int(num),int(bas)))