/**
 *	Solution of the problem 
 *	Sort the odd
 *	https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

public class Kata {
	public static int[] sortArray(int[] array) {
		List<Integer> odds = new ArrayList<>();
		for (int i = 0; i < array.length; i++) {
			if (array[i]%2==1)
				odds.add(array[i]);
		}

		Collections.sort(odds);
		int j = 0;
		for (int i = 0; i < array.length; i++) {
			if (array[i]%2==1) {
				array[i] = odds.get(j);
				j++;
			}
		}

		return array;
	}
}