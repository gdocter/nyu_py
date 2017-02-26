#!/usr/bin/env python3

#diff between methods
fh = open('../python_data/FF_abbreviated.txt')

# for lines in fh:
#     print(repr(lines))

#
# text = fh.read()
# print (repr(text))

text_again = fh.readlines()
print(repr(text_again))

# exercise 3.1 - 3.3
# counter = 0
#
# fh = open('../python_data/FF_abbreviated.txt')
# for lines in fh:
#     counter = counter + 1
#     print(counter, repr(lines))

#3.4

# #open file, a STRING object is returned, open returns a file object
# fh = open('../python_data/FF_abbreviated.txt')
# #loop through FILE object with 'for'
# for lines in fh:
#     year_only = lines[0:4]
#     print(year_only)

#3.5 solution
# string_var = '1928'
#
# file_holder = open('../python_data/FF_abbreviated.txt')
#
# for all_lines in file_holder:
#     year_check = all_lines[0:4]
#     if year_check == string_var:
#         print(all_lines)

#3.6
# string_var = '1928'
# counter = 0
#
# file_holder = open('../python_data/FF_abbreviated.txt')
#
# for each_line in file_holder:
#     grab_year = each_line [0:4]
#     if grab_year == string_var:
#         counter = counter + 1
#         print (each_line)
#
# print(counter)

#3.7 solution 1
# file_holder = open('../python_data/FF_abbreviated.txt')
#
# text = file_holder.read()
# lines = text.splitlines()
#
# for line in lines:
#     stripped = line.split()
#     print(stripped)

#3.7 solution 2 // 3.8 // 3.9
# file_holder = open('../python_data/FF_abbreviated.txt')
# for xx in file_holder:
#     chop_into_lists_of_strings = xx.split()
#     print(chop_into_lists_of_strings[0])

#3.10
# year_string = '1928'
#
# file_holder = open('../python_data/FF_abbreviated.txt')
# for all_lines in file_holder:
#     grab_year = all_lines [0:4] #look for str 1928
#     if grab_year == year_string: #if str is found
#         chop_str = all_lines.split() # split line on space delimeter
#         print(chop_str[1])  # select 2nd column
# #3.11
# year_string = '1928'
#
# open_again = open('../python_data/FF_abbreviated.txt')#open file
# for all_lines in open_again: #parse through file object
#     get_year = all_lines [0:4]#slice string to ID correct
#     if get_year == year_string: # if string is correct year_string
#         split_list_str = all_lines.split()# chop string up based on space delimeter
#         col_str = split_list_str[1]
#         col_float = float (col_str)
#         two_ex = col_float * 2
#         print(col_str, two_ex)

#3.12 with counter
# year_string = '1928'
# counter = 0
#
# open_again = open('../python_data/FF_abbreviated.txt')
# for all_lines in open_again:
#     get_year = all_lines[0:4]
#     if get_year == year_string:
#         split_list_str = all_lines.split()
#         column_string = split_list_str[1]
#         column_float = float(column_string)
#         two_ex = column_float * 2
#         counter = counter + 1
#         print(counter, column_string, two_ex)

#3.13 sum
# floatsum = 0
# year_string = '1928'
#
# list_again = open('../python_data/FF_abbreviated.txt')
# for all_lines in list_again:
#     get_year = all_lines[0:4]
#
#     if get_year == year_string:
#         split_list_str = all_lines.split()
#         column_string = split_list_str[1]
#         column_float = float(column_string)
#         floatsum = floatsum + column_float
#
# print(floatsum)

# #3.14 string length
# new_list = open('../python_data/pyku.txt')
# text = new_list.read()#read entire file into a string
# print(len(text))#print the length of this string

#3.15 Word Count
# string_holder = open('../python_data/pyku.txt')
# text = string_holder.read()
# word_count = text.count('spam')
# print(word_count)

#3.16

# open_file = open('../python_data/pyku.txt') #open file
# string = open_file.read() #read into string
# split_list = string.splitlines() # splitlines() to split into list of lines
# print(type(split_list))
# print(split_list[0])
# print(split_list[2])

#3.17
# file_holder = open('../python_data/pyku.txt')# open file
#
# string_read = file_holder.read()# read into string
# splitter = string_read.split()# use VARIABLE.split() to turn string into list of words
# print(type(splitter))# print type
# print(len(splitter))
# print(splitter[0])
# print(splitter[14])


#3.18
# var = ['a', 'b', 'c', 'd']
# print(len(var))
