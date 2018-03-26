/**
 *	Solution of the problem 
 *	Counting Duplicates
 *	https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
import java.util.HashMap;
import java.util.Map;

public class CountingDuplicates {
	public static int duplicateCount(String text) {
		text = text.toLowerCase();
		Map<Character, Boolean> characters = new HashMap();
		int count = 0;
		for (int i = 0; i < text.length(); i++) {
			if (characters.containsKey(text.charAt(i))) {
				if(characters.get(text.charAt(i))) {
					characters.put(text.charAt(i),false);
					count++;
				}
			} else {
				characters.put(text.charAt(i),true);
			}
		}
		return count;
	}
}