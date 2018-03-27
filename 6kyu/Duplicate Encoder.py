"""
	Solution of the problem 
	Duplicate Encoder
	https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def duplicate_encode(word):
    word = word.lower()
    ans = ""
    for letter in word:
        ans += ')' if word.count(letter) > 1 else '('
    return ans