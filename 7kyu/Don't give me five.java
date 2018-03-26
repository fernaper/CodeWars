/**
 *	Solution of the problem 
 *	Don't give me five!
 *	https://www.codewars.com/kata/5813d19765d81c592200001a
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
public class Kata {
	public static int dontGiveMeFive(int start, int end) {
		int count = 0;
		for (int i = start; i <= end; i++)
			count += containsFive(i)?0:1;
		return count;
	}

	private static boolean containsFive(int i) {
		return String.valueOf(i).contains("5");
	}
}