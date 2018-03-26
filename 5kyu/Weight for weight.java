/**
 *	Solution of the problem 
 *	Weight for weight
 *	https://www.codewars.com/kata/55c6126177c9441a570000cc
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
import java.util.Arrays;

public class WeightSort {

	public static String orderWeight(String strng) {
		String weights[] = strng.split(" ");

		Arrays.sort(weights, new java.util.Comparator<String>() {
			@Override
			public int compare(String s1, String s2) {
				int v1 = 0;
				for (int i = 0; i < s1.length(); i++) {
					int valor = (int)s1.charAt(i)-48;
					if (valor <= 9) { // Its a number
						v1 += valor;
					}
				}
				int v2 = 0;
				for (int i = 0; i < s2.length(); i++) {
					int valor = (int)s2.charAt(i)-48;
					if (valor <= 9) { // Its a number
						v2 += valor;
					}
				}
				if (v1-v2 == 0)
					return s1.compareTo(s2);

				return v1 - v2;// comparision
			}
		});
		return String.join(" ", weights);
	}
}