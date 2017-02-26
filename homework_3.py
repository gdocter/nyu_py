#!/usr/bin/env python3

# #homework 3.1 using For Loop
counter = 0
sum_float = 0.00
file_holder = open('../python_data/Fama-French_data.txt')

while True:
    user_input = input('Type in a 4 digit year: ')
    if user_input.isdigit():
        break
    else:
        print('{} is not a year, try again and use all digits'.format(user_input))

for all_lines in file_holder:
    get_year = all_lines[0:4]

    if user_input == get_year:
        string_split = all_lines.split()
        mkt_rf_string = string_split[1]
        mkt_rf_float = float(mkt_rf_string)
        sum_float = sum_float + mkt_rf_float
        counter = counter + 1

mkt_rf_average = (sum_float/counter)
print('count {}, sum {}, average {}'.format(counter, round(sum_float,4), round(mkt_rf_average,4)))

#3.2 using read()
# while True:  #I know this is a "dumb" loop
#     user_input = input('please enter a filename: ')
#     if user_input == 'sawyer.txt':
#         break
#     else:
#         print('sorry,you must enter SAWYER.TXT')
#
# file_holder = open('../python_data/{}'.format(user_input))
# single_string = file_holder.read()
#
# lines = single_string.splitlines()
# words = single_string.split()
#
# num_chars = str(len(single_string))
# num_lines = str(len(lines))
# num_words = str(len(words))
#
# print(num_lines.rjust(8,' '), num_words.rjust(8,' '),num_chars.rjust(8,' '), user_input)

# #3.2 with readlines()
# sum_words_per_line = 0
# sum_chars = 0
#
# file_holder = open('../python_data/sawyer.txt')
# single_list = file_holder.readlines()
# print(type(single_list)) #this is a list
#
# num_lines = len(single_list) # find number of lines in list
# print(num_lines)
#
# for lines in single_list:
#     words = lines.split()
#     words_per_line = int(len(words))
#     sum_words_per_line = sum_words_per_line + words_per_line
#
# print(sum_words_per_line) #number of words in list
# DID NOT GET TO COUNTING NUMBER OF CHARACTERS
