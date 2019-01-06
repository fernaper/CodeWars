"""
	Solution of the problem
	Strip Comments
	https://www.codewars.com/kata/51c8e37cee245da6b40000bd

	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def solution(string,markers):
    ans = []
    for line in string.split('\n'):
        for marker in markers:
            index = line.find(marker)
            if index != -1:
                line = line[:index]
        ans.append(line.strip())
    return '\n'.join(ans)
