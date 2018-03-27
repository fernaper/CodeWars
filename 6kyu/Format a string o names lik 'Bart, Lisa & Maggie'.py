"""
	Solution of the problem 
	Format a string o names lik 'Bart, Lisa & Maggie'
	https://www.codewars.com/kata/53368a47e38700bd8300030d
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def namelist(names):
    ans = ""
    if len(names) == 1:
        return names[0]['name']
    for i in range(0,len(names)-1):
        ans += names[i]['name'] + ", " if i+1 < len(names)-1 else names[i]['name'] + " & " + names[i+1]['name']
        
    return ans