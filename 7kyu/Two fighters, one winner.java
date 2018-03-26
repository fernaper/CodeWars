/**
 *	Solution of the problem 
 *	Two fighters, one winner.
 *	https://www.codewars.com/kata/577bd8d4ae2807c64b00045b
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
public class Kata {
	public static String declareWinner(Fighter fighter1, Fighter fighter2, String firstAttacker) {
		boolean turn1 = fighter1.name == firstAttacker;
		while (true) {
			if (turn1) {
				fighter2.health -= fighter1.damagePerAttack;
				if (fighter2.health <= 0)
				return fighter1.name;
			} else {
				fighter1.health -= fighter2.damagePerAttack;
				if (fighter1.health <= 0)
					return fighter2.name;
			}
			turn1 = !turn1;
		}
	}
}