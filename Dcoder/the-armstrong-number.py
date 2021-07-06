'''
Problem Statement
An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. 
For example, consider the number 371. The sum of the cube of its digits is 3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371. 
Therefore, 371 is an Armstrong Number. Given a 3 digit integer, determine whether the number is Armstrong Number or not. 
If it is, print "YES" else print "NO", without the quotes.

Input
A 3-digit integer N.

Output
"YES" or "NO", without the quotes

Constraints
100 ≤ N ≤ 999

Sample Input
371

Sample Output

YES

https://code.dcoder.tech/challenges/5b1b76608c7f54cf188ed87d/the-armstrong-number
'''

n = int(input())
a = n // 100
b = (n % 100) // 10
c = n % 10

if ((a**3) + (b**3) + (c**3)) == n:
    print("YES")
else:
    print("NO")
    