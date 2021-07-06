'''
Problem Statement
Cody is stuck in a problem and needs your help to get out of trouble. 
He was given a sorted array by his teacher. After his teacher left, he mistakenly rearranged some elements of the array. 
Help Cody sort the array before his teacher arrives.

Input
The first line of input contains N, the number of elements in the array A. The second line of input contains N space separated integers.

Output
Print the sorted array.

Constraints
3 ≤ N ≤ 50 -1000 ≤ A[i] ≤ 1000

Sample Input
5
8 4 12 2 10

Sample Output

12 10 8 4 2

https://code.dcoder.tech/challenges/5b191e3abe95b1e16447882e/help-cody
'''

n = int(input())
arr = input().split()
lista = []
text = ""
for x in arr:
    lista.append(int(x))
lista.sort(reverse = True)
for x in lista:
    text = text + str(x) + ' '
print(text)