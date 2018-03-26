/**
 *	Solution of the problem 
 *	Take a Ten Minute Walk
 *	https://www.codewars.com/kata/54da539698b8a2ad76000228
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
public class TenMinWalk {
	public static boolean isValid(char[] walk) {
		if (walk.length != 10)
			return false;
		int n = 0;
		int e = 0;
		for (int i = 0; i < walk.length; i++) {
			if (walk[i] == 'n')
				n++;
			else if (walk[i] == 's')
				n--;
			else if (walk[i] == 'e')
				e++;
			else
				e--;
		}

		return e == 0 && n == 0;
	}
}