"""
	Solution of the problem
	Decode the morse code advanced
	https://www.codewars.com/kata/5672682212c8ecf83e000050

	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
from collections import deque
def dbl_linear(n):
    h = 1
    cnt = 0
    q1, q2 = deque([]), deque([])
    while True:
        if cnt >= n:
            return h
        q1.append(2*h+1)
        q2.append(3*h+1)
        h = min(q1[0], q3[0])
        if h == q1[0]:
            h = q1.popleft()
        if h == q2[0]:
            h = q2.popleft()
        cnt += 1
