/*
	Solution of the problem
	Find the divisors!
	https://www.codewars.com/kata/544aed4c4a30184e960010f4

	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
*/
using System;
using System.Collections.Generic;

public class Kata
{
  public static int[] Divisors(int n)
  {
    List<int> div = new List<int>();
    for (int i = 2; i <= Math.Sqrt(n); i++) {
      if (n % i == 0) {
        div.Add(i);
        if (n/i != i) {
          div.Add(n/i);
        }
      }
    }
    div.Sort((a, b) => a.CompareTo(b));
    int[] ans = div.ToArray();
    if (ans.Length == 0)
      return null;
    return ans;
  }
}
