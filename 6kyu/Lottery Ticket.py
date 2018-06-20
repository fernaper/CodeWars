"""
	Solution of the problem 
	Lottery Ticket
	https://www.codewars.com/kata/57f625992f4d53c24200070e
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def bingo(ticket,win):
    count = 0
    
    for mini in ticket:
        for letter in mini[0]:
            if ord(letter)==mini[1]:
                count += 1
                break
    
    if count >= win:
        return 'Winner!'
    return 'Loser!'