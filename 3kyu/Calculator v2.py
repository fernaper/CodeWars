"""
	Solution of the problem 
	Calculator (v2)
	http://www.codewars.com/kata/5235c913397cbf2508000048
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
class Calculator(object):
    def evaluate(self, string):
        return round(eval(string), 12)