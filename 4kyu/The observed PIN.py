"""
	Solution of the problem
	The observed PIN
	https://www.codewars.com/kata/5263c6999e0f40dee200059d

	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
import itertools

'''
    Other option:

    get_candidates = {
        '1':['1','2','4'],
        '2':['1','2','3','5'],
        '3':['2','3','6'],
        '4':['1','4','5','7'],
        '5':['2','4','5','6','8'],
        '6':['3','5','6','9'],
        '7':['4','7','8'],
        '8':['0','5','7','8','9'],
        '9':['6','8','9'],
        '0':['0','8'],
    }
'''
def get_candidates(digit):
    if digit == '1':
        return ['1','2','4']
    if digit == '2':
        return ['1','2','3','5']
    if digit == '3':
        return ['2','3','6']
    if digit == '4':
        return ['1','4','5','7']
    if digit == '5':
        return ['2','4','5','6','8']
    if digit == '6':
        return ['3','5','6','9']
    if digit == '7':
        return ['4','7','8']
    if digit == '8':
        return ['0','5','7','8','9']
    if digit == '9':
        return ['6','8','9']
    if digit == '0':
        return ['0','8']

def get_pins(observed):
    # It is going to be a list of lists
    # Position 0 means all the possible digits for character 0
    candidates = []
    for char in observed:
        candidates.append(get_candidates(char))
    ans = []
    for item in list(itertools.product(*candidates)):
        partial = ''
        for pos in item:
            partial += pos
        ans.append(partial)
    return ans
