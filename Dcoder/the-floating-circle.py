'''
Problem Statement
Cody is a student in Trumph Academy, He is preparing for SSC, while he was solving some problems,
he found an easy problem of Circles. 
The problem is You have to calculate the area of a Circle, radius of the circle is given. 
He decided to solve it using code, let us help Cody solving the problem.

Input
Input containts a float number,radius of circle r.

Output
Print area of circle. If the radius is negative or zero then the area would be "0" without quotes. 
PS: Take PI=3.14 and answer should be precise to 2 digit after '.'

Constraints
-1000≤r≤1000

Sample Input
5

Sample Output

78.50

https://code.dcoder.tech/challenges/580601a9ba0d95f40dca3067/the-floating-circle
'''


n = float(input())
pi = 3.14
area = pi * (n**2)
if(n <= 0):
    print("0")
else:
    print("{0:.2f}".format(area))
	