"""
	Solution of the problem 
	Anagram Detection
	https://www.codewars.com/kata/529eef7a9194e0cbc1000255
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def is_anagram(test, original):
    test = test.lower();
    original = original.lower();
    if len(test) != len(original):
        return False
    
    for key in test:
        if test.count(key) != original.count(key):
            return False
        test.replace(key,"");
        original.replace(key,"");
    
    return True