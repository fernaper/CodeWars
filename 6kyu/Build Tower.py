"""
	Solution of the problem 
	Build Tower
	https://www.codewars.com/kata/576757b1df89ecf5bd00073b
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def tower_builder(n_floors):
    tower = []
    for i in range(0,n_floors):
        tower.append(" "*int(n_floors-i-1/2) +"**"*i + "*"+" "*int(n_floors-i-1/2))
    return tower