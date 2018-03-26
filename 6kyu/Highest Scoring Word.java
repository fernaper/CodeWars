/**
 *	Solution of the problem 
 *	Highest Scoring Word
 *	https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
public class Kata {

	public static String high(String s) {
		String arr[] = s.split(" ");
		int maxSuma = 0;
		int pos = 0;
		for (int i = 0; i < arr.length; i++) {
			int suma = 0;
			for (int j = 0; j < arr[i].length(); j++)
				suma += ((int)arr[i].charAt(j))-96;

			if (suma > maxSuma) {
				maxSuma = suma;
				pos = i;
			}
		}
		return arr[pos];
	}
}