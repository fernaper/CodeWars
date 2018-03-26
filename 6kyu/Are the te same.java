/**
 *	Solution of the problem 
 *	Are they the "same"?
 *	https://www.codewars.com/kata/550498447451fbbd7600041c
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
 public class AreSame {
	public static boolean comp(int[] a, int[] b) {
		if (a == null || b == null || a.length != b.length)
			return false;

		boolean[] c = new boolean[a.length];
		for (int i = 0; i < a.length;i++)
			c[i] = true;

		for (int i = 0; i < a.length; i++) {
			boolean done = false;
			for (int j = 0; j < b.length; j++) {
				if (c[j] && comp(a[i],b[j])) {
					done = true;
					c[j] = false;
					break;
				}
			}
			if (!done)
				eturn false;
		}
		return true;
	}

	public static boolean comp(int a, int b) {
		return a == b*b || a*a==b;
	}
}