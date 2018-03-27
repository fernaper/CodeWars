"""
	Solution of the problem 
	Find next perfect square!
	https://www.codewars.com/kata/56269eb78ad2e4ced1000013
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
import math

def find_next_square(sq):
    n = math.sqrt(sq) + 1
    return n*n if n == int(n) else -1