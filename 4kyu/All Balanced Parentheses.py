"""
	Solution of the problem
	All Balanced Parentheses
	https://www.codewars.com/kata/5426d7a2c2c7784365000783

	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def balanced_parens(n):
    if n == 0:
        return ['']
    elif n == 1:
        return ['()']

    ans = []
    for entry in balanced_parens(n-1):
        for i in range(len(entry)):
            ans.append('()' + entry)
            ans.append(entry + '()')
            ans.append(entry[:i] + '()' + entry[i:])
            ans.append('(' + entry[:i] + ')' + entry[i:])
            ans.append('(' + entry[:i] + entry[i:] + ')')
            ans.append(entry[:i] + '(' + entry[i:] + ')')
    return list(set(ans))
