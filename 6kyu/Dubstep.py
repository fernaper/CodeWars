"""
	Solution of the problem 
	Dubstep
	https://www.codewars.com/kata/551dc350bf4e526099000ae5
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def song_decoder(song):
    return ' '.join (song.replace("WUB", " ").split())