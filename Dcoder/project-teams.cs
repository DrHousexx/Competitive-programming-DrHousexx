/*

Problem Statement
There are N students in a class and Teacher want to divide these students into some groups . 
Teacher told  that groups consisting of two or less students not allowed , 
so Teacher want to have as many groups consisting of three or more students as possible. 
Divide the students so that the number of groups consisting of three or more students is maximized.

Input
Single integer N

Output
Maximum number of groups can be formed

Constraints
1<=N<100000

Sample Input
6

Sample Output
2

https://code.dcoder.tech/challenges/5cf3f4881681076686eade89/project-teams
*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

//Compiler version 4.0, .NET Framework 4.5

namespace Dcoder
{
  public class Program
  {
    public static void Main(string[] args)
    {
      //Your code goes here
      int N = int.Parse(Console.ReadLine());
            int udiv = 0;
            N = N /3;
            Console.Write(N);
    }
  }
}