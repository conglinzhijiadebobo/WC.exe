from sys import argv
import os
import Tkinter, tkFileDialog


#read by characters in the process down here.

def is_letter(c): 
    if c >= 'A' and c <= 'Z' or c >= 'a' and c <= 'z':
        return True
    else:
        return False
		
def count_words(s):
    word_number = 0
    flag = 0
    for char in s:
        if flag == 0 and is_letter(char) == True:
            flag = 1
            word_number = word_number + 1
        if (flag == 1 and is_letter(char) == False) :
            flag = 0
    return word_number

	
def count_lines(s):
    line_number = 0
    for char in s:
        if char == '\n':
            line_number = line_number + 1
    if s and s[-1] != '\n' :   #s[]is not empty and the final one is not a enter.
        line_number = line_number + 1
    return line_number
	
	


#should read by lines in the process down here.



def is_code_line(l):
    if len(l) >= 2 and (l[0] != '/' and l[1] != '/' or l[1] != '/'and l[2] != '/'):
        return True
    else:
        return False
	
def count_lines_of_code(l):
    lines_of_code = 0
    for line in l:
        if is_code_line(line) == True:
            lines_of_code = lines_of_code + 1
    return lines_of_code

	
def is_visible_character(c):
    if c >= '!' and c <= '~':
        return True
    else:
        return False
		
def get_number_of_visible_characters_in_a_line(l):
    number = 0
    for char in l:
        if is_visible_character(char) == True:
            number = number + 1
    return number

def is_blank_line(l):
    if get_number_of_visible_characters_in_a_line(l) >= 2:
        return False
    else:
        return True
	
def count_blank_lines(l):
    number_of_blank_line = 0
    for line in l:
        if is_blank_line(line) == True:
            number_of_blank_line = number_of_blank_line + 1
    return number_of_blank_line

	
def is_comment_line(l):
    if len(l) >= 2 and (l[1] == '/'and l[2] == '/' or l[0] == '/' and l[1] == '/'):
        return True
    else:
        return False    
	
def count_comment_lines(l):
    number_of_comment_lines = 0
    for line in l:
        if is_comment_line(line) == True:
            number_of_comment_lines = number_of_comment_lines + 1
    return number_of_comment_lines
	
	
	
def get_file_from_path(path, all_file):  #get the file from the path, return a list of the file
    file_list = os.listdir(path)
    for filename in file_list:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            get_file_from_path(filepath, all_file)
        else:
            all_file.append(filepath)
    return all_file

	
def print_a_number(order, s, l):
    if order == '-c': 
        print len(s)
    elif order == '-w':
        print count_words(s)
    elif order == '-l':
        print count_lines(s)
    elif order == '-a':
        print count_lines_of_code(l)
        print count_blank_lines(l)
        print count_comment_lines(l)
	
def print_numbers(f, orders):
    file = open(f)
    str = file.read()
    file.close()
		
    file = open(f)  
    lines = file.readlines()
    file.close()
    for order in orders:
        print_a_number(order, str, lines)
		
		
def give_all_the_number(f):
    file = open(f)
    str = file.read()
    file.close()
		
    file = open(f)  
    lines = file.readlines()
    file.close()
    c = len(str)
    w = count_words(str)
    l = count_lines(str)
    code_line = count_lines_of_code(lines)
    blank_line = count_blank_lines(lines)
    comment_line = count_comment_lines(lines)
    numbers = [c, w, l, code_line, blank_line, comment_line]
    return numbers
	
def gui():
    root = Tkinter.Tk()
    root.title('Counter')
    root.geometry('400x500')
    
    filename = tkFileDialog.askopenfilename()

    numbers = give_all_the_number(filename)
    the_info = ["Characters:" + str(numbers[0]), "Words: " + str(numbers[1]), "lines: " + str(numbers [2]), "Code lines: " + str(numbers[3]), "Blank lines: " + str(numbers[4]), "Comment lines: " + str(numbers[5])] 
    
    file_display = Tkinter.Label(root, text = open(filename).read(), justify = 'left')
    numbers_display = Tkinter.Listbox(root, width = 400)
	
    for item in the_info:
	    numbers_display.insert('end', item)
    
    file_display.pack()
    numbers_display.pack()
    root.mainloop()
	



if __name__=="__main__":
    if len(argv) >=2 and argv[1] == '-x':
        gui()
    elif len(argv) >=2 and argv[1] == '-s' :
        path = argv[-1].split('*')
        all_file = []
        all_file = get_file_from_path(path[0], all_file)    
        for file in all_file:
            print_numbers(file, argv[2:-1])
    else:
        print_numbers(argv[-1], argv[1:-1])