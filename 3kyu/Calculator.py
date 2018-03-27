"""
	Solution of the problem 
	Calculator
	http://www.codewars.com/kata/5235c913397cbf2508000048
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
class Calculator(object):
  def evaluate(self, string):
      # From now on, string is really an array of strings
      string = string.split(" ")
      if len(string) == 0:
          return 0
      # Mathematical operations of multiplication and division
      i = 1
      while("*" in string or "/" in string):
          if string[i] == '/':
              string = string[:i-1] + [str(float(string[i-1]) / float (string[i+1]))] + string[i+2:]
              i = i-1
          elif string[i] == '*':
              string = string[:i-1] + [str(float(string[i-1]) * float (string[i+1]))] + string[i+2:]
              i = i-1
          i += 1

      i = 1
      # Mathematical operations of addition and subtraction
      while("+" in string or "-" in string):
          if string[i] == '+':
              string = string[:i-1] + [str(float(string[i-1]) + float (string[i+1]))] + string[i+2:]
              i = i-1
          elif string[i] == '-':
              string = string[:i-1] + [str(float(string[i-1]) - float (string[i+1]))] + string[i+2:]
              i = i-1
          i += 1

      return float(string[0])