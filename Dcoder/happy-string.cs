/*

Problem Statement
A happy string is a string in which each character is lexicographically greater than its next character. 
You are given a positive integer N as an input. You need to print the smallest lexicographical string possible of length N. 
NOTE: All characters in a happy string are in lowercase.

Input
A single integer N.

Output
Print the lexicographically smallest string of length N.

Constraints
1 ≤ N ≤ 26

Sample Input
2

Sample Output

ba

https://code.dcoder.tech/challenges/5b5ee71361601549b1d0b92b/happy-string
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
      //THIS CODE IS VERY NOOB PROGRAMING :v PACMAN FACE!
	  
      int N = int.Parse(Console.ReadLine());

            char[] abc = new char[26];
            abc[0] = 'a';
            abc[1] = 'b';
            abc[2] = 'c';
            abc[3] = 'd';
            abc[4] = 'e';
            abc[5] = 'f';
            abc[6] = 'g';
            abc[7] = 'h';
            abc[8] = 'i';
            abc[9] = 'j';
            abc[10] = 'k';
            abc[11] = 'l';
            abc[12] = 'm';
            abc[13] = 'n';
            abc[14] = 'o';
            abc[15] = 'p';
            abc[16] = 'q';
            abc[17] = 'r';
            abc[18] = 's';
            abc[19] = 't';
            abc[20] = 'u';
            abc[21] = 'v';
            abc[22] = 'w';
            abc[23] = 'x';
            abc[24] = 'y';
            abc[25] = 'z';
            string r = "";
            for (int i = 0; i < N; i++)
            {
                r = abc[i]+r;
            }
            Console.Write(r);
    }
  }
}