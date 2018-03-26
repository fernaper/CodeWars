/**
 *	Solution of the problem 
 *	Checking Groups
 *	https://www.codewars.com/kata/54b80308488cb6cd31000161
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
public class Groups{
	public static boolean groupCheck(String s){
		int size;
		do {
			size = s.length();
			s = s.replaceAll("\\(\\)","").replaceAll("\\[\\]","").replaceAll("\\{\\}","");
			if (s.length() == 0)
				return true;
		} while (s.length() != size);
		return false;
	}
}