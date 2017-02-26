#!/usr/bin/env python3
# #FIRST
#set a sum FLOAT value to 0.0
sum_value = 0.0

#open file, a STRING object is returned, open returns a file object
fhxx = open('../python_data/FF_abbreviated.txt')

#loop through FILE object with 'for'
for myline in fhxx: #myline is a string, it gets a new value each iteration
    # each line of the file is retrieved in the loop
    # split the line (a STRING) into a LIST of strings
    items = myline.split()
    # select the second element (a string) of the list of strings
    str_val = items[1]
    # convert string to an FLOAT
    float_val = float(str_val)
    # add the integer to a sum
    sum_value = sum_value + float_val
#report the sum
print(sum_value, type(sum_value))

# =======================

#ask user for 4 digit year
# user_input = '1927'
#
# x = '19270101'
# num = x[0:4] #up to but not including, this is a slice
# while True:
#     user_input = input('type 1927: ')
#
# if user_input == num:
#     print('you got it {}'.format(user_input))
