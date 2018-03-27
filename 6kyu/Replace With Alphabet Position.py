"""
	Solution of the problem 
	Replace With Alphabet Position
	https://www.codewars.com/kata/546f922b54af40e1e90001da
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def alphabet_position(text):
    text = text.lower()
    ans = ""
    for letter in text:
        if ord(letter) > 96 and ord(letter) < 123:
            ans += str(ord(letter)-96) + " "
        
    return ans[0:-1]