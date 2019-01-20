"""
	Solution of the problem
	Last digit of large number
	https://www.codewars.com/kata/52685f7382004e774f0001f7

	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
import math

def get_mod(a, b) :
    mod = 0
    for i in range(len(b)) :
        mod = (mod * 10 + (int)(b[i])) % a
    return mod

def last_digit(n1, n2):
    a = str(n1)
    b = str(n2)
    len_a = len(a)
    len_b = len(b)

    # if base is 0
    if (len_a == 1 and a[0] == '0') :
        return 0
    # if a and b both are 0 or exponent is 0
    if (len_a == 1 and len_b == 1 and b[0] == '0' and a[0] == '0') or \
       (len_b == 1 and b[0]=='0'):
        return 1

    # if exponent is divisible by 4 -> last digit is pow(a, 4) % 10
    # if not -> last digit is pow(a, b % 4) % 10
    mod = get_mod(4, b)
    exp = mod
    if mod == 0:
        exp = 4

    return math.pow((int)(a[len_a - 1]), exp) % 10
