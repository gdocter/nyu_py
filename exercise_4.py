# #!/usr/bin/env python3
#
# ### Lesson 4 in class notes ###
#
# #negative slice
# # mylist = ['a','b','c','d']
# # print(mylist[1]) #b
# # print(mylist[-1]) #d
# # mylist[1:-1] #['b', 'c']
#
# #fama french has 6 lines we don't want at beginning, and 2
# #use negative index
#
# my_list =[1,2,8,4,3.4,22, .2]
# my_sum = sum(my_list)
# my_len = len(my_list)
# my_avg = my_sum/my_len
#
# my_max = max(my_list)
# my_min = min(my_list)
#
# slist = sorted(my_list)
#
# top_3 = slist[0:3] # 0.2, 1, 2
# bottom_3 = slist[-3:] #4,8,22
#
# #median
# lenlist = len(my_list)
# median_index = int(lenlist/2)
# my_median = my_list[median_index]
#
# my_list.append(2000) # DO NOT ASSIGN !! because lists are mutable
# my_list.append(-100) # python allocates more space and adds more elements
# print(sorted(my_list))
# exit()
#
# ## instead of sum() append to lists ##
# mylist = []
# fh = open('')
#
# for line in fh:
#     items = line.split()
#     floatval = float(items[1])
#     mylist.append(floatval)
#
# print (dir(mylist))# using 'dir' shows you
# exit()

#set###
# x = set()
# x.add(4)
# x.add(5)
# x.add(5)
# x.add(9)
# print(x)

## SPELL CHECKER ##
# spell checkers compare text against a set of "defined"/accepted words
# id every word in the file
# compare to dictionary or word-list
# use set () for dictionary (elements unique)
# split each line
# prepare each word to comp against set (lower case, stripped)
# if word not in spelling set

## homework start...create set of words in pyku ##
# my_set = set()
# fh = open('../python_data/pyku.txt')
#
# full_string = fh.read()
# print(full_string)
# print(type(full_string))
# print()
# string_split = full_string.split()
# print(string_split)
# print(type(string_split))
# print()
#
# for words in string_split:
#     my_set.add(words)
#
# print(my_set)
# print(type(my_set))

#
# # #exercise 4.1/4.2
# fh = open('../python_data/passwords.txt')
# all_lines = fh.readlines()
# print (all_lines[0:3])
#
# #exercise 4.3
# state_list = []
# fh = open('../python_data/student_db.txt')
#
# for lines in fh:
#     word_split = lines.split(':')
#     state_list.append(word_split[3])
#
# print(state_list)
#
# #exercise 4.4, readlines to elim first line
# state = []
#
# fh = open('../python_data/student_db.txt')
# file_lines = fh.readlines()
# line_omitted = file_lines[1:]
#
# for lines in line_omitted:
#     words_split = lines.split(':')
#     state.append(words_split[3])
#
# print(state)
# #
#
# #exercise 4.5
# student_id = []
# fh = open('../python_data/student_db.txt')
#
# for lines in fh:
#     split_str = lines.split(':')
#
#     if split_str[3] == 'NY':
#         student_id.append(split_str[0])
#
# print(student_id)
#
# # #4.6 / 4.7
# sum_list = []
#
# fh = open('../python_data/revenue.txt')
#
# for lines in fh:
#     line_split = lines.split(',')
#     float_rev = float(line_split[2])
#     sum_list.append(float_rev)
#
# # length = len(sum_list)
# # total = sum(sum_list)
# average = sum(sum_list)/len(sum_list)
# print(average)
#
# #4.8 median
# #
# values = [1,2,3,4,5]
# middle_num = int((len(values))/2)
# print(values[middle_num])
#
# #4.9
# values = [3,1,5,2,4]
# sorted_values = sorted(values)
# index = int(len(sorted_values)/2)
# print(sorted_values[index])
#
# #4.10
# values = [6,1,3,2,4,5]
# sorted_values = sorted(values)
# len_vals_mid = int(len(sorted_values)/2)
#
# rval = sorted_values[len_vals_mid]
# lval = sorted_values[len_vals_mid-1]
#
# median = (lval + rval)/2
# print(median)

#4.11
# blank_set = set()
#
# dupvals = [1,3,1,1,2,3,2,1,3]
#
# for lines in dupvals:
#     blank_set.add(lines)
#
# print (blank_set)

#4.12
# file_holder = open('../python_data/revenue.txt')
# what_is_this = file_holder.read() #version 1, no loop
# print(what_is_this.strip('\n'))

# for lines in file_holder: #version 2, loop
#     removed = lines.strip('\n')
#     print(removed)

#4.13
# pos_list = []
#
# mylist = [-5,-2,1,-3,1.5,7,9]
# for nums in mylist:
#     if nums >= 0:
#         pos_list.append(nums)
#
# print (pos_list)

# #4.14 / 4.15 /4.16 /4.17 stripping and adding t set
# sentence = "I could; I wouldn't.  I might?  Might I!"
# my_set = set()
#
# new_string = sentence.split()
# strippers = ';.?!'
#
# for words in new_string:
#     my_set.add(words.rstrip(strippers).lower())
#
# print(my_set)

# #4.18 4.19 4.20
# pyku_set = set()
# strip_set = '.,'
#
# text = "we're certainly out of gouda but Python is great."
# holder = open('../python_data/pyku.txt')
#
#
# reader = holder.read() #splitting pyku shit
# split_words = reader.split()
#
# for words in split_words:
#     pyku_set.add(words.rstrip(strip_set).lower())
#
# text_reader = text.split()
#
#
# for new_words in text_reader:
#     if new_words not in pyku_set:
#         print(new_words)
