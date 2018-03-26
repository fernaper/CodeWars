/**
 *	Solution of the problem 
 *	Reverse polish notation calculator
 *	https://www.codewars.com/kata/52f78966747862fc9a0009ae
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
import java.util.Stack;

public class Calc {
	public double evaluate(String expr) {
		String [] arr = expr.split(" ");
		Stack<Double> parcial = new Stack();
		for (int i = 0; i < arr.length; i++) {
			double f,s;
			switch(arr[i]) {
				case "+":
					parcial.push(parcial.pop()+parcial.pop());
					break;
				case "-":
					f = parcial.pop();
					s = parcial.pop();
					parcial.push(s-f);
					break;
				case "*":
					parcial.push(parcial.pop()*parcial.pop());
					break;
				case "/":
					f = parcial.pop();
					s = parcial.pop();
					parcial.push(s/f);
					break;
				default: // Number
					try {
						parcial.push(Double.parseDouble(arr[i]));
					} catch(NumberFormatException ex) {}
			}
		}
		return parcial.empty()?0:parcial.pop();
	}
}