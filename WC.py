from sys import argv

script, filename = argv

file = open(filename)
str = file.read()

def judgeword(c): 
    if c >= 'A' and c <= 'Z' or c >= 'a' and c <= 'z':
        return True
    else:
        return False
		

def code_line(l):
    if len(l) >= 2:
        return True
    else:
        return False

def chara_count(s):
    return len(s)
	
	
def word_count(s):
    word_number = 0
    flag = 0
    for char in s:
        if flag == 0 and judgeword(char) == True:
            flag = 1
            word_number = word_number + 1
        if (flag == 1 and judgeword(char) == False) :
            flag = 0
    return word_number

	
def line_count(s):
    line_number = 0
    for char in s:
        if char == '\n':
            line_number = line_number + 1
    if char[-1] != '\n':
        line_number = line_number + 1
    return line_number
	

def lines_of_code_count(filename):
    lines_of_code = 0
    f = open(filename)
    for line in f.readlines():
        if code_line(line) == True:
            lines_of_code = lines_of_code + 1
    return lines_of_code



print lines_of_code_count(filename)	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
