'''
Problem Statement
Ross has always been a geek and loves to puzzle his friends. 
His ideas of fun games were always met with bored expressions from Chandler. 
Ross always won the games he invented and Chandler wanted to beat him at least once to end the trail of boring board games. 
Today, Ross invented a new game where he gives his friends a number in its binary form and the first one to convert it to its decimal 
form and say whether its a prime number or not wins the game.

Input
A string representing a positive integer in its binary form.

Output
Print the decimal form of the number in the first line. In the next line, if its a prime number, 
print "Prime" else print "Not Prime", without the double quotes.

Constraints
1 ≤ string.length ≤ 10

Sample Input
10101

Sample Output

21
Not Prime

https://code.dcoder.tech/challenges/5b5c9c9461601549b1d0afcb/the-prime-of-the-binaries
'''

b = input()
b = reversed(b)
y=0
c=0
for n in b:
  c = c + (int(n) * (2**y))
  y+=1
s = 0
print(c)
for i in range(1,int(c)+1):
  if c % i == 0:
    s+=1
if s == 2:
  print("Prime")
else:
  print("Not Prime")