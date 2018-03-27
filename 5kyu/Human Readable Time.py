"""
	Solution of the problem 
	Human Readable Time
	https://www.codewars.com/kata/52685f7382004e774f0001f7
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def make_readable(seconds):
    hours = int(seconds/3600)
    seconds -= hours*3600
    minutes = int(seconds/60)
    seconds -= minutes*60
    
    return str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2)