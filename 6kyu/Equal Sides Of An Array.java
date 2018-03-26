/**
 *	Solution of the problem 
 *	Equal Sides Of An Array
 *	https://www.codewars.com/kata/5679aa472b8f57fb8c000047
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
public class Kata {
	public static int findEvenIndex(int[] arr) {
		int right= 0;
		int left = 0;

		for (int i = 0; i < arr.length; i++)
			right+=arr[i];

		for (int i = 0; i < arr.length; i++) {
			right -= arr[i];
			if (right==left)
			return i;
			left += arr[i];
		}

		return -1;
	}
}
