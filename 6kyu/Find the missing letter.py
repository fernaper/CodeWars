"""
	Solution of the problem 
	Find the missing letter
	https://www.codewars.com/kata/5839edaa6754d6fec10000a2
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def find_missing_letter(chars):
    for i in range(0,len(chars)-1):
        if ord(chars[i])+1 != ord(chars[i+1]):
            return chr(ord(chars[i])+1)
    return 'error'