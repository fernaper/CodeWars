/**
 *	Solution of the problem 
 *	Growth of Population
 *	https://www.codewars.com/kata/563b662a59afc2b5120000c6
 *	
 *		@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
 */
class Arge {
    public static int nbYear(int p0, double percent, int aug, int p) {
        int year = 0;
        int population = p0;
        while (population < p) {
			population += population*percent/100 + aug;
			year++;
        }
        return year;
    }
}