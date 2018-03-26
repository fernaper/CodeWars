/**
 *	Solution of the problem 
 *	Ones and Zeros
 *	https://www.codewars.com/kata/578553c3a1b8d5c40300037c
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
import java.util.List;

public class BinaryArrayToNumber {

	public static int ConvertBinaryArrayToInt(List<Integer> binary) {
		int l = binary.size();
		int answer = 0;
		for (int i = 0; i < l; i++)
			answer += binary.get(i)*(int)Math.pow(2,l-i-1);
		return answer;
	}
}