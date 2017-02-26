# #!/usr/bin/env python3
#
# #4.1 homework
# user_list = []
# fh = open('../python_data/F-F_Research_Data_Factors_daily.txt')
# file_lines = fh.readlines()
# wanted_lines = file_lines[5:-2]
# factor_index = 1
#
#
# while True: #set factor index
#     user_year = input('enter 4 digit year: ')
#     print('available factors:  [Mkt-RF, SMB, HML, RF]')
#     user_data = input('Please enter a factor: ')
#     if user_data == 'Mkt-RF': #I am certain that there is a better way of doing this. alas..
#         factor_index = 1
#         break
#     elif user_data == 'SMB':
#         factor_index = 2
#         break
#     elif user_data == 'HML':
#         factor_index = 3
#         break
#     elif user_data == 'RF':
#         factor_index = 4
#         break
#     else:
#         print('that factor does not exist, try again')
#
#
# for lines in wanted_lines:
#     get_year = lines [0:4]
#     if user_year == get_year:
#         line_split = lines.split()
#         user_list.append(float(line_split[factor_index]))
#
# if not user_list:
#     print('no values found')
#     exit()
#
# list_len = len(user_list)
# max_val = max(user_list)
# min_val = min(user_list)
# total = sum(user_list)
# average = total/list_len
#
# print('{} ({}): {} values, max {}, min {}, average {}'.format(user_year,user_data, list_len, max_val, min_val, average))
#
#4.2 homework
sawyer_raw = open('../python_data/sawyer.txt')
dictionary_raw = open('../python_data/words.txt')
clean_dictionary = set()
strips = '.,;:&'
count = 0 #added

full_string = dictionary_raw.read() #read entire file as a string
dictionary_split = full_string.split() #split the giant string into a bunch of little strings based on spaces

for dictionary_words in dictionary_split: #parse through each string
    clean_dictionary.add(dictionary_words.lower().strip(strips)) #clean the string and add to new dictionary set

word_count = len(clean_dictionary) #count number of words
print('{} words in spelling words'.format(word_count))
print()

for lines in sawyer_raw: #parse line by line through sawyer text
    words_list = lines.split() #split lines into individual words
    for words in words_list: #parse through each word in each "line"/list of strings
        clean_words = words.strip(strips).lower() #clean the word
        if clean_words not in clean_dictionary: #compare it to the new dictionary, this interrupts the line
            count = count + 1 ## added
            print(count) #added
            print('misspelled word: {}'.format(clean_words)) #print the misspelled word
            print('REPEAT') #returns to whatever WORD it was on , even in middle of line
