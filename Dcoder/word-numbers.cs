/*
Problem Statement
Wade is unable to convert a number in its word form. 
Help Wade to convert a number to its word form. For example, the word form of 198 would 'one nine eight'.

Input
A single integer N

Output
Print the word form of N

Constraints
0 ≤ N ≤ 10000

Sample Input
200

Sample Output

two zero zero

https://code.dcoder.tech/challenges/5b195160928314bb78743140/word-numbers
*/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
 // Compiler version 4.0, .NET Framework 4.5


 namespace Dcoder
 {
   public class Program
   {
     public static void Main(string[] args)
     {
       
       string N = Console.ReadLine();
       
       string[] v = new string[10];
       v[0]="zero";
       v[1]="one";
       v[2]="two";
       v[3]="three";
       v[4]="four";
       v[5]="five";
       v[6]="six";
       v[7]="seven";
       v[8]="eight";
       v[9]="nine";
       string r ="";
       
       for(int i =0;i<N.Length;i++)
       {
         r = r + v[int.Parse(N[i].ToString())]+" ";
       }
       Console.Write(r);
     }
   }
 }