'''
Problem Statement
Joey went for shopping. The shopkeeper gives a discount of 10% if the total expense exceeds 1000 .
 Given total expense as input, write a program to calculate the total money Joey has to give to the shopkeeper after the discount, 
 if discount is applicable.

Input
The first line contains an integer T, total number of test cases. The next T lines consist of an integer each representing total cost.

Output
Print the total money Joey has to pay after the discount. The precision must be upto 2 decimal places.

Constraints
1 ≤ T ≤ 100 1 ≤ total_cost ≤ 100000

Sample Input
2
900
1100

Sample Output

900.00
990.00

https://code.dcoder.tech/challenges/5b2134b1ac71d7305eae7a0d/total-expenses
'''

n = int(input())
for i in range(0,n):
    monto = float(input())
    if monto > 1000:
        monto = monto - (monto * 0.10)
    print("{0:.2f}".format(monto))