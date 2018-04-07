"""
	Solution of the problem 
	Counting Change Combinations
	https://www.codewars.com/kata/541af676b589989aed0009e7
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def count_change(money, coins):
    if money == 0:
        return 1
    elif money < 0 or len(coins) == 0:
        return 0
    return count_change(money-coins[0],coins) + count_change(money,coins[1:])