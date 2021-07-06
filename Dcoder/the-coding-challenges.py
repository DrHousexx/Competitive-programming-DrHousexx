'''

Problem Statement
There are n participants appearing for one on one coding challenge.
Each participant plays twice (challenges) with each of his opponents.
You need to compute the total number of challenges.

Input
First line contains an integer n, represent number of participants.

Output
Print the total number of challenges.

Constraints
1≤n≤100

Sample Input
16

Sample Output

240

https://code.dcoder.tech/challenges/58263370a153276059495787/the-coding-challenges
'''

n = int(input())
n = (n**2) - n
print(n)