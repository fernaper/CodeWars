"""
	Solution of the problem
	Most frequently used words in a text
	https://www.codewars.com/kata/51e056fe544cf36c410000fb

	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
import re

def top_3_words(text):
    re_non_valid = re.compile('[^a-z\' ]')
    re_chars = re.compile('[a-z]')
    text = text.lower()
    text = ' '.join([x for x in re_non_valid.sub(' ',text).split() if re_chars.search(x)])
    words = {}
    top = {}                    # Dictionary with no more than 3 words
    for word in text.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
        top[word] = words[word] # Add the new word to the top
        if len(top) > 3:        # If the top is too big remove the worst word
            top.pop(min(top, key=top.get))
    return sorted(top, key=top.get, reverse=True)
