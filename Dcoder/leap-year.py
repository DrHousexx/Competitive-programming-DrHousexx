'''
Problem Statement
Steve is playing a quiz game with his brother John. 
As Steve just learned the concept of leap year, John wanted to test his knowledge. 
For that, John started to ask Steve whether a year is a leap year or not by giving him a random year. 
Steve is little confused and he asks your help to the quiz.

Input
The first line of input contains one integer T. Next T lines will have years given by John.

Output
For each test case print "Yes" if it is a leap year else "No".

Constraints
1<=T<=100. 10^3<=Year<=10^5.

Sample Input
2
2000
2017

Sample Output

Yes
No

https://code.dcoder.tech/challenges/5b28ea8562db8b46ab2ac711/leap-year
'''

cont = int(input())
lista = []
for i in range(0,cont):
  year= int(input())
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    lista.append("Yes")
  else:
    lista.append("No")
    
for x in range(0,cont):
  print(lista[x])