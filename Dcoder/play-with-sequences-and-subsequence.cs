/*
Problem Statement
Rick is Professor at Zing University. He teaches Maths there. 
One day he was teaching Sequence, suddenly he came up on a problem, which was taking alot of time.
Cody being a Coder, decided to solve the problem using code, so he just put his mobile out , opened the Dcoder app and started coding. 
Meanwhile his teacher was solving the problem on board, the problem statment was like, There is a sequence of n integers, 
you have to find the longest increasing subsequence of it, in case more than 1 sequence exists, output the earliest one. 
Now this becomes a "Coder vs Mathematician" problem, being a coder lets help Cody in solving the problem first.

Input
First line of the input contains number of elements in the sequence n, next line contains n space separated integers.

Output
Output the longest increasing subsequence in the given sequence.

Constraints
1≤n≤10000 1≤intger values≤100000

Sample Input
5
4 2 6 3 8

Sample Output

4 6 8


https://code.dcoder.tech/challenges/57cd4d1d7b6a33c622e8ee98/play-with-sequences-and-subsequence
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
      string num = Console.ReadLine();
      string[] numas = num.Split(' ');
      int[] nums = new int[N];
      for(int i = 0; i<N;i++)
      {
        nums[i] = int.Parse(numas[i]);
      }
      int aux = nums[0];
      string res = Convert.ToString(aux);
      for(int i = 1; i<N;i++)
      {
        if(nums[i]>aux)
        {
          res = res + " " + Convert.ToString(nums[i]);
        }
      }
      Console.Write(res);
    }
  }
}