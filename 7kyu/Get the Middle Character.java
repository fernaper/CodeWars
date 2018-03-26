/**
 *	Solution of the problem 
 *	Get the Middle Character
 *	https://www.codewars.com/kata/56747fd5cb988479af000028
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
class Kata {
	public static String getMiddle(String word) {
		int l = word.length();
		if (l%2==1)
			return word.substring(l/2,(l/2)+1);
		return word.substring(l/2-1,l/2+1);
	}
}