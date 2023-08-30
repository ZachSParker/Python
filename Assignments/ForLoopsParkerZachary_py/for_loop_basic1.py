#Basic ↓
# -print all integers from 0-150
# for i in range(0,151):
#     print(i)

#Multiples of 5 ↓
# print all the multiples of 5 from 5-1000
# for i in range(5,1005,5):
#     print(i)

#Counting, The Dojo Way ↓
#counting, the dojo way- print integers 1 to 100, if divisible by 5, print 'Coding' instead,
#if divisible by 10 print "Coding Dojo"
# for i in range(1,101):
#     if i % 10 == 0:
#         print('Coding Dojo')
#     elif i % 5 == 0:
#         print('Coding')
#     else:
#         print(i)

#Whoa that Sucker's huge ↓
#add integers from 0-500,000 and print the final sum
# sum = 0
# for i in range(0,500000):
#     sum += i
# print(sum)

#Countdown by Fours ↓
#print positive numbers starting at 2018 and decrementing by 4
# for i in reversed(range(0,2021,4)):
#     print(i)

#Flexible Counter ↓
#set three changeable variables called lowNum,mult, and highNum, only print the evenly divisible numbers of mult
mult = 32
lowNum = 32
highNum = 1000
for i in range(lowNum,highNum):
    if i % mult == 0:
        print(i)
    else:
        continue
