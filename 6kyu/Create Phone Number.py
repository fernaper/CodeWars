"""
	Solution of the problem 
	Create Phone Number
	https://www.codewars.com/kata/525f50e3b73515a6db000b83
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def create_phone_number(n):   
    ans = '('+''.join(str(e) for e in n)
    return ans[0:4] + ") " + ans[4:7] + "-" + ans[7:]