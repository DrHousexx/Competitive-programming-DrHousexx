'''
Problem Statement
You are on a treasure hunt and your team just managed to unlock the treasure chest. 
You brought a bag with a maximum weight capacity of maxW to carry the treasure home. 
The treasure chest has two items each with a certain value and a certain weight. 
Find out the maximum value of treasure that you can take home in your bag. 
You can take both items too if your bag can hold it.

Input
First line of input contains the maximum weight capacity of the bag. 
The second line of input contains the value and weight of item1. 
The third line of input contains the value and weight of item2.

Output
Print the maximum value that you can carry

Constraints
1 ≤ maxW, value1, weight1, value2, weight2 ≤ 1000

Sample Input
20
30 8
50 10

Sample Output

80

https://code.dcoder.tech/challenges/5b192072a2e6485077c2b42d/treasure-hunt
'''


max = int(input())
valora,pesoa = input().split(' ')
valorb,pesob = input().split(' ')
valora = int(valora)
pesoa = int(pesoa)
valorb = int(valorb)
pesob = int(pesob)

if(pesoa + pesob <= max):
    print((valora+valorb))
elif (pesoa <= max and valora > valorb):
    print(valora)
elif (pesob <= max and valorb > valora):
    print(valorb)
else:
    print(0)