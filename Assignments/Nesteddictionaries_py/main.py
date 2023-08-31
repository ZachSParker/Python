#Update Values in Dictionaries and Lists
"""
1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
2.Change the last_name of the first student from 'Jordan' to 'Bryant'
3.In the sports_directory, change 'Messi' to 'Andres'
4.Change the value 20 in z to 30
"""
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]
#1A ↓
# x[1][0] = 15
# for i in x:
#     print(i)
#1B ↓
# students[0]['last_name'] = 'Bryant'
# for items in students:
#     print(items)
#1C ↓
# sports_directory['soccer'][0] = 'Andres'
# for items in sports_directory['soccer']:
#     print(items)
#1D ↓
# z[0]['y'] = 30
# print(z[0]['y'])


#2.iterate through a list of dictionaries
students = [
    {'first_name' : 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(students):
    
#     for key in students:
#         print(key)
# iterateDictionary(students)
"""iterateDictionary(students) 
should output: (it's okay if each key-value pair ends up on 2 separate lines;
bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel"""
#3 Get values from a list of dictionaries ↓
# def iterateDictionary2(key,list):
#     for items in list:
#         print(items[key])
# iterateDictionary2('first_name',students)
# iterateDictionary2('last_name',students)

#4 iterate through a dictionary with list values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(dict):
    for key,val in dict.items(): #.items returns the key value pairs of the dictionary as tuples in a list
        print(len(val),key)#print the amount of list values in each list, display the key
        for i in range(0,len(val)):#start at the beginning of the index position and stop at the last value in each list
            print(val[i])#print the value at the index in the list
printInfo(dojo)#call the function and pass in the precreated dictionary dojo

