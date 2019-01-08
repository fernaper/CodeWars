"""
	Solution of the problem
	Decode the morse code
	https://www.codewars.com/kata/54b724efac3d5402db00065e

	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
def decodeMorse(morse_code):
    MORSE_CODE['@'] = ' '
    return ''.join([MORSE_CODE[code] for code in morse_code.strip().replace('  ',' @ ').split()])
