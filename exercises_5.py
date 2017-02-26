#!/usr/bin/env python3

################5.2
# mydict = {}
#
# mylist = ['Hey', 'there', 'I', 'am', 'amazing!']
#
# for word in mylist:
#     length = len(word)
#     mydict[word] = length
#
# print(mydict)

################5.3
# mydict = {}
#
# mylist = ['Hey', 'there', 'I', 'am', 'amazing!']
#
# for word in mylist:
#     length = len(word)
#     mydict[word] = length
#
# for key_val in mydict:
#     str_value = mydict[key_val]
#     print (' "{}" is len {}'.format(key_val, str_value))

################5.4 & 5.5
# mydict = {}
# mylist = ['Hey', 'there', 'I', 'am', 'amazing!']
#
# user_input = input('please enter a word: ')
#
# for word in mylist: #building up the dict
#     length = len(word)
#     mydict[word] = length
#
# if user_input in mydict:
#     print('the word "{}" is len {}'.format(user_input,mydict[user_input]))
#
# else:
#     print('the word "{}" does not exist in the dictiony'.format(user_input))
#
# if user_input not in mydict:
#     print('ANOTHER WAY the word "{}" does not exist in the dictiony'.format(user_input))


################# 5.6
# my_dict = {}
# fh = open('../python_data/revenue.txt')
#
# for line in fh:
#     broken_line = line.split(',')
#     my_dict[broken_line[0]] = broken_line[2]
#
# print(my_dict)

################5.7

# my_dict = {}
# file_direct = '../python_data/revenue.txt'
#
# for line in open(file_direct):
#     remove_new = line.rstrip()
#     indexable_line = remove_new.split(',')
#     print(indexable_line)
#     print(type(indexable_line))
#     my_dict[indexable_line[0]] = indexable_line[2]
#
# print(my_dict)

################5.8
# personal_info = "595-33-9193:68:Columbus, OH"
# indexable_line  = personal_info.split(':')
#
# my_new_str = "SS#: {}\nAge: {}\nResidence: {}".format(indexable_line[0],indexable_line[1],indexable_line[2],)
#
# print(my_new_str)

################5.9
# mydict = {}
# cities = ['Boston', 'Chicago', 'New York', 'Boston', 'Chicago', 'Boston']
# for loc in cities:
#     if loc not in mydict:
#         mydict[loc] = 0
#     mydict[loc] = mydict[loc] + 1
#
# print(mydict)

################5.10
# my_dict = {}
# fh = open('../python_data/student_db.txt')
#
# for line in fh.readlines()[1:]:
#     items = line.split(':')
#     print(items)
#     state = items[3]
#     if state not in my_dict:
#         my_dict[state] = 0
#     my_dict[state] = my_dict[state] +1
#
# print(my_dict)

################5.11
# my_dict = {}
# fh = open('../python_data/revenue.txt')
#
# for line in fh.readlines():
#     items = line.split(',')
#     state = items[1] # could clean this out
#     rev = float(items[2].rstrip()) #could clean this out , rstrip to revmoe new line)
#     if state not in my_dict:
#         my_dict[state] = 0.0
#     my_dict[state] = my_dict[state] + rev
#
# print(my_dict)

################5.12
# mydict = {'c': 0.3, 'b': 7, 'a': 5}
#
# keys = list(mydict.keys()) #look at keys in dict, conver to list
# keys.sort() #sort this list
#
# for key in keys: #loop through sorted list
#     print(key, '-->' ,mydict[key])

################5.13
# mydict = {'c': 0.3, 'b': 7, 'a': 5}
#
# sorted_values = sorted(mydict, key=mydict.get)
# for val in sorted_values:
#     print(mydict[val])

################5.14
# mydict = {'c': 0.3, 'b': 7, 'a': 5}
#
# sorted_values = sorted(mydict, key=mydict.get, reverse=True)
# for vals in sorted_values:
#     print(mydict[vals])

################5.15
# mydict = {'c': 0.3, 'b': 7, 'a': 5}
#
# while True:
#     user_input=input('please enter a direction [asc / desc]: ')
#
#     if user_input == 'asc':
#         rev = False
#         sorted_values = sorted(mydict, key=mydict.get, reverse=rev)
#         for vals in sorted_values:
#             print(mydict[vals])
#         break
#
#     elif user_input == 'desc':
#         rev = True
#         sorted_values = sorted(mydict, key=mydict.get, reverse=rev)
#         for vals in sorted_values:
#             print(mydict[vals])
#         break
#
#     else:
#         print('invalid input, try again')

#5.16 & 5.17
my_dict = {}
fh = open('../python_data/revenue.txt')

for line in fh.readlines():
    items = line.split(',')
    state = items[1] # could clean this out
    rev = float(items[2].rstrip()) #could clean this out , rstrip to revmoe new line)
    if state not in my_dict:
        my_dict[state] = 0.0
    my_dict[state] = my_dict[state] + rev

print(my_dict)

# keys = list(my_dict.keys()) #5.16
# keys.sort()
# for key in keys:
#     print(key, '-->', my_dict[key])


sorted_values = sorted(my_dict, key=my_dict.get)
 #5.17
for val in sorted_values:
    print(val, '-->', my_dict[val])

    #stikk asdlkjf39!)@(
