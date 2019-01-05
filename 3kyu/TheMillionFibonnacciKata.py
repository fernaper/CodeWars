"""
	Solution of the problem
	The Million Fibonnacci Kata
	http://www.codewars.com/kata/53d40c1e2f13e331fc000c26

	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def calc(num):
    if num == 0:
        return (0, 1)
    elif num == 1:
        return (1, 1)
    else:
        first, second = calc(num // 2)
        p = first * (2 * second - first)
        q = second * second + first * first
        return (p, q) if num % 2 == 0 else (q, p + q)

def fib(n):
    if n < 0:
        return -calc(-n)[0] if n % 2 ==0 else calc(-n)[0]
    return calc(n)[0]
