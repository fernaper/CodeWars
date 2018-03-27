"""
	Solution of the problem 
	Categorize New Member
	https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def openOrSenior(data):
    ans = []
    for item in data:
        if item[0] >= 55 and item[1] > 7:
            ans.append('Senior')
        else:
            ans.append('Open')
        
    return ans