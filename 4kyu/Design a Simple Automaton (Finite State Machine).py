"""
	Solution of the problem 
	Design a Simple Automaton (Finite State Machine)
	https://www.codewars.com/kata/5268acac0d3f019add000203
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
class Automaton(object):

    def read_commands(self, commands):
        state = 1
        for a in commands:
            if state == 1:
                if a == "1":
                    state = 2
            elif state == 2:
                if a == "0":
                    state = 3
            else:
                state = 2
            
        return state == 2

my_automaton = Automaton()