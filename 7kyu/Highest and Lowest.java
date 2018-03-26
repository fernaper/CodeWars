/**
 *	Solution of the problem 
 *	Highest and Lowest
 *	https://www.codewars.com/kata/554b4ac871d6813a03000035
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
public class Kata {
	public static String HighAndLow(String numbers) {
		String[] n = numbers.split(" ");
		int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
		try {
			for (int i = 0; i < n.length; i++) {
				int elem = Integer.parseInt(n[i]);
				if (elem > max)
					max = elem;
				if (elem < min)
					min = elem;
			}
		} catch(NumberFormatException ex) {
			return "error";
		}

		return max + " " + min;
	}
}