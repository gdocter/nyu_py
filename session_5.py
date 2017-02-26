# #!/usr/bin/env python3
### Dictionaries ###

# x = {'acme':3, 'beta':5}
#
# x['conway'] = 1.1 #add to a dict, setting key/val
# x['beta'] = 2.3 #overwrites previous beta
#
#
# zz = x['conway'] #getting value from key
# x['beta'] = x['beta'] + 1 # make key value 1 greater
#
#
# for item in x: #loops twice
#     print(item) #acme beta
#     print(x[item]) #print values
#     print('this is the key: {}. This is the value {}'.format(item, x[item])) #print both




#sorting - sorts by keys
mydict = {'c':1, 'a':55, 'b':0.9 }

# mykeys = sorted(x) ## lines 22 -- 25 are 1 part; lines 28 - 33 are seperate
# print (mykeys)
# print(type(mykeys)) # sorted sorts keys
# print(max(x))


mykeys = sorted(mydict, key=mydict.get, reverse=True) #ranks by value ***** pasing the key, returns the value
#asking pyhon to call 'get' on each key and sort by the value
print (mykeys)

print(mydict.get('a')) #55
print(mydict.get('c')) #1

summar = list(mydict.values()) #VALUABLE TOOL RIGHT HERE
print(sum(summar))





#counting dictionary
# fh = open('../python_data/student_db.txt')
# mydict = {}
#
# for line in fh.readlines()[1:]: #readlines returns list of strings, slice off header
#     items = line.split(':')
#     state = items [3]
#     if state not in mydict:
#     #if state is not in dict, set count to one
#         mydict[state] = 1
#     #else if the state is a dict, add 1 to count
#     else:
#         mydict[state] = mydict[state] + 1
#
#
# print(mydict)
