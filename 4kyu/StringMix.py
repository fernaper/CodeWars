"""
	Solution of the problem
	String Mix
	https://www.codewars.com/kata/5629db57620258aa9d000014

	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
import string
from collections import Counter

def mix(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    ans = []
    for char in string.ascii_lowercase:
        n1 = c1[char]
        n2 = c2[char]
        if n1 > 1 or n2 > 1:
            if n1 > n2:
                ans.append('1:{}'.format(char*n1))
            elif n1 == n2:
                ans.append('=:{}'.format(char*n1))
            else:
                ans.append('2:{}'.format(char*n2))
    ans.sort(key=lambda x:(-len(x),x))
    return '/'.join(ans)
