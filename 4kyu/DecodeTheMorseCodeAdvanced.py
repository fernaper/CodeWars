"""
	Solution of the problem
	Decode the morse code advanced
	https://www.codewars.com/kata/54b72c16cd7f5154e9000457

	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
import re

def decodeBits(bits):
    bits = re.sub('^(0+)','',bits)
    bits = re.sub('(0+)$','',bits)
    speed = get_rate(bits)
    return bits.replace('1'*speed,'1').replace('0'*speed,'0').replace('0000000',' @ ').replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')

def get_rate(bits):
    sequences = set()
    for match in re.findall("(0+|1+)", bits):
        sequences.add(match)
    min = -1
    for s in sequences:
        if min == -1 or len(s) < min:
            min = len(s)
    return min

def decodeMorse(morse_code):
    MORSE_CODE['@'] = ' '
    return ''.join([MORSE_CODE[code] for code in morse_code.strip().split()]).replace('  ',' ')
