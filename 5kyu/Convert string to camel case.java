/**
 *	Solution of the problem 
 *	Convert string to camel case
 *	https://www.codewars.com/kata/517abf86da9663f1d2000003
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
import java.lang.StringBuilder;
class Solution{
	static String toCamelCase(String s){
		for (int i = 0; i < s.length()-1; i++) {
			char letra = s.charAt(i);
			if (letra == '-' || letra == '_') {
				String c = String.valueOf(Character.toUpperCase(s.charAt(i+1)));
				s = s.substring(0,i)+c+s.substring(i+2);
			}
		}
		return s;
	}
}