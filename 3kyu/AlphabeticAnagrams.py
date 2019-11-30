
"""
	Solution of the problem 
	Calculator (v2)
	http://www.codewars.com/kata/53e57dada0cb0400ba000688
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
# Executed with Python 2.7 becaouse it doesn't have the same precission with Python 3.x
import math
# from functools import reduce # This is needed if you use Python 3

def listPosition(word):
  """Return the anagram list position of the word"""
  if len(word) == 1:
      return 1

  unique_words = sorted(list(set(word)))
  freq_letters = [word.count(letter) for letter in unique_words]
  # Total number of possible combinations
  total_combinations = math.factorial(len(word)) / reduce(lambda x,y: x * y, [math.factorial(freq) for freq in freq_letters])

  increment = [0] + [freq * total_combinations / len(word) for freq in freq_letters[:-1]]
  increment = [sum(increment[:i + 1]) for i in range(len(increment))]
  
  return increment[unique_words.index(word[0])] + listPosition(word[1:])
