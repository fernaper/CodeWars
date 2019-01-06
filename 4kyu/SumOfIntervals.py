"""
	Solution of the problem
	Most frequently used words in a text
	https://www.codewars.com/kata/52b7ed099cdc285c300001cd

	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def sum_of_intervals(intervals):
    nums = []
    for entry in intervals:
        for e in range(entry[0],entry[1]):
            nums.append(e)
    return len(set(nums))
