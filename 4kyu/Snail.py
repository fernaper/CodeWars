"""
	Solution of the problem
	Snail
	https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def get_first_line(array):
    if not array: return [],[]
    return array[0], array[1:]

def get_first_column(array):
    if not array: return [],[]
    return [x[0] for x in array], [[x[i] for i in range(1,len(x))] for x in array]

def get_last_line(array):
    if not array: return [],[]
    return array[-1], array[:-1]

def get_last_column(array):
    if not array: return [],[]
    return [x[-1] for x in array], [[x[i] for i in range(len(x)-1)] for x in array]

def snail(array):
    ans = []
    while array:
        fl,array = get_first_line(array)
        lc,array = get_last_column(array)
        ll,array = get_last_line(array)
        fc,array = get_first_column(array)
        ans += fl + lc + ll[::-1] + fc[::-1]
    return ans
