/**
 *	Solution of the problem 
 *	Square Every Digit
 *	https://www.codewars.com/kata/546e2562b03326a88e000020
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
public class SquareDigit {

	public int squareDigits(int n) {
		int a = n;
		int d = 0;
		int answer = 0;
		while (a!=0) {
			int rest = a%10;
			a = a/10;
			answer += rest*rest*(int)Math.pow(10,d);
			System.out.println("d= " + d + "," + (rest*rest));
			d = (rest*rest)>9?d+2:d+1;
		}
		return answer;
	}
}