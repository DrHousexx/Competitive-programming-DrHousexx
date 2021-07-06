/*

Problem Statement
All numbers in NumberLand are standing in a circle for a dancing ceremony. 
Every number needs a dancing partner. Dancing partner of any number is the number which is standing radially opposite to it in the circle. 
The numbers are from 0 to N-1. A certain number X wants to know who will be its dancing partner. Please help X.

Input
Two positive integers denoting the value of N and X.

Output
Print the number radially opposite to X in a circle of N numbers.

Constraints
4 ≤ N ≤ 20 0 ≤ X < N

Sample Input
8 2

Sample Output

6

https://code.dcoder.tech/challenges/5b85bc2bb6415039901fa9d4/circle-of-numbers
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
      string numst = Console.ReadLine();
            string[] nums = numst.Split(' ');
            int[] num = new int[nums.Length];
            for (int i = 0; i < nums.Length; i++)
            {
                num[i] = int.Parse(nums[i]);
            }
            int N = num[0];
            int N2 = num[1];

            N = N / 2;
            if (N2 >= N)
                N2 = N2 - N;
            else if (N2 < N)
                N2 = N2 + N;

            Console.Write(N2);
    }
  }
}