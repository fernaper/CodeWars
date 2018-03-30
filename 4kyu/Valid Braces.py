"""
	Solution of the problem 
	Valid Braces
	https://www.codewars.com/kata/5277c8a221e209d3f6000b56
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def validBraces(string):
    size = len(string)+1
    while len(string) != size:
        size = len(string)
        string = string.replace("()","")
        string = string.replace("{}","")
        string = string.replace("[]","")
        if len(string)==0:
            return True
        
    return False