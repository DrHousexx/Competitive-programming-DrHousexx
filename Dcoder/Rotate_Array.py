'''
Problem Statement
You are given an array of N length. 
You have to rotate the array rightwards by K rotations, that is, 
shift each element to the right by K positions. Print the rotated array.

Input
First line contains N and K. Second line contains N integers denoting the array.

Output
Print the array after the rotation.

Constraints

1 <= N, K <= 100000 1 <= Arr[i] <= 10^9

Sample Input
5 2
1 2 3 4 5

Sample Output

4 5 1 2 3

https://code.dcoder.tech/challenges/5dff4233a1312802b296cfab/rotate-array

'''


n,pos = input().split()
n = int(n)
pos = int(pos)

cadena = input().split(' ')
arr = []

for x in cadena:
  arr.append(x)

for i in range(0,pos):
  arr.insert(0,arr[-1])
  del arr[-1]

aux =''
for c in arr:
  aux = aux + c +' '
  

print(aux)