"""
	Solution of the problem 
	extract file name
	https://www.codewars.com/kata/597770e98b4b340e5b000071
	
	@author Fernando Pérez Gutiérrez <fernaperg@gmail.com>
"""
class FileNameExtractor:
    def extract_file_name(dirty_file_name):
        return dirty_file_name[dirty_file_name.find('_')+1:dirty_file_name.rfind('.')]