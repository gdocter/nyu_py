#!/usr/bin/env python3

#### 5.1
# student_dict = {}
# fh = open('../python_data/student_db.txt')
# quit_list = ['q','Q','Quit','quit']
#
# for line in fh.readlines():
#     items = line.split(':')
#     student_id = items[0]
#     address = items[1:4]
#     student_dict[student_id] = address
#
# while True:
#     user_input = input('Please enter student id ("Q" to exit): ')
#     if user_input in student_dict:
#         print('Address for student with ID: {}'.format(user_input))
#         for line in student_dict[user_input]:
#             print(line)
#
#     elif user_input in quit_list:
#         exit('goodbye')
#
#     else:
#         print('The ID you entered does not exist')


#### 5.2
asc_desc = False
rf_dict = {}

fh = open('../python_data/F-F_Research_Data_Factors_daily.txt')
file_lines = fh.readlines()
wanted_lines = file_lines[5:-2]

for line in wanted_lines:
    splitter = line.split()
    first_col = splitter[0]
    year = first_col [0:4]
    mkt_rf = float(splitter[1])

    if year not in rf_dict:
        rf_dict[year] = mkt_rf

    else:
        rf_dict[year] = rf_dict[year] + mkt_rf

while True:
    order_input = input('Select "lowest" or "highest" results: ')

    if order_input in ['highest', 'lowest']:

        if order_input == 'lowest':
            asc_desc = asc_desc
            break

        else:
            asc_desc = True
            break
    else:
        print('Try again, must type "highest" or "lowest"')

while True:
    user_results = input('please enter the number of results: ')

    if user_results.isdigit() and int(user_results) <= len(rf_dict):
        int_results = int(user_results)
        break

    else:
        print('Your input was either 1) Not a positive number or 2) greater than the number of possible results. Try again.')

sorted_list = sorted(rf_dict, key=rf_dict.get, reverse=asc_desc)
limited_results = sorted_list[0:int_results]

for val in limited_results:
    print (val, round(rf_dict[val],2))
