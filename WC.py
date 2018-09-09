#coding=utf-8
from sys import argv

script, filename = argv

file = open(filename)
str = file.read()

def judge_letter(c): 
    if c >= 'A' and c <= 'Z' or c >= 'a' and c <= 'z':
        return True
    else:
        return False
		
		
def judge_visible_character(c):
    if c >= '!' and c <= '~':
        return True
    else:
        return False

def code_line(l):
    if len(l) >= 2 and (l[0] != '/' and l[1] != '/' or l[1] != '/'and l[2] != '/'):
        return True
    else:
        return False
		
		
def number_of_visible_characters_in_a_line(l):
    number = 0
    for char in l:
        if judge_visible_character(char) == True:
            number = number + 1
    return number

def blank_line(l):
    if number_of_visible_characters_in_a_line(l) >= 2:
        return False
    else:
        return True
		

def comment_line(l):
    if len(l) >= 2 and (l[1] == '/'and l[2] == '/' or l[0] == '/' and l[1] == '/'):
        return True
    else:
        return False
	
	
def word_count(s):
    word_number = 0
    flag = 0
    for char in s:
        if flag == 0 and judge_letter(char) == True:
            flag = 1
            word_number = word_number + 1
        if (flag == 1 and judge_letter(char) == False) :
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
	
	
file.close()


file = open(filename)
lines = file.readlines()
	

def lines_of_code_count(l):
    lines_of_code = 0
    for line in l:
        if code_line(line) == True:
            lines_of_code = lines_of_code + 1
    return lines_of_code


def blank_lines_count(l):
    number_of_blank_line = 0
    for line in l:
        if blank_line(line) == True:
            number_of_blank_line = number_of_blank_line + 1
    return number_of_blank_line
    
	
	
def comment_lines_count(l):
    number_of_comment_lines = 0
    for line in l:
        if comment_line(line) == True:
            number_of_comment_lines = number_of_comment_lines + 1
    return number_of_comment_lines
	
	
	
	
	
print comment_lines_count(lines)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
